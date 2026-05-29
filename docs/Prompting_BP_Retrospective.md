# Prompting BP 회고 — Magic_Square_XX

| 항목 | 내용 |
|------|------|
| **프로젝트** | Magic_Square_XX (4×4 Magic Square · Dual-Track TDD · Clean Architecture) |
| **문서 유형** | Prompting 리뷰 · 회고 · 개선 계획 |
| **작성일** | 2026-05-29 |
| **근거 산출물** | `Prompt/01~22`, `Report/01~18`, `README.md`, `.cursor/rules/magicsquare-*.mdc`, `docs/test_plan.md` |
| **대상 독자** | 본인 회고 · 팀 공유 · 현업 적용 검토 |

---

## 1. Keep — 잘 유지할 프롬프팅·협업 관행

### 1.1 SSOT·계약을 먼저 고정하는 프롬프트

- **Report/01·02를 선행 SSOT로 명시**한 뒤 DT-* / UT-* / IT-* ID, BV 번호, ERROR 문자열을 프롬프트에 그대로 인용하면 AI가 추측 구현을 줄이고 테스트·문서 정합이 높아졌다.
- **금지 패턴**(literal `34`, `except: pass`, UT에서 concrete solver import, boundary에서 `SolutionVector` 재배열 등)을 `.cursor/rules/magicsquare-forbidden.mdc`에 두고, 세션마다 “RG-01~05 준수”를 요구한 것이 False Green을 예방했다.

### 1.2 TDD Phase를 프롬프트 1행에 박는 방식

- **RED → GREEN → REFACTOR**를 프롬프트 제목·첫 문단에 명시(`Prompt/11` RED QA, `Prompt/14~16` GREEN, `Prompt/19~21` REFACTOR·Ask)하면, 분석 세션에서 production 미수정(Ask only)과 구현 세션을 구분하기 쉬웠다.
- **GREEN은 BV·G-01~G-05 단위**로 쪼개 요청한 결과, AC-FR-01-01 Boundary **33/33 passed** Phase 1 DoD를 달성했다 (`Report/10`, `Report/12`).

### 1.3 산출물 이중화: Report + Transcript Export

- 세션 종료 시 **Report(요약·수치·판정) + Prompt Transcript(대화 원문)**를 쌍으로 남긴 체계(`Report/05` Agent Setup 이후 07~22) 덕분에 “왜 그 결정을 했는지”를 나중에 추적할 수 있었다.
- **backup-report-github-manager** 규칙(요약 대체 금지·원문 우선)은 프롬프트 품질 리뷰의 1차 증거로 유효했다.

### 1.4 역할 분리형 멀티 에이전트·서브에이전트

- **code-reviewer**로 REFACTOR 전 ECB·계약 위반·스멜 목록을 먼저 받고(`Report/15`), 구현 프롬프트에 반영하는 흐름이 “한 번에 다 고쳐줘”보다 안전했다.
- **quality-assurance-engineer** 관점의 RED QA·defect_list·test_plan 연계(`Report/07`, `docs/defect_list.md`)는 프롬프트만으로는 부족한 검증 축을 보완했다.

### 1.5 게이트·로드맵을 문서화한 뒤 프롬프트에 링크

- REFACTOR 18항목 → **A/B/C 3그룹 To-Do**, **Phase 0 gate G-01~G-05**, **Wave 1~4**를 README·Report/16에 고정한 뒤, 후속 프롬프트가 “지금은 REFACTOR 불가, GREEN-P1 먼저”라고 명확히 말할 수 있게 되었다.
- **Golden Master 6건**을 REFACTOR 전 안전장치로 요구한 것은 회귀 논의의 공통 언어가 되었다 (`Report/14`, `Prompt/18`).

### 1.6 검증 명령을 프롬프트에 포함

- `pytest -q`, `pytest tests/boundary/test_ac_fr_01_01_invalid_size.py`, `pytest -m golden_master`, `pytest --cov=...` 등 **실행 가능한 Exit criteria**를 넣으면 AI가 “완료” 주장 전에 수치를 남기는 비율이 높아졌다 (`Report/17` Step 0 실측).

---

## 2. Problem — 문제·리스크·개선 필요점

### 2.1 프롬프트 엔지니어링·구조화 부족

