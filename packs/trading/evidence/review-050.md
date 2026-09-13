## UBC-MDS-2023-24/fixml
Source: https://github.com/UBC-MDS-2023-24/fixml
{"stars": 4, "observed_at": "2026-09-13T15:41:12.553856+00:00", "latest_commit": "10b8f41b2fd5a264bc4612df7d27aecee74adfee", "last_commit_date": "2024-11-28T18:46:35Z", "license": "NOASSERTION", "license_path": "LICENSE", "bank_status": "NEW", "bank_layers": [], "archived": false, "commits_since_20260313_count_capped100": 0, "language": "Python"}
Description [vendor]: LLM Tool for effective test evaluation of ML projects with curated Checklists and LLM prompts
README excerpt [vendor, not an endorsement]: # FixML [![Python 3.12.0+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/) [![GitHub Release](https://img.shields.io/github/release/ubc-mds/fixml.svg?style=flat)]() [![PyPI - Version](https://img.shields.io/pypi/v/fixml)](https://pypi.org/project/fixml/) [![GitHub Activity](https://img.shields.io/github/last-commit/ubc-mds/fixml/main.svg?style=flat)]() [![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![Documentation Status](https://readthedocs.org/projects/fixml/badge/?version=latest)](https://fixml.readthedocs.io/en/latest/?badge=latest) ![CI status check](https://github.com/UBC-MDS/fixml/actions/workflows/ci.yml/badge.svg) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) A tool for providing context-aware evaluations using a checklist-based approach on the Machine Learning project code bases. ## Documentations - Guides and API documentations: [https://fixml.readthedocs.org](https://fixml.readthedocs.org) - Reports and proposals: [https://ubc-mds.github.io/fixml](https://ubc-mds.github.io/fixml) ## Ins
Actual LICENSE excerpt: # Instructional Material All reports and non-software related materials including tables, plots and images under this project is made available under the **Creative Commons Attribution 4.0 International License** ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)). ## You are free to: **Share** — copy and redistribute the material in any medium or format for any purpose, even commercially. **Adapt** — remix, transform, and build upon the material for any purpose, even commercially. The l
Recent author count: 0; sampled contributors: 6
Adoption bank: null
Issue sample: {"url": "https://github.com/UBC-MDS-2023-24/fixml/issues/211", "created_at": "2024-11-01T21:50:03Z", "state": "open", "comments": 1, "first_staff_comment_in_sample": "2024-11-03T22:00:53Z", "sample_limit": 20}
Manifests: pyproject.toml

## uberdeveloper/omspy
Source: https://github.com/uberdeveloper/omspy
{"stars": 55, "observed_at": "2026-09-13T15:41:12.553856+00:00", "latest_commit": "1fbd39331e1568fb259364c3b3bb2a7a647cec0b", "last_commit_date": "2025-12-01T18:21:41Z", "license": "MIT", "license_path": "LICENSE", "bank_status": "NEW", "bank_layers": [], "archived": false, "commits_since_20260313_count_capped100": 0, "language": "Python"}
Description [vendor]: Improved Order Management System for stock trading
README excerpt [vendor, not an endorsement]: # 📈 OMSpy Order Management A powerful yet simple order management system for trading operations. Build, track, and execute orders with confidence. ## ✨ Features - 🎯 **Simple API** - Intuitive order creation and management - 📊 **Position Tracking** - Real-time position and P&L monitoring - 💾 **Database Integration** - Built-in SQLite persistence - 🔄 **Order Types** - Market, Limit, Stop, and complex orders - 📦 **Order Baskets** - Group and manage multiple orders - ⚡ **High Performance** - Optimized for trading workflows ## 🚀 Quick Start ### 🎯 Create a Basic Order ```python from omspy.order import Order # Create a simple market buy order order = Order(symbol="AAPL", side="buy", quantity=10) print(f"Order ID: {order.id}") ``` ### 💰 Create Different Order Types ```python # Market order (executes immediately) market_order = Order(symbol="TSLA", side="buy", quantity=5) # Limit order (executes at specific price or better) limit_order = Order(symbol="MSFT", side="sell", quantity=3, order_type="LIMIT", price=380.50) # Stop loss order (triggers when price drops) stop_order = Order(symbol="NVDA", side="sell", quantity=2, order_type="STOP", trigger_price=450.00) ``` ### ⏰ Time-Based Orders ```python # Order that expires after 30 minutes short_order = Order(symbol="GOOGL", side="buy", quantity=1, expires_in=1800) # 30 minutes # Day order (valid until market close) day_order = Order(symbol="
Actual LICENSE excerpt: MIT License Copyright (c) 2021-present, Ubermensch Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyri
Recent author count: 0; sampled contributors: 3
Adoption bank: null
Issue sample: {"url": "https://github.com/uberdeveloper/omspy/issues/49", "created_at": "2024-12-14T14:55:40Z", "state": "closed", "comments": 0, "first_staff_comment_in_sample": null, "sample_limit": 20}
Manifests: pyproject.toml

