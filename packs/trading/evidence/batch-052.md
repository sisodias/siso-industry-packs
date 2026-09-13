## databento/epoch
https://github.com/databento/epoch
{"id": 1054483755, "stars": 5, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "0686095e126874fca1799db594b976faaf982ddd", "last_commit_date": "2026-01-27T17:06:12Z", "license": "MIT", "actual_license_paths": ["LICENSE"], "license_files_read": true, "archived": false, "recent_commit_count": 0, "recent_authors_sample50": [], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] Utility for converting UNIX timestamps to human-readable date strings
README: # epoch [![build](https://github.com/databento/epoch/actions/workflows/build.yaml/badge.svg)](https://github.com/databento/epoch/actions/workflows/build.yaml) [![license](https://img.shields.io/github/license/databento/epoch?color=blue)](./LICENSE) [![Current Crates.io Version](https://img.shields.io/crates/v/epoch-to.svg)](https://crates.io/crates/epoch-to) Utility for making UNIX timestamps human-readable
Headings: # epoch
Runtime: [![license](https://img.shields.io/github/license/databento/epoch?color=blue)](./LICENSE)
LICENSE: MIT License Copyright (c) 2022 Zach Banks Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
Adoption: null
Issue sample: []

## databento/.github
https://github.com/databento/.github
{"id": 727210448, "stars": 0, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "73db9fc9d5c038a6684bfcd2e4e6dd8f576ce667", "last_commit_date": "2024-09-12T23:54:08Z", "license": null, "actual_license_paths": [], "license_files_read": false, "archived": false, "recent_commit_count": 0, "recent_authors_sample50": [], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] None
README: 
Headings: 
Runtime: 
LICENSE: 
Adoption: null
Issue sample: []

## beancount/smart_importer
https://github.com/beancount/smart_importer
{"id": 112750160, "stars": 308, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "db71e8cd5538d079324472d276708979adc95506", "last_commit_date": "2026-07-26T12:59:06Z", "license": "MIT", "actual_license_paths": ["LICENSE"], "license_files_read": true, "archived": false, "recent_commit_count": 4, "recent_authors_sample50": ["yagebu"], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] Augment Beancount importers with machine learning functionality.
README: smart_importer ============== https://github.com/beancount/smart_importer .. image:: https://github.com/beancount/smart_importer/actions/workflows/ci.yml/badge.svg?branch=main :target: https://github.com/beancount/smart_importer/actions?query=branch%3Amain Augments `Beancount `__ importers with machine learning functionality. Status ------ Working protoype, development status: beta Installation ------------ The ``smart_importer`` can be installed from PyPI: .. code:: bash pip install smart_importer Quick Start ----------- This package provides import hooks that can modify the imported entries. When running the importer, the existing entries will be used as training data for a machine learning model, which will then predict entry attributes. The following example shows how to apply the ``PredictPostings`` hook to an existing CSV importer: .. code:: python from beangulp.importers import csv from beangulp.importers.csv import Col from smart_importer import PredictPostings class MyBankImporter(csv.Importer): '''Conventional importer for MyBank''' def __init__(self, *, account): super().__init__( {Col.DATE: 'Date', Col.PAYEE: 'Transaction Details', Col.AMOUNT_DEBIT: 'Funds Out', Col.AMOUNT_CREDIT: 'Funds In'}, account, 'EUR', ( 'Date, Transaction Details, Funds Out, Funds In' ) ) CONFIG = [ MyBankImporter(account='Assets:MyBank:MyAccount'), ] HOOKS = [ PredictPostings().hook ] Documentation ------------- This section explains in detail the relevant concepts and artifacts needed for enhancing Beancount importers with machine learning. Beancount Importers ~~~~~~~~~~~~~~~~~~~~ Let's assume you have created an importer
Headings: 
Runtime: .. code:: python | .. code:: python | .. code:: python | .. code:: python | Simply run (requires tox): | Python's `logging` module is used by the smart_importer module. | .. code:: python | First make sure that `jieba` is installed in your python environment: | .. code:: python | All data processing happens on the local machine; no data is sent to or retrieved from external servers or the cloud. | The trained model is used locally on your machine during the import process, as follows.
LICENSE: MIT License Copyright (c) 2018 Johannes Harms Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
Adoption: null
Issue sample: [{"url": "https://github.com/beancount/smart_importer/issues/158", "createdAt": "2026-07-02T06:21:27Z", "state": "CLOSED", "comments": {"nodes": [{"createdAt": "2026-07-26T12:59:23Z", "authorAssociation": "MEMBER"}]}}, {"url": "https://github.com/beancount/smart_importer/issues/156", "createdAt": "2026-05-05T00:36:46Z", "state": "CLOSED", "comments": {"nodes": []}}]

## beancount/beancount-mode
https://github.com/beancount/beancount-mode
{"id": 303555018, "stars": 159, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "37648f983ff42426b1f364831ce7d2d0d735686b", "last_commit_date": "2026-05-17T18:03:30Z", "license": "GPL-3.0", "actual_license_paths": ["COPYING"], "license_files_read": true, "archived": false, "recent_commit_count": 9, "recent_authors_sample50": ["HeinrichTaver", "blais"], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] Emacs major-mode to work with Beancount ledger files
README: 
Headings: 
Runtime: 
LICENSE: GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/> Everyone is permitted to copy and distribute verbatim
Adoption: null
Issue sample: [{"url": "https://github.com/beancount/beancount-mode/issues/73", "createdAt": "2026-09-10T15:59:42Z", "state": "OPEN", "comments": {"nodes": []}}, {"url": "https://github.com/beancount/beancount-mode/issues/72", "createdAt": "2026-09-10T15:48:54Z", "state": "OPEN", "comments": {"nodes": []}}]

## beancount/ledger2beancount
https://github.com/beancount/ledger2beancount
{"id": 125626223, "stars": 95, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "e56300d3db06d5b94df2e0cacbab3072585a4e1a", "last_commit_date": "2026-06-14T07:15:15Z", "license": "GPL-3.0", "actual_license_paths": ["LICENSE"], "license_files_read": true, "archived": false, "recent_commit_count": 1, "recent_authors_sample50": ["zacchiro"], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] Ledger to Beancount text-based converter
README: [![Build Status](https://travis-ci.org/beancount/ledger2beancount.svg?branch=master)](https://travis-ci.org/beancount/ledger2beancount) # ledger2beancount A script to automatically convert [Ledger](https://www.ledger-cli.org/)-based textual ledgers to [Beancount](http://furius.ca/beancount/) ones. Conversion is based on (concrete) syntax, so that information that is not meaningful for accounting reasons but still valuable (e.g., comments, formatting, etc.) can be preserved. ledger2beancount supports the file formats from: * [ledger](https://ledger-cli.org/) * [hledger](https://hledger.org/) ## Usage ledger2beancount accepts input from `stdin` or from a file and will write the converted data to `stdout`. You can run ledger2beancount like this: ledger2beancount test.ledger > test.beancount ## Installation Please see [the installation information](docs/installation.md) for dependencies and installation instructions. ## Documentation ledger2beancount comes with extensive documentation. You can also [read the documentation online](https://ledger2beancount.readthedocs.io/) thanks to Read the Docs. ## Features The majority of features from ledger are supported by ledger2beancount. Here is an overview of fully supported, partly supported and unsupported features. Please refer to [the user guide](docs/guide.md) for more details on how to use ledger2beancount and to configure it to your needs. ### Fully supported * Accounts * Account declarations (`account ...`) * Conversion of invalid account names * Mapping of account names * Directive `apply
Headings: # ledger2beancount; ## Usage; ## Installation; ## Documentation; ## Features; ### Fully supported; ### Partly supported; ### Not supported; ### Supported features from hledger; ## Authors; ## License
Runtime: * `python`: skipped (not supported in beancount) | ## License | This program is free software: you can redistribute it and/or modify | it under the terms of the GNU General Public License as published by | the Free Software Foundation, either version 3 of the License, or | This program is distributed in the hope that it will be useful, | GNU General Public License for more details. | You should have received a copy of the GNU General Public License | along with this program.  If not, see <http://www.gnu.org/licenses/>. | SPDX-License-Identifier: GPL-3.0-or-later
LICENSE: GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/> Everyone is permitted to copy and distribute verbatim
Adoption: null
Issue sample: [{"url": "https://github.com/beancount/ledger2beancount/issues/277", "createdAt": "2025-05-06T10:28:15Z", "state": "OPEN", "comments": {"nodes": [{"createdAt": "2025-05-06T10:38:29Z", "authorAssociation": "NONE"}, {"createdAt": "2025-05-06T10:40:57Z", "authorAssociation": "NONE"}, {"createdAt": "2025-05-06T10:53:54Z", "authorAssociation": "COLLABORATOR"}, {"createdAt": "2025-05-06T11:23:31Z", "authorAssociation": "NONE"}, {"createdAt": "2026-06-14T07:26:35Z", "authorAssociation": "COLLABORATOR"}]}}, {"url": "https://github.com/beancount/ledger2beancount/issues/287", "createdAt": "2026-03-10T03:10:14Z", "state": "OPEN", "comments": {"nodes": []}}]

## beancount/beangrow
https://github.com/beancount/beangrow
{"id": 333634558, "stars": 89, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "1477a7efc49001dc5c2fa9f19fb3a426a164c0d1", "last_commit_date": "2025-10-15T03:43:30Z", "license": "GPL-2.0", "actual_license_paths": ["COPYING"], "license_files_read": true, "archived": false, "recent_commit_count": 0, "recent_authors_sample50": [], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] Returns calculations on portfolios in Beancount
README: # Compute Returns This directory contains code which computes investment returns on a variety of assets, as recorded by Beancount, fed directly from a Beancount file. See this document for details: https://docs.google.com/document/d/1nPsMIunLnDvdsg6TSsd0PZb7jngojNpFlqnaX36WRp8/ ## Scripts There are three related scripts: - configure.py: This attempts to automatically infer and generate configuration to compute returns from an existing Beancount ledger. - compute_returns.py: This extracts data for each of the investments defined in the configuration and computes the returns and generates output for each requested returns report. - download_prices.py: The compute_returns.py script outputs a list of missing (or inadequately dated) price directives to properly do its job as a side-product. This script can read that file and fetch those missing dates, which you can insert in your ledger and then rerun compute_returns.py for a more precise calculation. ## Example To run the example: ``` cd example uv run beangrow-returns ledger.beancount config.pbtxt ./reports ``` The reports are available at `example/reports/groups`.
Headings: # Compute Returns; ## Scripts; ## Example
Runtime: 
LICENSE: GNU GENERAL PUBLIC LICENSE Version 2, June 1991 Copyright (C) 1989, 1991 Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
Adoption: null
Issue sample: [{"url": "https://github.com/beancount/beangrow/issues/51", "createdAt": "2026-08-24T13:05:05Z", "state": "OPEN", "comments": {"nodes": []}}, {"url": "https://github.com/beancount/beangrow/issues/50", "createdAt": "2025-12-16T21:55:41Z", "state": "OPEN", "comments": {"nodes": []}}]

## ib-api-reloaded/memorial
https://github.com/ib-api-reloaded/memorial
{"id": 773595216, "stars": 6, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "d3c7eacab341c0a8a23e0e037e02c950bd963284", "last_commit_date": "2024-03-25T22:34:36Z", "license": null, "actual_license_paths": [], "license_files_read": false, "archived": false, "recent_commit_count": 0, "recent_authors_sample50": [], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] A place for people to write rememberances of original ib_insync creator Ewald de Wit including personal notes or just historical messages from forums/issues/email. Feel free to create new issues or PRs on this repository with your messages or links to others and we will get all updates added.
README: # Memories of Ewald de Wit [From his family](https://github.com/erdewit/ib_insync): > Unfortunately, our dear brother Ewald de Wit passed away monday, March eleven as a result
Headings: # Memories of Ewald de Wit; ## 2024; ## 2021; ## More
Runtime: Notes from [archived thread](https://old.reddit.com/r/algotrading/comments/1b89p89/does_anyone_know_why_the_ib_insync_python_library/?sort=new):
LICENSE: 
Adoption: null
Issue sample: [{"url": "https://github.com/ib-api-reloaded/memorial/issues/1", "createdAt": "2024-04-12T02:02:29Z", "state": "OPEN", "comments": {"nodes": []}}]

## ib-api-reloaded/eventkit
https://github.com/ib-api-reloaded/eventkit
{"id": 842727217, "stars": 5, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "141c9b6abf4418b47a03c10d44c6bbd9d9d55f5d", "last_commit_date": "2025-06-22T00:41:13Z", "license": "BSD-2-Clause", "actual_license_paths": ["LICENSE"], "license_files_read": true, "archived": false, "recent_commit_count": 0, "recent_authors_sample50": [], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] maintaining: event-driven data pipelines
README: |Build| |PyVersion| |Status| |PyPiVersion| |License| |Docs| Introduction ------------ The primary use cases of eventkit are * to send events between loosely coupled components; * to compose all kinds of event-driven data pipelines. The interface is kept as Pythonic as possible, with familiar names from Python and its libraries where possible. For scheduling asyncio is used and there is seamless integration with it. See the examples and the `introduction notebook `_ to get a true feel for the possibilities. Installation ------------ :: pip3 install eventkit Python_ version 3.6 or higher is required. Examples -------- **Create an event and connect two listeners** .. code-block:: python import eventkit as ev def f(a, b): print(a * b) def g(a, b): print(a / b) event = ev.Event() event += f event += g event.emit(10, 5) **Create a simple pipeline** .. code-block:: python import eventkit as ev event = ( ev.Sequence('abcde') .map(str.upper) .enumerate() ) print(event.run()) # in Jupyter: await event.list() Output:: [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')] **Create a pipeline to get a running average and standard deviation** .. code-block:: python import
Headings: 
Runtime: |Build| |PyVersion| |Status| |PyPiVersion| |License| |Docs| | The interface is kept as Pythonic as possible, | with familiar names from Python and its libraries where possible. | Python_ version 3.6 or higher is required. | .. code-block:: python | .. code-block:: python | .. code-block:: python | .. code-block:: python | .. code-block:: python | async for frame, persons in lastScene: | .. code-block:: python | * `itertools <https://docs.python.org/3/library/itertools.html>`_ | .. _Python: http://www.python.org | .. _`Interactive Brokers Python API`: http://interactivebrokers.github.io | :target: https://pypi.python.org/pypi/eventkit | .. |PyVersion| image:: https://img.shields.io/badge/python-3.6+-blue.svg | .. |License| image:: https://img.shields.io/badge/license-BSD-blue.svg
LICENSE: BSD 2-Clause License Copyright (c) 2023, Ewald de Wit All rights reserved. Redistribution and use in source and binary forms, with or without modification, are
Adoption: null
Issue sample: [{"url": "https://github.com/ib-api-reloaded/eventkit/issues/12", "createdAt": "2025-10-25T17:02:30Z", "state": "OPEN", "comments": {"nodes": [{"createdAt": "2025-10-26T12:29:32Z", "authorAssociation": "COLLABORATOR"}, {"createdAt": "2025-11-05T18:19:23Z", "authorAssociation": "CONTRIBUTOR"}]}}, {"url": "https://github.com/ib-api-reloaded/eventkit/issues/10", "createdAt": "2025-09-27T15:43:04Z", "state": "OPEN", "comments": {"nodes": []}}]
