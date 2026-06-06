# Younghwan Chae — Resume

[![Build Resume PDFs](https://github.com/younghwan91/resume/actions/workflows/build.yml/badge.svg)](https://github.com/younghwan91/resume/actions/workflows/build.yml)

PhD-trained ML/AI engineer specializing in Physical AI, sensor fusion, and real-time embedded inference — with 8 peer-reviewed publications and 10 patents.

**Links:** [LinkedIn](https://linkedin.com/in/younghwanchae) · [GitHub](https://github.com/younghwan91) · [Email](mailto:chyohw97@gmail.com)

## Download

| Version | Link |
|---------|------|
| English | [resume_en.pdf](https://github.com/younghwan91/resume/releases/latest/download/resume_en.pdf) |
| Korean  | [resume_ko.pdf](https://github.com/younghwan91/resume/releases/latest/download/resume_ko.pdf) |

## Highlights

- **Sr. ML Engineer @ Doosan Robotics** — Physical AI platform for collaborative robots (Aug 2025–present)
- **AI/Perception Engineer @ bitsensing** — 4D radar DoA estimation (2× resolution), radar-camera fusion (51% RMSE reduction), 10 patents filed
- **PhD, Mechanical Engineering, University of Pretoria** — All four degrees Cum Laude
- 8 publications: IEEE Sensors, IEEE RadarConf, Springer Nature, Elsevier

## Structure

```
resume/
├── en/resume.tex   # English version
├── ko/resume.tex   # Korean version
└── .github/
    └── workflows/
        └── build.yml  # Auto-build and release on push to main
```

## Build locally

Requires a LaTeX distribution with XeLaTeX (e.g. TeX Live, MiKTeX).

```bash
# English
cd en && xelatex resume.tex

# Korean (requires kotex)
cd ko && xelatex resume.tex
```