## uebber/ibkr-german-tax-declaration-engine
Source: https://github.com/uebber/ibkr-german-tax-declaration-engine
{"stars": 18, "observed_at": "2026-09-13T15:41:12.553856+00:00", "latest_commit": "5a64079c277451da1b082a1d7f753821cc68466f", "last_commit_date": "2026-08-09T11:42:17Z", "license": "MIT", "license_path": "LICENSE", "bank_status": "NEW", "bank_layers": [], "archived": false, "commits_since_20260313_count_capped100": 100, "language": "Python"}
Description [vendor]: Automate the generation of figures for your German tax declaration (Anlage KAP, KAP-INV, SO) based on Interactive Brokers (IBKR) Flex Query reports.
README excerpt [vendor, not an endorsement]: # IBKR German Tax Declaration Engine **Automate the generation of figures for your German tax declaration (Anlage KAP, KAP-INV, SO) based on Interactive Brokers (IBKR) Flex Query CSV reports.** ## What is this? German tax residents using Interactive Brokers (IBKR) often face significant challenges in accurately completing their tax declaration forms, especially Anlage KAP, Anlage KAP-INV, and Anlage SO. This tool aims to simplify this process by: 1. Parsing your IBKR Flex Query CSV reports (with full historical data for FIFO cost basis). 2. Identifying and classifying your assets (stocks, bonds, ETFs, options, CFDs, etc.). 3. Performing currency conversions to EUR using daily ECB rates. 4. Calculating capital gains/losses using the FIFO method (with `Decimal` precision). 5. Handling corporate actions (splits, cash mergers, stock-for-stock mergers, taxable stock dividends). 6. Processing option exercises, assignments, expirations, and cash settlements (index options). 7. Tracking position flips (IBKR `C;O` / `O;C` indicators) with automatic FIFO lot splitting. 8. Calculating income from dividends, interest, and fees within the tax year. 9. Applying German Teilfreistellung (partial tax exemption) for investment funds. 10. Calculating Vorabpauschale for investment funds. 11. Tracking foreign currency positions and FX gains/losses under section 23 EStG. 12. Aggregating figures requ
Actual LICENSE excerpt: MIT License Copyright (c) 2025 uebber Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice an
Recent author count: 2; sampled contributors: 2
Adoption bank: null
Issue sample: {"url": "https://github.com/uebber/ibkr-german-tax-declaration-engine/issues/85", "created_at": "2026-08-26T21:21:56Z", "state": "open", "comments": 0, "first_staff_comment_in_sample": null, "sample_limit": 20}
Manifests: pyproject.toml

