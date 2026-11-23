# AI-STOCK | Intelligent Stock Decision System

中文名称：AI-STOCK｜智能股票决策系统

This repository contains a small, independent open-source market-data utility package extracted conceptually from the AI-STOCK engineering project. It is not the complete stock decision application.

## Public components
- Versioned market-data metadata validation.
- Explicit-root quote and candle path construction.
- Market-data error codes.

No live market feeds, trading strategies, portfolio data, AI decision algorithms, credentials, or private runtime configuration are included.

## Requirements
Python 3.9+; standard-library runtime only.

## Tests
Run from the repository root:

    python3 -B -m unittest discover -s tests -v

All test inputs are synthetic. No external network access is required.

## Scope
This package does not implement trading decisions, market prediction, investment advice, or a production data provider. Paths are constructed but files are not opened. Callers must separately enforce filesystem trust boundaries if using untrusted directories or symlinks.

## License
MIT. Maintainer: markmiaoxg008.
