## 0-don/polymarket-wallet-recovery
Source: https://github.com/0-don/polymarket-wallet-recovery
{"stars": 10, "observed_at": "2026-09-13T15:41:12.553856+00:00", "latest_commit": "66fb2f376eaed784ea27da786360e63821876c82", "last_commit_date": "2026-01-10T03:06:34Z", "license": null, "license_path": null, "bank_status": "NEW", "bank_layers": [], "archived": false, "commits_since_20260313_count_capped100": 0, "language": "TypeScript"}
Description [vendor]: Recover USDC and prediction market positions from Polymarket smart contract wallets (Proxy & Safe). Sell positions, redeem winnings, and withdraw funds directly.
README excerpt [vendor, not an endorsement]: # Polymarket Wallet Recovery Tools Recover funds stuck in Polymarket smart contract wallets. If you've lost access to your Polymarket account or have funds trapped in proxy/safe wallets, these tools can help you retrieve your USDC and positions. ## What This Solves Polymarket uses smart contract wallets internally. When you create an account: - **Email/Magic accounts** use Proxy Wallets - **Browser wallets** (MetaMask, Coinbase Wallet, Rainbow, etc.) use Safe Wallets Your funds can get "stuck" in these wallets if: - You lose access to your Polymarket account - The website is unavailable - You want to withdraw directly without using the UI - You have unresolved winning positions that need redemption ## Features - **Wallet Discovery**: Automatically finds all wallets (EOA, Proxy, Safe) associated with your private key - **Position Scanning**: Detects all prediction market positions with balances - **Market Selling**: Sells active positions at market price - **Position Redemption**: Redeems winning positions from resolved markets - **USDC Withdrawal**: Withdraws all USDC from smart contract wallets to your EOA ## Prerequisites - [Bun](https://bun.com/) - A Polygon RPC URL (Alchemy, Infura, or other provider) - Your wallet's private key ## Quick Start 1. Clone the repository: ```bash git clone https://github.com/0-don/polymarket-wallet-recovery.git cd polymarket-wallet-recovery ```
Actual LICENSE excerpt: 
Recent author count: 0; sampled contributors: 1
Adoption bank: null
Issue sample: {"url": "https://github.com/0-don/polymarket-wallet-recovery/issues/2", "created_at": "2026-05-08T16:49:27Z", "state": "closed", "comments": 0, "first_staff_comment_in_sample": null, "sample_limit": 20}
Manifests: package.json

## 0xNetuser/Polymarket-golang
Source: https://github.com/0xNetuser/Polymarket-golang
{"stars": 76, "observed_at": "2026-09-13T15:41:12.553856+00:00", "latest_commit": "c632343dce50e5068aa68b4ea3cfc12a4c8a1473", "last_commit_date": "2026-05-20T09:58:48Z", "license": null, "license_path": null, "bank_status": "NEW", "bank_layers": [], "archived": false, "commits_since_20260313_count_capped100": 11, "language": "Go"}
Description [vendor]: Polymarket Clob Golang Client
README excerpt [vendor, not an endorsement]: # Polymarket Go SDK [English](README.md) | [中文](README_zh.md) A comprehensive Go SDK for the Polymarket CLOB. Aligned with both [py-clob-client](https://github.com/Polymarket/py-clob-client) (V1, archived 2026-05) and [py-clob-client-v2](https://github.com/Polymarket/py-clob-client-v2) (V2, current). Follow at X: @netu5er ## Features - ✅ **V2-native** — aligned with `py-clob-client-v2` (V1 was archived 2026-05) - ✅ **CTF Exchange V2** order signing (EIP-712 EOA + EIP-1271 Solady wrapped for Deposit Wallet) - ✅ **Automatic version negotiation** — `/version` cache + retry on `order_version_mismatch` - ✅ **Builder code / Builder API key** for fee attribution - ✅ **Three Authentication Levels**: L0, L1, L2 (with HMAC body signing aligned to V2) - ✅ **Order Management**: limit + market, post-only, GTC/GTD/FOK/FAK, batch - ✅ **RFQ**: request-for-quote flow - ✅ **WebSocket** — `/ws/market` + `/ws/user` with typed dispatcher, read deadline, reconnect-aware sentinels - ✅ **Bridge** — cross-chain deposit/withdraw via `bridge.polymarket.com` - ✅ **Rewards / Rebates** — full earnings + market reward configs - ✅ **Gasless on-chain ops** — split / merge / redeem / convert / wrap USDC.e→pUSD - ✅ **Strong typing** + byte-for-byte tested against py-clob-client-v2 golden signatures ## What's new in v0.3.0 Full V2 migration plus four new module groups. Quick taste of each — see [CHANGELOG.md](CHA
Actual LICENSE excerpt: 
Recent author count: 1; sampled contributors: 1
Adoption bank: null
Issue sample: {"url": "https://github.com/0xNetuser/Polymarket-golang/issues/7", "created_at": "2026-05-20T15:06:15Z", "state": "open", "comments": 2, "first_staff_comment_in_sample": "2026-05-23T08:53:23Z", "sample_limit": 20}
Manifests: 

