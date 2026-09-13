## Polymarket/real-time-data-client
https://github.com/Polymarket/real-time-data-client
{"id": 942875438, "stars": 229, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "c937d9c11cdd2b771aa4818392a1b6dda65c25de", "last_commit_date": "2026-03-03T18:38:55Z", "license": "MIT", "actual_license_paths": ["LICENSE"], "license_files_read": true, "archived": false, "recent_commit_count": 0, "recent_authors_sample50": [], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] A TypeScript client to receive real time data messages
README: # Real time data client This client provides a wrapper to connect to the `real-time-data-streaming` `WebSocket` service. ## How to use it Here is a quick example about how to connect to the service and start receiving messages (you can find more in the folder `examples/`): ```typescript import { RealTimeDataClient } from "../src/client"; import { Message } from "../src/model"; const onMessage = (message: Message): void => { console.log(message.topic, message.type, message.payload); }; const onConnect = (client: RealTimeDataClient): void => { // Subscribe to a topic client.subscribe({ subscriptions: [ { topic: "comments", type: "*", // "*"" can be used to connect to all the types of the topic filters: `{"parentEntityID":100,"parentEntityType":"Event"}`, // empty means no filter }, ], }); }; new RealTimeDataClient({ onMessage, onConnect }).connect(); ``` ## How to subscribe and unsubscribe from messages Once the connection is stablished and you have a `client: RealTimeDataClient` object, you can `subscribe` and `unsubscribe` to many messages streamings using the same connection. ### Subscribe Subscribe to 'trades' messages from the topic 'activity' and to the all comments messages. ```typescript client.subscribe({ subscriptions: [ { topic: "activity", type:
Headings: # Real time data client; ## How to use it; ## How to subscribe and unsubscribe from messages; ### Subscribe; ### Unsubscribe; ### Disconnect; ## Messages hierarchy; ## Auth; ### ClobAuth; ## Message types; ### Activity; #### Trade; ### Comments; #### Comment; #### Reaction; ### CryptoPrice; #### Filters; ### EquityPrice; #### Filters; #### Initial data dump on connection
Runtime: 
LICENSE: MIT License Copyright (c) 2022 Polymarket Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation
Adoption: null
Issue sample: [{"url": "https://github.com/Polymarket/real-time-data-client/issues/26", "createdAt": "2025-12-04T10:20:13Z", "state": "OPEN", "comments": {"nodes": [{"createdAt": "2025-12-05T19:28:28Z", "authorAssociation": "NONE"}, {"createdAt": "2025-12-06T20:33:09Z", "authorAssociation": "NONE"}, {"createdAt": "2025-12-06T23:02:38Z", "authorAssociation": "NONE"}, {"createdAt": "2025-12-17T07:14:36Z", "authorAssociation": "NONE"}, {"createdAt": "2025-12-17T07:42:59Z", "authorAssociation": "NONE"}, {"createdAt": "2025-12-17T07:44:55Z", "authorAssociation": "NONE"}, {"createdAt": "2025-12-17T08:06:07Z", "authorAssociation": "NONE"}, {"createdAt": "2026-01-01T14:40:44Z", "authorAssociation": "NONE"}, {"createdAt": "2026-01-02T23:43:36Z", "authorAssociation": "NONE"}, {"createdAt": "2026-01-16T03:55:38Z", "authorAssociation": "NONE"}]}}, {"url": "https://github.com/Polymarket/real-time-data-client/issues/47", "createdAt": "2026-08-15T09:25:32Z", "state": "OPEN", "comments": {"nodes": []}}]

## Polymarket/builder-signing-sdk
https://github.com/Polymarket/builder-signing-sdk
{"id": 1062854511, "stars": 27, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "036f63a2d0ae357c436a2f412778d2ca77c8047a", "last_commit_date": "2026-03-24T13:41:55Z", "license": null, "actual_license_paths": [], "license_files_read": false, "archived": false, "recent_commit_count": 2, "recent_authors_sample50": ["carlos-poly"], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] TypeScript SDK for creating authenticated builder headers
README: # builder-signing-sdk A TypeScript SDK for creating authenticated builder headers ## Installation ```bash pnpm install @polymarket/builder-signing-sdk ``` ## Quick Start ```typescript import { BuilderSigner }
Headings: # builder-signing-sdk; ## Installation; ## Quick Start
Runtime: // Local | localBuilderCreds: {
LICENSE: 
Adoption: null
Issue sample: [{"url": "https://github.com/Polymarket/builder-signing-sdk/issues/5", "createdAt": "2026-02-11T05:12:40Z", "state": "CLOSED", "comments": {"nodes": []}}]

