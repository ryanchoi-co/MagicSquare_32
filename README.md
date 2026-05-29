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
│   ├── boundary/             # dto, ports, orchestrator, presenter, screen/ (ui_boundary·input_validator 예정)
│   ├── control/              # (예정) solve_partial_magic_square — use case
│   └── entity/               # User (DT-USER-*); solver·Grid4x4 (예정)
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
| [12 … Phase 1 GREEN G-02~G-05](Report/12.Magic_Square_AC_FR_01_01_Phase1_GREEN_G02_G05_And_Transcript_Export_Report.md) | BV-02~04b GREEN · 33 passed DoD |
| [13 … PyQt GUI · Demo](Report/13.Magic_Square_PyQt_GUI_And_Demo_Fix_And_Transcript_Export_Report.md) | PyQt6 Screen Layer · BV-04a/b 데모 정합 |
| [14 … Golden Master](Report/14.Magic_Square_Golden_Master_And_Transcript_Export_Report.md) | Approval 회귀 · GM-TC-01~05 · baseline |
| [15 … REFACTOR · ECB 분석](Report/15.Magic_Square_REFACTOR_ECB_Analysis_And_README_Update_Report.md) | 코드 리뷰 · ECB · 리팩토링 계획 · README |
| [16 … REFACTOR 프로그램 · Phase 0](Report/16.Magic_Square_REFACTOR_Program_Phase0_And_README_3Group_ToDo_Report.md) | 3그룹 To-Do · Phase 0 게이트 · Wave 로드맵 |
| [docs/test_plan.md](docs/test_plan.md) | AC-FR-01-01 pytest 범위·BV·커버리지 |
| [docs/defect_list.md](docs/defect_list.md) | RED 실행 기반 결함 DEF-001~009 |
| [Prompt/11 … RED QA Transcript](Prompt/11.Magic_Square_AC_FR_01_01_RED_QA_Interactive_Prompt_Transcript.md) | RED QA 세션 Export |
| [Prompt/14 … GREEN Transcript](Prompt/14.Magic_Square_AC_FR_01_01_GREEN_Interactive_Prompt_Transcript.md) | GREEN 1사이클 Export |
| [Prompt/15 … 로드맵 Transcript](Prompt/15.Magic_Square_GREEN_Roadmap_And_README_Update_Interactive_Prompt_Transcript.md) | GREEN 로드맵 · README 갱신 Export |
| [Prompt/16 … Phase 1 GREEN Transcript](Prompt/16.Magic_Square_AC_FR_01_01_Phase1_GREEN_G02_G05_Interactive_Prompt_Transcript.md) | G-02~G-05 GREEN · 33 passed Export |
| [Prompt/17 … PyQt GUI Transcript](Prompt/17.Magic_Square_PyQt_GUI_And_Demo_Fix_Interactive_Prompt_Transcript.md) | PyQt6 GUI · Demo BV 정합 Export |
| [Prompt/18 … Golden Master Transcript](Prompt/18.Magic_Square_Golden_Master_Interactive_Prompt_Transcript.md) | Golden Master · GM-TC Export |
| [Prompt/19 … REFACTOR ECB Transcript](Prompt/19.Magic_Square_REFACTOR_ECB_Analysis_Interactive_Prompt_Transcript.md) | REFACTOR · ECB 분석 Export |
| [Prompt/20 … REFACTOR 프로그램 Transcript](Prompt/20.Magic_Square_REFACTOR_Program_And_3Group_ToDo_Interactive_Prompt_Transcript.md) | 3그룹 To-Do · Phase 0 · Wave 로드맵 Export |

---

## 현재 상태

| 구분 | 상태 |
|------|------|
| 문제 인식 · Why · 진짜 문제 정의 | ✅ 완료 (Report 01) |
| TDD · Dual-Track · Clean Architecture 설계 | ✅ 완료 (Report 02) |
| AC-FR-01-01 RED 테스트 | ✅ 33건 수집 (`test_ac_fr_01_01_invalid_size.py`) |
| AC-FR-01-01 GREEN (Boundary) | ✅ **33 / 33 passed** — Phase 1 완료 |
| Boundary 스켈레ton | ✅ `dto`, `ports`, `orchestrator`, `presenter`, PyQt `screen/` |
| Domain 솔버 · Control | ❌ 미착수 |
| Entity User (DT-USER-*) | ✅ 9 passed |

