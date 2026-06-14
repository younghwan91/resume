# Younghwan Chae — Resume

[![Build Resume PDFs](https://github.com/younghwan91/resume/actions/workflows/build.yml/badge.svg)](https://github.com/younghwan91/resume/actions/workflows/build.yml)

PhD-trained ML/AI & optimization engineer — Physical AI, sensor fusion, and real-time embedded inference, with **8 peer-reviewed publications and 10 patents**. Currently applying numerical optimization and machine learning to **quantitative trading systems**.

**Links:** [LinkedIn](https://linkedin.com/in/younghwanchae) · [GitHub](https://github.com/younghwan91) · [Email](mailto:chyohw97@gmail.com)

## Download

| Version | Link |
|---------|------|
| English | [resume_en.pdf](https://github.com/younghwan91/resume/releases/latest/download/resume_en.pdf) |
| Korean  | [resume_ko.pdf](https://github.com/younghwan91/resume/releases/latest/download/resume_ko.pdf) |

## Highlights

- **4D radar DoA estimation** — 2× angular resolution over the prior baseline
- **Radar-camera fusion** — 51% reduction in measurement error
- **8 peer-reviewed papers** (IEEE/Springer), **10 patents**
- Core: numerical optimization · sensor fusion · computer vision · embedded inference

## Selected projects

Applying the same optimization/engineering rigor to quantitative finance:

| Project | Description |
|---------|-------------|
| [**quantbox-engine**](https://github.com/younghwan91/quantbox-engine) | Strategy-agnostic crypto-futures backtest & execution engine — no-look-ahead, backtest/live parity |
| [**kr-quant**](https://github.com/younghwan91/kr-quant) | Korean equity investor-flow collection + Wyckoff-style accumulation screener + signal validation |
| [**opt_portfolio**](https://github.com/younghwan91/opt_portfolio) | VAA tactical asset allocation — walk-forward backtest + Sharpe-ratio weight optimization |

Supporting data infrastructure: [kiwoom-rest-api](https://github.com/younghwan91/kiwoom-rest-api) · [krx-fundamentals-api](https://github.com/younghwan91/krx-fundamentals-api) · [krx-news-rest-api](https://github.com/younghwan91/krx-news-rest-api)

## Structure

```
resume/
├── en/resume.tex          # English version
├── ko/resume.tex          # Korean version
└── .github/workflows/
    └── build.yml          # auto-builds & releases PDFs on push to main
```

## Build locally

Requires a LaTeX distribution with XeLaTeX (TeX Live, MiKTeX).

```bash
cd en && xelatex resume.tex   # English
cd ko && xelatex resume.tex   # Korean (requires kotex)
```
