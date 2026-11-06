# resume — 공개 이력서 (PUBLIC)

마스터 이력서 두 종 × 두 언어 = 네 파일:
- **엔지니어판** `en/resume.tex`·`ko/resume.tex` → `resume_en.pdf`·`resume_ko.pdf` (프로필 README 가 이 링크를 쓴다 — 경로·이름 유지)
- **퀀트판** `quant/en/resume.tex`·`quant/ko/resume.tex` → `resume_quant_en.pdf`·`resume_quant_ko.pdf`

`main` 에 푸시하면 CI(`build.yml`)가 네 PDF 를 빌드해 공개 릴리스 `latest` 를 **즉시 덮어쓴다** — 푸시 = 공개 배포.
그래서 푸시는 사용자가 "푸시"라고 한 뒤에만.

## 지원처별·비공개 이력서는 이 레포가 아니다
- 회사별 맞춤 이력서·JD·지원 현황(`STATUS.md`)은 **`~/git/resume-private`**(PRIVATE, 기본 브랜치 `master`).
  특정 회사 지원용 요청은 그쪽에서 작업한다. 그 레포의 CLAUDE.md 를 먼저 읽는다.
- 비공개 레포 내용(지원처, JD, 개인 연락처)을 이 공개 레포로 옮기지 않는다.
- `.orca/` 는 JD PDF·회사 자료 드롭존 — gitignore 돼 있다. 절대 커밋하지 않는다.

## 로컬 빌드 (LaTeX 는 설치돼 있다)
시스템 `xelatex` 는 없지만 메인 체크아웃 `~/git/resume/tectonic` 에 바이너리가 있다(gitignore — 워크트리엔 없으니
`./tectonic` 말고 이 절대 경로를 쓴다). 새로 내려받지 않는다.
```bash
O=<scratchpad>/build; mkdir -p $O/en $O/ko
~/git/resume/tectonic -X compile en/resume.tex --outdir $O/en
~/git/resume/tectonic -X compile ko/resume.tex --outdir $O/ko
for d in quant/en quant/ko; do mkdir -p $O/$d; ~/git/resume/tectonic -X compile $d/resume.tex --outdir $O/$d; done
uv run -q --with pymupdf python -I -c "import pymupdf,sys; [print(f, pymupdf.open(f).page_count) for f in sys.argv[1:]]" $O/en/resume.pdf $O/ko/resume.pdf $O/quant/*/resume.pdf
```
- 빌드 산출물은 scratchpad 로. 레포 안 `resume.pdf` 네 개는 gitignore(CI 가 만든다).
- 수정 뒤에는 고치기 전 PDF(`gh release download latest`)와 쪽수를 비교해 보고한다(통합판이라 늘어도 된다).

## 두 판의 차이 — 나머지는 같아야 한다
- 엔지니어판: 요약은 최적화 → 비트센싱 → 두산 → LLM 에이전트 흐름, 퀀트 프로젝트는 3줄 요약 섹션(경력 뒤), 기술에 Quant Research 줄 없음.
- 퀀트판: 퀀트 중심 요약, 퀀트 리서치 프로젝트 전체(5건)를 경력 앞에, 기술은 Optimization·Quant Research 줄이 맨 위.
- 경력·학력·논문·특허·수상 본문은 네 파일이 같다 — 사실을 고치면 네 파일을 같은 커밋에서 고친다.
  `python3 scripts/check_shared.py` 가 대조한다(CI 첫 단계, 다르면 빌드 실패).
- 둘 다 해당 트랙의 통합판(superset)이다: 쪽수·관련성 때문에 빼지 않는다. 공개 불가 정보(전화, 사내 일정·내부 벤치마크·인프라)만 뺀다.

## 내용 규칙
- **기여 범위는 사용자가 말한 그대로** — 부풀리지도 줄이지도 않는다. 모르면 묻는다.
- 영문·국문을 **같은 커밋에서 함께** 고치고, 직함·날짜·수치·용어가 두 판에서 일치하는지 대조한다.
- 국문판: 어색한 음차(서로게이트 등)보다 영어 원어를 쓴다.
- 공개 레포다 — 휴대폰 번호·거주 도시·회사 내부 정보는 넣지 않는다. 이메일·LinkedIn·GitHub 는 공개 OK.
- README 에 요청 없는 섹션(License 등)을 덧붙이지 않는다.