| 증상 | 프로젝트 사례 | 영향 |
|------|----------------|------|
| 목표·범위·금지·완료 조건이 한 메시지에 섞임 | 초기 대화형 transcript(`Prompt/01~03`)는 탐색 비중이 큼 | 턴 수 증가·되돌리기 비용 |
| 타 프로젝트 템플릿 잔존 | `Prompt/05.Multi_Agent_Collaboration_Prompt.md`의 “Refrigerator” 예시 | 신규 참여자 혼선 |
| 파일 경로·테스트 ID 불일치 | GM 경로를 `test_gm_01_...`로 지시했으나 실제는 `tests/golden_master/...` (`Report/16`) | AI가 잘못된 파일을 찾거나 헛수고 |
| Phase 미명시 요청 | 단일 커밋 REFACTOR 시도 → Step 0에서 **RED 23건** 확인 후 중단 (`Report/16`) | TDD 규칙 위반 직전까지 진행 |

### 2.2 AI 제안 검증·판단 미흡

- **False Green 위험**: 커버리지 54%·entity 0%인데 “REFACTOR 가능”처럼 들릴 수 있는 요약을 그대로 수용하면 gate RF-01을 놓친다 (`Report/17`: NFR gate 미충족).
- **구현 전 RED 확인 습관 부족**: 23건 RED가 `pytest.fail` 스켈레톤임을 매 세션 첫 턴에 확인하지 않으면, 이미 GREEN인 AC-FR과 Phase 2 skeleton을 혼동한다.
- **코드 리뷰 Major 7건**(orchestrator `NotImplementedError`, GM이 reference만 검증 등)을 프롬프트에 넣지 않으면 AI가 “리팩터링 완료”라고 말해도 계약 갭이 남는다 (`Report/15`).

### 2.3 프롬프트·문서·코드 SSOT 드리프트

- `defect_list.md`·README To-Do·실제 pytest 결과가 어긋나면, 다음 프롬프트가 **옛 결함 ID**를 기준으로 지시한다.
- ERROR 메시지·`INVALID_SIZE` 분기가 orchestrator·screen·grid_io에 **이중화**된 상태에서 “한 곳만 고쳐줘” 프롬프트는 부분 수정만 남긴다 (`Report/15` P0 스멜).

### 2.4 협업·운영 측면

- Transcript 22개·Report 18개로 **검색 비용**이 커짐 — “지금 phase가 뭐였지?”를 매번 README·최신 Report에서 다시 읽어야 함.
- **Ask vs Agent** 모드 구분을 프롬프트에 안 쓰면, 분석만 원하는 세션에서도 파일이 수정될 수 있음 (`Report/17`은 Ask·미수정 의도).

### 2.5 개인 역량 갭 (솔직한 자기 진단)

- “좋아 보이는” AI 리팩터 제안을 **pytest + GM + RED 건수**로 반증하기 전에 수용하려는 경향.
- 프롬프트에 **반례·실패 시나리오**(예: RG-04 golden 변경 금지)를 먼저 적는 습관이 약함.

---

## 3. Try — 다음에 시도할 프롬프트·워크플로

### 3.1 세션 시작 템플릿 (복붙용)

```markdown
## Context
- SSOT: Report/02 §<section>, docs/test_plan.md TP-AC-FR-01-01
- Branch: <name>
- TDD phase: RED | GREEN | REFACTOR | Ask (analysis only)
- Track: Domain | Boundary | Integration
- Target IDs: <DT-xxx / UT-xxx / BV-xx>

## Must
- Run Step 0: `pytest -q` (expect: passed X, failed Y)
- If GREEN: one BV / one test function / minimal diff
- If REFACTOR: confirm G-01~G-05 gate table in README

## Must NOT
- Change golden fixtures / ERROR strings without explicit approval
- Refactor while RED > 0 for target module
- Import PartialGridSolver in boundary tests

## Done when
- Command: `<exact pytest>`
- Result: `<N passed, M failed, exit code>`
- Files touched: `<list>`
```

### 3.2 Phase별 프롬프트 전략

