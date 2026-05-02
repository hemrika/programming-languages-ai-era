# Programming Languages in the AI Era

Research repository for evaluating programming languages against the demands of AI-assisted and AI-agentic software development.

**Framework version:** v0.5 (2026-05-02). Snapshot below; see `framework/evaluation-framework.md` for the full version history.

## Core thesis

The AI era will favor languages that are not merely easy to write, but easy to analyze, verify, refactor, test, and operate by both humans and machines — whose load-bearing dependencies are resilient enough to underwrite that promise, and whose forward trajectory plausibly closes the remaining gaps.

## Framing

**Greenfield.** Installed base, existing code volume, and incumbent gravity are not scored as advantages. Languages are credited for forward-looking properties (governance, future fit, AI-training-corpus representation, ecosystem velocity, library maturity for new projects). Maintenance-estate teams should re-weight.

**Native vs ecosystem.** AI-systems and structured-output capability are scored separately for what the language/runtime/stewards ship directly versus what the third-party ecosystem provides. A 5.0 backed by Microsoft does not read identical to a 5.0 backed by three OSS volunteers — the de