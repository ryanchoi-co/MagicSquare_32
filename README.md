# Magic_Square_XX

4×4 **일반 마방진**을 다루는 프로그램 프로젝트입니다.  
현재 단계는 **문제 정의 · TDD·Clean Architecture 설계** 완료 후, **Dual-Track TDD RED → GREEN** 진행 중입니다.  
AC-FR-01-01 Boundary **1차 GREEN**(`grid=None` → `INVALID_SIZE`)까지 반영되었습니다.

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
├── pyproject.toml
├── docs/
│   ├── test_plan.md          # AC-FR-01-01 테스트 계획 (TP-AC-FR-01-01)
│   └── defect_list.md        # 결함 목록 DEF-001~009
├── src/magicsquare/
│   ├── boundary/             # GREEN 진행 중 (dto, ports, orchestrator)
│   └── entity/               # User 엔티티 (DT-USER-*)
├── tests/
│   ├── boundary/             # AC-FR-01-01 RED 33건 + U-IN/U-OUT skeleton
│   ├── entity/
│   └── fixtures/
├── Report/                   # 01~10 설계·QA·GREEN 보고서
└── Prompt/                   # 01~14 Interactive Transcript
```

---

## 문서 가이드

| 문서 | 용도 |
|------|------|
| [01.Magic_Square_Problem_Definition_Report.md](Report/01.Magic_Square_Problem_Definition_Report.md) | 관찰, Why #1~#3, 진짜 문제 정의 |
| [02.Magic_Square_TDD_Clean_Architecture_Design_Report.md](Report/02.Magic_Square_TDD_Clean_Architecture_Design_Report.md) | Dual-Track, Domain/UI/Data 계약·테스트·통합 (SSOT) |
| [07 … AC-FR-01-01 RED QA](Report/07.Magic_Square_AC_FR_01_01_RED_QA_And_Transcript_Export_Report.md) | RED 테스트·결함 목록·QA 산출물 |
| [08 … FR01~05 RED 설계](Report/08.Magic_Square_FR01_FR05_Dual_Track_RED_Design_Report.md) | U-IN/D-SOL 설계표 |
| [09 … RED Skeleton](Report/09.Magic_Square_FR01_FR05_RED_Skeleton_And_Transcript_Export_Report.md) | Boundary/Domain skeleton 23건 |
| [10 … AC-FR-01-01 GREEN](Report/10.Magic_Square_AC_FR_01_01_GREEN_And_Transcript_Export_Report.md) | BV-01 `grid=None` GREEN 1사이클 |
| [11 … GREEN 로드맵 · README](Report/11.Magic_Square_GREEN_Roadmap_And_README_Update_Report.md) | G-01~G-05 커밋 계획 · To-Do 갱신 |
| [docs/test_plan.md](docs/test_plan.md) | AC-FR-01-01 pytest 범위·BV·커버리지 |
| [docs/defect_list.md](docs/defect_list.md) | RED 실행 기반 결함 DEF-001~009 |
| [Prompt/11 … RED QA Transcript](Prompt/11.Magic_Square_AC_FR_01_01_RED_QA_Interactive_Prompt_Transcript.md) | RED QA 세션 Export |
| [Prompt/14 … GREEN Transcript](Prompt/14.Magic_Square_AC_FR_01_01_GREEN_Interactive_Prompt_Transcript.md) | GREEN 1사이클 Export |
| [Prompt/15 … 로드맵 Transcript](Prompt/15.Magic_Square_GREEN_Roadmap_And_README_Update_Interactive_Prompt_Transcript.md) | GREEN 로드맵 · README 갱신 Export |

---

## 현재 상태

| 구분 | 상태 |
|------|------|
| 문제 인식 · Why · 진짜 문제 정의 | ✅ 완료 (Report 01) |
| TDD · Dual-Track · Clean Architecture 설계 | ✅ 완료 (Report 02) |
| AC-FR-01-01 RED 테스트 | ✅ 33건 수집 (`test_ac_fr_01_01_invalid_size.py`) |
| AC-FR-01-01 GREEN (Boundary) | 🔄 **30 / 33 passed** — BV-01~04a 구현 |
| Boundary 스켈레ton | ✅ `dto`, `ports`, `orchestrator` (최소) |
| Domain 솔버 · Control | ❌ 미착수 |
| Entity User (DT-USER-*) | ✅ 9 passed |

### 최근 pytest (AC-FR-01-01 스위트)

```bash
.venv\Scripts\python.exe -m pytest tests/boundary/test_ac_fr_01_01_invalid_size.py -q
# 30 passed, 3 failed  (BV-04b 대기)
```

---

## 로컬 실행

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -e ".[dev]"

# AC-FR-01-01 전체
pytest tests/boundary/test_ac_fr_01_01_invalid_size.py -v

# HTML 커버리지
pytest --cov=src/magicsquare/boundary --cov-report=html
# → htmlcov/index.html
```

> `pydantic`은 dev 의존성입니다. 시스템 Python 대신 **`.venv`** 를 사용하세요.

---

## TDD To-Do 체크리스트

> 기준: [docs/test_plan.md](docs/test_plan.md), [docs/defect_list.md](docs/defect_list.md)  
> **RED** = 실패 테스트 존재 · **GREEN** = 최소 구현으로 해당 테스트 통과  
> GREEN 커밋 묶음: **BV 입력 오름차순** (G-01 → G-05)

### Phase 0 — RED (테스트 작성)

| ID | 항목 | 상태 |
|----|------|------|
| R-0 | AC-FR-01-01 Boundary RED 33건 | [x] |
| R-1 | FR-01~05 Boundary skeleton 11건 | [x] |
| R-2 | Domain `test_d_*` / `Grid4x4.fromRaw` RED | [ ] |
| R-3 | Integration IT-03 RED | [ ] |

