# Younghwan Chae — Resume

[![Build Resume PDFs](https://github.com/younghwan91/resume/actions/workflows/build.yml/badge.svg)](https://github.com/younghwan91/resume/actions/workflows/build.yml)

LaTeX source for my resume, with automatic PDF build via GitHub Actions.

## Download

| Version | Link |
|---------|------|
| English | [resume_en.pdf](https://github.com/younghwan91/resume/releases/latest/download/resume_en.pdf) |
| Korean  | [resume_ko.pdf](https://github.com/younghwan91/resume/releases/latest/download/resume_ko.pdf) |

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