## 106968687/DTC-SC
Source: https://github.com/106968687/DTC-SC
{"stars": 4, "observed_at": "2026-09-13T15:41:12.553856+00:00", "latest_commit": "89c8f9d70b36f5bb0a4cf8e43132bea16fd3af09", "last_commit_date": "2020-06-18T03:51:58Z", "license": null, "license_path": null, "bank_status": "NEW", "bank_layers": [], "archived": false, "commits_since_20260313_count_capped100": 0, "language": null}
Description [vendor]: The smart contracts for data trading certification
README excerpt [vendor, not an endorsement]: # DTC-SC The smart contracts for data trading certification
Actual LICENSE excerpt: 
Recent author count: 0; sampled contributors: 1
Adoption bank: null
Issue sample: null
Manifests: 

## 1nchaos/adata
Source: https://github.com/1nchaos/adata
{"stars": 5187, "observed_at": "2026-09-13T15:41:12.553856+00:00", "latest_commit": "b14f4e57b2175302f18b6eaf934f7dff9207a141", "last_commit_date": "2025-12-26T11:09:57Z", "license": "Apache-2.0", "license_path": "LICENSE", "bank_status": "ALREADY IN THE BANK", "bank_layers": ["bank_best", "liftable"], "archived": false, "commits_since_20260313_count_capped100": 0, "language": "Python"}
Description [vendor]: 免费开源A股量化交易数据库； 专注A股，专注量化，向阳而生； 开放、纯净、持续、为Ai(爱)发电。为个人量化交易而生，保卫3000点，珍惜底部机会......【股票数据，股票行情数据，股票量化数据，股票交易数据，k线行情数据，股票概念数据，股票数据接口，行情数据接口，量化交易数据】【多数据源融合，动态设置代理，保障数据高可用性】
README excerpt [vendor, not an endorsement]: # [AData](https://adata.30006124.xyz) ![GitHub language count](https://img.shields.io/github/languages/count/1nchaos/adata)![GitHub top language](https://img.shields.io/github/languages/top/1nchaos/adata)[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/adata?color=d)](https://pypi.org/project/adata/)[![Licence](https://img.shields.io/hexpm/l/apa?color=d)](https://gitee.com/inchaos/adata/blob/main/LICENSE)[![Downloads](https://static.pepy.tech/badge/adata/week)](https://pepy.tech/project/adata)![GitHub Repo stars](https://img.shields.io/github/stars/1nchaos/adata)![GitHub issues](https://img.shields.io/github/issues/1nchaos/adata)![GitHub contributors](https://img.shields.io/github/contributors/1nchaos/adata)![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/1nchaos/adata)[![Downloads](https://static.pepy.tech/badge/adata)](https://pepy.tech/project/adata)![PyPI - Version](https://img.shields.io/pypi/v/adata) ## 0、[介绍](https://adata.30006124.xyz/idea.html) > 专注A股，专注量化，向阳而生；开放、纯净、持续、为Ai(爱)发电。 > > 专注股票行情数据，为了保证数据的高可用性，采用多数据源融合切换。 > > 目标：支持个人量化行情的需要；众人拾柴火焰高，欢迎加入。 **市场寒冷，发热不易，坚持更难；如有帮助到你，右上角点 ⭐Star 一键三连，谢谢支持和收藏^_^** ## 一、[快速开始](https://adata.30006124.xyz/quickStart.html) ### （1）安装sdk ~~~python # 首次安装 pip install adata # 指定镜像源 pip install adata -i http://mirrors.aliyun.com/pypi/simple/ # 升级版本 pip install -U adata # 指定镜像源 pip install -U adata -
Actual LICENSE excerpt: Apache License Version 2.0, January 2004 http://www.apache.org/licenses/ TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION 1. Definitions. "License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document. "Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License. "Legal Entity" shall mean the union of the acting entity and all other entities that control, a
Recent author count: 0; sampled contributors: 10
Adoption bank: null
Issue sample: {"url": "https://github.com/1nchaos/adata/issues/188", "created_at": "2026-08-27T09:05:12Z", "state": "open", "comments": 0, "first_staff_comment_in_sample": null, "sample_limit": 20}
Manifests: pyproject.toml, requirements.txt

