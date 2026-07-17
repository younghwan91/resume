# Younghwan Chae — Résumé

[![Build Resume PDFs](https://github.com/younghwan91/resume/actions/workflows/build.yml/badge.svg)](https://github.com/younghwan91/resume/actions/workflows/build.yml)
[![Latest Release](https://img.shields.io/github/v/release/younghwan91/resume?label=latest%20release)](https://github.com/younghwan91/resume/releases/latest)

PhD-trained ML/AI and optimization engineer specializing in Physical AI, sensor fusion, and real-time embedded inference, with **8 peer-reviewed publications and 10 patents**. Currently applying numerical optimization and machine learning to **quantitative trading systems**.

**Contact:** [LinkedIn](https://www.linkedin.com/in/younghwan-chae/) · [GitHub](https://github.com/younghwan91) · [Email](mailto:chyohw97@gmail.com)

---

## Contents

- [Download](#download)
- [Highlights](#highlights)
- [Selected Projects](#selected-projects)
- [Repository Layout](#repository-layout)
- [Building Locally](#building-locally)

## Download

PDFs are built and published automatically on every push to `main`.

| Version | Link |
|---------|------|
| English | [resume_en.pdf](https://github.com/younghwan91/resume/releases/latest/download/resume_en.pdf) |
| Korean  | [resume_ko.pdf](https://github.com/younghwan91/resume/releases/latest/download/resume_ko.pdf) |

## Highlights

- **4D radar DoA estimation** — 2× angular resolution over the prior baseline
- **Radar-camera fusion** — 51% reduction in measurement error
- **8 peer-reviewed papers** (IEEE/Springer) and **10 patents**
- Core competencies: numerical optimization · sensor fusion · computer vision · embedded inference

## Selected Projects

Independent side projects, unrelated to my day job — applying the same optimization and noisy-signal estimation toolkit used in sensor perception to financial markets, as a demonstration of technical range rather than a change in focus:

| Project | Description |
|---------|-------------|
| [**quantbox-engine**](https://github.com/younghwan91/quantbox-engine) | Strategy-agnostic crypto-futures backtest and execution engine with no-look-ahead guarantees and backtest/live parity |
| [**kr-quant**](https://github.com/younghwan91/kr-quant) | Korean equity investor-flow collection, Wyckoff-style accumulation screener, and signal validation |
| [**opt_portfolio**](https://github.com/younghwan91/opt_portfolio) | VAA tactical asset allocation with walk-forward backtesting and Sharpe-ratio weight optimization |

**Supporting data infrastructure:** [kiwoom-rest-api](https://github.com/younghwan91/kiwoom-rest-api) · [krx-fundamentals-api](https://github.com/younghwan91/krx-fundamentals-api) · [krx-news-rest-api](https://github.com/younghwan91/krx-news-rest-api)

## Repository Layout

```
resume/
├── en/resume.tex              # English version (source)
├── ko/resume.tex              # Korean version (source, requires kotex)
└── .github/workflows/
    └── build.yml               # CI: builds and releases PDFs on push to main
```

## Building Locally

**Requirements:** a LaTeX distribution with XeLaTeX support (e.g., [TeX Live](https://www.tug.org/texlive/) or [MiKTeX](https://miktex.org/)).

```bash
# English version
cd en && xelatex resume.tex

# Korean version (requires the kotex package)
cd ko && xelatex resume.tex
```

CI builds both versions with `latexmk` in XeLaTeX mode; using `latexmk -xelatex resume.tex` locally will more closely match the CI environment.
