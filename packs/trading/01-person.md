# The person — independent traders and small trading desks

Research cut: 2026-09-13. Status: sourced desk research; no operator interview or time-and-motion study. Evidence classes: **[vendor]** published product claims; **[practitioner]** self-described users' reports, not verified incidents or a representative sample; **[analysis]** design choices and inferences.

## Continuity: extend the operating workflow, not a prediction product

[analysis] The supplied assignment reports substantial earlier SISO work covering an executive verdict, OSS composition, a workflow-oriented wedge and an evaluation plan. It identifies the missing person, workflow, incumbent and value research. This pack extends that direction rather than claiming to have recreated or independently verified the private earlier report. No private report, account record or runtime handoff is republished here. The public [trading entry](README.md) is the continuity pointer. The earlier reported MiroFish build/tests are not tests executed for this pack.

## One operator to design for

[analysis] **Primary design target: an own-account, discretionary equity/options trader who also runs occasional strategy experiments, works alone on a laptop, and maintains an IBKR-style brokerage record plus a separate journal.** This is a deliberately bounded design target, not an invented named interviewee. No country of residence, account size, profitability, household dependence, exact working hours or trading permission is asserted. A second person may review the records as an accountant; they do not approve orders in this first pilot.

[analysis] This person is not paid for producing a dashboard. In the own-account model there is no external client buying a deliverable: their economic result is net trading gains or losses after costs. The software's bounded deliverable is a trustworthy record of **what was believed, what was planned, what actually happened, and what remains unexplained**. Better recordkeeping is not evidence of profitable trading.