## aarora4/Awesome-Prediction-Market-Tools
Source: https://github.com/aarora4/Awesome-Prediction-Market-Tools
{"stars": 740, "observed_at": "2026-09-13T15:41:12.553856+00:00", "latest_commit": "865e5e9fc4698c05a7b546159b097203cbe54af3", "last_commit_date": "2026-09-03T22:24:58Z", "license": null, "license_path": null, "bank_status": "NEW", "bank_layers": [], "archived": false, "commits_since_20260313_count_capped100": 39, "language": null}
Description [vendor]: A curated list of Prediction Market Tools - AI Agents, Analytics, APIs, Dashboards, Copy Trading, Alerting, Tracking and More!!
README excerpt [vendor, not an endorsement]: # Awesome Prediction Market Tools [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re) > The most complete, community-maintained directory of prediction market tools — analytics platforms, trading bots, dashboards, APIs, data feeds, alert systems, educational resources, and more. > Covering Polymarket, Kalshi, Manifold, Hyperliquid, and the wider forecasting ecosystem. Pull requests welcome — add your tool or improve the list! --- ## ⭐ Featured: Oddpool **[Oddpool](https://www.oddpool.com)** — _The Bloomberg for prediction markets._ Oddpool aggregates cross-venue prediction market data across platforms like Polymarket and Kalshi, including live odds, spreads, liquidity, orderbook depth, arbitrage opportunities, and historical market data. It provides real-time feeds, analytics dashboards, and institutional-grade datasets for traders, quants, and researchers building strategies or analyzing prediction-market microstructure. 👉 **Check out the live dashboards:** **https://www.oddpool.com** --- ## Contents - [🧠 AI Agents](#ai-agents) - [🧩 APIs](#apis) - [🔹 Aggregator](#aggregator) - [🔔 Alerts](#alerts) - [📊 Analytics Tools](#analytics-tools) - [🔹 Arbitrage tools](#arbitrage-tools) - [📈 Dashboards](#dashboards) - [📡 Data](#data) - [💸 DeFi](#defi) - [📚 Educational Resources](#educational-resources) - [🔹 Extensions](#extensions) - [🔹 Funds](#funds) - [🏗️ Infrastructure]
Actual LICENSE excerpt: 
Recent author count: 15; sampled contributors: 20
Adoption bank: null
Issue sample: null
Manifests: 

## aasmith/ofx-parser
Source: https://github.com/aasmith/ofx-parser
{"stars": 59, "observed_at": "2026-09-13T15:41:12.553856+00:00", "latest_commit": "fa26c9360ed81b80617a2ed5edd3966dff84ba4b", "last_commit_date": "2015-04-06T20:55:27Z", "license": null, "license_path": null, "bank_status": "NEW", "bank_layers": [], "archived": false, "commits_since_20260313_count_capped100": 0, "language": "Ruby"}
Description [vendor]: Parses OFX
README excerpt [vendor, not an endorsement]: == ofx-parser by Andrew A. Smith http://ofx-parser.rubyforge.org/ http://rubyforge.org/projects/ofx-parser/ == DESCRIPTION: ofx-parser is a ruby library to parse a realistic subset of the lengthy OFX 1.x specification. == FEATURES/PROBLEMS: * Reads OFX responses - i.e. those downloaded from financial institutions and puts it into a usable object graph. * Supports the 3 main message sets: banking, credit card and investment accounts, as well as the required 'sign on' set. * Knows about SIC codes - if your institution provides them. See http://www.eeoc.gov/stats/jobpat/siccodes.html * Monetary amounts can be retrieved either as a raw string, or in pennies. * Supports OFX timestamps. == SYNOPSIS: Supports bank accounts: require 'rubygems' require 'ofx-parser' ofx = OfxParser::OfxParser.parse(open("bank-statement.ofx")) bank_acct = ofx.bank_accounts.first bank_acct.number # => '103333333333' bank_acct.routing_number # => '033000033' bank_acct.balance # => '123.45' bank_acct.balance_in_pennies # => 12345 bank_acct.statement.start_date # => DateTime bank_acct.statement.end_date # => DateTime bank_acct.statement.transactions.size # => 4 bank_acct.statement.transactions.first.payee # => "FOO, INC." bank_acct.statement.transactions.first.type # => :DEBIT bank_acct.statement.transactions.first.amount # => '-11.11' bank_acct.statement.transactions.first.amount_in_pennies # => -1111 Also s
Actual LICENSE excerpt: 
Recent author count: 0; sampled contributors: 7
Adoption bank: null
Issue sample: {"url": "https://github.com/aasmith/ofx-parser/issues/21", "created_at": "2025-07-08T08:26:41Z", "state": "open", "comments": 0, "first_staff_comment_in_sample": null, "sample_limit": 20}
Manifests: 

