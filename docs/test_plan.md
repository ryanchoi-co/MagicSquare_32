# Magic Square XX — 테스트 계획서

| 항목 | 내용 |
|------|------|
| **문서 ID** | TP-AC-FR-01-01 |
| **작성 역할** | 시니어 QA 리드 |
| **대상 AC** | `AC-FR-01-01` — 입력 참조 없음(`grid=None`) 시 크기 오류 반환 |
| **기술 스택** | Python 3.11+, pytest ≥8, pydantic (입력 DTO·응답 스키마), `unittest.mock` |
| **SSOT** | `Report/02.Magic_Square_TDD_Clean_Architecture_Design_Report.md`, `Report/06.Magic_Square_User_Journey_Story_Scenario_Verification_Report.md` |
| **상태** | 계획 (구현·테스트 코드 미포함) |

---

## 1. 목적 및 범위

### 1.1 목적

`AC-FR-01-01`을 기준으로 **입력 유효성 검사의 최선행 조건(4×4 존재)** 을 Dual-Track TDD 관점에서 검증한다.

- **Boundary:** 외부 계약 위반 시 고정 오류 코드·메시지 반환, Domain 솔버 **미호출**
- **Domain:** `Grid4x4.fromRaw` 진입점에서 크기 불변(`D-C1`) 위반 시 `D_ERR_NOT_4X4` 발생

### 1.2 테스트 플랜 ↔ Report SSOT 매핑

| 테스트 플랜 (본 문서) | Report/02 SSOT | 비고 |
|----------------------|------------------|------|
| `INVALID_SIZE` | `UI_ERR_NOT_4X4` (Boundary) | 외부 응답 `code` |
| `Grid must be 4x4.` | `ERROR: grid must be 4x4` (UX-02 접두 포함) | Boundary 메시지는 Report 고정 문자열 **완전 일치** |
| — | `D_ERR_NOT_4X4` | Domain `fromRaw` 실패 |
| `UT-01` | Report/02 §2.3 | 3×4 → `UI_ERR_NOT_4X4` |
| `SC-BND-VAL-004` | Report/06 §5 | not-4x4 rejection |
| `IT-03` | Report/02 §4.2 | P1 통합 — `UI_ERR_NOT_4X4` |

### 1.3 In-Scope / Out-of-Scope

| 구분 | 내용 |
|------|------|
| **In-Scope** | `grid` 형태·크기 선행 검증, Boundary Mock 격리, Domain `fromRaw` 크기 검증, 솔버 호출 0회 |
| **Out-of-Scope** | `grid` 4×4 정상 입력, 빈칸 개수·값 범위·중복·솔버·golden `F-OK-01` (별도 AC/UT) |

---

## 2. pytest 기반 단위 테스트 범위 및 우선순위

### 2.1 레이어·디렉터리

| 우선순위 | 레이어 | 경로 (예정) | pytest 마커 | Report 테스트 접두 |
|----------|--------|-------------|---------------|-------------------|
| **P0** | Domain (Entity) | `tests/entity/test_grid4x4_from_raw.py` | `@pytest.mark.domain` | `DT-GRID-01` ~ `DT-GRID-07` |
| **P0** | Boundary | `tests/boundary/test_input_validator_not_4x4.py` | `@pytest.mark.boundary` | `UT-01`, `UT-01b` |
| **P1** | Boundary (격리) | `tests/boundary/test_solver_port_not_called_on_invalid_size.py` | `@pytest.mark.boundary` | `UT-01` + Story 1 AC |
| **P2** | Integration | `tests/integration/test_it03_not_4x4.py` | `@pytest.mark.integration` | `IT-03` |

> **금지 (Report/02, Forbidden rules):** `tests/boundary/` 에서 `PartialGridSolver` 등 Domain 구현체 직접 import.

### 2.2 실행 우선순위 (TDD RED 순서)

1. **P0-Domain RED** — `Grid4x4.fromRaw` + `D_ERR_NOT_4X4` (크기 불일치·`None` 계열)
2. **P0-Boundary RED** — Validator/Presenter + `UI_ERR_NOT_4X4` / 테스트 플랜 `INVALID_SIZE` 매핑
3. **P1-Boundary RED** — `DomainSolverPort` Mock, `solve` 호출 **0회** assert
4. **P2-Integration** — P1 경로 E2E (`IT-03`)

### 2.3 단위 테스트 책임 분리