| Phase | Try | 기대 효과 |
|-------|-----|-----------|
| **RED** | 실패 assertion·fixture·Test ID만 — `src/` 구현 금지 명시 | RG-01 준수 |
| **GREEN** | BV 하나 + mock port 검증(TC-B) + message 문자 단위 | 33→N 점진 GREEN |
| **REFACTOR** | A그룹(#1~6)만·Wave·게이트 표 첨부 | Phase 0 미충족 시 자동 중단 |
| **Ask** | “production/tests 미수정” + Step 0 실측만 | 분석 오염 방지 |

### 3.3 검증 루프 강화

1. AI 응답 후 **항상** 동일 pytest 명령 재실행(사용자 또는 AI).
2. 커버리지는 **Dual-Track 분리** 측정(entity / boundary) 후 gate 표에 기록 (`Report/17` 방식 유지).
3. code-reviewer 결과를 **체크리스트 ID**(C-1, M-3…)로 다음 프롬프트에 carry-over.

### 3.4 문서·프롬프트 정리

- `Prompt/05` 등 **범용 템플릿을 Magic_Square 전용으로 정리**하거나 `Prompt/_archive/`로 분리.
- 세션마다 **Report ID 1개 + Transcript 1개**만 “활성 SSOT”로 README 상단에 링크(이미 부분 적용 — 계속 유지).

### 3.5 팀 공통 “프롬프트 리뷰” 체크리스트 (3분)

- [ ] Phase·Track·Layer 명시?
- [ ] SSOT Report/문서 링크?
- [ ] Done when = 명령 + 숫자?
- [ ] Must NOT = RG/forbidden 표?
- [ ] Ask면 미수정 선언?

---

## 4. 개인별 학습 성과

> 본 프로젝트(Magic_Square_XX) 수행을 통해 체감·습득한 역량. 수치는 Report/17·18 Step 0 기준.

### 4.1 도메인·아키텍처

| 영역 | 학습 내용 | 증거·산출물 |
|------|-----------|-------------|
| TDD Dual-Track | Domain(DT-*)와 Boundary(UT-*)를 분리해 RED→GREEN; UT는 `DomainSolverPort` mock | `Report/02`, `tests/boundary/`, `tests/entity/` |
| ECB | Entity는 boundary/control/data 미import; Screen은 orchestrator 경유 설계 | `Report/15` ECB 표, REFACTOR 18항목 |
| 계약 | `INVALID_SIZE`, int[6], 1-index, row-major, Golden Master | AC-FR 33 passed, GM 6/6 |
| REFACTOR 게이트 | RED 23건 존재 시 Wave REFACTOR 착수 불가 | `Report/16` Phase 0, 중단 사례 |

### 4.2 프롬프팅·AI 협업

| 영역 | 학습 내용 | 증거·산출물 |
|------|-----------|-------------|
| 구조화 프롬프트 | SSOT + Phase + Test ID + pytest Done when | `Prompt/14~16`, `Report/10~12` |
| 멀티 에이전트 | code-reviewer → 계획 → 구현 순 | `Report/15`, `.cursor/agents/` |
| 증거 기반 완료 | “했다”가 아니라 exit code·passed/failed 수치 | `Report/17` Step 0 |
| Transcript 운영 | 리뷰·회고·재현을 위한 대화 보존 | `Prompt/` 22건 |

### 4.3 품질·QA 사고

| 영역 | 학습 내용 | 증거·산출물 |
|------|-----------|-------------|
| RED 스켈레톤 | `pytest.fail("RED: …")`로 의도적 실패 유지 | 23 failed 일관 (`Report/18`) |
| NFR·커버리지 gate | 전체 54% ≠ REFACTOR 허용; entity 0% 병목 인지 | `Report/17` |
| 결함 추적 | DEF-001~009와 BV·TC 매핑 | `docs/defect_list.md` |

### 4.4 아직 부족한 영역 (다음 학습 목표)

- 프롬프트 **한 번에 성공**시키기보다, **짧은 턴·좁은 범위** 반복에 익숙해지기.
- AI diff를 **RG 규칙 체크리스트**로 읽는 속도 올리기.
- Domain GREEN(12 RED) 착수 전 **Grid4x4·solver 계약**을 Report/02에서 먼저 요약해 두는 습관.

---

## 5. 팀 차원의 개선 액션 아이템

| ID | 액션 | 담당 | 우선순위 | 완료 기준 | 목표일 |
|----|------|------|----------|-----------|--------|
| ACT-01 | **세션 프롬프트 템플릿** 저장소 공유 (`docs/prompt_session_template.md`) | 전원 | P0 | README 링크·1회 워크숍 시연 | 1주 내 |
| ACT-02 | **Prompt/05 등 외부 예시** Magic Square용으로 개정 또는 archive | 문서 담당 | P1 | Refrigerator 참조 제거 | 2주 내 |
| ACT-03 | 세션 종료 **필수 산출물**: Report 1 + Transcript 1 + pytest 로그 스니펫 | 전원 | P0 | Report/17 형식 8섹션 채택 | 즉시 |
| ACT-04 | **Phase 0 gate 표**를 모든 REFACTOR 프롬프트에 첨부 | 개발 | P0 | RED≠0 시 REFACTOR PR 반려 | 즉시 |
| ACT-05 | 주 1회 **15분 Prompt 리뷰** (Keep/Problem 1건씩 공유) | 팀 | P1 | 회의록 `docs/prompt_review_log.md` | 2주 내 |
| ACT-06 | **Ask 모드** 분석 세션 규칙 문서화 (src/tests 미수정) | QA·개발 | P1 | Report/17을 팀 표준으로 명명 | 2주 내 |
| ACT-07 | code-reviewer **Critical/Major**를 defect_list·To-Do에 동기화 | QA | P1 | C-1·C-2 추적 ID 생성 | GREEN-P2 전 |
| ACT-08 | Transcript **인덱스 표**(Report↔Prompt↔phase) README 유지 | 문서 | P2 | 01~22 1표로 정리 | 3주 내 |
| ACT-09 | 커버리지 **Dual-Track** CI 스크립트(선택) | DevOps | P2 | entity/boundary % artifact | REFACTOR Wave 1 전 |
| ACT-10 | 프롬프트에 **민감정보·force push 금지** 팀 합의 재확인 | 전원 | P0 | backup agent 규칙 리뷰 완료 | 즉시 |

---

## 6. 현업 적용 계획

### 6.1 적용 원칙 (3줄)

1. **명세(SSOT) → 계약 테스트 → 최소 구현** 순서를 AI에게도 강제한다.  
2. **Phase·Done when·Must NOT** 없는 작업 지시는 리뷰에서 반송한다.  
3. **AI 산출물은 항상 로컬 pytest/CI 숫자로만** “완료” 처리한다.

### 6.2 단계별 롤아웃

| 단계 | 기간 | 내용 | 성공 지표 |
|------|------|------|-----------|
| **Pilot** | 2주 | 소형 모듈 1개에 세션 템플릿·Report+Transcript 적용 | PR마다 pytest 스니펫 첨부 100% |
| **Expand** | 4~8주 | code-reviewer·QA gate를 PR 템플릿에 통합 | REFACTOR PR 중 RED 잔존 0건 |
| **Standardize** | 분기 말 | 팀 Wiki에 Prompting BP·금지 패턴·Ask 규칙 고정 | 신규 온보딩 1일 내 첫 GREEN 사이클 |

### 6.3 현업 시나리오별 프롬프트 가이드

| 시나리오 | 권장 프롬프트 골격 | 금지 |
|----------|-------------------|------|
| 버그 수정 | 재현 테스트 → RED 확인 → 최소 수정 → 회귀 pytest | golden·ERROR 문자 임의 변경 |
| 신규 API | OpenAPI/계약 먼저 → UT mock → 구현 | boundary에 domain 알고리즘 |
| 리팩터링 | 게이트 표 + GM + cov 기준선 첨부 | RED>0 모듈 구조 변경 |
| 코드 리뷰 only | Ask + file list + RG 체크리스트 | 무분별 전체 rewrite |

### 6.4 Magic_Square_XX 잔여 작업에의 직접 적용

| 순서 | 작업 | 프롬프트에 넣을 핵심 |
|------|------|---------------------|
| 1 | **GREEN-P1** Boundary 11 RED (U-IN/U-FLOW/U-OUT) | `input_validator`·`ui_boundary` 신설만; BV·TC-B mock |
| 2 | **GREEN-P2** Entity 12 RED (D-VAL~D-SOL) | `Report/02` solver 계약; UT에 PartialGridSolver import 금지 |
| 3 | **Phase 0 충족** | `pytest tests/` 77 passed 목표 |
| 4 | **Wave 1 REFACTOR** A그룹 C1~C4 | README 3그룹 #1~6만; B·C는 gate 후 |

### 6.5 리스크·완화

| 리스크 | 완화 |
|--------|------|
| AI가 문서만 갱신하고 코드 미수정 | Done when에 `src/` diff 필수 명시 |
| 커버리지만 올리고 계약 깨짐 | GM + AC-FR 스위트 병행 |
| 프롬프트 피로 | 템플릿·서브에이전트·15분 리뷰로 반복 비용 절감 |

---

## 부록 — 본 프로젝트 프롬프팅 타임라인 (요약)

| 시기 | 대표 Prompt/Report | Phase | 핵심 성과 |
|------|-------------------|-------|-----------|
| 설계·규칙 | 01~04, Report 01~04 | 설계 | SSOT·Cursor rules MDC |
| RED·QA | 11, Report 07 | RED | 33 RED·defect_list |
| GREEN | 14~16, Report 10~12 | GREEN | AC-FR 33/33 |
| GUI·GM | 17~18, Report 13~14 | GREEN+GM | PyQt·GM 6/6 |
| REFACTOR 준비 | 19~22, Report 15~18 | REFACTOR·Ask | 3그룹 To-Do·cov gate·세션 요약 |

---

*본 문서는 Magic_Square_XX 실제 세션 산출물을 바탕으로 작성되었으며, 팀 회고·제출용으로 1~6장 구조를 채운 초안이다. 팀명·담당자·목표일은 실제 조직에 맞게 수정하면 된다.*
