## spmason/qif2json
https://github.com/spmason/qif2json
{"id": 5143017, "stars": 26, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "d81b0bfda0ca917023452c5a1da88e1cbd1238f1", "last_commit_date": "2026-08-12T12:03:11Z", "license": "MIT", "actual_license_paths": ["LICENSE-MIT"], "license_files_read": true, "archived": false, "recent_commit_count": 4, "recent_authors_sample50": ["dependabot[bot]", "github-actions[bot]"], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] Parse .qif files into a sensible JSON format
README: # qif2json Parse .qif files into a sensible JSON format [![Build Status](https://travis-ci.org/spmason/qif2json.svg)](https://travis-ci.org/spmason/qif2json) ## Getting Started Install the module with: `npm install qif2json` ```javascript var qif2json = require('qif2json'); qif2json.parse(qifData, options); // Or to read in a file directly qif2json.parseFile(filePath, options, function(err, qifData){ // done! }); ``` If installed globally, the `qif2json` command can also be used with an input file and the output JSON will be pretty-printed to the console ## Options * `dateFormat` - The format of dates within the file. The `fecha` module is used for parsing them into Date objects. See https://www.npmjs.com/package/fecha#formatting-tokens for available formatting tokens. The special format `"us"` will use us-format MM/DD/YYYY dates. Dates are normalised before parsing so `/`, `'` become `-` and spaces are removed. On the commandline you can specify multiple date formats comma-delimited. ## Contributing Take care to maintain the existing coding style. Add unit tests for any new or changed functionality. Lint and test your code using `npm test`. ## Release History * 0.0.1 Initial release, small subset of qif fields understood, please make a pull request if you need more
Headings: # qif2json; ## Getting Started; ## Options; ## Contributing; ## Release History; ## License
Runtime: ## License | Licensed under the MIT license.
LICENSE: Copyright (c) 2012 Steve Mason Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
Adoption: null
Issue sample: [{"url": "https://github.com/spmason/qif2json/issues/10", "createdAt": "2019-01-26T00:31:44Z", "state": "OPEN", "comments": {"nodes": [{"createdAt": "2020-05-01T16:15:10Z", "authorAssociation": "CONTRIBUTOR"}, {"createdAt": "2020-10-12T21:09:27Z", "authorAssociation": "CONTRIBUTOR"}, {"createdAt": "2024-05-29T01:02:28Z", "authorAssociation": "NONE"}, {"createdAt": "2024-05-29T06:07:11Z", "authorAssociation": "OWNER"}]}}, {"url": "https://github.com/spmason/qif2json/issues/57", "createdAt": "2020-03-04T06:45:20Z", "state": "OPEN", "comments": {"nodes": [{"createdAt": "2020-05-04T01:41:22Z", "authorAssociation": "CONTRIBUTOR"}, {"createdAt": "2020-10-19T19:29:39Z", "authorAssociation": "CONTRIBUTOR"}]}}]

## saltedge/salt-parser
https://github.com/saltedge/salt-parser
{"id": 43501284, "stars": 18, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "869cf36cd7f913652dd302d83144848db0758b8f", "last_commit_date": "2015-11-06T15:01:40Z", "license": null, "actual_license_paths": [], "license_files_read": false, "archived": false, "recent_commit_count": 0, "recent_authors_sample50": [], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] Library for parsing OFX, QIF and SWIFT formats.
README: ### Salt Parser [![Build Status](https://travis-ci.org/saltedge/salt-parser.svg?branch=master)](https://travis-ci.org/saltedge/salt-parser) Library for parsing OFX, QIF and SWIFT formats. ### Install ```ruby gem install salt-parser ``` ### Examples: ```ruby require 'salt-parser'
Headings: ### Salt Parser; ### Install; ### Examples:; ### Credits; ### License
Runtime: ### License | (The MIT License) | distribute, sublicense, and/or sell copies of the Software, and to
LICENSE: 
Adoption: null
Issue sample: [{"url": "https://github.com/saltedge/salt-parser/issues/3", "createdAt": "2015-11-06T12:18:05Z", "state": "CLOSED", "comments": {"nodes": [{"createdAt": "2015-11-06T13:35:14Z", "authorAssociation": "NONE"}, {"createdAt": "2015-11-06T17:08:12Z", "authorAssociation": "CONTRIBUTOR"}]}}]

