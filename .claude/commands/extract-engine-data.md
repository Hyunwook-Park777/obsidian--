Data 폴더($ARGUMENTS 또는 기본 경로)의 모든 .xls 엔진 시험 데이터 파일에서 핵심 성능 컬럼을 추출하여 하나의 Excel 파일로 통합해줘.

## 수행 절차
1. 지정된 폴더(기본: Projects/퇴직준비세미나/Homeworks/Phase 2/Data)에서 .xls 파일을 탐색
2. 각 파일의 컬럼 구조를 확인
3. 다음 컬럼을 추출: Time, DynoTorque_Avg, BrakePower_Avg, FuelMassFlowRate_Avg, IntakeAirMassFlow_Avg, BSFC_Avg
4. Source_File 컬럼을 추가하여 출처 추적 가능하게 함
5. 모든 파일을 통합하여 Extracted_Performance_Data.xlsx로 저장
6. 결과 미리보기를 출력

## 주의사항
- pandas, openpyxl, xlrd 라이브러리가 필요함 (없으면 자동 설치)
- .xls 파일이 없으면 오류 메시지 출력
- 기존 출력 파일이 있으면 덮어쓰기