[practitioner] The choice is grounded in separate reports of journal-entry burden, missing historical entry/exit markers, and difficulty reconciling broker statements, rather than an assumption that every trader wants another automated strategy. See P01, P02, P05 and P08 below. [vendor] IBKR already offers business accounts and reporting; the pilot must improve a specific gap around existing records, not pretend the incumbent lacks an operating surface: [small-business offering](https://www.interactivebrokers.com/en/accounts/small-business.php), [account management and reporting](https://www.interactivebrokers.com/en/trading/account-management.php).

## A proposed Tuesday — a study script, not an observed diary

[analysis] Times below are relative to the operator's chosen market session; they are not the user's Vietnam timetable or a claim about exchange opening times. Frequencies and durations must be measured with a consenting participant. Each row describes the evidence the pilot should capture.

| Relative hour | Work and tools touched | Waiting / handoff | Durable record |
|---|---|---|---|
| T−2 | Read an email, chat message, filing or saved link; decide which ideas deserve investigation. | Source may be incomplete or unattributed. | Evidence item with original URL/file, timestamp and provenance. |
| T−1 | Open charts and broker/watchlist data; identify instrument, contract and relevant account. | Data entitlements, delayed feeds, inconsistent symbols. | Instrument mapping and dated data snapshot. |
| T | Write a thesis and disconfirming observation; optionally run a notebook/backtest. | Missing history or non-reproducible experiment. | Research case and linked experiment receipt. |
| T+1 | Set a proposed risk budget and record the intended action or decision not to trade. | Operator approval; current cash/positions and stale-data check. | Versioned trade plan, including a no-trade state. |
| T+2 | Use the broker's existing interface; record the resulting order/fill identifiers. | Broker acknowledgement is separate from an intended order. | Actual account event, not a fabricated fill. |
| T+3 | Monitor only while the laptop is awake; inspect exceptions rather than assuming alerts always arrive. | External feed and broker state. | Alert delivery/staleness evidence. |
| T+4 | Import statements or fill exports and reconcile partial fills, fees, corrections and cash. | Ambiguous trade grouping or unexplained difference. | Reconciliation exception with source records. |
| T+5 | Review the day's cases, attach selected screenshots/notes, and explain departures from the plan. | Human interpretation; a metric does not explain a decision. | Journal linked to actual events and original reasoning. |
| Weekly/monthly | Package records for an accountant; keep unresolved items explicit. | Accountant or broker clarification; jurisdiction-specific treatment. | Reviewed export and acknowledgement, not an automated tax conclusion. |

## Eight practitioner complaints — exact excerpts

All links were read on **2026-09-13**. These are eight distinct threads, not eight independently verified customers. Historical reports identify failure modes; they do not prove a current vendor defect. Where a thread's date is not reliably established in this research cut, the observation date is the only date claimed. Quotations retain users' wording.

| ID | Exact quotation [practitioner] | Source | Bounded implication [analysis] |
|---|---|---|---|
| P01 | “I’ve created an excel trade tracker but I have to be honest, filling it out every day fills me with dread.” | [How do you journal your trades?](https://www.reddit.com/r/Daytrading/comments/14y4zlz/how_do_you_journal_your_trades/) | Measure manual entry effort; an import-and-review flow may beat repeated typing. |
| P02 | “My broker doesnt show me entry/close of past trades in the chart which makes it hard to review just by looking at the chart.” | [How do you journal?](https://www.reddit.com/r/Daytrading/comments/1nxwpa4/how_do_you_journal/) | Preserve links between executions, timestamps and chart evidence; do not reduce a journal to aggregate P&L. |
| P03 | “used tradersync before that, i mean i log my trades and write my notes but then idk if its even helping?” | [What journal do you guys use?](https://www.reddit.com/r/Daytrading/comments/1szvtye/what_journal_do_you_guys_use/) | More metrics alone are not a validated benefit. Test whether the operator can answer a useful review question. |
| P04 | “Alerts are being sent out with delays ranging from a few seconds to several minutes” | [TradingView webhook-delay report](https://www.reddit.com/r/TradingView/comments/1dap1qu/ongoing_issues_with_alert_webhook_delays_on/) | Record event time, receipt time and stale state. This anecdote does not establish a latency distribution or SLA. |
| P05 | “But for some reason it's not showing in my realized S/T or L/T.” | [IBKR performance-statement discussion, October 2023](https://www.reddit.com/r/interactivebrokers/comments/17cz6zq/need_help_understanding_the_performance_statement/) | Assignment/exercise and realized/unrealized interpretations need explicit reconciliation. The poster's accounting interpretation is not adopted as correct. |
| P06 | “This was working perfectly for several weeks, now everything is broken.” | [Flex queries from multiple IP addresses](https://www.reddit.com/r/interactivebrokers/comments/1t8onmo/flex_queries_from_multiple_ip_addresses/) | Provide a file-import fallback and an intelligible fetch failure. The user's suspected cause is not verified. |
| P07 | “IBKR API seems to be quite awful to read.” | [What is your data provider?](https://www.reddit.com/r/algotrading/comments/1i2h8x1/what_is_your_data_provider/) | Hide connector complexity behind an explicit data contract, while preserving broker semantics and error details. |
| P08 | “I've been talking for several months with my accountant and Interactive Brokers about a big mismatch in some tax reports” | [Forex P&L statement discussion, January 2021](https://www.reddit.com/r/interactivebrokers/comments/ku2lgm/forex_pl_details_statement_doubt_proceeds_in_gbp/) | Export traceable source evidence and unresolved differences. Do not promise tax correctness from an imported P&L total. |

### Counterevidence matters

[practitioner] In the P01 thread another user describes an Excel import workflow: “Now it’s one copy and paste with 2 clicks and done. Beats me paying for a service to do it in my opinion.” [Source](https://www.reddit.com/r/Daytrading/comments/14y4zlz/how_do_you_journal_your_trades/).

[analysis] That is a direct competitor to this proposal. If the participant's existing broker export and spreadsheet already produce a reliable review with negligible effort, **do not migrate them merely to consolidate screens**. P03 also challenges the assumption that journaling software itself changes outcomes.

[practitioner] A separate discussion describes a spreadsheet with daily-progress, trade and statistics tabs, including risk, criteria and result fields. This is a concrete example of the operator's custom schema, not proof that every trader uses the same fields: [journal spreadsheet discussion](https://www.reddit.com/r/Daytrading/comments/1d1v6tc/how_do_you_journal/).

## Eight workflow-distinct segments

[analysis] These are proposed segmentation boundaries for discovery, not measured market shares.

| Segment | Distinct workflow / required evidence | Relationship to pilot |
|---|---|---|
| Discretionary equities/options, own account | Thesis, broker fills, partial closes, exercise/assignment, daily review. | **Primary**: evidence-backed import-to-review wedge. |
| Futures/order-flow discretionary | Tick/order-book replay, session calendars, exchange entitlements and delivery latency. | Later; bar-based journal cannot claim order-flow parity. |
| Systematic strategy developer | Dataset versions, experiment reproducibility, parameter selection and simulated/live divergence. | Notebook and engine extension; separate from first import pilot. |
| Portfolio/rebalancing investor | Holdings, allocation, cash flows, benchmark comparison, less intraday interaction. | Adjacent; wealth trackers may already fit better. |
| Crypto multi-exchange trader | Venue-specific fills, funding, transfers, asset identity and reconciliation. | Separate connector and event-semantic qualification. |
| Prediction-market researcher | Question/condition/outcome identity, evidence, resolution terms and settlement. | Important SISO extension; not silently treated as ordinary equities. |
| Prop-evaluation participant | Provider-specific account/rule constraints and multiple evaluation accounts. | Excluded until exact provider rules and rights are sourced. |
| Small managed-money desk | Client mandates, permissions, allocations, supervision and external reporting. | Excluded from own-account pilot; not made safe by adding a second login. |

## Questions the first participant must resolve

[analysis] Obtain consented examples of one normal day, one partial-fill/correction day and one difficult reporting period; identify current tools and actual bills; observe total human minutes including rework; identify which conversations arrive through email, WhatsApp, Telegram, Discord or elsewhere. Those channels and their response-time expectations have **not** been established for a specific participant. Do not manufacture chat demand, customer orders, payroll needs or assets under management to fill a template.

[analysis] Research conclusion: test **reconciled account events linked to original reasoning and review**. Retain broker execution and professional accounting authority. The evidence supports a testable workflow hypothesis, not profitability, demand volume or a finished product.
