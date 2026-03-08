"""PDF to Markdown converter using pdftext (MinerU's text extraction backend)."""
import os
import sys
from pathlib import Path

def convert_pdf_to_md(pdf_path: Path, output_dir: Path) -> bool:
    """Convert a single PDF to Markdown using pdftext."""
    try:
        from pdftext.extraction import plain_text_output

        # Extract text
        text = plain_text_output(str(pdf_path))

        # Create output filename
        stem = pdf_path.stem
        # Sanitize filename
        safe_name = stem.replace(" ", "_").replace(",", "").replace(".", "_")
        md_path = output_dir / f"{safe_name}.md"

        # Write markdown
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# {stem}\n\n")
            f.write(text)

        print(f"  OK: {pdf_path.name} -> {md_path.name}")
        return True
    except Exception as e:
        print(f"  FAIL: {pdf_path.name} - {e}")
        # Fallback: try pypdf
        try:
            from pypdf import PdfReader
            reader = PdfReader(str(pdf_path))
            text_parts = []
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)

            text = "\n\n".join(text_parts)
            stem = pdf_path.stem
            safe_name = stem.replace(" ", "_").replace(",", "").replace(".", "_")
            md_path = output_dir / f"{safe_name}.md"

            with open(md_path, "w", encoding="utf-8") as f:
                f.write(f"# {stem}\n\n")
                f.write(text)

            print(f"  OK (pypdf fallback): {pdf_path.name} -> {md_path.name}")
            return True
        except Exception as e2:
            print(f"  FAIL (both methods): {pdf_path.name} - {e2}")
            return False


def main():
    pdf_folder = Path(r"C:\Users\hwpar\Desktop\Claude_Code\Projects\Journal_summary")
    output_dir = pdf_folder / "converted_md"
    output_dir.mkdir(exist_ok=True)

    # Find all PDFs recursively
    pdf_files = list(pdf_folder.glob("**/*.pdf"))
    # Exclude any PDFs in output directory
    pdf_files = [p for p in pdf_files if "converted_md" not in str(p)]

    print(f"Found {len(pdf_files)} PDF files")
    print(f"Output directory: {output_dir}")
    print("=" * 60)

    success = 0
    failed = 0

    for pdf_path in sorted(pdf_files):
        print(f"\nConverting: {pdf_path.name}")
        if convert_pdf_to_md(pdf_path, output_dir):
            success += 1
        else:
            failed += 1

    print("\n" + "=" * 60)
    print(f"Results: {success} success, {failed} failed, {len(pdf_files)} total")


if __name__ == "__main__":
    main()
