"""엔지니어판과 퀀트판의 공통 섹션(경력·학력·논문·특허·수상)이 같은지 검사한다."""
import re, sys

SHARED = {
    "en": ["Experience", "Education", "Publications", "Patent Applications", "Awards"],
    "ko": ["경력", "학력", "주요 논문", "특허 출원", "수상 경력"],
}


def sections(path):
    text = open(path, encoding="utf-8").read()
    text = text[: text.index(r"\end{document}")]
    parts = re.split(r"(?m)^\\section\{", text)[1:]
    out = {}
    for part in parts:
        title = part.split("}", 1)[0]
        body = re.sub(r"(?m)^%.*\n|^\\needspace.*\n", "", part)  # 주석·쪽 나눔 힌트는 무시
        out[title] = body.strip()
    return out


bad = 0
for lang, names in SHARED.items():
    eng, quant = sections(f"{lang}/resume.tex"), sections(f"quant/{lang}/resume.tex")
    for name in names:
        e = next((v for k, v in eng.items() if k.startswith(name)), None)
        q = next((v for k, v in quant.items() if k.startswith(name)), None)
        if e is None or q is None or e != q:
            bad += 1
            print(f"MISMATCH {lang}: section '{name}' differs between {lang}/ and quant/{lang}/")
sys.exit(1 if bad else 0)
