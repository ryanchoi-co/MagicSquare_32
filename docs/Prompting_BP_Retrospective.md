# Magic_Square_XX — 학습·개선 KPT 회고 세션 기획서

| 항목 | 내용 |
|------|------|
| **프로젝트** | Magic_Square_XX (4×4 Magic Square · Dual-Track TDD · Clean Architecture · AI 협업) |
| **문서 유형** | 회고 세션 진행 가이드 · 액션 추적 · 학습 자료 · 다음 프로젝트 개선 계획 |
| **방법론** | KPT (Keep · Problem · Try) |
| **권장 소요** | 90~120분 (팀 3~6명 기준) |
| **근거 산출물** | `Prompt/01~22`, `Report/01~18`, `README.md`, `docs/test_plan.md`, `.cursor/rules/` |
| **작성일** | 2026-05-29 |

---

## 문서 구성 (4종 산출물)

| # | 산출물 | 본 문서 위치 |
|---|--------|--------------|
| A | **회고 세션 진행 가이드** | [Part A](#part-a-회고-세션-진행-가이드) |
| B | **액션 아이템 추적 템플릿** | [Part B](#part-b-액션-아이템-추적-템플릿) |
| C | **학습 자료 정리 문서** | [Part C](#part-c-학습-자료-정리-문서) |
| D | **다음 프로젝트 개선 계획서** | [Part D](#part-d-다음-프로젝트-개선-계획서) |

> **세션 전 준비:** 참가자 각자 Part A의 [사전 준비 체크리스트](#사전-준비-체크리스트)를 24시간 전까지 작성.  
> **세션 후:** Part B 액션 보드 갱신 · Part C에 신규 자료 추가 · Part D를 다음 스프린트 킥오프에 첨부.

---

# Part A: 회고 세션 진행 가이드

## A.1 세션 목표

1. 프로젝트 전 기간의 **잘된 점(Keep)** 과 **장애물(Problem)** 을 공유한다.  
2. **Try** 항목을 팀 합의 가능한 실험·관행으로 구체화한다.  
3. 개인 학습 성과를 팀 지식으로 전환한다.  
4. Part B 액션 아이템에 **책임자·일정·성공 기준**을 확정한다.

## A.2 참가 역할

| 역할 | 담당 | 비고 |
|------|------|------|
| **진행자(Facilitator)** | KPT 시간 관리·발언 균등 | 본인 작업 방어하지 않기 |
| **기록자(Scribe)** | Keep/Problem/Try 보드·액션 초안 | Part B 실시간 갱신 |
| **시간관리자** | 섹션별 타이머 | 5분 전 알림 |
| **참가자** | 사전 준비·발표·투표 | 1인 3~5분 발언 권장 |

## A.3 타임테이블 (90분 예시)

| 시간 | 구간 | 활동 | 산출 |
|------|------|------|------|
| 0:00~0:10 | 오프닝 | 목표·규칙·KPT 소개 | 공통 이해 |
| 0:10~0:30 | **Keep** | 개인 포스트잇 → 클러스터 → 투표 Top3 | Keep 목록 |
| 0:30~0:50 | **Problem** | 개인 포스트잇 → 원인 5Why(선택) | Problem 목록 |
| 0:50~1:05 | **Try** | Problem 1건당 Try 1~2개 매핑 | Try 백로그 |
| 1:05~1:20 | **개인 학습 공유** | 라운드로빈 (Part A.5 양식) | Part C 초안 |
| 1:20~1:30 | **액션 확정** | Part B 표 채우기·담당·일정 | 액션 보드 v1 |

## A.4 진행 규칙

- **비난 금지:** 사람이 아닌 프로세스·도구·프롬프트를 논의한다.  
- **증거 우선:** “느렸다”보다 `pytest` 수치·Report ID·커밋 hash를 말한다.  
- **AI 산출물:** “완료”는 AI 말이 아니라 **로컬/CI 검증 결과**로만 인정한다.  
- **결정:** Try·액션은 **SMART**(구체·측정·기한·담당) 미충족 시 다음 회의로 이관하지 않고 당일 축소 합의.

---

## A.5 KPT 회고 — 진행 질문 & 프로젝트 사례

> **진행 방법:** 각 섹션마다 (1) 진행자가 질문을 읽고 2분 침묵 작성 → (2) 라운드로빈 공유 → (3) 클러스터링 → (4) 투표.  
> 아래 **「프로젝트 사례」** 는 Magic_Square_XX 실제 경험 예시이며, 세션에서 그대로 쓰거나 수정·보완한다.

---

### Keep — 계속 유지할 것들

#### 진행 질문 (팀에 던질 질문)

| # | 질문 |
|---|------|
| K1 | **무엇이 잘 되었는가?** (기술·프로세스·협업·AI 사용 중 1가지 이상) |
| K2 | **어떤 관행을 계속 유지해야 하는가?** (다음 스프린트에도 그대로 둘 것) |
| K3 | **팀에게 도움이 된 것들은?** (문서·도구·역할·규칙·의사결정 방식) |

#### 기록 템플릿 (세션 중 작성)

| Keep 항목 | 근거(Report/Test/PR) | 유지 이유 | 담당 확인 |
|-----------|----------------------|-----------|-----------|
| *(예시)* SSOT Report/02 + Test ID 인용 프롬프트 | Report/10~12, Prompt/14~16 | 추측 구현·False Green 감소 | ☐ 전원 |
| | | | |
| | | | |

#### 프로젝트 사례 (Magic_Square_XX — Keep 후보)

| Keep | 잘 된 점 | 유지할 관행 | 팀에 도움 된 점 |
|------|----------|-------------|-----------------|
| **SSOT 선행** | Report/01·02 기준 DT-*/UT-*/BV·ERROR 문자 인용 | 프롬프트 1행에 SSOT 링크 | 테스트·문서·AI 출력 정합 |
| **TDD Phase 명시** | RED→GREEN→REFACTOR·Ask 구분 | 세션 제목에 phase 표기 | 분석 세션에서 code 미수정 |
| **점진 GREEN** | AC-FR-01-01 **33/33** (G-01~G-05) | BV 단위·최소 diff | Phase 1 DoD 달성 |
| **Report + Transcript** | Report/05 이후 07~22 쌍 보존 | 세션 종료 Export 필수 | 결정 근거 재현 |
| **서브에이전트** | code-reviewer → 계획 → 구현 | REFACTOR 전 리뷰 선행 | “한 번에 다 고침” 방지 |
| **Golden Master** | GM 6/6 회귀 안전장치 | REFACTOR 전 GM 통과 | row-major·1-index·ERROR 계약 보호 |
| **금지 규칙** | `.cursor/rules/magicsquare-forbidden.mdc` | RG-01~05 매 PR 체크 | literal 34·golden 변경 방지 |
| **Exit criteria** | `pytest -q` 수치를 Done when에 명시 | AI “완료” = exit code | Report/17 Step 0 실측 문화 |

---

### Problem — 문제점들

#### 진행 질문

| # | 질문 |
|---|------|
| P1 | **어떤 장애물이 있었는가?** (기술·도구·커뮤니케이션·지식 격차) |
| P2 | **무엇이 팀을 느리게 했는가?** (되돌리기·재작업·검색·대기) |
| P3 | **어떤 프로세스가 비효율적이었는가?** (TDD·리뷰·문서·AI 프롬프트·Git) |

#### 기록 템플릿

| Problem | 장애물 유형 | 느려진 구간 | 비효율 프로세스 | 영향(정량 가능 시) |
|---------|-------------|-------------|-----------------|-------------------|
| *(예시)* Phase 미명시 REFACTOR 시도 | 프로세스 | Step 0 RED 23 확인 후 중단 | TDD phase 생략 | 1세션 낭비 |
| | | | | |

#### 프로젝트 사례 (Problem 후보)

| Problem | 장애물 | 느린 원인 | 비효율 프로세스 |
|---------|--------|-----------|----------------|
| **프롬프트 비구조화** | 목표·금지·Done when 혼재 | 초기 탐색 턴 증가 (`Prompt/01~03`) | “대화형”만으로 구현 지시 |
| **템플릿 드리프트** | 타 프로젝트 예시 잔존 | `Prompt/05` Refrigerator 혼선 | 공통 Prompt 미정리 |
| **경로·ID 불일치** | GM 파일 경로 오지시 | AI 헛수고 (`Report/16`) | SSOT와 프롬프트 불일치 |
| **REFACTOR 조기 착수** | RED 23건 잔존 | 단일 커밋 REFACTOR 시도·중단 | Phase 0 gate G-01~G-05 미적용 |
| **False Green 위험** | cov 54%·entity 0% | “REFACTOR 가능” 오해 | NFR gate 미습관화 |
| **문서·코드 SSOT 어긋남** | defect_list·README·pytest 불일치 | 옛 DEF ID 기준 지시 | 세션 후 문서 미동기화 |
| **검색 비용** | Report 18·Prompt 22 | “지금 phase?” 재독 | 활성 SSOT 인덱스 부족 |
| **AI 검증 습관** | Major 7건 미반영 프롬프트 | 리팩터 제안 조기 수용 | code-reviewer → To-Do 미연결 |

---

### Try — 시도해볼 것들

#### 진행 질문

| # | 질문 |
|---|------|
| T1 | **다음에는 무엇을 다르게 해볼까?** (Problem 1건당 Try 1개 이상) |
| T2 | **어떤 새로운 도구나 방법을 시도해볼까?** (템플릿·CI·에이전트·모드) |
| T3 | **문제 해결을 위한 실험은?** (기간·측정·성공/실패 기준 포함) |

#### Try ↔ Problem 매핑 템플릿

| Problem (요약) | Try (실험) | 기간 | 성공 기준 | 실패 시 |
|----------------|------------|------|-----------|---------|
| Phase 미명시 | 세션 프롬프트 템플릿 의무화 | 2주 | PR 100% template 첨부 | 리뷰 반송 |
| REFACTOR 조기 | G-01~G-05 gate PR 체크리스트 | 즉시 | RED≠0 REFACTOR PR 0건 | Wave 1 보류 |
| | | | | |

#### 프로젝트 사례 (Try 후보)

| Try | 다르게 할 것 | 새 도구·방법 | 실험·측정 |
|-----|--------------|--------------|-----------|
| **세션 템플릿** | Context / Must / Must NOT / Done when 고정 | `docs/prompt_session_template.md` | 2주간 PR template 첨부율 |
| **Ask 모드 표준** | 분석만 시 `src/tests` 미수정 명시 | Cursor Ask + Report/17 형식 | 분석 세션 오염 0건 |
| **15분 Prompt 리뷰** | 주 1회 Keep/Problem 1건 공유 | `docs/prompt_review_log.md` | 4회 연속 기록 |
| **Dual-Track cov** | entity/boundary 분리 측정 | pytest-cov + gate 표 | REFACTOR 전 RF-01 판정 |
| **활성 SSOT 인덱스** | README 상단 Report↔Prompt↔phase 표 | README 유지 | 신규 온보딩 1일 내 GREEN 1사이클 |
| **Prompt/05 정리** | Magic Square 전용 또는 archive | `Prompt/_archive/` | 외부 예시 참조 0건 |
| **짧은 턴 GREEN** | BV 1개·테스트 함수 1개·최소 diff | 기존 pytest | GREEN-P1 11건 순차 |

#### 세션 프롬프트 템플릿 (Try — 즉시 적용용)

```markdown
## Context
- SSOT: Report/02 §<section>, docs/test_plan.md
- Branch: <name> | TDD phase: RED | GREEN | REFACTOR | Ask
- Track: Domain | Boundary | Target IDs: <DT-/UT-/BV->

## Must
- Step 0: `pytest -q` → expect passed __, failed __

## Must NOT
- golden/ERROR 변경 무단 | RED>0 REFACTOR | UT→concrete solver

## Done when
- Command: `<pytest …>` | Result: `<N passed, M failed, exit __>`
```

---

## A.6 개인별 학습 성과 공유 (라운드로빈)

**시간:** 15분 · **인원:** 참가자 전원 · **형식:** 1인 3분 (아래 양식)

### 개인 발표 양식 (복사용)

```markdown
### 이름: ___________

#### 1) 배운 새로운 기술/개념
- 

#### 2) 개인 역량 향상 부분
- 

#### 3) 팀에 공유하고 싶은 인사이트
- 

#### 4) 추천 학습 자료
- 제목/링크:
- 누구에게:
- 한 줄 이유:
```

### 프로젝트 기반 작성 예시 (참고)

| 항목 | 예시 내용 |
|------|-----------|
| **기술/개념** | Dual-Track TDD(DT-* / UT-*), ECB 4레이어, Golden Master approval, `DomainSolverPort` mock 계약 |
| **역량 향상** | RED 스켈레톤 설계, BV 단위 GREEN, pytest 기반 “완료” 판정, AI diff RG 체크 |
| **인사이트** | “커버리지 54%” ≠ REFACTOR 가능 — **entity 0%**가 병목 (`Report/17`) |
| **추천 자료** | `Report/02` (설계 SSOT), `docs/test_plan.md`, Kent Beck TDD 챕터, Cursor rules MDC |

---

## A.7 세션 마무리 체크리스트

- [ ] Keep Top 5 합의·Part B “유지 관행”에 반영  
- [ ] Problem Top 5 · 각 1개 이상 Try 매핑  
- [ ] Part B 액션 **담당·목표일·성공 기준** 100% 기입  
- [ ] Part C 신규 학습 자료 1건 이상 추가  
- [ ] Part D 다음 스프린트 1순위 3개 확정  
- [ ] 다음 회고 일정·진행자·기록자 지명  

---

## 사전 준비 체크리스트 (참가자 · 세션 24h 전)

| # | 준비 항목 | 완료 |
|---|-----------|------|
| 1 | 최근 `pytest -q` 결과 스크린샷 또는 로그 | ☐ |
| 2 | 본인이 쓴 Prompt/Report 1건 링크 | ☐ |
| 3 | Keep 2건 · Problem 2건 · Try 1건 (각 1문장) | ☐ |
| 4 | 개인 발표 양식(A.6) 초안 | ☐ |
| 5 | 추천 학습 자료 1건 | ☐ |

---

# Part B: 액션 아이템 추적 템플릿

## B.1 추적 원칙

| 원칙 | 설명 |
|------|------|
| **SMART** | Specific · Measurable · Assignable · Realistic · Time-bound |
| **WIP 제한** | 동시 진행 P0 액션 ≤ 3건/팀 |
| **주간 리뷰** | 매주 금요일 15분 — 상태·블로커·일정 조정 |
| **완료 정의** | “문서 작성”만으로 Done 불가 — **측정 가능 산출물** 필수 |

## B.2 액션 보드 (마스터)

> **상태:** `⬜ Todo` · `🔄 Doing` · `✅ Done` · `⏸ Blocked` · `❌ Cancelled`  
> **진행 추적:** README To-Do · GitHub Issue/Project · 주간 회의록 `docs/prompt_review_log.md`

| ID | 액션 (구체적) | Problem/Keep 연결 | 담당 | 우선 | 목표일 | 상태 | 성공 기준 (측정) | 진행 추적 방법 | 비고 |
|----|---------------|-------------------|------|------|--------|------|------------------|----------------|------|
| ACT-01 | `docs/prompt_session_template.md` 작성·README 링크 | Try: 템플릿 | *(이름)* | P0 | YYYY-MM-DD | ⬜ | README 링크·워크숍 1회 시연 | PR + 회의록 | |
| ACT-02 | `Prompt/05` Magic Square용 개정 또는 `_archive/` | Problem: 드리프트 | *(이름)* | P1 | | ⬜ | Refrigerator 참조 0건 | grep 검색 | |
| ACT-03 | 세션 종료 산출물: Report 1 + Transcript 1 + pytest 스니펫 | Keep: Export | 전원 | P0 | | ⬜ | 3회 연속 3종 첨부 | Report 목록 | Report/17 8섹션 |
| ACT-04 | REFACTOR PR에 Phase 0 gate 체크리스트 | Problem: 조기 REFACTOR | *(이름)* | P0 | | ⬜ | RED≠0 REFACTOR PR 0건 | PR template | G-01~G-05 |
| ACT-05 | 주 1회 15분 Prompt 리뷰 | Try: 리뷰 | *(이름)* | P1 | | ⬜ | 4주 연속 `prompt_review_log` | docs 파일 | |
| ACT-06 | Ask 모드 규칙 문서화 | Try: Ask | QA+Dev | P1 | | ⬜ | Report/17 = 팀 표준 명시 | README | |
| ACT-07 | code-reviewer C/M → defect_list 동기화 | Problem: 검증 | QA | P1 | | ⬜ | C-1·C-2 추적 ID | defect_list | GREEN-P2 전 |
| ACT-08 | Report↔Prompt↔phase 인덱스표 | Problem: 검색 | *(이름)* | P2 | | ⬜ | README 1표 완성 | README diff | |
| ACT-09 | Dual-Track cov CI 스크립트(선택) | Try: cov gate | DevOps | P2 | | ⬜ | entity/boundary % artifact | CI log | Wave 1 전 |
| ACT-10 | 민감정보·force push 금지 재확인 | Keep: 안전 | 전원 | P0 | | ⬜ | backup agent 규칙 리뷰 서명 | 회의록 | |

## B.3 주간 스탠드업 기록 (복사용)

| 주차 | 날짜 | ACT-ID | 진행 | 블로커 | 다음 주 |
|------|------|--------|------|--------|---------|
| W1 | | ACT-01 | | | |
| W1 | | ACT-03 | | | |

## B.4 완료 증거 체크리스트 (액션 Done 시)

- [ ] 성공 기준 수치·링크가 PR/Report/회의록에 남음  
- [ ] 관련 Problem이 재발하지 않았음을 1회 확인  
- [ ] Part C 학습 자료에 “배운 점” 1줄 추가(해당 시)  

---

# Part C: 학습 자료 정리 문서

## C.1 프로젝트 SSOT (필독 순서)

| 순서 | 자료 | 경로 | 학습 목표 |
|------|------|------|-----------|
| 1 | 문제 정의·불변 | [Report/01](../Report/01.Magic_Square_Problem_Definition_Report.md) | C1~C5, V1~V3 |
| 2 | TDD·Clean Architecture | [Report/02](../Report/02.Magic_Square_TDD_Clean_Architecture_Design_Report.md) | Dual-Track, DT/UT/IT |
| 3 | 테스트 계획 | [docs/test_plan.md](test_plan.md) | BV, AC-FR-01-01 |
| 4 | 결함 목록 | [docs/defect_list.md](defect_list.md) | DEF-001~009 |
| 5 | GREEN 로드맵 | [Report/11](../Report/11.Magic_Square_GREEN_Roadmap_And_README_Update_Report.md) | G-01~G-05 |
| 6 | REFACTOR·ECB | [Report/15](../Report/15.Magic_Square_REFACTOR_ECB_Analysis_And_README_Update_Report.md) | 18항목·스멜 |
| 7 | QA·커버리지 gate | [Report/17](../Report/17.Magic_Square_QA_Coverage_DualTrack_And_Transcript_Export_Report.md) | NFR, Dual-Track cov |

## C.2 프롬프팅·AI 협업

| 자료 | 경로 | 대상 | 요약 |
|------|------|------|------|
| Cursor Rules (금지·TDD) | `.cursor/rules/magicsquare-*.mdc` | 전원 | RG-01~05, RED-first |
| Agent 역할 정의 | `.cursor/agents/*.md` | 진행자 | code-reviewer, QA 등 |
| Prompt Transcript 샘플 | `Prompt/14~16`, `Prompt/19~21` | 신규 | GREEN·REFACTOR·Ask 패턴 |
| Multi-agent (정리 필요) | `Prompt/05.Multi_Agent_Collaboration_Prompt.md` | 리드 | ⚠ 타 프로젝트 예시 — archive 예정 |

## C.3 기술·테스트 실습

| 주제 | 명령·파일 | 비고 |
|------|-----------|------|
| AC-FR GREEN | `pytest tests/boundary/test_ac_fr_01_01_invalid_size.py -q` | 33 passed 목표 |
| Golden Master | `pytest -m golden_master -v` | 6 passed |
| 전체 기준선 | `pytest -q` | 54 passed / 23 failed (Phase 2 RED) |
| 커버리지 | `pytest --cov=src/magicsquare --cov-report=html` | `htmlcov/` |
| GUI | `python -m magicsquare.boundary.screen` | PyQt 선택 |

## C.4 외부·추천 학습 (팀 공유용)

| 분류 | 추천 | 추천 대상 | 이유 |
|------|------|-----------|------|
| TDD | Kent Beck, *Test-Driven Development* | 개발 전원 | RED-GREEN-REFACTOR 사이클 |
| 아키텍처 | Clean Architecture (Martin) 요약 자료 | 설계 담당 | ECB·의존 방향 |
| 계약 테스트 | pytest mock · ports 패턴 | Boundary | UT-* mock 검증 |
| AI 협업 | Cursor Docs — Rules, Agents, Ask mode | 전원 | phase·readonly 활용 |

## C.5 세션 후 추가 기록 (팀이 채움)

| 날짜 | 공유자 | 자료/링크 | 한 줄 요약 | Part B ACT 연결 |
|------|--------|-----------|------------|-----------------|
| | | | | |

---

# Part D: 다음 프로젝트 개선 계획서

## D.1 비전 (한 문장)

**「SSOT·계약 테스트·증거 기반 완료」를 AI 협업에도 동일하게 적용하여, Magic_Square_XX의 잔여 RED 23건을 게이트 준수 하에 GREEN하고, REFACTOR Wave를 안전하게 완료한다.**

## D.2 현재 기준선 (Step 0 · Report/17·18)

| 지표 | 현재 | 다음 마일스톤 |
|------|------|----------------|
| `pytest tests/` | 54 passed · 23 failed | 77 passed (Phase 0) |
| AC-FR-01-01 | 33/33 ✅ | 유지 |
| Golden Master | 6/6 ✅ | 유지 |
| Entity cov | 0% | GREEN-P2 후 상승 |
| REFACTOR Wave 1 | ❌ Phase 0 미충족 | G-01~G-05 충족 후 |

## D.3 실행 로드맵

| 단계 | 기간(예) | 목표 | 주요 Try·액션 | 성공 기준 |
|------|----------|------|---------------|-----------|
| **0. 정비** | 1주 | 프롬프트·문서 SSOT | ACT-01,02,08 | 템플릿·인덱스·archive |
| **1. GREEN-P1** | 2~3주 | Boundary 11 RED | `input_validator`, `ui_boundary` | U-IN/FLOW/OUT GREEN |
| **2. GREEN-P2** | 2~3주 | Entity 12 RED | D-VAL~D-SOL, Grid4x4 | Domain skeleton 0 failed |
| **3. Phase 0 gate** | 1주 | G-01~G-05 | `test_main_window` 등 | `pytest tests/` 전체 GREEN |
| **4. REFACTOR Wave 1** | 2주 | A그룹 C1~C4 | README 3그룹 #1~6 | RF-01~04 + GM 유지 |
| **5. 표준화** | 분기 | 팀 Wiki·CI | ACT-09, Pilot→Expand | 온보딩 1일 1 GREEN 사이클 |

## D.4 프로세스 개선 (다음 프로젝트 공통)

| 영역 | As-Is | To-Be | 담당 | 추적 |
|------|-------|-------|------|------|
| 프롬프트 | 대화형·혼재 | 템플릿 필수 | 전원 | PR checklist |
| TDD phase | 가끔 생략 | 제목+gate 표 | 개발 | REFACTOR PR 반송 |
| 완료 정의 | AI 서술 | pytest 수치 | QA | Report pytest 스니펫 |
| 문서 | 22 Transcript 분산 | 활성 SSOT 1표 | 문서 | README |
| 회고 | ad-hoc | KPT 90분·Part B 주간 | 진행자 | `prompt_review_log` |

## D.5 리스크·완화

| 리스크 | 영향 | 완화 | Owner |
|--------|------|------|-------|
| False Green | 계약 파괴 | GM + AC-FR 병행 | QA |
| AI 대량 리팩터 | RED 증가 | Phase 0 gate | Tech Lead |
| 문서 드리프트 | 잘못된 지시 | 세션 후 defect_list 동기화 | Scribe |
| 프롬프트 피로 | 참여 저하 | 템플릿·15분 리뷰 | Facilitator |

## D.6 다음 회고 일정 (예약)

| 회차 | 일정 | 초점 | 준비물 |
|------|------|------|--------|
| KPT #2 | *(YYYY-MM-DD)* | GREEN-P1 중간 | pytest + Keep/Problem 각 2건 |
| KPT #3 | *(YYYY-MM-DD)* | Phase 0 gate | Part B ACT 전체 리뷰 |

---

## 부록: 프로젝트 타임라인 (회고 발표용)

| 시기 | Report / Prompt | Phase | 성과 |
|------|-----------------|-------|------|
| 설계·규칙 | 01~04 | 설계 | SSOT·Cursor MDC |
| RED·QA | 07, Prompt/11 | RED | 33 RED·defect_list |
| GREEN | 10~12, Prompt/14~16 | GREEN | AC-FR 33/33 |
| GUI·GM | 13~14, Prompt/17~18 | GREEN+GM | PyQt·GM 6/6 |
| REFACTOR·QA | 15~18, Prompt/19~22 | REFACTOR·Ask | 3그룹 To-Do·cov gate |

---

*본 문서는 Magic_Square_XX 산출물을 바탕으로 한 **회고 세션 기획·운영 패키지**이다. Part B 담당·일정은 팀 회의에서 확정하고, 세션 후 `docs/prompt_review_log.md`로 추적을 이어간다.*