## codito/bout
https://github.com/codito/bout
{"id": 115207040, "stars": 17, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "63cda67e19706bd627db3410d4b02a9f67d2505c", "last_commit_date": "2023-12-30T11:35:48Z", "license": "MIT", "actual_license_paths": ["LICENSE.md"], "license_files_read": true, "archived": false, "recent_commit_count": 0, "recent_authors_sample50": [], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] Parse and export pdf bank statements to QIF format.
README: # Bout Parse bank statements (csv) and export them to qif format. [![PyPI](https://img.shields.io/pypi/v/bout.svg)](https://pypi.python.org/pypi/bout) Supports _ICICI_ bank and credit card statements out of box. Contributions are most welcome for adding support for another bank. Create an [issue](https://github.com/codito/bout/issues/new) to start. Download the bank statements in `csv` format from the ICICI website and provide them as an input to the tool. # Installation pip install bout Arch Linux may use the `bout` package from [AUR](https://aur.archlinux.org/packages/bout/). yaourt -S bout # Usage $ # convert an ICICI statement to qif $ bout ~/Downloads/icici_statement.csv --profile icici > /tmp/icici.qif $ cat /tmp/icici.qif !Account NMyAccount TMyBank ^ !Type:Bank D01/07/2017 MBIL/12419860068/VF M Jun 17/344548182 T-354.56 ^ $ # convert a password protected ICICI Credit Card statement $ bout ~/Downloads/cc_jun.csv --profile icicicc > /tmp/icicicc.qif $ cat /tmp/icicicc.qif !Account NMyAccount TMyBank ^ !Type:Bank D14/06/2017 MAPOLLO HOSPITALS HYDERABAD IN T-60.00 ^ $ # print verbose messages to diagnose conversion $ bout ~/Downloads/cc_jun.csv --debug --profile icicicc > /tmp/icicicc.qif # Contribute Please try `bout` and file any issues at github issues page. Your patches are welcome!
Headings: # Bout; # Installation; # Usage; # Contribute
Runtime: [![PyPI](https://img.shields.io/pypi/v/bout.svg)](https://pypi.python.org/pypi/bout)
LICENSE: Copyright (c) 2017 Arun Mahapatra Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
Adoption: null
Issue sample: []

## dandrake/betterment-pdf-to-qif
https://github.com/dandrake/betterment-pdf-to-qif
{"id": 39156764, "stars": 10, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "9a02ae464a65edfd028b0b49766521bb81cc01d9", "last_commit_date": "2025-07-06T18:13:28Z", "license": null, "actual_license_paths": [], "license_files_read": false, "archived": false, "recent_commit_count": 0, "recent_authors_sample50": [], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] Parse Betterment's PDF statements, output QIF files
README: # Parse Betterment's PDF statements, output QIF [Betterment](http://betterment.com) is a nice brokerage service but they don't provide transaction data in any parseable, structured format. The
Headings: # Parse Betterment's PDF statements, output QIF; ## Requirements; ## On rounding and number of shares
Runtime: Python script here will parse your quarterly statement PDF and produce | QIF files suitable for importing into an accounting program. (I use | You'll need Python 3 and the `pdftotext` utility. I use Ubuntu Linux and | Because their reported number of shares isn't accurate, this program
LICENSE: 
Adoption: null
Issue sample: []

## antoinejaussoin/rust-qif-parser
https://github.com/antoinejaussoin/rust-qif-parser
{"id": 278689748, "stars": 4, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "28b669f60ba25d5ae89029a5fdf8b349ed5db57c", "last_commit_date": "2023-11-29T22:01:56Z", "license": "MIT", "actual_license_paths": ["LICENSE"], "license_files_read": true, "archived": false, "recent_commit_count": 0, "recent_authors_sample50": [], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] QIF (Quicken Interchange Format) parser in Rust
README: # QIF Parser Very high performance QIF (Quicken Interchange Format) parser in Rust. ## What is QIF? QIF is a format invented by Quicken to record financial data. You can read more on [this Wikipedia article](https://en.wikipedia.org/wiki/Quicken_Interchange_Format). ## What does this library do? This library will take your QIF data as a string, parse it, and return some structured data for further processing. ## What about performance? This repository compares the same functionality written in Node.JS and in Rust. If you have both Node and Rust installed, you can run both by doing `make compare`. Spoiler alert: for 1 million transaction items, the Node implementation would take about **4 minutes** on a M1 Mac, and the Rust implementation a little over... **1 second**. We then have a **200x** speed difference between the two. Fancy that! Actual output from my M1 Mac: ``` Executing both NODE: Done processing 1000 items. Time it would take to process 1M items: 238793ms RUST: Done processing 100000 items. Time it would take to process 1M items: 1430ms ``` ## Various links https://en.wikipedia.org/wiki/Quicken_Interchange_Format https://rust-lang.github.io/api-guidelines/checklist.html https://stevedonovan.github.io/rust-gentle-intro/6-error-handling.html ## Change
Headings: # QIF Parser; ## What is QIF?; ## What does this library do?; ## What about performance?; ## Various links; ## Change Log; ### Version 0.4.0; ### Version 0.3.0; ### Version 0.2.0; ### Version 0.1.0; ### Version 0.0.6
Runtime: Very high performance QIF (Quicken Interchange Format) parser in Rust. | This repository compares the same functionality written in Node.JS and in Rust. | If you have both Node and Rust installed, you can run both by doing `make compare`. | Spoiler alert: for 1 million transaction items, the Node implementation would take about **4 minutes** on a M1 Mac, and the Rust implementation a little over... **1 second**. We then have a **200x** speed difference between the two. Fancy that! | RUST: Done processing 100000 items. Time it would take to process 1M items: 1430ms | https://rust-lang.github.io/api-guidelines/checklist.html | https://stevedonovan.github.io/rust-gentle-intro/6-error-handling.html | - Make the code more Rusty (using match instead of if-statements) | - Return &str instead of String on the returned object (except for the date). This should improve performance dramatically.
LICENSE: MIT License Copyright (c) 2020 Antoine Jaussoin Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
Adoption: null
Issue sample: [{"url": "https://github.com/antoinejaussoin/rust-qif-parser/issues/9", "createdAt": "2024-12-21T06:43:17Z", "state": "OPEN", "comments": {"nodes": []}}]

## danielvlopes/quicken
https://github.com/danielvlopes/quicken
{"id": 683730, "stars": 4, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "aee00d0dcd94a4fdf33142d20d6eaafa5c96a28d", "last_commit_date": "2010-06-02T03:14:09Z", "license": "MIT", "actual_license_paths": ["LICENSE"], "license_files_read": true, "archived": false, "recent_commit_count": 0, "recent_authors_sample50": [], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] Ruby parser for QIF files
README: 
Headings: 
Runtime: 
LICENSE: Copyright (c) 2009 Daniel Lopes Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
Adoption: null
Issue sample: []

## acw/qif
https://github.com/acw/qif
{"id": 80264349, "stars": 3, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "b00b140e50bfae27b16e6acba802ee71f0cc15a0", "last_commit_date": "2023-10-14T14:49:40Z", "license": "BSD-3-Clause", "actual_license_paths": ["LICENSE"], "license_files_read": true, "archived": false, "recent_commit_count": 0, "recent_authors_sample50": [], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] A Haskell library for parsing and rendering QIF files.
README: # Haskell QIF Library This library is designed to do simple parsing and rendering of QIF financial documents. The goal is to support transmission of financial information between programs, not to serve as the back end to any particular financial software. There does not appear to be a specification of QIF by any standards body, so this parser attempts to be as general as possible given the limited documentation I've seen. I have tested it against the output of at least one financial program; I don't know that it will work with others, though. If you find a QIF file for which this parser does not work, please report the problem and, if possible, provide the file.
Headings: # Haskell QIF Library
Runtime: programs, not to serve as the back end to any particular financial software. | financial program; I don't know that it will work with others, though.
LICENSE: Copyright (c) 2016, Adam Wick All rights reserved. Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
Adoption: null
Issue sample: [{"url": "https://github.com/acw/qif/issues/1", "createdAt": "2018-09-19T15:06:27Z", "state": "OPEN", "comments": {"nodes": [{"createdAt": "2018-09-24T16:35:05Z", "authorAssociation": "OWNER"}, {"createdAt": "2018-09-25T14:34:13Z", "authorAssociation": "NONE"}]}}]

## lukerosiak/pysec
https://github.com/lukerosiak/pysec
{"id": 9861504, "stars": 346, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "b9ea1ca3e52d9656f01b1b2fa61b27a7ed0493f6", "last_commit_date": "2014-01-22T21:15:22Z", "license": null, "actual_license_paths": [], "license_files_read": false, "archived": false, "recent_commit_count": 0, "recent_authors_sample50": [], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] Parse XBRL filings from the SEC's EDGAR in Python
README: This is Django code that compiles a list of all SEC filings from EDGAR into SQL, allows you to download them at will, and parses
Headings: 
Runtime: This is Django code that compiles a list of all SEC filings from EDGAR into SQL, allows you to download them at will, and parses 50+ key accounting terms from XBRL filings. It is also a Python XBRL parser that allows you to easily extract arbitrary XBRL terms  | python manage.py syncdb | python manage.py sec_import_index | Or if you just want to use the Python XBRL parser on a .xml file: | x = xbrl.XBRL(PATH TO LOCAL XML 10-K FILING)
LICENSE: 
Adoption: null
Issue sample: [{"url": "https://github.com/lukerosiak/pysec/issues/18", "createdAt": "2017-10-27T11:15:03Z", "state": "CLOSED", "comments": {"nodes": [{"createdAt": "2018-10-26T13:08:44Z", "authorAssociation": "NONE"}]}}, {"url": "https://github.com/lukerosiak/pysec/issues/11", "createdAt": "2014-01-27T00:53:29Z", "state": "OPEN", "comments": {"nodes": [{"createdAt": "2014-01-30T15:39:57Z", "authorAssociation": "NONE"}, {"createdAt": "2017-05-11T15:34:27Z", "authorAssociation": "NONE"}, {"createdAt": "2017-08-14T23:30:01Z", "authorAssociation": "NONE"}, {"createdAt": "2018-10-26T13:09:53Z", "authorAssociation": "NONE"}]}}]
