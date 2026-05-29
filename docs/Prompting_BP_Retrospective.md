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
| — | **KPT · 개인 학습 요약** (제출용) | [KPT 요약](#kpt-회고-요약-magic_square_xx) · [개인 학습 요약](#개인별-학습-성과-공유-요약-magic_square_xx) |

> **세션 전 준비:** 참가자 각자 Part A의 [사전 준비 체크리스트](#사전-준비-체크리스트)를 24시간 전까지 작성.  
> **세션 후:** Part B 액션 보드 갱신 · Part C에 신규 자료 추가 · Part D를 다음 스프린트 킥오프에 첨부.

---

## KPT 회고 요약 (Magic_Square_XX)

### Keep
- Dual-Track 병렬 설계
- 작은 단위 GREEN · 테스트 통과 후 커밋
- 설계서(SSOT) 선행
- 보고서 + AI 대화 기록 보관
- ECB 책임 분리 유지
- Golden Master 구축
- Cursor 규칙 · AI 코드 리뷰 활용
- Cursor Ask 모드 활용
- pytest로 완료 확인

### Problem
- RED → GREEN → 리팩터 경계 혼용
- 리팩터 조기 착수 (테스트 미통과 상태)
- 프롬프트 엔지니어링 부족
- AI 제안 검증 능력 미흡
- 문서·코드·테스트 불일치
- 커버리지 목표 미달
- ECB 레이어 책임 혼재
- 공통 프롬프트·경로 혼선

### Try
- 테스트 단계 프롬프트에 명시
- AC·테스트 ID 명시 관행 강화
- GM approve 절차 문서화
- 경계 테스트 Mock만 사용 (구현체 직접 연결 금지)
- 상수·에러 메시지 SSOT 선행 정의
- 리팩터 전 Phase 0 Gate 체크리스트
- 공통 프롬프트 템플릿 공유
- Ask 모드 규칙 문서화

---

## 개인별 학습 성과 공유 요약 (Magic_Square_XX)

> 팀원 누구나 이 프로젝트를 거치며 비슷하게 익힐 수 있는 내용입니다. 세션에서 본인 경험 1~2줄씩 덧붙여 공유합니다.

### 1) 배운 새로운 기술/개념
- 테스트 먼저 짜기 (RED → 통과시키기 GREEN → 정리 REFACTOR)
- 도메인·화면(경계) 테스트를 나눠 설계하는 Dual-Track
- 레이어 나누기: 화면 / 검증 / 핵심 로직 (ECB·클린 아키텍처 기본)
- 계약 테스트: “이 입력이면 이 에러/이 결과”를 코드로 고정
- Golden Master: 정답 파일을 두고 나중에 결과가 바뀌지 않게 검사
- AI와 협업: Cursor 규칙, Ask 모드, 역할 나눈 에이전트(리뷰·QA 등)
- pytest로 테스트 실행·통과 개수로 완료 판단

### 2) 개인 역량 향상 부분
- 요구사항을 테스트 케이스·AC ID로 쪼개 말하기
- 한 번에 크게 만들지 않고, 작게 통과시키며 커밋하기
- AI에게 “뭘 하지 말지”, “언제 끝인지”를 문장으로 명확히 주기
- AI가 고친 코드를 pytest·golden으로 직접 확인하는 습관
- 설계서·테스트 계획·결함 목록을 같이 보며 작업하기
- 회고·보고서·대화 기록을 남겨 나중에 이유를 찾는 능력

### 3) 팀에 공유하고 싶은 인사이트
- “테스트 많이 통과”만으로 끝이 아님 — **아직 실패하는 테스트(RED)** 가 있으면 리팩터는 이르다
- “커버리지 숫자”만 보면 위험 — **도메인/경계를 나눠** 어디가 비었는지 봐야 한다
- AI가 “완료했습니다”라고 해도, **내 PC에서 pytest 한 번**이 최종 확인
- 문서·코드·테스트 결과가 어긋나면 다음 AI 지시도 틀어진다 → 작업 끝날 때 한 번 맞춰 보기
- 프롬프트는 길게 잘 쓰는 것보다 **단계·범위·완료 조건**이 짧게 명확한 편이 낫다
- 화면(UI)에 검증 규칙을 넣으면 나중에 고치기 어렵다 → 검증은 경계 레이어로

### 4) 추천 학습 자료
- **프로젝트 설계서** — `Report/02` (TDD·레이어·테스트 종류 이해)
- **테스트 계획** — `docs/test_plan.md` (무엇을 어떤 순서로 검증할지)
- **문제·불변 정의** — `Report/01` (왜 4×4·합 34인지)
- **README To-Do** — 지금 단계·남은 GREEN/리팩터 목록
- **Kent Beck, TDD** — RED-GREEN-REFACTOR 사이클 (책·요약 글이면 충분)
- **Cursor 문서** — Rules, Agents, Ask 모드 (팀 규칙과 같이 보면 좋음)

**세션에서 각자 추가할 한 줄:**  
- 내가 새로 배운 것:  
- 내가 다음에 쓸 습관:  

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
| 1:05~1:20 | **개인 학습 공유** | 라운드로빈 (Part A.6 양식) | Part C 초안 |
| 1:20~1:30 | **액션 확정** | Part B 표 채우기·담당·일정 | 액션 보드 v1 |

## A.4 진행 규칙

- **비난 금지:** 사람이 아닌 프로세스·도구·프롬프트를 논의한다.  
- **증거 우선:** “느렸다”보다 `pytest` 수치·Report ID·커밋 hash를 말한다.  
- **AI 산출물:** “완료”는 AI 말이 아니라 **로컬/CI 검증 결과**로만 인정한다.  
- **결정:** Try·액션은 **SMART**(구체·측정·기한·담당) 미충족 시 다음 회의로 이관하지 않고 당일 축소 합의.

---

## A.5 KPT 회고

> **진행 방법:** 질문 1개씩 읽기 → 2분 개인 메모 → 돌아가며 공유 → 비슷한 항목 묶기 → 중요한 것 3~5개 투표.  
> 아래 목록은 **Magic_Square_XX** 회고 초안이다. 세션에서 추가·삭제·수정한다.

### 회고 때 물어볼 질문 (간단版)

| 구분 | 질문 |
|------|------|
| **Keep** | 뭐가 잘 됐나? · 뭘 계속 할까? · 팀에 뭐가 도움이 됐나? |
| **Problem** | 뭐가 막혔나? · 뭐 때문에 느렸나? · 어떤 방식이 비효율적이었나? |
| **Try** | 다음엔 뭐를 바꿀까? · 뭘 새로 써볼까? · 짧게 실험해볼 건? |

---

### Keep — 계속 유지할 것

- Dual-Track 병렬 설계 (도메인 테스트 · 경계 테스트 나눠서 진행)
- 작은 단위로 GREEN (한 번에 하나씩, 테스트 통과 확인 후 커밋)
- 설계서·테스트 계획을 먼저 보고 작업 (SSOT)
- 작업 후 보고서 + AI 대화 기록 남기기
- ECB 책임 분리 유지 (화면 / 검증 / 비즈니스 로직 나누기)
- Golden Master로 결과값 회귀 방지
- Cursor 규칙·코드 리뷰 AI 역할 활용
- Cursor Ask 모드로 “분석만” 하는 세션 구분
- pytest로 완료 여부 확인 (AI 말만 믿지 않기)

**세션에 추가할 Keep:**  
-  
-  

---

### Problem — 문제점

- RED → GREEN → 리팩터 단계 혼용
- 테스트가 아직 실패하는데 리팩터를 너무 일찍 시작
- 프롬프트 엔지니어링 부족 (목표·범위·완료 조건이 한꺼번에)
- AI 제안 검증 능력 미흡 (바로 적용·되돌리기 반복)
- 문서·코드·테스트 결과가 서로 안 맞음
- 커버리지 목표 미달 (특히 도메인 쪽)
- ECB 레이어 책임 혼재 (검증·화면·로직이 한곳에 몰림)
- 공통 프롬프트·파일 경로 혼선 (다른 프로젝트 예시 섞임)
- 보고서·기록이 많아서 “지금 어디까지 했지?” 찾기 어려움

**세션에 추가할 Problem:**  
-  
-  

---

### Try — 시도해볼 것

- 테스트 단계(RED / GREEN / 리팩터)를 프롬프트 맨 위에 적기
- AC·테스트 ID를 프롬프트에 명시하는 관행 강화
- Golden Master approve(승인) 절차 문서화
- 경계 테스트는 Mock만 사용, 실제 구현체 직접 연결 금지 철저
- 상수·에러 메시지는 한곳에서 먼저 정의 (SSOT)
- 리팩터 전 통과 조건 체크리스트 (Phase 0 Gate)
- 팀 공통 프롬프트 템플릿 만들어서 공유
- Ask 모드 = 코드 수정 없이 분석만, 규칙 문서화
- 주 1회 짧은 프롬프트 회고 (Keep / Problem 각 1건)
- 도메인·경계 커버리지를 나눠서 보기

**세션에 추가할 Try:**  
-  
-  

---

## A.6 개인별 학습 성과 공유 (라운드로빈)

**시간:** 15분 · **인원:** 참가자 전원 · **형식:** 1인 3분  

> 공통 예시는 문서 상단 [개인별 학습 성과 공유 요약](#개인별-학습-성과-공유-요약-magic_square_xx)을 참고하고, **본인만의 경험 1~2줄**을 아래 양식에 적어 발표한다.

### 1) 배운 새로운 기술/개념 (프로젝트 공통)

- 테스트 먼저 짜기 (RED → GREEN → 리팩터)
- Dual-Track: 도메인 테스트와 경계(화면) 테스트 분리
- 레이어 나누기 (화면 / 검증 / 핵심 로직)
- Golden Master로 결과 회귀 방지
- Cursor + AI (규칙, Ask 모드, 리뷰 역할)
- pytest로 통과·실패 개수 확인

**내가 추가로 배운 것:**  
-  

---

### 2) 개인 역량 향상 부분 (프로젝트 공통)

- 요구사항을 테스트·AC 단위로 나누기
- 작게 만들고 테스트 통과 후 커밋하기
- AI에게 범위·금지·완료 조건 명확히 주기
- AI 결과를 pytest로 직접 검증하기
- 설계서·테스트 계획·결함 목록 함께 보기
- 작업 기록(보고서·대화) 남기기

**내가 더 성장한 부분:**  
-  

---

### 3) 팀에 공유하고 싶은 인사이트 (프로젝트 공통)

- 실패 테스트가 남아 있으면 리팩터는 이르다
- 커버리지는 전체만 보지 말고 영역별로 본다
- AI “완료”보다 내 pytest가 기준이다
- 문서·코드·테스트가 어긋나면 다음 작업도 틀어진다
- 프롬프트는 짧고 명확할수록 좋다 (단계·범위·끝 조건)
- 검증 규칙은 UI가 아니라 경계 레이어에 두는 편이 낫다

**팀에 꼭 말하고 싶은 것:**  
-  

---

### 4) 추천 학습 자료 (프로젝트 공통)

| 자료 | 누구에게 | 한 줄 이유 |
|------|----------|------------|
| `Report/02` 설계서 | 개발 전원 | TDD·레이어·테스트 종류의 기준 |
| `docs/test_plan.md` | 테스트·개발 | 무엇을 어떤 순서로 검증할지 |
| `Report/01` 문제 정의 | 기획·개발 | 왜 이 규칙·불변인지 이해 |
| `README` To-Do | 신규 합류 | 지금 단계·남은 일 한눈에 |
| Kent Beck TDD (책·요약) | TDD 입문 | RED-GREEN-REFACTOR 습관 |
| Cursor Rules / Ask 문서 | AI 협업하는 사람 | 팀 규칙과 도구 맞추기 |

**내가 추가 추천하는 자료:**  
- 제목/링크:  
- 누구에게:  
- 이유:  

---

### 개인 발표 양식 (복사용)

```markdown
### 이름: ___________

#### 1) 배운 새로운 기술/개념
- (공통 중 골라 1~2개 + 본인 경험 1줄)

#### 2) 개인 역량 향상 부분
- 

#### 3) 팀에 공유하고 싶은 인사이트
- 

#### 4) 추천 학습 자료
- 
```

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
