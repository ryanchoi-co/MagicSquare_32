# Magic Square XX — 결함 목록 (Defect List)

| 항목 | 내용 |
|------|------|
| **문서 버전** | 1.0 |
| **작성일** | 2026-05-29 |
| **작성 역할** | QA 리드 |
| **기준 AC** | AC-FR-01-01 |
| **관련 테스트** | `tests/boundary/test_ac_fr_01_01_invalid_size.py` |
| **관련 계획** | [test_plan.md](test_plan.md) |

---

## 요약

| 구분 | 값 |
|------|-----|
| **마지막 pytest 실행** | `pytest tests/boundary/test_ac_fr_01_01_invalid_size.py -v` |
| **결과** | **29 failed**, 4 passed, 0 skipped |
| **통과 4건** | `TestAcFr0101ScopeLimit` 정적 catalog 검증 (구현 없이 통과 — 테스트 설계 결함 아님) |
| **실패 공통 메시지** | `AC-FR-01-01 RED: … missing — No module named 'magicsquare.boundary'` |
| **Entity 회귀** | `pytest tests/entity/` → 9 passed (영향 없음) |

---

## 결함 테이블

| ID | Severity | AC ID | 재현 절차 | 기대값 | 실제값 | 근본 원인 | 수정 요약 |
|----|----------|-------|-----------|--------|--------|-----------|-----------|
| DEF-001 | Critical | AC-FR-01-01 | 가상환경에서 `pytest tests/boundary/test_ac_fr_01_01_invalid_size.py -v` 실행 | Boundary 패키지 로드 후 테스트 수집·실행 | `ModuleNotFoundError: No module named 'magicsquare.boundary'` (29건 `pytest.fail`로 FAILED) | `src/magicsquare/boundary/` 패키지 미구현 | `boundary` 패키지 스켈레톤 생성 (`__init__.py` 등) |
| DEF-002 | Critical | AC-FR-01-01 | `grid=None` 입력 후 `process_grid_submission` 호출 (TC-A-01~03, TC-A-07) | `{ code: "INVALID_SIZE", message: "Grid must be 4x4." }` 를 담은 `ValidationFailureResult` 반환 | `magicsquare.boundary.dto` 없음 → orchestrator 진입 불가 | `ValidationFailureResult` pydantic DTO 미구현 | `boundary/dto.py`에 `code`, `message` 필드 모델 추가 |
| DEF-003 | Critical | AC-FR-01-01 | Mock `DomainSolverPort` 주입 후 `grid=None` 제출 (TC-A-04, TC-B-01~03) | `resolve()` 호출 **0회** (검증 전 early return) | `magicsquare.boundary.ports` 없음 → 포트 타입·오케스트레이션 불가 | `DomainSolverPort` 프로토콜/`resolve()` 계약 미정의 | `boundary/ports.py`에 `DomainSolverPort` + `resolve()` 시그니처 정의 |
| DEF-004 | Critical | AC-FR-01-01 | `grid=None` / `grid=[]` / `grid=3×4` 등 BV-01~04 입력 | 각 입력마다 `code="INVALID_SIZE"`, `message="Grid must be 4x4."` | `magicsquare.boundary.orchestrator` 없음 → S2 입력 검증·S3 분기 없음 | `process_grid_submission` 및 크기 선행 검증 로직 미구현 | `orchestrator.py`: `raw is None`, `len(rows)!=4`, `len(cols)!=4` → `ValidationFailureResult`; 유효 시에만 `resolve()` |
| DEF-005 | High | AC-FR-01-01 | `grid=[[]]*4` (행 4, 열 0) 제출 | `INVALID_SIZE` / `UI_ERR_NOT_4X4` 동등 실패 | DEF-004와 동일 — orchestrator 없음 | 열 길이 4 검사 누락(구현체 없음) | DEF-004 구현 시 `any(len(row) != 4 for row in raw)` 분기 포함 |
| DEF-006 | High | AC-FR-01-01 | `grid` = 3×4 (`UT-01` 정본 픽스처) 제출 | `code="INVALID_SIZE"` | DEF-004와 동일 | 3행 격자 거부 분기 없음 | `len(raw) != 4` 시 즉시 실패 반환 |
| DEF-007 | Medium | AC-FR-01-01 | `pytest --cov=src/magicsquare/boundary --cov-report=html` | Boundary branch **≥ 85%** ([test_plan.md](test_plan.md) §6) | 측정 대상 패키지 없음 → **0%** (또는 N/A) | Boundary 소스 미존재 | DEF-001~004 해결 후 AC-FR-01-01 스위트로 커버리지 재측정 |
| DEF-008 | Medium | AC-FR-01-01 | Report/02 §2.2 UX-02 대비 message 필드 검증 | 테스트 플랜: `Grid must be 4x4.` / Report SSOT: `ERROR: grid must be 4x4` | 구현 전 — Presenter·ERROR 접두 매핑 미결정 | 외부 문자열 계약(접두 `ERROR: `) vs DTO `message` 필드 정책 미고정 | GREEN 전 Presenter에서 SSOT 문자열 **완전 일치**로 매핑 문서·코드 고정 (RG-03) |
| DEF-009 | Low | AC-FR-01-01 | `TestAcFr0101ScopeLimit` 3건 catalog 테스트만 실행 | RED 단계에서도 동작 검증 실패 기대 | **PASSED** (카탈로그 상수만 검사) | 동작 미검증 정적 테스트 — RED 신호 약화 | 유지 가능; 동작 결함은 DEF-001~004로 추적. 필요 시 `@pytest.mark.skip` 없이 orchestrator 연동 테스트로 보강 |