### 최근 pytest (AC-FR-01-01 스위트)

```bash
.venv\Scripts\python.exe -m pytest tests/boundary/test_ac_fr_01_01_invalid_size.py -q
# 33 passed  (Phase 1 DoD 달성)
```

---

## 로컬 실행

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -e ".[dev]"

# PyQt GUI (선택)
pip install -e ".[gui]"
python -m magicsquare.boundary.screen
# 또는: magicsquare-gui

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

### Golden Master 회귀 안전장치

> Refactoring 시작 전 구축. GREEN 완료 후 즉시 적용.

#### 기준 파일 생성

- [x] **GM-01:** `golden_master_expected.txt` 생성
- [x] **GM-02:** 정상/역순/오류 시나리오 추가
- [x] **GM-03:** `git add tests/golden_master_expected.txt`

#### 테스트 코드

- [x] **GM-04:** `test_golden_master_magic_square` 작성
- [x] **GM-05:** approve 패턴 적용
- [x] **GM-06:** Golden Master 테스트 PASS 확인

```bash
pytest -m golden_master -v
# 6 passed
```

#### 회귀 보호

- [x] **GM-07:** row-major 규칙 보호
- [x] **GM-08:** 1-index 출력 보호
- [x] **GM-09:** reverse 조합 fallback 보호
- [x] **GM-10:** Error Contract 보호

> 설계: [docs/golden_master_approve_design.md](docs/golden_master_approve_design.md)

### Phase 1 — GREEN · AC-FR-01-01 (Boundary, BV 오름차순)

| 커밋 | BV | 입력 | 구현 분기 | pytest (대표) | GREEN |
|------|-----|------|-----------|---------------|-------|
| **G-01** | BV-01 | `None` | `grid is None` | `test_none_grid_returns_invalid_size_code` | [x] |
| **G-02** | BV-02 | `[]` | `len(grid) == 0` | `test_empty_list_returns_invalid_size_code` | [x] |
| **G-03** | BV-03 | `[[]]*4` | `any(len(row) == 0 …)` | `test_four_empty_rows_returns_invalid_size_code` | [x] |
| **G-04** | BV-04a | 3×4 | `len(grid) != 4` | `test_3x4_grid_returns_invalid_size_code` | [x] |
| **G-05** | BV-04b | 4×3 | `any(len(row) != 4 …)` | `test_4x3_grid_returns_invalid_size_code` | [x] |

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

**G-05 완료 — Phase 1 DoD**

- [x] TC-A-06 (4×3): `grid=4×3` → `INVALID_SIZE`
- [x] AC-FR-01-01 스위트 **33 passed** (DoD)

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

### REFACTOR · ECB 분리 계획

> **기준:** `.cursor/rules/magicsquare-tdd-testing.mdc` REFACTOR phase — 동작·계약(E001~E007, int[6], F-OK-01, ERROR 문자열) 불변, pytest GREEN, 커버리지 미감소.  
> **3그룹:** **A** 레이어 신설(GREEN) → **B** 역할 분리(REFACTOR) → **C** SSOT·품질 (B와 병행 가능; C-16은 Entity GREEN 후).

#### 리팩토링 To-Do (3그룹 · 순번 1~18)

##### 그룹 A — 레이어 신설 · GREEN 선행 (순번 1~6)

ECB 빈 공간을 채우고 검증·유스케이스·솔버를 올바른 레이어에 **신규** 구현. RED→GREEN 선행.

- [ ] **A-1 · #1 · P0** `pyproject.toml` — pydantic `[dev]`/`[gui]` only → core `dependencies` 이동 또는 stdlib 대체
- [ ] **A-2 · #2 · P0** `boundary/input_validator.py` *(신규)* — E001~E005 단일 SSOT (Extract Class); orchestrator/grid_io/grid_panel 3중 검증 해소
- [ ] **A-3 · #3 · P0** `boundary/ui_boundary.py` *(신규)* — validate→port→envelope Facade; Screen orchestrator 직접 호출·`NotImplementedError` 제거
- [ ] **A-4 · #4 · P0** `boundary/presenter.py` — E001→`UI_ERR_NOT_4X4`·E006/E007 매핑 (Extract Method / SSOT constants)
- [ ] **A-5 · #5 · P0** `control/solve_partial_magic_square.py` *(신규)* — locate→find→solve Use Case (Control layer)
- [ ] **A-6 · #6 · P0** `entity/services/partial_grid_solver.py` *(신규)* — Step A/B·int[6]·judge Entity 이동; GM `reference.py` 이중화 해소