## UFund-Me/Qbot
Source: https://github.com/UFund-Me/Qbot
{"stars": 18496, "observed_at": "2026-09-13T15:41:12.553856+00:00", "latest_commit": "f0425ae4ae8bd02b79656b8f7039f4cd6874095e", "last_commit_date": "2026-03-11T12:16:11Z", "license": "MIT", "license_path": "LICENSE", "bank_status": "ALREADY IN THE BANK", "bank_layers": ["liftable"], "archived": false, "commits_since_20260313_count_capped100": 0, "language": "Jupyter Notebook"}
Description [vendor]: [🔥updating ...] AI 自动量化交易机器人(完全本地部署) AI-powered Quantitative Investment Research Platform. 📃 online docs: https://ufund-me.github.io/Qbot   ✨ :news: qbot-mini: https://github.com/Charmve/iQuant
README excerpt [vendor, not an endorsement]: 👆 右上角点击 告诉我，你希望这个项目继续加速开发迭代 ❤️ & ☕️ 🤖 Qbot since Sep 26 [![CodeQL](https://github.com/UFund-Me/Qbot/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/UFund-Me/Qbot/actions/workflows/codeql-analysis.yml) [![AutoTrade](https://github.com/UFund-Me/Qbot/actions/workflows/auto-trade.yml/badge.svg)](https://github.com/UFund-Me/Qbot/actions/workflows/auto-trade.yml) [![Pylint](https://github.com/UFund-Me/Qbot/actions/workflows/pylint.yml/badge.svg)](https://github.com/UFund-Me/Qbot/actions/workflows/pylint.yml) [![Coverage](https://github.com/UFund-Me/Qbot/actions/workflows/coverage.yml/badge.svg)](https://github.com/UFund-Me/Qbot/actions/workflows/coverage.yml) &nbsp; Qbot website HOT &nbsp;&nbsp;&nbsp;&nbsp; Qbot DeepWiki TRY IT OUT &nbsp; AI智能量化投研平台 > Qbot is an AI-oriented automated quantitative investment platform, which aims to realize the potential, empower AI technologies in quantitative investment. Qbot supports diverse machine learning modeling paradigms. including supervised learning, market dynamics modeling, and RL. --> ``` 🤖 Qbot = 智能交易策略 + 回测系统 + 自动化量化交易 (+ 可视化分析工具) | | | | | | | \_ quantstats (dashboard\online operation) | | \______________ Qbot - vnpy, pytrader, pyfunds | \____________________________ BackTest - backtrader, easyquant \________________________________________ quant.ai - qlib, deep learning strategies ``` 🎺 号外 ：Qbot微信小程序开发招募 [UFund-mi
Actual LICENSE excerpt: MIT License Copyright (c) 2022 UFund-Me Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice 
Recent author count: 0; sampled contributors: 3
Adoption bank: null
Issue sample: {"url": "https://github.com/UFund-Me/Qbot/issues/73", "created_at": "2023-11-16T15:32:10Z", "state": "open", "comments": 2, "first_staff_comment_in_sample": "2024-05-14T09:56:04Z", "sample_limit": 20}
Manifests: requirements.txt

## ultimatesimp/Cloneberg-Terminal
Source: https://github.com/ultimatesimp/Cloneberg-Terminal
{"stars": 0, "observed_at": "2026-09-13T15:41:12.553856+00:00", "latest_commit": null, "last_commit_date": null, "license": null, "license_path": null, "bank_status": "NEW", "bank_layers": [], "archived": false, "commits_since_20260313_count_capped100": 0, "language": null}
Description [vendor]: An (very basic) alternative to the bloomberg terminal
README excerpt [vendor, not an endorsement]: 
Actual LICENSE excerpt: 
Recent author count: 0; sampled contributors: 0
Adoption bank: null
Issue sample: null
Manifests: 

## umutto/crypto-tax
Source: https://github.com/umutto/crypto-tax
{"stars": 1, "observed_at": "2026-09-13T15:41:12.553856+00:00", "latest_commit": "8c8147dfd17537a3b59e72e6673ed4fc066ab0a1", "last_commit_date": "2022-02-20T10:11:02Z", "license": "MIT", "license_path": "LICENSE", "bank_status": "NEW", "bank_layers": [], "archived": false, "commits_since_20260313_count_capped100": 0, "language": "TypeScript"}
Description [vendor]: Personal cryptocurrency tax calculator for Japan's miscellaneous income. 
README excerpt [vendor, not an endorsement]: # crypto-tax Personal cryptocurrency tax calculator for Japan's miscellaneous income. This is a rough project that I've did for myself while studying react/nextjs and nosql for the first time, so it may not work correctly... --- This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).
Actual LICENSE excerpt: MIT License Copyright (c) 2021 Umut Karakulak Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright n
Recent author count: 0; sampled contributors: 1
Adoption bank: null
Issue sample: null
Manifests: package.json

## uniswap-python/uniswap-python
Source: https://github.com/uniswap-python/uniswap-python
{"stars": 1012, "observed_at": "2026-09-13T15:41:12.553856+00:00", "latest_commit": "bc8fdf4b915efac134c2cb6cadca8ec5073b1c48", "last_commit_date": "2026-08-05T18:10:34Z", "license": "MIT", "license_path": "LICENSE", "bank_status": "ALREADY IN THE BANK", "bank_layers": ["bank_best", "liftable"], "archived": false, "commits_since_20260313_count_capped100": 8, "language": "Python"}
Description [vendor]: 🦄 The unofficial Python client for the Uniswap exchange.
README excerpt [vendor, not an endorsement]: # uniswap-python [![GitHub Actions](https://github.com/shanefontaine/uniswap-python/workflows/Test/badge.svg)](https://github.com/shanefontaine/uniswap-python/actions) [![codecov](https://codecov.io/gh/uniswap-python/uniswap-python/branch/master/graph/badge.svg?token=VHAZHHLFX8)](https://codecov.io/gh/uniswap-python/uniswap-python) [![Downloads](https://pepy.tech/badge/uniswap-python)](https://pepy.tech/project/uniswap-python) [![License](http://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/shanefontaine/uniswap-python/master/LICENSE) [![PyPI](https://img.shields.io/pypi/v/uniswap-python)](https://pypi.org/project/uniswap-python/) [![Typechecking: Mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![GitPOAP Badge](https://public-api.gitpoap.io/v1/repo/uniswap-python/uniswap-python/badge)](https://www.gitpoap.io/gh/uniswap-python/uniswap-python) [![GitHub Repo stars](https://img.shields.io/github/stars/uniswap-python/uniswap-python?style=social)](https://github.com/uniswap-python/uniswap-python/stargazers) [![Twitter Follow](https://img.shields.io/twitter/follow/UniswapPython?label=Follow&style=social)](https://twitter.com/UniswapPython) The unofficial Python client for [Uniswap](https://uniswap.io/). Docume
Actual LICENSE excerpt: The MIT License (MIT) Copyright (c) 2018 Shane Fontaine Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above c
Recent author count: 4; sampled contributors: 28
Adoption bank: null
Issue sample: {"url": "https://github.com/uniswap-python/uniswap-python/issues/342", "created_at": "2023-07-24T14:45:51Z", "state": "closed", "comments": 1, "first_staff_comment_in_sample": "2023-07-28T23:37:46Z", "sample_limit": 20}
Manifests: pyproject.toml

## vbmithr/poloniex
Source: https://github.com/vbmithr/poloniex
{"stars": 7, "observed_at": "2026-09-13T15:41:12.553856+00:00", "latest_commit": "27ab33c7db1e96b77d136ce8222072a4bbd4c2b7", "last_commit_date": "2019-05-21T09:50:18Z", "license": null, "license_path": null, "bank_status": "NEW", "bank_layers": [], "archived": false, "commits_since_20260313_count_capped100": 0, "language": "OCaml"}
Description [vendor]: Poloniex trading DTC server
README excerpt [vendor, not an endorsement]: 
Actual LICENSE excerpt: 
Recent author count: 0; sampled contributors: 1
Adoption bank: null
Issue sample: null
Manifests: 