| 테스트 대상 | 검증 책임 | 사용 도구 |
|-------------|-----------|-----------|
| `Grid4x4.fromRaw` | `D-C1`, 예외 타입·코드 | pytest, `pytest.raises` |
| Boundary Validator | S2 입력 계약, `UI_ERR_NOT_4X4` | pytest, pydantic `ValidationError` 또는 앱 전용 `InvalidGridError` |
| Boundary Orchestrator | S3 미진입, Mock 0회 | `unittest.mock.Mock` / `MagicMock(spec=DomainSolverPort)` |
| Presenter/Response DTO | `code`, `message` 필드 | pydantic 모델 `assert` |

---

## 3. 경계값 케이스 목록

모든 케이스는 **동일 기대 결과군**: 테스트 플랜 응답 `{ "code": "INVALID_SIZE", "message": "Grid must be 4x4." }`  
구현·Report 검증 시 Boundary는 `UI_ERR_NOT_4X4` + `ERROR: grid must be 4x4` 로 매핑한다.

| ID | 입력 (`grid`) | 설명 | Boundary 기대 | Domain `fromRaw` | 솔버 `solve` 호출 |
|----|---------------|------|---------------|------------------|-------------------|
| **BV-01** | `None` | 명시적 `None` — 참조 없음 | `INVALID_SIZE` / `UI_ERR_NOT_4X4` | 호출 안 함 (Validator 선행 차단) | **0** |
| **BV-02** | `[]` | 빈 리스트 — 행 0 | 동일 | 동일 | **0** |
| **BV-03** | `[[]] * 4` | 행 4개, 열 길이 0 | 동일 | `D_ERR_NOT_4X4` (열≠4) | **0** |
| **BV-04a** | `3×4` (`rows=3, cols=4`) | Report `UT-01` 정본 | 동일 | `D_ERR_NOT_4X4` | **0** |
| **BV-04b** | `4×3` | 열 부족 | 동일 | `D_ERR_NOT_4X4` | **0** |
| **BV-04c** | `5×5` | 초과 크기 | 동일 | `D_ERR_NOT_4X4` | **0** |

### 3.1 AC-FR-01-01 범위 외 — 포함 금지

| 입력 | 제외 사유 |
|------|-----------|
| `grid` = **4×4 정상** (예: `F-OK-01` 또는 유효 부분 격자) | 크기 검증 **통과** 케이스 — `AC-FR-01-02` 이후(빈칸·값·중복) 또는 `UT-07`/`DT-11` 영역 |
| 4×4이나 빈칸 1/3, 값 17, 중복 등 | `UT-02`~`UT-06` 전용 |

> 본 테스트 계획서의 pytest 스위트에 **4×4 정상 입력 테스트를 추가하지 않는다.**

### 3.2 픽스처 표현 (pytest `parametrize` 후보)

```text
# BV-04a 예: 3행 × 4열
[[1,2,3,4], [5,6,7,8], [9,10,11,12]]

# BV-04b 예: 4행 × 3열
[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

# BV-04c 예: 5행 × 5열 — 최소 1셀만 채워도 크기 판정에 충분
[[1,2,3,4,5], ...]  # 5 rows
```

---

## 4. 예외·특이 케이스 목록

| ID | 케이스 | 입력/조건 | 기대 동작 | 비고 |
|----|--------|-----------|-----------|------|
| **EX-01** | `None` vs 미전달 | `solve(grid=None)` vs 파라미터 생략(기본값 `None`) | 동일 오류군 | API 기본값 정책 문서화 |
| **EX-02** | 비정형 타입 | `grid="invalid"`, `grid=123`, `grid={}` | `INVALID_SIZE` (또는 Boundary 전용 `TypeError` → `UI_ERR_NOT_4X4` 매핑) | pydantic DTO 사용 시 1차 차단 |
| **EX-03** | `None` 행 | `[[1,2,3,4], None, ...]` | `INVALID_SIZE` | 행 요소가 `None`이면 4×4 구조 불성립 |
| **EX-04** | 가변 길이 행 | `[[1,2], [3,4,5,6], ...]` (4행이나 열 길이 상이) | `INVALID_SIZE` | **첫 위반 시 단일 실패** (메시지 재사용) |
| **EX-05** | Domain 예외 전파 | Boundary가 `fromRaw` 호출 경로일 때 | Domain `D_ERR_NOT_4X4` → Boundary `UI_ERR_NOT_4X4` 매핑 | S2/S3 경계 설계에 따라 Validator-only vs 변환 후 매핑 중 **하나만** 선택·고정 |
| **EX-06** | 이중 실패 금지 | 크기 오류 + 솔버 실패 동시 | `UX-03`: 성공·실패 동시 반환 금지 | 크기 오류 시 솔버 미호출로 자동 충족 |
| **EX-07** | 메시지 회귀 | 고정 문자열 변경 | RG-03 위반 | `ERROR: grid must be 4x4` 완전 일치 테스트 유지 |