### Phase 1 — GREEN · AC-FR-01-01 (Boundary, BV 오름차순)

| 커밋 | BV | 입력 | 구현 분기 | pytest (대표) | GREEN |
|------|-----|------|-----------|---------------|-------|
| **G-01** | BV-01 | `None` | `grid is None` | `test_none_grid_returns_invalid_size_code` | [x] |
| **G-02** | BV-02 | `[]` | `len(grid) == 0` | `test_empty_list_returns_invalid_size_code` | [x] |
| **G-03** | BV-03 | `[[]]*4` | `any(len(row) == 0 …)` | `test_four_empty_rows_returns_invalid_size_code` | [x] |
| **G-04** | BV-04a | 3×4 | `len(grid) != 4` | `test_3x4_grid_returns_invalid_size_code` | [x] |
| **G-05** | BV-04b | 4×3 | (열 길이 검사) | `test_4x3_grid_returns_invalid_size_code` | [ ] |

**G-01 완료 시 통과 항목 (Track A/B)**

- [x] TC-A-01: `grid=None` → 실패 결과 반환
- [x] TC-A-02: `code == "INVALID_SIZE"`
- [x] TC-A-03: `message == "Grid must be 4x4."` (문자 단위)
- [x] TC-A-04: `grid=None` 시 `resolve()` 0회 (mock)
- [x] TC-A-07: 반환 타입 `ValidationFailureResult`
- [x] TC-B-01~03: None 입력 시 Domain 포트 격리

**G-02 완료 시 추가 통과**

- [x] TC-A-05: `grid=[]` → `INVALID_SIZE`
- [x] `grid=[]` 시 `resolve()` 0회 (mock)
- [x] `grid=[]` message 문자 단위 일치

**G-03 완료 시 추가 통과**

- [x] `grid=[[]]*4` → `INVALID_SIZE`
- [x] `grid=[[]]*4` 시 `resolve()` 0회 (mock)

**G-04 완료 시 추가 통과**

- [x] TC-A-06 (3×4): `grid=3×4` → `INVALID_SIZE`
- [x] `grid=3×4` 시 `resolve()` 0회 (mock)

**G-05 대기**
- [ ] AC-FR-01-01 스위트 **33 passed** (DoD)

### Phase 2 — GREEN · FR-01 확장 (Report/08, skeleton)

| Test ID | AC | 파일 | GREEN |
|---------|-----|------|-------|
| U-IN-04~05 | FR-01-02 빈칸 개수 | `test_u_in_validation.py` | [ ] |
| U-IN-06~07 | FR-01-03 값 범위 | 동일 | [ ] |
| U-IN-08 | FR-01-04 중복 | 동일 | [ ] |
| U-FLOW-02 | Story 1 격리 | `test_u_flow_isolation.py` | [ ] |
| U-OUT-01~03 | FR-01-05 출력 계약 | `test_u_out_contract.py` | [ ] |

> U-IN-01~03은 `test_ac_fr_01_01_invalid_size.py`와 중복 — Phase 1 완료로 커버.

### Phase 3 — Domain · Integration

- [ ] Domain L0: `Grid4x4.fromRaw`, `D_ERR_NOT_4X4` (DT-GRID-*)
- [ ] Domain L1~L3: 빈칸·누락·솔버 (D-LOC / D-MIS / D-SOL)
- [ ] Integration IT-03: not-4×4 E2E

### 커버리지 목표

- [ ] Boundary Layer: **≥ 85%** (`pytest --cov=src/magicsquare/boundary`)
- [ ] Domain Logic: **≥ 95%** (`pytest --cov=src/magicsquare/entity`)
- [ ] 전체 TOTAL: **≥ 90%**

### 결함 목록 ([docs/defect_list.md](docs/defect_list.md))

- [x] DEF-001: `magicsquare.boundary` 패키지 생성
- [x] DEF-002: `ValidationFailureResult` DTO
- [x] DEF-003: `DomainSolverPort` + `resolve()`
- [ ] DEF-004: orchestrator size 검증 전체 (현재 `None`, `[]`, 빈 행)
- [ ] DEF-005: 열 길이 분기 (G-05)
- [ ] DEF-006: 3×4 분기 (G-04 완료)
- [ ] DEF-007: Boundary 커버리지 ≥ 85% 재측정
- [ ] DEF-008: Presenter·ERROR 문자열 RG-03 정합
- [ ] 모든 결함 수정 후 AC-FR-01-01 회귀 **33 passed**

---

## 열린 결정 (구현 전에 확정 필요)

1. **출력:** 맞음/틀림만 vs **어느 라인이 깨졌는지** 진단  
2. **생성 범위:** 해 하나 / 표준 배치 / 전체 열거  
3. **대각:** 주대각 2개만 vs 추가 선(패닝 대각 등)  
4. **동형:** 회전·반사를 같은 해로 볼지 여부  
5. **완료 정의:** 검증기 우선 vs 생성 포함  
6. **오류 문자열:** 테스트 플랜 `Grid must be 4x4.` vs Report/02 `ERROR: grid must be 4x4` (DEF-008)

---

## 권장 다음 단계

1. **G-05 GREEN:** 4×3 → AC-FR-01-01 **33 passed**  
3. Report 02 **RG-01~06** 회귀 규칙 유지 (golden·assert 완화 금지)  
4. REFACTOR는 AC-FR-01-01 전체 GREEN 후 별도 사이클  

---

## 라이선스 · 기여

아직 미정. 구현 단계 진입 시 추가 예정.

---

*최종 갱신: 2026-05-29 · AC-FR-01-01 GREEN G-01, Report 07~11, Prompt 11·14·15, docs/defect_list.md*