##### 그룹 B — 기존 코드 역할 분리 · ECB REFACTOR (순번 7~10, 17~18)

그룹 A GREEN 후. orchestrator·Screen에 흩어진 검증·비즈니스 판단을 A 모듈로 위임하고 얇게.

- [ ] **B-1 · #7 · P0** `boundary/orchestrator.py` — Facade 위임 후 역할 축소 또는 제거 (검증+DTO+`NotImplementedError` 혼재 해소)
- [ ] **B-2 · #8 · P0** `boundary/screen/main_window.py` — Thin Screen (`UIBoundary`·presenter만); UI 비즈니스 판단(157–160, 170–172) 제거
- [ ] **B-3 · #9 · P1** `boundary/screen/grid_io.py` — parse만 유지 (Separate Concerns; size·범위 검증 제거)
- [ ] **B-4 · #10 · P1** `boundary/screen/grid_panel.py` — UI 전용; size 검증·BV demo 주입 제거 (Extract Method)
- [ ] **B-5 · #17 · P2** `boundary/orchestrator.py` — ValidationFailureResult 5회 중복·26줄 함수 분리 (Extract Method)
- [ ] **B-6 · #18 · P2** `boundary/screen/main_window.py` — `__init__`/`_on_submit` UI 조립 분리 (Extract Method)

##### 그룹 C — SSOT · 계약 · 품질 정비 (순번 11~16)

