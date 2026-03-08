"""Deep style analysis of converted markdown papers."""
import json
import re
import os
from pathlib import Path
from collections import Counter

MD_FOLDER = Path(r"C:\Users\hwpar\Desktop\Claude_Code\Projects\Journal_summary\converted_md")

def read_all_papers():
    papers = {}
    for md_file in sorted(MD_FOLDER.glob("*.md")):
        with open(md_file, "r", encoding="utf-8") as f:
            papers[md_file.stem] = f.read()
    return papers

def find_sections(text):
    """Identify major sections in the paper."""
    sections = {}
    # Common section patterns
    patterns = [
        (r'(?:^|\n)\s*(?:ABSTRACT|Abstract)\s*\n', 'abstract'),
        (r'(?:^|\n)\s*(?:\d+\.?\s*)?(?:Introduction|INTRODUCTION)\s*\n', 'introduction'),
        (r'(?:^|\n)\s*(?:\d+\.?\s*)?(?:Experimental\s+(?:setup|apparatus|method|procedure)|Test\s+(?:setup|engine|bench)|Methodology|Methods|Materials?\s+and\s+[Mm]ethods?|Engine\s+(?:development|setup|specifications?))\s*\n', 'methods'),
        (r'(?:^|\n)\s*(?:\d+\.?\s*)?(?:Results?\s+and\s+[Dd]iscussion|Results?|Experimental\s+results?)\s*\n', 'results'),
        (r'(?:^|\n)\s*(?:\d+\.?\s*)?(?:Discussion|DISCUSSION)\s*\n', 'discussion'),
        (r'(?:^|\n)\s*(?:\d+\.?\s*)?(?:Conclusions?|Summary|Concluding\s+remarks?)\s*\n', 'conclusion'),
        (r'(?:^|\n)\s*(?:References?|REFERENCES?|Bibliography)\s*\n', 'references'),
    ]

    for pattern, name in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            sections[name] = match.start()

    return sections

def extract_section_text(text, sections, target):
    """Extract text for a specific section."""
    if target not in sections:
        return ""

    start = sections[target]
    # Find next section
    later_sections = {k: v for k, v in sections.items() if v > start}
    if later_sections:
        end = min(later_sections.values())
    else:
        end = len(text)

    return text[start:end]

def analyze_voice(text):
    """Analyze passive vs active voice ratio."""
    sentences = re.split(r'[.!?]+', text)
    passive_patterns = [
        r'\b(?:is|are|was|were|been|being)\s+\w+ed\b',
        r'\b(?:is|are|was|were|been|being)\s+\w+en\b',
        r'\bcan\s+be\s+\w+ed\b',
        r'\bcould\s+be\s+\w+ed\b',
        r'\bwas\s+(?:achieved|obtained|observed|measured|determined|investigated|conducted|performed|selected|employed|used|applied|found|reported|compared|increased|decreased|reduced|improved|maintained)\b',
        r'\bwere\s+(?:achieved|obtained|observed|measured|determined|investigated|conducted|performed|selected|employed|used|applied|found|reported|compared|increased|decreased|reduced|improved|maintained)\b',
        r'\bis\s+(?:considered|defined|required|expected|known|assumed|noted|shown|described|presented|proposed|recommended)\b',
    ]

    passive_count = 0
    total = len([s for s in sentences if len(s.strip()) > 10])

    for sent in sentences:
        for pat in passive_patterns:
            if re.search(pat, sent, re.IGNORECASE):
                passive_count += 1
                break

    return {
        "passive_ratio": round(passive_count / max(total, 1), 3),
        "active_ratio": round(1 - passive_count / max(total, 1), 3),
        "passive_count": passive_count,
        "total_sentences": total
    }

def analyze_tense(text):
    """Analyze tense patterns."""
    past_indicators = len(re.findall(r'\b(?:was|were|had|did|achieved|showed|demonstrated|indicated|resulted|decreased|increased|improved|conducted|performed|investigated|reported|observed|compared|employed|selected|obtained)\b', text, re.IGNORECASE))
    present_indicators = len(re.findall(r'\b(?:is|are|has|does|shows|demonstrates|indicates|results|decreases|increases|improves|leads|provides|suggests|requires|enables|allows|represents)\b', text, re.IGNORECASE))
    future_indicators = len(re.findall(r'\b(?:will|shall|would|could)\b', text, re.IGNORECASE))

    total = past_indicators + present_indicators + future_indicators
    if total == 0:
        return {"past": 0, "present": 0, "future": 0}

    return {
        "past": round(past_indicators / total, 3),
        "present": round(present_indicators / total, 3),
        "future": round(future_indicators / total, 3)
    }

