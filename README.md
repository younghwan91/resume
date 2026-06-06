# Younghwan Chae — Resume

LaTeX source for my resume, with automatic PDF build via GitHub Actions.

## Download

| Version | Link |
|---------|------|
| English | [resume_en.pdf](../../releases/latest/download/resume.pdf) |
| Korean  | [resume_ko.pdf](../../releases/latest/download/resume.pdf) |

## Structure

```
resume/
├── en/resume.tex   # English version
├── ko/resume.tex   # Korean version
└── .github/
    └── workflows/
        └── build.yml  # Auto-build on push to main
```

## Build locally

Requires a LaTeX distribution with XeLaTeX (e.g. TeX Live, MiKTeX).

```bash
# English
cd en && xelatex resume.tex

# Korean (requires kotex)
cd ko && xelatex resume.tex
```
