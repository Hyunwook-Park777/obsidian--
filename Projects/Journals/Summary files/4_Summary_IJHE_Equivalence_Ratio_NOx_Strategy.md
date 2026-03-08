# SCIE Journal Summary

---

## 1. Paper Information

| Item                       | Details |
| -------------------------- | ------- |
| **Title**                  | Effect of Equivalence Ratios on the Power, Combustion Stability and NOx Controlling Strategy for the Turbocharged Hydrogen Engine at Low Engine Speeds |
| **Authors**                | Qing-he Luo, Ji-Bin Hu, Bai-gang Sun*, Fu-shui Liu, Xi Wang, Chao Li, Ling-zhi Bao |
| **Journal**                | International Journal of Hydrogen Energy |
| **Volume / Issue / Pages** | Vol. 44, pp. 17095-17102 |
| **Year**                   | 2019 |
| **DOI**                    | 10.1016/j.ijhydene.2019.03.245 |
| **IF (Impact Factor)**     | - |
| **Keywords**               | Turbocharged, Hydrogen engine, H2-TWC, Low engine speeds |

---

## 2. Research Background & Objective

- **Research Gap:** 터보차저 수소 엔진은 저속에서 터빈 에너지 부족으로 토크가 감소하는 문제가 있음. 기존 EGR+TWC NOx 저감 전략은 수증기 열용량 한계, 냉각 EGR의 수분 부식, 고온 배기의 역화 위험 등의 문제 존재. 수소 자체를 TWC 환원제로 활용하는 전략에 대한 연구 필요.
- **Objective:** 2.3L 터보차저 PFI 수소 엔진에서 저속(1500/2000 rpm) 당량비 증가가 출력, BTE, 연소안정성에 미치는 영향을 분석하고, H2+TWC를 이용한 NOx 제어 전략의 타당성 검증.

---

## 3. Methodology

- **Approach:** 실험 연구. 저속(1500/2000 rpm) 조건에서 당량비(λ=0.4-1.1) 변화에 따른 출력, BTE, 연소안정성(COVimep) 분석. TWC 전후 NOx 측정으로 H2+TWC 전략 검증.
- **Tools / Software:** CW250 와전류 동력계, PROtronic/Simulink 기반 ECU, Kistler 연소분석기, CMF010/CMF025 유량계, AVL DiGas 4000 Light
- **Experimental / Simulation Conditions:**
  - 엔진: 2.3L, 4기통, PFI 터보차저 수소 엔진 (CR 9.3, 논문 #2/#3과 동일)
  - 속도: 1500 rpm (스로틀 17°), 2000 rpm (스로틀 16°)
  - 당량비: λ = 0.4-1.1
  - TWC 전후 NOx 동시 측정

---

## 4. Key Results

1. **출력:** 당량비 증가 시 출력 상승(2000 rpm: 6.8→21 kW, 1500 rpm: 6.4→16.5 kW). 최대 출력 λ: 1500 rpm에서 0.8, 2000 rpm에서 0.9(터보 압력 차이). λ 초과 시 수소가 실린더 체적을 점유하여 공기량 감소 → 출력 하락.
2. **BTE:** 최대 BTE 30.1% (2000 rpm), 29.3% (1500 rpm) λ=0.65-0.8 범위. 기계효율 향상(73%→92%)과 연소지속기간 단축(25.4→5.1°CA)이 주요 원인.
3. **연소안정성:** COVimep < 1.5%로 매우 안정. 당량비 증가 시 COVimep 감소(1500 rpm: 0.85%→0.35%). 150 사이클 이상이면 누적평균 변동폭 <0.3%.
4. **H2+TWC 전략:** λ>0.95에서 TWC 후단 NOx 절벽 하락. 양론비에서 전환효율 >99% (1500 rpm: 877→0 ppm, 2000 rpm: 1259→17 ppm). 수소가 최적 환원제 역할.

---

## 5. Discussion & Contribution

- **Novelty:** 수소를 TWC 환원제로 직접 활용하는 H2+TWC NOx 제어 전략의 실험적 검증. 기존 EGR+TWC의 문제(수분 부식, 역화 위험)를 회피. 저속 터보차저 수소 엔진에서 당량비 증가의 출력/효율/안정성 종합 분석.
- **Limitations:** 저속(1500/2000 rpm) 2개 조건만 시험. 양론비 초과 운전 시 연료 소비 증가에 대한 정량적 분석 부족. TWC 내구성/열화 미고려.
- **Future Work:** 중/고속 영역으로 확장. TWC 장기 내구성 평가. H2+TWC 전략의 과도운전 적용성 검증.

---

## 6. Relevance to My Research

> Digital Twin / Carbon-Free Engine 관점에서의 활용 가능성

- **Applicable Concepts:** H2+TWC 전략은 추가 장비(EGR 쿨러, 환원제 탱크) 없이 NOx를 제어할 수 있는 단순하고 효과적인 방법. 디지털 트윈 기반 λ 정밀 제어의 핵심 대상.
- **Potential Application:** λ=0.95 임계점에서의 NOx 절벽 하강 현상을 활용한 실시간 λ 피드백 제어 설계. COVimep 데이터로 연소안정성 모니터링 모델 구축.
- **Related References:** 논문 #1 (Verhelst, EGR+TWC 원형), 논문 #2 (동일 엔진 에너지 분석), 논문 #3 (동일 엔진 연소 특성)

---

## 7. Key Figures & Tables

| Figure / Table | Description | Page |
|----------------|-------------|------|
| Fig. 2 | 출력 vs 당량비 (1500/2000 rpm) | 3 |
| Fig. 5 | BTE vs 당량비 | 3 |
| Fig. 8 | 연소지속기간 vs 당량비 | 4 |
| Fig. 12 | COVimep vs 당량비 | 5 |
| Fig. 15-16 | TWC 전후 NOx vs 당량비 (1500/2000 rpm) | 6 |
| Fig. 17 | 양론비에서 TWC 전/후 NOx 비교 | 6 |

---

## 8. Notable Equations

| Eq. No. | Equation | Description |
|---------|----------|-------------|
| - | COVimep = σ(IMEP) / mean(IMEP) × 100% | 연소안정성 평가 지표. 터보 수소 엔진에서 <1.5% |

---

## 9. Personal Notes

- **Rating:** ★★★★★ (5/5)
- **Read Date:**
- **Memo:** H2+TWC 전략의 핵심 논문. λ>0.95에서 NOx 절벽 하강 현상은 매우 실용적. 논문 #1(Verhelst)의 EGR+TWC를 더 단순한 H2+TWC로 대체한 진보. 저속 성능 개선 + NOx 제어를 동시에 달성. 시리즈 논문(#2→#3→#4) 중 전략적 완성편.

---