---

## AC-FR-01-01 테스트 실패 ↔ 결함 매핑

| 실패 테스트 그룹 | 건수 | 관련 DEF |
|------------------|------|----------|
| `TestAcFr0101NormalFailureReturn` | 5 | DEF-001, DEF-002, DEF-004 |
| `TestAcFr0101BoundaryValues` | 9 | DEF-001, DEF-004, DEF-005, DEF-006 |
| `TestAcFr0101Isolation` | 5 | DEF-001, DEF-003, DEF-004 |
| `TestAcFr0101MessageExactness` | 5 | DEF-001, DEF-002, DEF-004, DEF-008 |
| `TestAcFr0101ScopeLimit` (parametrize 동작 검증) | 5 failed | DEF-001, DEF-004 |
| `TestAcFr0101ScopeLimit` (정적 catalog) | 4 passed | DEF-009 (결함 아님) |

---

## 범위 외 (본 목록에 미등록)

다음은 **AC-FR-01-01 RED 스위트에서 의도적으로 제외**되었으며, 현재 실패로 기록하지 않습니다.

- 4×4 정상·부분 격자 (`F-OK-01` 등) → AC-FR-01-02 이후 / `UT-07`, `DT-11`
- 빈칸 1·3개, 값 17, 중복 → `UT-02`~`UT-06`
- `Grid4x4.fromRaw` Domain 단위 RED (`tests/entity/test_grid4x4_from_raw.py`) → 미작성

---

## 수정 우선순위 (권장)

1. **DEF-001** — `boundary` 패키지 생성  
2. **DEF-002, DEF-003** — DTO·Port 계약  
3. **DEF-004** — orchestrator + `None` / `[]` / 3×4 / 4×3 / `[[]]*4` 선행 검증  
4. **DEF-008** — Presenter ERROR 문자열 RG-03 정합  
5. **DEF-007** — 커버리지 게이트 재실행  

**완료 기준:** `pytest tests/boundary/test_ac_fr_01_01_invalid_size.py` → 33 passed (또는 parametrize 포함 전체 GREEN), README 결함 체크리스트 2항목 완료.

---

## 변경 이력

| 버전 | 날짜 | 변경 |
|------|------|------|
| 1.0 | 2026-05-29 | AC-FR-01-01 RED 실행 결과 기반 초안 (DEF-001~009) |