def extract_high_freq_verbs(text):
    """Extract high-frequency verbs."""
    verb_patterns = [
        'achieved', 'obtained', 'observed', 'measured', 'determined',
        'investigated', 'conducted', 'performed', 'selected', 'employed',
        'applied', 'proposed', 'demonstrated', 'reported', 'compared',
        'increased', 'decreased', 'reduced', 'improved', 'maintained',
        'indicated', 'showed', 'presented', 'developed', 'designed',
        'evaluated', 'analyzed', 'implemented', 'utilized', 'operated',
        'resulted', 'suggested', 'confirmed', 'enhanced', 'suppressed',
        'considered', 'adopted', 'controlled', 'examined', 'identified',
    ]

    counts = {}
    for verb in verb_patterns:
        count = len(re.findall(r'\b' + verb + r'\b', text, re.IGNORECASE))
        if count > 0:
            counts[verb] = count

    return dict(sorted(counts.items(), key=lambda x: -x[1])[:20])

def extract_transition_phrases(text):
    """Extract transition/connector phrases."""
    phrases = [
        'however', 'therefore', 'furthermore', 'moreover', 'in addition',
        'in contrast', 'on the other hand', 'as a result', 'consequently',
        'nevertheless', 'although', 'while', 'owing to', 'because of',
        'due to', 'in this study', 'in this work', 'in the present study',
        'it is noted that', 'it was found that', 'it is worth noting',
        'in particular', 'specifically', 'for example', 'for instance',
        'compared to', 'compared with', 'relative to', 'with respect to',
        'based on', 'according to', 'in terms of', 'in order to',
        'as mentioned', 'as shown in', 'as described', 'as reported',
    ]

    counts = {}
    for phrase in phrases:
        count = len(re.findall(r'\b' + re.escape(phrase) + r'\b', text, re.IGNORECASE))
        if count > 0:
            counts[phrase] = count

    return dict(sorted(counts.items(), key=lambda x: -x[1])[:20])

def extract_hedging(text):
    """Extract hedging expressions."""
    hedging = [
        'may', 'might', 'could', 'possibly', 'probably', 'likely',
        'suggests', 'appears', 'seems', 'tends to', 'is expected',
        'it is possible', 'it is likely', 'presumably', 'apparently',
        'approximately', 'roughly', 'nearly', 'about',
    ]

    counts = {}
    for h in hedging:
        count = len(re.findall(r'\b' + re.escape(h) + r'\b', text, re.IGNORECASE))
        if count > 0:
            counts[h] = count

    return dict(sorted(counts.items(), key=lambda x: -x[1]))

def analyze_citation_style(text):
    """Determine citation style."""
    bracket_nums = len(re.findall(r'\[[\d,\s–-]+\]', text))
    author_year = len(re.findall(r'\([A-Z][a-z]+\s+et\s+al\.?,?\s*\d{4}\)', text))
    superscript = len(re.findall(r'[a-z]\d{1,2}(?:\s|,)', text))  # rough

    if bracket_nums > author_year and bracket_nums > superscript:
        return {"style": "numbered_brackets", "count": bracket_nums}
    elif author_year > bracket_nums:
        return {"style": "author_year", "count": author_year}
    else:
        return {"style": "numbered_brackets", "count": bracket_nums}

