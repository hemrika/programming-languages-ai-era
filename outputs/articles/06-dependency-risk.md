# Pydantic Has More Power Over Your Stack Than You Think

*The Ecosystem Dependency Risk dimension makes visible what most language-choice frameworks miss: who actually controls your platform.*

By Rutger Hemrika · 2026-05-02

## The metaphor that isn't a metaphor

When I rank dependency risk in the cohort, Microsoft's stewardship of .NET ranks higher than the entire Pydantic-plus-Instructor-plus-Outlines stack. That's not a metaphor. It is a structural fact on a 1.0–5.0 scale, and the gap is two full points: .NET 4.5 versus Python 2.5, with .NET alone at the cohort ceiling and Python alone at the cohort floor.

Most language-choice frameworks miss this because they treat the headline ecosystem score as a single number. The Ecosystem Dependency Risk dimension splits the score into who carries the load. A 5.0 backed by Microsoft does not read identical to a 5.0 backed by three open-source volunteers, and I refuse to flatten the two into the same cell. The decision implication for a CTO is direct: dependency risk is a vendor-concentration question, the same way multi-cloud and multi-region are vendor-concentration questions, and the lens senior teams already apply to AWS or Azure exposure is the lens that applies to library stewardship. Almost no team applies it.

## Backer types

The EDR rubric scores load-bearing dependencies by backer mix. Six categories with named examples:

- **Language stewards.** The organization that ships the canonical language toolchain. Microsoft for .NET. JetBrains for Kotlin. Apple for Swift. Google for Go. The Python Software Foundation for Python. The Rust Foundation for Rust. OpenJDK plus Oracle for Java. ISO plus the major-vendor compilers for C++. Dashbit / Plataformatec for Elixir.
- **Commercial first-party.** A commercial entity that ships an SDK or library directly tied to its own product, with company-attributed engineering. Anthropic's official Python and TypeScript SDKs. OpenAI's official SDKs. Vercel for the AI SDK. Hugging Face for Transformers.
- **Commercial third-party.** A commercial entity stewarding a library that wraps multiple vendors. LangChain (LangChain AI). LlamaIndex. The Astral toolchain (`uv`, `ruff`).
- **Community multi-maintainer.** Three or more active maintainers, no single commercial backer, recurring release cadence. Pydantic. Serde (Rust). LangChain4j (Java).
- **Community single-maintainer.** One person carries the load. Instructor (Jason Liu). Zod (Colin McDonnell). nlohmann/json (Niels Lohmann). llama.cpp (Georgi Gerganov, with growing co-maintenance).
- **Research / academic.** A university or research lab as primary steward. Bumblebee and Nx (Dashbit-stewarded, with research-tier tooling underneath).

The categories are not stylistic. They map to the bus-factor question — if the named maintainer or steward stops investing tomorrow, what does the load look like? — and the EDR score for a language is the weighted average over its load-bearing dependency set.

## EDR scoring across the cohort