## ab2163/market-data-streamer
Source: https://github.com/ab2163/market-data-streamer
{"stars": 1, "observed_at": "2026-09-13T15:41:12.553856+00:00", "latest_commit": "f57cc729f6568cdd9253b9936ca81f83f1a230e6", "last_commit_date": "2025-11-28T15:44:31Z", "license": "MIT", "license_path": "LICENSE", "bank_status": "NEW", "bank_layers": [], "archived": false, "commits_since_20260313_count_capped100": 0, "language": "C++"}
Description [vendor]: High-performance market data streamer and order book reconstruction engine. Streams Databento DBN data and rebuilds a market-by-order (MBO) book with low latency.
README excerpt [vendor, not an endorsement]: # Market Data Streamer and Order Book Engine High-throughput C++ system that replays historical market data over TCP to multiple clients, which reconstruct limit order books and track best bid/offer (BBO) in real time. ## At a Glance * *High throughput*: ~1M messages/second (single client) and ~2.5M messages/second aggregate (five clients). * *Order book engine*: builds order books from MBO (message-by-order) data using exchange-style semantics (e.g. modify changes order priority). * *Modern C++ implementation*: uses `std::unordered_map` and tracked best bid/ask for speed, batched TCP sends, and a simple thread pool for scaling. * *Tests and benchmarks included*: Catch2 unit and integration tests and a benchmark script that runs with a user-selected number of clients. ![Class diagram](/docs/system-diag.png) ## Benchmarks and Tests **Benchmark script** (`run_bench.sh`) runs system with user-selected number of clients and reports: * Messages sent * Messages received * Error rates * Throughput (messages/second) **Catch2 tests:** * Unit tests for order book engine * Unit tests for TCP mechanics * Integration tests covering entire pipeline ## Performance **Single Client** ~1M messages/second **Five Clients** ~500k messages/second per client Benchmarks were run on i7 dual-core laptop with Ubuntu 22.04. ## Getting Started *Prerequisites* * Linux environment (tested on Ubuntu 22.04) * 
Actual LICENSE excerpt: MIT License Copyright (c) 2025 Ajinkya Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice a
Recent author count: 0; sampled contributors: 1
Adoption bank: null
Issue sample: null
Manifests: 

## abdelkaderamar/fix2xml
Source: https://github.com/abdelkaderamar/fix2xml
{"stars": 3, "observed_at": "2026-09-13T15:41:12.553856+00:00", "latest_commit": "fa781b747a8e40ed4c2d3dee8294fb51654f7428", "last_commit_date": "2018-09-06T13:02:11Z", "license": "MIT", "license_path": "LICENSE", "bank_status": "NEW", "bank_layers": [], "archived": false, "commits_since_20260313_count_capped100": 0, "language": "C++"}
Description [vendor]: A C++ library to convert messages between Quickfix and FIXML
README excerpt [vendor, not an endorsement]: # FIX2XML Key Features How To Use Compilation Credit License ## Key Features - Convert C++ quickfix messages to FIXML - Convert a FIXML messages to a C++ quickfix messages ## How To Use The code below shows how to convert a C++ quickfix message to its FIXML representation. ```cpp fixml2fix_converter converter (fix_filename, xsd_schema); NewOrderSingle fix_message; // set FIX messages fields // ... // ... converter.fix2fixml(fix_message, str); ``` The conversion from a FIXML message to its equivalent C++ quickfix message can be done using the same converter type `fixml2fix_converter` ```cpp string str = " " " " " " " " " " " " ; FIX::Message fix_msg; converter.fixml2fix(str, fix_msg); ``` ## Compilation ## Credit - [gcc](https://gcc.gnu.org/) - [boost](https://www.boost.org/) - [Apache Xerces-C++](http://xerces.apache.org/xerces-c/) - [Cmake](https://cmake.org/) - [Google Test](https://github.com/google/googletest) ## License MIT
Actual LICENSE excerpt: MIT License Copyright (c) 2018 abdelkaderamar Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright n
Recent author count: 0; sampled contributors: 1
Adoption bank: null
Issue sample: null
Manifests: 