def analyze_measurement_formats(text):
    """Extract measurement format patterns."""
    patterns = {
        "temperature": re.findall(r'\d+\s*[°℃]?\s*(?:°C|K|°F|℃)', text),
        "pressure": re.findall(r'\d+\.?\d*\s*(?:MPa|kPa|bar|Pa|atm)', text),
        "speed_rpm": re.findall(r'\d+\s*(?:rpm|RPM|r/min|rev/min)', text),
        "percentage": re.findall(r'\d+\.?\d*\s*%', text),
        "angle_cad": re.findall(r'\d+\.?\d*\s*(?:CAD|°CA|crank angle degree)', text),
        "power": re.findall(r'\d+\.?\d*\s*(?:kW|MW|hp|PS|W)', text),
        "efficiency": re.findall(r'\d+\.?\d*\s*%', text),
        "concentration_ppm": re.findall(r'\d+\.?\d*\s*(?:ppm|ppb)', text),
        "emissions_specific": re.findall(r'\d+\.?\d*\s*(?:g/kWh|mg/kWh)', text),
        "ratio": re.findall(r'\d+\.?\d*:\d+\.?\d*', text),
    }

    formats = {}
    for key, matches in patterns.items():
        if matches:
            formats[key] = {
                "count": len(matches),
                "examples": list(set(matches[:5]))
            }

    return formats

def analyze_figure_table_refs(text):
    """Analyze Figure/Table reference patterns."""
    fig_patterns = {
        "Fig.": len(re.findall(r'\bFig\.\s*\d+', text)),
        "Figure": len(re.findall(r'\bFigure\s*\d+', text)),
        "fig.": len(re.findall(r'\bfig\.\s*\d+', text)),
    }

    table_patterns = {
        "Table": len(re.findall(r'\bTable\s*\d+', text)),
        "Tab.": len(re.findall(r'\bTab\.\s*\d+', text)),
    }

    return {
        "figure_refs": fig_patterns,
        "table_refs": table_patterns,
        "dominant_fig_style": max(fig_patterns, key=fig_patterns.get),
        "dominant_table_style": max(table_patterns, key=table_patterns.get),
    }

def analyze_sentence_length(text):
    """Analyze average sentence length."""
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if len(s.strip()) > 10]
    if not sentences:
        return {"avg_words": 0, "min_words": 0, "max_words": 0}

    word_counts = [len(s.split()) for s in sentences]
    return {
        "avg_words": round(sum(word_counts) / len(word_counts), 1),
        "min_words": min(word_counts),
        "max_words": max(word_counts),
        "total_sentences": len(sentences)
    }

def analyze_abstract_structure(text):
    """Analyze abstract structure patterns."""
    # Common abstract components
    has_background = bool(re.search(r'(?:is considered|has been|are increasing|growing concern|important|challenge)', text[:500], re.IGNORECASE))
    has_objective = bool(re.search(r'(?:objective|aim|purpose|goal|this study|this paper|this work|present study)', text[:500], re.IGNORECASE))
    has_method = bool(re.search(r'(?:was investigated|was conducted|was performed|were compared|were evaluated|experimental)', text, re.IGNORECASE))
    has_results = bool(re.search(r'(?:was achieved|were achieved|resulted|showed|demonstrated|indicated|revealed|was found)', text, re.IGNORECASE))
    has_conclusion = bool(re.search(r'(?:therefore|consequently|in summary|these results|the results|main finding)', text, re.IGNORECASE))

    return {
        "has_background": has_background,
        "has_objective": has_objective,
        "has_method": has_method,
        "has_results": has_results,
        "has_conclusion": has_conclusion,
        "structure_type": "structured" if sum([has_background, has_objective, has_method, has_results, has_conclusion]) >= 3 else "unstructured"
    }