## Polymarket/builder-relayer-client
https://github.com/Polymarket/builder-relayer-client
{"id": 1068072689, "stars": 56, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "9122f6fb1856f1ecfe4406685bfa19a2c5a7b290", "last_commit_date": "2026-05-28T18:34:51Z", "license": null, "actual_license_paths": [], "license_files_read": false, "archived": false, "recent_commit_count": 3, "recent_authors_sample50": ["adi-poly", "cesarenaldi"], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] Typescript Client for the Polymarket Relayer API
README: # builder-relayer-client TypeScript client library for interacting with Polymarket relayer infrastructure ## Installation ```bash pnpm install @polymarket/builder-relayer-client ``` ## Quick Start ### Basic Setup ```typescript
Headings: # builder-relayer-client; ## Installation; ## Quick Start; ### Basic Setup; ### Transaction Types; ### With Local Builder Authentication; ### With Remote Builder Authentication; ## Examples; ### Execute ERC20 Approval Transaction; ### Deploy Safe Contract; ### Redeem Positions; #### CTF (ConditionalTokensFramework) Redeem; #### NegRisk Adapter Redeem; ### Deposit Wallet; #### Derive Deposit Wallet Address; #### Deploy Deposit Wallet; #### Execute Deposit Wallet Batch; #### Check Deposit Wallet Deployment
Runtime: The transaction type is specified as the last parameter when creating a `RelayClient` instance. All examples use the `Transaction` type - the client automatically converts transactions to the appropriate format (`SafeTransaction` or `ProxyTransaction`) based o | ### With Local Builder Authentication | localBuilderCreds: builderCreds | url: "http://localhost:3000/sign", | #### CTF (ConditionalTokensFramework) Redeem | The standalone `deriveDepositWallet()` helper only derives UUPS deposit wallet addresses and is deprecated. Prefer `client.deriveDepositWalletAddress()`.
LICENSE: 
Adoption: null
Issue sample: [{"url": "https://github.com/Polymarket/builder-relayer-client/issues/39", "createdAt": "2026-09-06T16:07:12Z", "state": "OPEN", "comments": {"nodes": [{"createdAt": "2026-09-06T16:11:30Z", "authorAssociation": "NONE"}, {"createdAt": "2026-09-07T03:32:27Z", "authorAssociation": "NONE"}]}}, {"url": "https://github.com/Polymarket/builder-relayer-client/issues/27", "createdAt": "2026-04-29T05:17:02Z", "state": "OPEN", "comments": {"nodes": [{"createdAt": "2026-05-15T23:16:32Z", "authorAssociation": "NONE"}, {"createdAt": "2026-07-23T13:35:08Z", "authorAssociation": "NONE"}, {"createdAt": "2026-07-24T06:23:36Z", "authorAssociation": "NONE"}]}}]

