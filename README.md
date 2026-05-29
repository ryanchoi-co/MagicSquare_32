# Magic_Square_XX

4×4 **일반 마방진**을 다루는 프로그램 프로젝트입니다.  
현재 단계는 **문제 정의(STEP 1~5)** 와 **TDD·Clean Architecture 설계(Report 02)** 까지 완료되었으며, **구현은 아직 시작하지 않았습니다.**

---

## 프로젝트 한 줄 요약

**4×4 격자에 1~16을 각각 한 번 배치했을 때, 고정한 라인(행 4·열 4·주대각 2)의 합이 모두 34인지를 반복적으로 판정할 수 있는 기준을 세우고, 유효·무효 사례를 구분하며, (선택적으로) 그 기준을 만족하는 배치를 확보하는 연습을 한다.**

표면적으로 말하는 「마방진 프로그램을 만든다」가 아니라, **판정 기준 · 불변 · 사고 훈련**을 먼저 고정하는 것이 이 저장소의 출발점입니다.

---

## 문제 범위 (현재 합의)

| 항목 | 내용 |
|------|------|
| 격자 | 4×4 (16칸) |
| 값 | 1~16, 중복·누락 없음 |
| 마법 상수 | 34 |
| 검사 라인 | 행 4 + 열 4 + **주대각** 2 |
| 1차 목적 | 위 규칙에 대한 **일관된 판정** |
| 2차 목적 (선택) | 유효 배치 **하나 이상** 확보 |

### 핵심 불변 (Invariant)

| ID | 내용 |
|----|------|
| **C1** | 정확히 4×4, 16칸 |
| **C2** | 값 = {1, …, 16} 각 1회 |
| **C3** | 지정 10개 라인의 합 = 34 |
| **C4** | 라인 집합 = 행4 + 열4 + 주대각2 |
| **C5** | 1+…+16 = 136 = 4×34 |
| **V1** | 동일 입력 → 동일 판정 |
| **V2** | 무효 시 위반 종류 구분 가능 |
| **V3** | 규칙 변경 시 의도 없는 회귀 없음 |

자세한 유도·Why 분석은 [보고서](Report/01.Magic_Square_Problem_Definition_Report.md)를 참고하세요.

---

## 왜 이 프로젝트인가

| 단계 | 질문 | 요약 |
|------|------|------|
| STEP 1 | 무엇을 다루는가 | 4×4·합 규칙을 **반복·검증 가능**하게 다루려는 상황 |
| STEP 2 | 왜 완성하는가 | 유효 배치 확보·검증 — 단, 「완성」 정의가 여러 갈래 |
| STEP 3 | 왜 프로그램인가 | 반복, 검증 자동화, 오류 억제, **규칙의 명시화** |
| STEP 4 | 왜 TDD 관점인가 | 통제·불변·**명확한 입출력** = 실행 가능한 명세 |
| STEP 5 | 진짜 문제는 | **판정 기준** 위에서만 「완성」을 말하는 연습 문제 |

---

## 훈련하려는 사고 능력

- 규칙의 명시화 · 불변식 사고 · 계약·경계 사고  
- 반례·케이스 설계 · **판정 vs 구성** 책임 분리  
- 검산·신뢰 · 점진적 범위 관리 (`XX` = 추후 확장 여지)

구현 기술 자체보다, **「무엇이 맞는가」를 흔들리지 않게 고정하는 것**이 1차 목표입니다.

---

## 저장소 구조

```
Magic_Square_XX/
├── README.md
├── Report/
│   ├── 01.Magic_Square_Problem_Definition_Report.md
│   └── 02.Magic_Square_TDD_Clean_Architecture_Design_Report.md
└── Prompt/
    ├── 01.Magic_Square_Interactive_Prompt_Transcript.md
    └── 02.Magic_Square_TDD_Design_Interactive_Prompt_Transcript.md
```

---

## 문서 가이드