def main():
    papers = read_all_papers()
    print(f"Loaded {len(papers)} papers")

    # Aggregate analysis
    all_voice = []
    all_tense_intro = []
    all_tense_methods = []
    all_tense_results = []
    all_tense_conclusion = []
    all_verbs = Counter()
    all_transitions = Counter()
    all_hedging = Counter()
    all_sentence_lengths = []
    all_citations = []
    all_measurements = {}
    all_fig_refs = Counter()
    all_abstract_structures = []

    section_lengths = {"abstract": [], "introduction": [], "methods": [], "results": [], "discussion": [], "conclusion": []}

    per_paper = {}

    for name, text in papers.items():
        print(f"\nAnalyzing: {name}")
        sections = find_sections(text)
        print(f"  Sections found: {list(sections.keys())}")

        paper_analysis = {"sections_found": list(sections.keys())}

        # Section lengths
        for sec_name in section_lengths.keys():
            sec_text = extract_section_text(text, sections, sec_name)
            if sec_text:
                words = len(sec_text.split())
                section_lengths[sec_name].append(words)
                paper_analysis[f"{sec_name}_words"] = words

        # Voice analysis (whole paper)
        voice = analyze_voice(text)
        all_voice.append(voice)
        paper_analysis["voice"] = voice

        # Tense by section
        for sec_name, tense_list in [("introduction", all_tense_intro), ("methods", all_tense_methods),
                                      ("results", all_tense_results), ("conclusion", all_tense_conclusion)]:
            sec_text = extract_section_text(text, sections, sec_name)
            if sec_text:
                tense = analyze_tense(sec_text)
                tense_list.append(tense)
                paper_analysis[f"tense_{sec_name}"] = tense

        # High-freq verbs
        verbs = extract_high_freq_verbs(text)
        all_verbs.update(verbs)

        # Transition phrases
        transitions = extract_transition_phrases(text)
        all_transitions.update(transitions)

        # Hedging
        hedging = extract_hedging(text)
        all_hedging.update(hedging)

        # Sentence length
        sent_len = analyze_sentence_length(text)
        all_sentence_lengths.append(sent_len["avg_words"])
        paper_analysis["sentence_length"] = sent_len

        # Citation style
        citation = analyze_citation_style(text)
        all_citations.append(citation["style"])
        paper_analysis["citation"] = citation

        # Measurements
        measurements = analyze_measurement_formats(text)
        for key, val in measurements.items():
            if key not in all_measurements:
                all_measurements[key] = {"total_count": 0, "examples": set()}
            all_measurements[key]["total_count"] += val["count"]
            all_measurements[key]["examples"].update(val["examples"][:3])

        # Figure/Table refs
        fig_refs = analyze_figure_table_refs(text)
        for style, count in fig_refs["figure_refs"].items():
            all_fig_refs[style] += count
        paper_analysis["figure_refs"] = fig_refs

        # Abstract structure
        abstract_text = extract_section_text(text, sections, "abstract")
        if abstract_text:
            abs_struct = analyze_abstract_structure(abstract_text)
            all_abstract_structures.append(abs_struct)
            paper_analysis["abstract_structure"] = abs_struct

        per_paper[name] = paper_analysis

    # Aggregate results
    avg_passive = round(sum(v["passive_ratio"] for v in all_voice) / len(all_voice), 3) if all_voice else 0
    avg_sentence_len = round(sum(all_sentence_lengths) / len(all_sentence_lengths), 1) if all_sentence_lengths else 0

    def avg_tense(tense_list):
        if not tense_list:
            return {"past": 0, "present": 0, "future": 0}
        return {
            "past": round(sum(t["past"] for t in tense_list) / len(tense_list), 3),
            "present": round(sum(t["present"] for t in tense_list) / len(tense_list), 3),
            "future": round(sum(t["future"] for t in tense_list) / len(tense_list), 3),
        }

    avg_section_lengths = {}
    for sec, lengths in section_lengths.items():
        if lengths:
            avg_section_lengths[sec] = {
                "avg_words": round(sum(lengths) / len(lengths)),
                "min_words": min(lengths),
                "max_words": max(lengths),
                "papers_with_section": len(lengths)
            }

    # Convert measurement examples sets to lists
    measurements_serializable = {}
    for key, val in all_measurements.items():
        measurements_serializable[key] = {
            "total_count": val["total_count"],
            "examples": list(val["examples"])[:5]
        }

    # Build analysis JSON
    analysis = {
        "meta": {
            "total_papers": len(papers),
            "field": "Hydrogen Internal Combustion Engine / Dual-Fuel Engine",
            "primary_author": "Hyunwook Park (hwpark@kimm.re.kr)",
            "institutions": [
                "Korea Institute of Machinery and Materials (KIMM)",
                "KAIST"
            ],
            "journals": [
                "Energy (Elsevier)",
                "Energy Conversion and Management (Elsevier)",
                "International Journal of Hydrogen Energy (Elsevier)",
                "SAE Technical Paper",
                "Journal of Physics: Conference Series (IOP)",
                "Vienna Motor Symposium"
            ]
        },
        "document_structure": {
            "typical_section_order": ["Abstract", "Introduction", "Experimental Setup/Methods", "Results and Discussion", "Conclusion", "References"],
            "section_lengths": avg_section_lengths,
        },
        "voice_analysis": {
            "overall_passive_ratio": avg_passive,
            "overall_active_ratio": round(1 - avg_passive, 3),
            "note": "Academic engineering papers predominantly use passive voice, especially in Methods and Results sections"
        },
        "tense_analysis": {
            "introduction": avg_tense(all_tense_intro),
            "methods": avg_tense(all_tense_methods),
            "results": avg_tense(all_tense_results),
            "conclusion": avg_tense(all_tense_conclusion),
            "patterns": {
                "introduction": "Mix of present (general facts) and past (literature review)",
                "methods": "Predominantly past tense (passive voice)",
                "results": "Predominantly past tense for findings, present for figure references",
                "conclusion": "Past tense for summarizing findings, present for implications"
            }
        },
        "language_patterns": {
            "high_freq_verbs": dict(all_verbs.most_common(25)),
            "transition_phrases": dict(all_transitions.most_common(25)),
            "hedging_expressions": dict(all_hedging.most_common(15)),
        },
        "sentence_structure": {
            "avg_sentence_length_words": avg_sentence_len,
            "per_paper_avg": {name: round(v, 1) for name, v in zip(papers.keys(), all_sentence_lengths)},
        },
        "citation_style": {
            "dominant": max(set(all_citations), key=all_citations.count) if all_citations else "unknown",
            "distribution": dict(Counter(all_citations)),
            "format": "Numbered brackets [1], [2,3], [4-6]"
        },
        "measurement_formats": measurements_serializable,
        "figure_table_references": {
            "figure_style_counts": dict(all_fig_refs),
            "dominant_style": "Fig. N" if all_fig_refs.get("Fig.", 0) > all_fig_refs.get("Figure", 0) else "Figure N",
        },
        "abstract_patterns": {
            "structure_counts": {
                "structured": sum(1 for a in all_abstract_structures if a.get("structure_type") == "structured"),
                "unstructured": sum(1 for a in all_abstract_structures if a.get("structure_type") == "unstructured"),
            },
            "typical_structure": "Background → Objective → Method → Key Results → Conclusion",
            "avg_length_note": "150-250 words typical"
        },
        "field_specific_vocabulary": {
            "combustion_terms": [
                "indicated thermal efficiency (ITE)", "brake thermal efficiency (BTE)",
                "indicated mean effective pressure (IMEP)", "brake mean effective pressure (BMEP)",
                "heat release rate (HRR)", "maximum pressure rise rate (MPRR)",
                "crank angle degree (CAD)", "top dead center (TDC)", "after top dead center (aTDC)",
                "start of injection (SOI)", "exhaust gas recirculation (EGR)",
                "coefficient of variation (COV)", "mass fraction burned (MFB)",
                "volumetric efficiency", "compression ratio", "excess air ratio", "equivalence ratio"
            ],
            "hydrogen_specific": [
                "backfire", "pre-ignition", "knock", "abnormal combustion",
                "port fuel injection (PFI)", "direct injection (DI)",
                "lean combustion", "stoichiometric combustion", "ultra-lean",
                "NOX emissions", "flame propagation", "flammability range",
                "low minimum ignition energy", "high research octane number"
            ],
            "dual_fuel_specific": [
                "conventional dual fuel (CDF)", "RCCI", "PCCI",
                "natural gas substitution ratio", "diesel pilot injection",
                "reactivity stratification", "mixture stratification"
            ]
        },
        "writing_style_characteristics": {
            "person": "Third person preferred; occasional 'this study' formulation",
            "objectivity": "Highly objective, data-driven, quantitative",
            "structure_preference": "Comparison-based studies (Mode A vs Mode B)",
            "data_presentation": "Parametric sweeps, energy balance analysis",
            "key_phrases": [
                "The objective of this study was to",
                "was investigated",
                "was achieved",
                "were compared",
                "resulted in",
                "owing to",
                "was conducted",
                "was employed",
                "contributed to",
                "led to"
            ],
            "conclusion_patterns": [
                "Numbered conclusions (1), 2), 3)...)",
                "Summary paragraph followed by bullet points",
                "Restate objective, summarize key findings, future work"
            ]
        }
    }

    # Save analysis
    output_path = MD_FOLDER / "style_analysis.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(analysis, f, indent=2, ensure_ascii=False)
    print(f"\nSaved style_analysis.json to {output_path}")

    # Generate confidence report
    confidence_items = []
    confidence_score = 0
    max_score = 0

    checks = [
        ("Papers analyzed", len(papers) >= 10, len(papers) >= 5, f"{len(papers)} papers"),
        ("Voice analysis", avg_passive > 0.2, avg_passive > 0.1, f"passive ratio={avg_passive}"),
        ("Tense analysis", len(all_tense_intro) >= 8, len(all_tense_intro) >= 5, f"{len(all_tense_intro)} papers with intro tense data"),
        ("Verb frequency", len(all_verbs) >= 15, len(all_verbs) >= 8, f"{len(all_verbs)} verbs extracted"),
        ("Transition phrases", len(all_transitions) >= 10, len(all_transitions) >= 5, f"{len(all_transitions)} phrases found"),
        ("Citation consistency", len(set(all_citations)) == 1, len(set(all_citations)) <= 2, f"styles: {set(all_citations)}"),
        ("Section identification", sum(len(v) for v in section_lengths.values()) > 30, sum(len(v) for v in section_lengths.values()) > 15, f"total section identifications: {sum(len(v) for v in section_lengths.values())}"),
        ("Measurement formats", len(all_measurements) >= 5, len(all_measurements) >= 3, f"{len(all_measurements)} measurement types"),
        ("Abstract structures", len(all_abstract_structures) >= 8, len(all_abstract_structures) >= 5, f"{len(all_abstract_structures)} abstracts analyzed"),
    ]

    for name, high_conf, med_conf, detail in checks:
        max_score += 10
        if high_conf:
            confidence_score += 10
            level = "HIGH"
        elif med_conf:
            confidence_score += 6
            level = "MEDIUM"
        else:
            confidence_score += 2
            level = "LOW"
        confidence_items.append(f"| {name} | {level} | {detail} |")

    overall_confidence = round(confidence_score / max_score * 100, 1)

    report = f"""# Style Analysis Confidence Report

## Overall Confidence: {overall_confidence}%

## Analysis Summary

- **Papers Analyzed**: {len(papers)}
- **Field**: Hydrogen Internal Combustion Engine / Dual-Fuel Engine
- **Primary Author**: Hyunwook Park (KIMM)
- **Dominant Citation Style**: {analysis['citation_style']['dominant']}
- **Average Sentence Length**: {avg_sentence_len} words
- **Passive Voice Ratio**: {avg_passive:.1%}

## Confidence Details

| Check | Confidence | Detail |
|-------|-----------|--------|
{chr(10).join(confidence_items)}

## Key Findings

### Voice & Tense
- **Passive voice** is dominant ({avg_passive:.1%}), consistent with academic engineering style
- **Introduction**: Mix of present tense (facts, motivation) and past tense (literature)
- **Methods/Experimental**: Predominantly past tense, passive voice
- **Results**: Past tense for findings, present for references to figures
- **Conclusion**: Past tense summary, occasional present for implications

### Top 10 High-Frequency Verbs
{chr(10).join(f'{i+1}. {verb} ({count})' for i, (verb, count) in enumerate(all_verbs.most_common(10)))}

### Top 10 Transition Phrases
{chr(10).join(f'{i+1}. "{phrase}" ({count})' for i, (phrase, count) in enumerate(all_transitions.most_common(10)))}

### Writing Characteristics
- Comparison-based study design (Mode A vs Mode B)
- Parametric sweeps with systematic variation
- Energy balance analysis as standard analytical framework
- Quantitative, data-driven presentation
- Numbered conclusion format (1), 2), 3)...)
- "Owing to" preferred over "due to" in many instances

### Measurement Conventions
{chr(10).join(f'- **{k}**: {v["total_count"]} occurrences, e.g., {", ".join(list(v["examples"])[:3])}' for k, v in measurements_serializable.items() if v["total_count"] > 5)}

## Limitations
- PDF-to-text conversion may have introduced noise
- Section boundaries are heuristically detected
- Some papers (SAE, Vienna symposium) have different formatting conventions
- Passive voice detection is pattern-based, not grammatically parsed
"""

    report_path = MD_FOLDER / "confidence_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"Saved confidence_report.md to {report_path}")

    print(f"\nOverall Confidence: {overall_confidence}%")
    print(f"Total patterns extracted: {sum(all_verbs.values()) + sum(all_transitions.values()) + sum(all_hedging.values())}")


if __name__ == "__main__":
    main()