| Language | EDR | Backer mix on the load-bearing layer |
|---|---:|---|
| .NET (C#) | 4.5 | Microsoft (runtime, language, AI surface, structured-output surface, MCP) |
| Java | 4.0 | OpenJDK multi-vendor (Oracle, IBM, Red Hat, Microsoft, Amazon); LangChain4j |
| Kotlin | 4.0 | JetBrains (language, tooling); kotlinx-serialization |
| Go | 3.5 | Google (language); Anthropic and OpenAI first-party Go SDKs |
| Rust | 3.5 | Rust Foundation (multi-vendor); Serde, schemars, candle, async-openai |
| Swift | 3.5 | Apple (language); ecosystem thin outside Apple platforms |
| TypeScript | 3.0 | Microsoft (language); Zod single-maintainer; Vercel commercial-first-party |
| C++ | 3.0 | ISO plus Microsoft plus GCC plus LLVM (compilers); llama.cpp plus nlohmann/json single-maintainer |
| Elixir | 3.0 | Dashbit; instructor_ex small-maintainer port |
| Python | 2.5 | PSF (language); Pydantic community-multi-small; Instructor single; Outlines small-commercial |

What 4.5 looks like is the .NET row: load-bearing layer is one steward deep, that steward funds the runtime, the language, the AI surface, the structured-output surface, and co-maintains the MCP C# SDK. .NET is alone at the cohort ceiling on EDR, with no other language reaching 4.5; the next-highest is Java and Kotlin tied at 4.0. The probability of a coordinated load-bearing failure is the probability of Microsoft pivoting away from .NET. The base rate is low.

What 2.5 looks like is the Python row: load-bearing AI-application layer rests on Pydantic plus Instructor plus Outlines, three different backer types stacked on top of each other. Python is alone at the cohort floor on EDR, with no other language sitting below 3.0; the next-lowest are TypeScript, Elixir, and C++ tied at 3.0. The probability of a coordinated load-bearing failure is the probability of Jason Liu's attention shifting plus Pydantic's maintainer group narrowing plus Outlines' commercial scope changing — three independent low-probability events that together carry meaningful aggregate exposure.

This is wrong if a "small commercial" backer effectively becomes a language steward at scale — Anthropic or OpenAI shipping first-party schema-validation primitives that absorb the load Pydantic, Instructor, and Outlines currently carry. The probability is non-zero, and one of the eight predictions I will be graded on (whether Microsoft ships a first-party Anthropic SDK for .NET by 2027-11-02) is the first testable form of this trend.

## Implications for CTOs

Senior teams already apply vendor-risk thinking to cloud providers. Multi-region is vendor-concentration mitigation. Multi-account is blast-radius isolation. Exit-cost analysis is the dollar-figure form of the question. The same lens applies to load-bearing libraries, and almost no team runs the analysis at the library level.

The CTO question to ask the architecture team is direct: if this maintainer disappears tomorrow, what does my stack look like? Run the question through the named libraries.

If Jason Liu disappears tomorrow, every team that built structured-extraction patterns on Instructor inherits the maintenance burden, with no first-party fallback. If Colin McDonnell disappears tomorrow, every TypeScript team that uses Zod for boundary validation, tool-call typing, and Vercel AI SDK structured outputs is one bus-factor event from a strategic problem — and Microsoft's stewardship of TypeScript does not extend to Zod. If Georgi Gerganov disappears tomorrow, every team running llama.cpp for local inference is in the same position. If the Pydantic maintainer group narrows from its current count to one, Python's SOE=5.0 score moves to 3.0 inside one revision cycle.

The pragmatic response is portfolio-level. Risk-conservative teams hedge load-bearing single-maintainer libraries with redundancy at the architectural seam — ArkType beside Zod, multiple inference backends behind a single interface, type definitions that survive a switch in the validation library. The hedge is the kind of thing that wants a paragraph in the architecture decision record. Most teams do not write that paragraph. The strongest objection is "fork it if it breaks." That objection is the moment the team owns a CVE response, an upstream API drift, and a frontier-model SDK change in the same week. Forking is a cost, not a hedge.

This is wrong if the field of maintainers expands faster than expected. Pydantic adding three or more active maintainers is the canonical case — if it lands, Python's EDR moves up and the dependency-risk thesis tightens around the libraries that did not.

## Where the risk is most concentrated

Three rows in the matrix carry concentrated single-maintainer exposure on load-bearing libraries.

Python is the canonical case — three single-points-of-failure in the AI-application layer (Pydantic count narrowing risk, Instructor single-maintainer, Outlines small-commercial). EDR=2.5 is the lowest vendor-stewardship score in the cohort.

TypeScript carries one — Zod, single-maintainer, sitting inside the Anthropic SDK tool-typing surface, the OpenAI SDK structured-output mode, the Vercel AI SDK `generateObject`, and the application's own boundary validation. EDR=3.0 reflects Microsoft's language-steward credit absorbing some of the exposure but not the Zod-specific concentration.

C++ carries multiple single-maintainer load-bearing dependencies — llama.cpp for inference, nlohmann/json for structured-output round-trip work — paired with single-vendor accelerator runtimes (CUDA, ROCm) that are commercial-first-party but vendor-locked. EDR=3.0 is a mixed signal: structural-vendor backing on the compilers, single-maintainer concentration on the application-layer libraries.

The contrast with .NET, Java, and Kotlin — all 4.0 or higher — is the structural read. Vendor-stewarded languages with vendor-stewarded ecosystem layers carry less aggregated dependency risk than community-stewarded languages with community-stewarded ecosystem layers, even when the ecosystem-half score (AIE, SOE) is identical or higher on the community-stewarded side.

## The strategic read

Dependency risk is the dimension I think most likely to move next. The reason is mechanical: the entities most likely to absorb load-bearing community libraries — Anthropic, OpenAI, Microsoft, JetBrains — are also the entities investing in AI-systems primitives at the highest velocity. A Microsoft-shipped first-party Anthropic SDK for .NET shifts AIN and EDR together. An OpenAI-shipped first-party schema-validation library shifts SON and EDR together. A Pydantic governance broadening shifts EDR alone but in the right direction.

I publish eight date-stamped, falsifiable predictions in piece 8. Three carry direct EDR signal. Either Pydantic gains at least three active maintainers by 2027-05-02, or Python's Ecosystem Dependency Risk score trends toward 2.0 in the next major framework revision. Either Microsoft ships a first-party Anthropic SDK for .NET by 2027-11-02, or .NET's AIN ceiling holds at 4.0. Either Apple ships cross-platform Swift AI SDKs through 2027-05-02, or Swift's AIE stays at or below 2.5. The v1.1 grading checkpoint in May 2027 is when the EDR cells get the first round of corrections. Pydantic's maintainership is the canonical case I will be graded on.

For CTOs running an architecture review in 2026: read the EDR column of the matrix, write down the load-bearing libraries by stewardship type, and ask the bus-factor question. The question is the architecture decision record paragraph almost no team writes. My working assumption is that the teams that write it have a structural advantage on the 5-year horizon.

## Closing

Microsoft's stewardship of .NET ranks higher than the entire Pydantic-plus-Instructor-plus-Outlines stack on the dependency-risk axis. Apply the vendor-concentration lens to your library stack the same way you apply it to your cloud bill, and write the paragraph in your architecture decision record.

Subscribe at `rutgerhemrika.substack.com` for piece 7 — reachability across the cohort, with the per-language gap walks behind .NET's Reach=4.5 and C++'s Reach=2.0. If you want the underlying data, claims, and sources, the fr