---

## 5. Domain 해(Solver) 결정 진입점 호출 횟수 검증 전략

### 5.1 검증 목표 (Story 1 AC)

> *On validation failure: Domain solver must not be called.*  
> (`Report/06` Story 1)

`AC-FR-01-01` 및 §3 경계값 **전 케이스**에서 `DomainSolverPort.solve` 호출 횟수 = **0**.

### 5.2 Mock / Spy 패턴

| 전략 | 적용 레이어 | 구현 요약 |
|------|-------------|-----------|
| **Mock (권장)** | Boundary `tests/boundary/` | `solver = Mock(spec=DomainSolverPort)` — `assert_not_called()` |
| **Spy (선택)** | Control/Orchestrator | `wraps=real_port` 대신 **본 AC 범위에서는 사용 금지** (Domain 구현 결합) |
| **call_count** | pytest | `assert solver.solve.call_count == 0` |

### 5.3 pytest 예시 패턴 (계획용 스니펫)

```python
from unittest.mock import Mock

def test_ut01_invalid_size_does_not_call_domain_solver():
    port = Mock()  # spec=DomainSolverPort when interface exists
    result = boundary_handle(grid=None, solver_port=port)

    assert result.code == "INVALID_SIZE"  # → UI_ERR_NOT_4X4 at impl
    port.solve.assert_not_called()
    assert port.solve.call_count == 0
```

### 5.4 Domain 레이어 호출 횟수 (별도 트랙)

| API | BV-01~04 기대 |
|-----|----------------|
| `Grid4x4.fromRaw` | Validator-only 설계: **0회** / 변환 설계: **0회 성공** (예외 발생) |
| `PartialGridSolver.solve` | **항상 0회** (본 AC) |

Domain 단위 테스트는 **Mock 없이** `pytest.raises(DomainNot4x4Error)` 로 `fromRaw`만 검증한다.

### 5.5 UT-11과의 구분

| Test ID | 조건 | `solve` 호출 기대 |
|---------|------|-------------------|
| **UT-01 / AC-FR-01-01** | 크기 오류 | **0** |
| **UT-11** (범위 외) | 4×4 유효 입력 + 성공 경로 | **1** |

---

## 6. 커버리지 목표

Report/02 §4.4 및 Epic 성공 기준을 따른다.

| 레이어 | branch 커버리지 목표 | 본 AC 기여 범위 |
|--------|---------------------|-----------------|
| **Domain (`src/magicsquare/entity/`)** | **≥ 95%** | `Grid4x4.fromRaw` 크기 분기, `D_ERR_NOT_4X4` 예외 경로 |
| **Boundary (`src/magicsquare/boundary/`)** | **≥ 85%** | Input Validator, Error Presenter, Orchestrator S2 분기 |

### 6.1 본 AC로 커버해야 할 분기 (최소)

- `raw is None` → 실패
- `len(raw) != 4` → 실패
- `any(len(row) != 4 for row in raw)` → 실패
- Boundary: 크기 실패 시 early return (S3 미진입)
- Boundary: `solve` 미호출 분기

### 6.2 커버리지에서 제외·별도 집계

| 항목 | 사유 |
|------|------|
| `PartialGridSolver`, `MagicSquareJudge` 본체 | AC-FR-01-01 범위 외 |
| `tests/entity/test_entity_user.py` (DT-USER-*) | User 엔티티 — 격자 AC와 분리 집계 |

---

## 7. pytest-cov 측정 전략

### 7.1 설치

```bash
pip install pytest-cov
```

개발 의존성 고정 시 (권장):

```bash
pip install -e ".[dev]"
pip install pytest-cov
```

### 7.2 실행 (전체)

```bash
pytest --cov=src --cov-report=term-missing
```

### 7.3 레이어별 집계 (AC-FR-01-01 검증용)

```bash
# Domain only
pytest tests/entity/test_grid4x4_from_raw.py \
  --cov=src/magicsquare/entity \
  --cov-report=term-missing \
  --cov-fail-under=95

# Boundary only
pytest tests/boundary/ \
  --cov=src/magicsquare/boundary \
  --cov-report=term-missing \
  --cov-fail-under=85
```

