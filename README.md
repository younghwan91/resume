# Younghwan Chae — Résumé

[![Build Resume PDFs](https://github.com/younghwan91/resume/actions/workflows/build.yml/badge.svg)](https://github.com/younghwan91/resume/actions/workflows/build.yml)
[![Latest Release](https://img.shields.io/github/v/release/younghwan91/resume?label=latest%20release)](https://github.com/younghwan91/resume/releases/latest)

PhD-trained ML/AI and optimization engineer specializing in Physical AI, sensor fusion, and real-time embedded inference, with **6 peer-reviewed publications and 10 patent applications**. Currently applying numerical optimization and machine learning to **quantitative trading systems**.

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

| Version | English | Korean |
|---------|---------|--------|
| Engineer (ML, optimization, Physical AI) | [resume_en.pdf](https://github.com/younghwan91/resume/releases/latest/download/resume_en.pdf) | [resume_ko.pdf](https://github.com/younghwan91/resume/releases/latest/download/resume_ko.pdf) |
| Quant (quant research projects first) | [resume_quant_en.pdf](https://github.com/younghwan91/resume/releases/latest/download/resume_quant_en.pdf) | [resume_quant_ko.pdf](https://github.com/younghwan91/resume/releases/latest/download/resume_quant_ko.pdf) |

## Highlights

- **4D radar DoA estimation** — 2× angular resolution over the prior baseline
- **Radar-camera fusion** — 51% reduction in measurement error
- **6 peer-reviewed papers** (IEEE/Springer/Elsevier) and **10 patent applications**
- Core competencies: numerical optimization · sensor fusion · computer vision · embedded inference

## Selected Projects

Independent side projects, unrelated to my day job — applying the same optimization and noisy-signal estimation toolkit used in sensor perception to financial markets, as a demonstration of technical range rather than a change in focus:

| Project | Description |
|---------|-------------|
| [**binance-quant-engine**](https://github.com/younghwan91/binance-quant-engine) | Strategy-agnostic Binance USDT-M futures backtest and execution engine with no-look-ahead guarantees and backtest/live parity |
| [**swing-it**](https://github.com/younghwan91/swing-it) | KOSPI/KOSDAQ alpha validation framework — judged on the per-trade distribution with random null controls, purged CV, and Deflated Sharpe |
| [**portfolio-research**](https://github.com/younghwan91/portfolio-research) | US equity factor engine + tactical asset allocation, gated by walk-forward validation (Deflated Sharpe, PBO) |

**Supporting data infrastructure:** [quant-airflow](https://github.com/younghwan91/quant-airflow) · [krx-quant-core](https://github.com/younghwan91/krx-quant-core) · [kiwoom-client](https://github.com/younghwan91/kiwoom-client) · [krx-fundamentals-client](https://github.com/younghwan91/krx-fundamentals-client) · [krx-news-client](https://github.com/younghwan91/krx-news-client)

## Repository Layout

```
resume/
├── en/resume.tex              # Engineer version, English
├── ko/resume.tex              # Engineer version, Korean (requires kotex)
├── quant/en/resume.tex        # Quant version, English
├── quant/ko/resume.tex        # Quant version, Korean (requires kotex)
└── .github/workflows/
    └── build.yml               # CI: builds and releases PDFs on push to main
```

## Building Locally

**Requirements:** a LaTeX distribution with XeLaTeX support (e.g., [TeX Live](https://www.tug.org/texlive/) or [MiKTeX](https://miktex.org/)).

```bash
# English / Korean engineer versions (Korean requires the kotex package)
cd en && xelatex resume.tex
cd ko && xelatex resume.tex

# Quant versions: same, in quant/en and quant/ko
```

CI builds all four files with `latexmk` in XeLaTeX mode; using `latexmk -xelatex resume.tex` locally will more closely match the CI environment.


## License

CC BY-NC-ND 4.0 — see [LICENSE](LICENSE).
