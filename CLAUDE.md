# resume — 공개 이력서 (PUBLIC)

`en/resume.tex`·`ko/resume.tex` 두 판. `main` 에 푸시하면 CI(`build.yml`)가 PDF 를 빌드해
공개 릴리스 `latest` 의 `resume_en.pdf`·`resume_ko.pdf` 를 **즉시 덮어쓴다** — 푸시 = 공개 배포.
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
uv run -q --with pymupdf python -I -c "import pymupdf,sys; [print(f, pymupdf.open(f).page_count) for f in sys.argv[1:]]" $O/en/resume.pdf $O/ko/resume.pdf
```
- 빌드 산출물은 scratchpad 로. `en/resume.pdf`·`ko/resume.pdf` 는 gitignore(CI 가 만든다).
- 수정 뒤에는 고치기 전 PDF(`gh release download latest`)와 쪽수를 비교해 늘지 않았는지 확인한다.

## 내용 규칙
- **기여 범위는 사용자가 말한 그대로.** 과장(led → contributed to 로 정정한 이력)도, 축소(공동 작업을
  "동료의 ~" 로 쓴 것을 지우라고 한 이력)도 안 된다. 모르면 묻는다.
- 영문·국문 두 판을 **같은 커밋에서 함께** 고치고, 직함·날짜·수치·용어가 두 판에서 일치하는지 대조한다.
- 국문판: 어색한 음차(서로게이트 등)보다 영어 원어를 쓴다.
- 공개 레포다 — 휴대폰 번호·거주 도시·회사 내부 정보는 넣지 않는다. 이메일·LinkedIn·GitHub 는 공개 OK.
- README 에 요청 없는 섹션(License 등)을 덧붙이지 않는다.