상수·픽스처·DTO·타입·GM 경로를 SSOT로 맞추고 계약 품질 향상. **C-6(#16)** 은 Entity GREEN 후.

- [ ] **C-1 · #11 · P1** `boundary/error_codes.py` *(신규)* — `INVALID_SIZE`/message SSOT Module (conftest 이중화 해소)
- [ ] **C-2 · #12 · P1** `boundary/screen/demo_grids.py` — fixture를 `tests/fixtures/`로 이동 (3중 SSOT 해소)
- [ ] **C-3 · #13 · P1** `boundary/dto.py` — success/pending DTO 추가 (Introduce DTO)
- [ ] **C-4 · #14 · P2** `boundary/ports.py` — `resolve` 반환 `Any` → 명시적 타입 (Replace Type)
- [ ] **C-5 · #15 · P2** `entity/user.py` — 유지 또는 Extract Validator *(선택; 격자 AC와 무관)*
- [ ] **C-6 · #16 · P1** `tests/golden_master/capture.py` — prod 경유 Adapter Switch (reference solver only → Entity GREEN 후)

#### 테스트 선행 필요 항목

리팩토링(구조 변경) 전 **RED→GREEN** 선행.

| 레이어 | 함수/모듈 (목표) | 선행 테스트 |
|--------|------------------|-------------|
| Boundary | `InputValidator.validate` | `test_u_in_validation.py` U-IN-04~08 |
| Boundary | `UIBoundary.solve` | `test_u_out_contract.py` U-OUT-01~03 |
| Boundary | invalid → resolve 0회 | `test_u_flow_isolation.py` U-FLOW-02 |
| Boundary | E001~E007 / `UI_ERR_*` 매핑 | *(신규)* `test_presenter.py` |
| Boundary | size regression | `test_ac_fr_01_01_invalid_size.py` **33건 기대값 변경 금지** |
| Entity | `MagicSquareJudge` | `test_d_val.py` D-VAL-01~06 |
| Entity | `EmptyCellScanner` | `test_d_loc.py` D-LOC-01 |
| Entity | `MissingValueFinder` | `test_d_mis.py` D-MIS-01 |
| Entity | `PartialGridSolver` | `test_d_sol.py` D-SOL-01~04 |
| Control | `SolvePartialMagicSquare.execute` | *(신규)* `tests/control/` 또는 IT-* |
| Screen | parse/submit 분기 | `test_screen_grid_io.py` 확장 + GUI smoke(mock) |
| Golden Master | baseline 고정 | `pytest -m golden_master` — `--approve` 없이 GREEN |

#### REFACTOR 진입 체크리스트

- [ ] **RF-01:** 대상 모듈 RED 0건 (REFACTOR 범위 RED 명시적 제외)
- [ ] **RF-02:** AC-FR-01-01 **33/33** — code/message diff 없음
- [ ] **RF-03:** `pytest -m golden_master` **6/6** — baseline 무변경
- [ ] **RF-04:** boundary ≥85%, entity ≥95% **미감소**
- [ ] **RF-05:** Green 작업과 Refactor **커밋/PR 분리**

#### 리팩토링 후 검증

**회귀 테스트**

```bash
python -m pytest tests/ -v
python -m pytest tests/boundary/test_ac_fr_01_01_invalid_size.py -v
python -m pytest -m boundary -v
python -m pytest -m domain -v
python -m pytest -m golden_master -v
python -m pytest tests/ --cov=src/magicsquare/boundary --cov=src/magicsquare/entity --cov-report=term-missing
```

**외부 동작 불변 확인**

| 항목 | Pass 기준 |
|------|-----------|
| E001 size 실패 | `INVALID_SIZE` + `"Grid must be 4x4."`; `resolve()` 0회 |
| ERROR 문자열 | Report/02 `UI_ERR_*` / E001~E005 message 바이트 동일 (RG) |
| int[6] 성공 | G1 `[2,2,7,3,3,10]`; len=6; 1-index; Domain vector verbatim |
| Golden Master | diff 없음 (`--approve` 없이 GREEN) |
| GUI smoke | BV-04a/b → INVALID_SIZE; valid 4×4 submit 동작 유지 |
| ECB 의존 | `entity` → `boundary\|control\|data` import 없음; Screen → Entity/Control 직접 호출 없음 |
| DT-USER | `test_entity_user.py` 9건 GREEN |

**실행 순서:** **그룹 A** (pydantic → input_validator + ui_boundary + presenter → Control + Entity) → **그룹 B** (orchestrator·Screen REFACTOR) → **그룹 C** (SSOT·fixture·DTO·타입; #16 Entity GREEN 후).

### 커버리지 목표

- [ ] Boundary Layer: **≥ 85%** (`pytest --cov=src/magicsquare/boundary`)
- [ ] Domain Logic: **≥ 95%** (`pytest --cov=src/magicsquare/entity`)
- [ ] 전체 TOTAL: **≥ 90%**

### 결함 목록 ([docs/defect_list.md](docs/defect_list.md))

- [x] DEF-001: `magicsquare.boundary` 패키지 생성
- [x] DEF-002: `ValidationFailureResult` DTO
- [x] DEF-003: `DomainSolverPort` + `resolve()`
- [x] DEF-004: orchestrator size 검증 전체
- [x] DEF-005: 열 길이 분기 (G-05)
- [x] DEF-006: 3×4 분기 (G-04)
- [ ] DEF-007: Boundary 커버리지 ≥ 85% 재측정
- [ ] DEF-008: Presenter·ERROR 문자열 RG-03 정합
- [x] 모든 결함 수정 후 AC-FR-01-01 회귀 **33 passed**

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

1. **그룹 A:** `pyproject.toml` pydantic → Phase 2/3 GREEN → `input_validator` + `ui_boundary` + presenter + Control + Entity  
2. **그룹 B:** [REFACTOR · ECB 분리 계획](#refactor--ecb-분리-계획) RF-01~05 충족 후 orchestrator·Screen 역할 분리  
3. **그룹 C:** error_codes·fixture·DTO·ports 타입·GM prod 연동 (#16)  
4. Report 02 **RG-01~06** 회귀 규칙 유지 (golden·assert 완화 금지)  

---

## 라이선스 · 기여

아직 미정. 구현 단계 진입 시 추가 예정.

---

*최종 갱신: 2026-05-29 · REFACTOR·ECB 3그룹 To-Do · Report/15 · Prompt/19*