### 7.4 CI·로컬 게이트 권장

| 게이트 | 명령 | 실패 조건 |
|--------|------|-----------|
| **G1 — AC 스위트** | `pytest -m "domain or boundary" tests/entity/test_grid4x4_from_raw.py tests/boundary/test_input_validator_not_4x4.py -v` | 1건이라도 실패 |
| **G2 — 커버리지** | §7.3 레이어별 명령 | `--cov-fail-under` 미달 |
| **G3 — 회귀** | `pytest tests/ -v` | RG-01: 기존 `DT-USER-*` 깨짐 |

### 7.5 `term-missing` 해석

- **Missing lines** 가 `fromRaw` 크기 검사 `else` 분기에만 남으면 → BV-04a/b/c 보완
- Boundary **Missing** 이 Orchestrator S3 진입부면 → BV-01~03 early-return 테스트 추가

### 7.6 (선택) `pyproject.toml` 설정 예정

```toml
[tool.coverage.run]
source = ["src"]
branch = true
omit = ["*/tests/*", "*/__init__.py"]

[tool.coverage.report]
fail_under = 85
show_missing = true
```

> Domain 95%는 **경로별 `--cov-fail-under=95`** 로 entity 패키지만 별도 게이트한다.

---

## 8. 테스트 케이스 매트릭스 (요약)

| Case ID | Layer | pytest 파일 (예정) | Test name (예정) | Assert 핵심 |
|---------|-------|-------------------|------------------|-------------|
| TC-01 | Boundary | `test_input_validator_not_4x4.py` | `test_bv01_grid_none` | `INVALID_SIZE`, solve×0 |
| TC-02 | Boundary | 동일 | `test_bv02_grid_empty_list` | 동일 |
| TC-03 | Boundary | 동일 | `test_bv03_four_empty_rows` | 동일 |
| TC-04 | Boundary | 동일 | `test_bv04a_grid_3x4` | 동일 (UT-01 정본) |
| TC-05 | Boundary | 동일 | `test_bv04b_grid_4x3` | 동일 |
| TC-06 | Boundary | 동일 | `test_bv04c_grid_5x5` | 동일 |
| TC-07 | Domain | `test_grid4x4_from_raw.py` | `test_from_raw_none_raises` | `D_ERR_NOT_4X4` |
| TC-08 | Domain | 동일 | `test_from_raw_*_parametrize` | BV-02~04c |
| TC-09 | Integration | `test_it03_not_4x4.py` | `test_p1_invalid_size` | `IT-03`, `UI_ERR_NOT_4X4` |

---

## 9. 추적성 (Traceability)

| Concept | Rule | Story | Scenario | Planned Test | Component |
|---------|------|-------|----------|--------------|-----------|
| Input 4×4 | D-C1 | Story 1 | SC-BND-VAL-004 | UT-01, DT-GRID-*, IT-03 | Validator, `Grid4x4` |
| AC-FR-01-01 | 선행 크기 검증 | Story 1 | SC-BND-VAL-004 | TC-01~09 | Boundary + Entity |
| Solver isolation | Story 1 AC | — | — | Mock `assert_not_called` | `DomainSolverPort` |
| ERROR string | UX-02, RG-03 | — | — | message exact match | Presenter |

---

## 10. 완료 정의 (Definition of Done — 본 AC)

- [ ] BV-01 ~ BV-04c **6건** Boundary 테스트 GREEN
- [ ] Domain `fromRaw` 크기 실패 **동등 6건** GREEN
- [ ] 모든 Boundary 실패 케이스에서 `DomainSolverPort.solve` **call_count == 0**
- [ ] 4×4 정상 입력 테스트가 **본 스위트에 없음** (§3.1)
- [ ] `pytest --cov=src --cov-report=term-missing` 실행 가능
- [ ] Domain entity ≥95%, Boundary ≥85% (레이어별 집계)
- [ ] Report/02 `UI_ERR_NOT_4X4` 메시지 **완전 일치** 회귀 테스트 통과

---

## 11. 참고

- Dual-Track: Domain RED → Boundary RED(Mock) → Integration 순서 유지 (`Report/03` 권장 착수 순서)
- Forbidden: Boundary 테스트에서 `PartialGridSolver` import 금지
- 본 문서는 **테스트 계획만** 포함하며, 프로덕션·테스트 구현 코드는 별도 TDD 사이클에서 작성한다.

---

*문서 버전: 1.0 · 2026-05-29 · 기준 AC: AC-FR-01-01*