| 문서 | 용도 |
|------|------|
| [01.Magic_Square_Problem_Definition_Report.md](Report/01.Magic_Square_Problem_Definition_Report.md) | 관찰, Why #1~#3, 진짜 문제 정의, 열린 결정 |
| [02.Magic_Square_TDD_Clean_Architecture_Design_Report.md](Report/02.Magic_Square_TDD_Clean_Architecture_Design_Report.md) | Dual-Track UI+Logic, Domain/UI/Data 계약·테스트·통합 |
| [01.Magic_Square_Interactive_Prompt_Transcript.md](Prompt/01.Magic_Square_Interactive_Prompt_Transcript.md) | 문제 정의 STEP 1~5 재실행 |
| [02.Magic_Square_TDD_Design_Interactive_Prompt_Transcript.md](Prompt/02.Magic_Square_TDD_Design_Interactive_Prompt_Transcript.md) | TDD·CA 설계 Turn 1~3 재실행 |

새 채팅에서 문제 정의만 다시 돌리려면 `Prompt/`의 MASTER 또는 Turn별 블록을 순서대로 사용하면 됩니다.

---

## 현재 상태

| 구분 | 상태 |
|------|------|
| 문제 인식 · Why · 진짜 문제 정의 | ✅ 완료 (Report 01) |
| TDD · Dual-Track · Clean Architecture 설계 | ✅ 완료 (Report 02) |
| 소스 코드 · 테스트 | ❌ 없음 |

---

## 열린 결정 (구현 전에 확정 필요)

1. **출력:** 맞음/틀림만 vs **어느 라인이 깨졌는지** 진단  
2. **생성 범위:** 해 하나 / 표준 배치 / 전체 열거  
3. **대각:** 주대각 2개만 vs 추가 선(패닝 대각 등)  
4. **동형:** 회전·반사를 같은 해로 볼지 여부  
5. **완료 정의:** 검증기 우선 vs 생성 포함  

---

## 권장 다음 단계

1. Report 02 체크리스트: **F-OK-01** golden·A/B/both-fail 픽스처 확정  
2. **Red** 순서대로 Domain → UI(Mock) → Data → Integration 테스트 구현  
3. Report 02 **RG-01~06** 회귀 규칙 유지  

`Prompt/02.*` transcript로 설계 워크플로를 새 세션에서 재실행할 수 있습니다.

---

## RED 단계 To-Do 리스트

> 이 체크리스트는 [docs/test_plan.md](docs/test_plan.md) 기반으로 생성되었습니다.
> 각 항목은 RED(실패 테스트 작성) 완료 시 체크합니다.

### Track A — UI / Boundary 테스트
- [ ] TC-A-01: grid=None 입력 → 실패 결과 반환 (Happy Path of Failure)
- [ ] TC-A-02: code가 정확히 "INVALID_SIZE" 문자열인지 검증
- [ ] TC-A-03: message가 "Grid must be 4x4." 와 문자 단위 동일한지 검증
- [ ] TC-A-04: grid=None 시 Domain 진입점 0회 호출 (mock/spy 검증)
- [ ] TC-A-05: grid=[] 빈 리스트 → 실패 결과 반환
- [ ] TC-A-06: grid=3×4 크기 불일치 → 실패 결과 반환
- [ ] TC-A-07: 반환 객체 타입이 지정 실패 결과 구조체인지 검증

### Track B — Domain / Logic 테스트
- [ ] TC-B-01: resolve()가 None grid를 직접 받지 않음을 격리 검증
- [ ] TC-B-02: Boundary가 None 분기를 처리 후 resolve() 미호출 확인
- [ ] TC-B-03: resolve() mock이 호출됐을 경우 테스트 실패 처리
- [ ] TC-B-04: AC-FR-01-02~05 범위의 케이스는 이 커밋에 포함하지 않음 확인

### 커버리지 목표
- [ ] Domain Logic: 95%+ (pip install pytest-cov)
- [ ] Boundary Layer: 85%+
- [ ] 전체 TOTAL: 90%+

### 결함 목록 연결
- [x] [defect_list.md](docs/defect_list.md) 생성 및 발견 결함 기록 (DEF-001~009, 2026-05-29)
- [ ] 모든 결함 수정 후 회귀 테스트 통과 확인

---

## 라이선스 · 기여

아직 미정. 구현 단계 진입 시 추가 예정.

---

*최종 갱신: 2026-05-28 · Report 01·02, Prompt 01·02 동기화*