## Polymarket/py-builder-signing-sdk
https://github.com/Polymarket/py-builder-signing-sdk
{"id": 1079894007, "stars": 8, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "e5403c4a86e28b8aa9105d52bc5606fdb5511be0", "last_commit_date": "2025-10-20T20:11:19Z", "license": null, "actual_license_paths": [], "license_files_read": false, "archived": false, "recent_commit_count": 0, "recent_authors_sample50": [], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] Python SDK for creating authenticated builder headers
README: # py-builder-signing-sdk Python SDK for Polymarket builder authentication and signing. ## Installation ```bash pip install py-builder-signing-sdk ``` ## Usage ```python from py_builder_signing_sdk import BuilderConfig, BuilderApiKeyCreds,
Headings: # py-builder-signing-sdk; ## Installation; ## Usage; # Local signing; # Remote signing; # Generate signed headers
Runtime: Python SDK for Polymarket builder authentication and signing. | ```python | # Local signing | config = BuilderConfig(local_builder_creds=creds) | url="http://localhost:3000/sign",
LICENSE: 
Adoption: null
Issue sample: [{"url": "https://github.com/Polymarket/py-builder-signing-sdk/issues/2", "createdAt": "2025-12-08T08:37:29Z", "state": "OPEN", "comments": {"nodes": []}}]

## Polymarket/py-builder-relayer-client
https://github.com/Polymarket/py-builder-relayer-client
{"id": 1081395207, "stars": 42, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "267a36d84d7839b6e4ac134297d9230fc224cf8f", "last_commit_date": "2026-05-29T14:08:30Z", "license": null, "actual_license_paths": [], "license_files_read": false, "archived": false, "recent_commit_count": 19, "recent_authors_sample50": ["cesarenaldi", "suhailkakar"], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] Python Client for the Polymarket Relayer API
README: # py-builder-relayer-client Python client library for interacting with the Polymarket Relayer infrastructure ## Installation ```bash pip install py-builder-relayer-client ``` ## Configuration Create a `.env` file
Headings: # py-builder-relayer-client; ## Installation; ## Configuration
Runtime: Python client library for interacting with the Polymarket Relayer infrastructure
LICENSE: 
Adoption: null
Issue sample: [{"url": "https://github.com/Polymarket/py-builder-relayer-client/issues/27", "createdAt": "2026-07-03T10:47:53Z", "state": "OPEN", "comments": {"nodes": [{"createdAt": "2026-07-09T00:20:00Z", "authorAssociation": "NONE"}, {"createdAt": "2026-07-15T02:04:05Z", "authorAssociation": "NONE"}, {"createdAt": "2026-07-25T15:09:37Z", "authorAssociation": "NONE"}, {"createdAt": "2026-09-06T15:56:15Z", "authorAssociation": "NONE"}, {"createdAt": "2026-09-06T16:06:18Z", "authorAssociation": "NONE"}]}}, {"url": "https://github.com/Polymarket/py-builder-relayer-client/issues/25", "createdAt": "2026-06-17T17:44:32Z", "state": "OPEN", "comments": {"nodes": [{"createdAt": "2026-08-14T13:57:45Z", "authorAssociation": "NONE"}]}}]

## Polymarket/safe-wallet-integration
https://github.com/Polymarket/safe-wallet-integration
{"id": 1120012436, "stars": 6, "observed_at": "2026-09-13T15:52:15.191909+00:00", "latest_commit": "49ec9991b7f3e95197a4d53910f6086bf3ff2294", "last_commit_date": "2025-12-22T14:47:09Z", "license": null, "actual_license_paths": [], "license_files_read": false, "archived": true, "recent_commit_count": 0, "recent_authors_sample50": [], "bank_status": "NEW", "bank_layers": [], "build_status": "NOT_EXECUTED", "license_warnings": []}
[vendor] None
README: # Polymarket Integration Reference A Next.js reference implementation for integrators to add Polymarket trading to their platforms. Works with any EIP-6963 compatible browser wallet. This
Headings: # Polymarket Integration Reference; ## Table of Contents; ## Overview; ## Quick Start; ### Prerequisites; ### Installation; ### Environment Setup; # Polygon RPC endpoint; # Builder credentials (from polymarket.com/settings?tab=builder); # Optional: Integrator fee collection; ### Run Development Server; ## Integration Guidelines; ### Geoblocking; ### Market Discovery; ### Wallet Infrastructure; #### RelayClient Initialization; #### Safe Address Derivation; #### Safe Deployment; ### Builder Codes; #### Remote Signing Architecture; #### Server-Side Signing Endpoint; #### Client-Side Configuration; ### User API Credentials; ### Token Approvals; ### Authenticated CLOB Client; ### Trading; ### Fee Collection; # .env.local; ### Position Management; ### IP Whitelists
Runtime: Create `.env.local`: | Open [http://localhost:3000](http://localhost:3000) | The `RelayClient` handles Safe deployment, token approvals, and CTF operations (splitting, merging, redeeming positions). It requires your builder credentials via a `BuilderConfig`: | **Docs:** [Builder Program](https://docs.polymarket.com/developers/builders/builder-intro) | [CLOB Authentication](https://docs.polymarket.com/developers/CLOB/authentication) | **Key Parameters:** | **Parameter Details:** | | Parameter | Value | Purpose | | # .env.local | | `next` | Framework | | - [Builder Program](https://docs.polymarket.com/developers/builder-program) | ## License
LICENSE: 
Adoption: null
Issue sample: []
