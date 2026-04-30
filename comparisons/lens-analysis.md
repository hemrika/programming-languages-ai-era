# Cross-Cutting Lens Analysis

The framework defines five cross-cutting lenses (`framework/evaluation-framework.md`). This document evaluates each language against each lens and reads across them to identify the strongest cross-lens profiles.

## 1. Verification advantage

Languages whose structure makes program properties machine-checkable.

| Tier | Languages |
|---|---|
| Strong | Rust, Haskell |
| Moderate | Kotlin, TypeScript, .NET, Swift, Java, Go, Zig |
| Weak | Python, Elixir, Julia, C++, Mojo (early) |

Pure verification ranking is led by Haskell and Rust. Rust's mature ecosystem and operability give it the strategically dominant position; Haskell remains valuable as an upper-bound reference and in domains where formal-methods cost is justified.

## 2. Agentic development advantage

Languages where AI agents can write, modify, test, and verify code with low friction.

| Tier | Languages |
|---|---|
| Strong | TypeScript, Go |
| Moderate | Python, Rust, .NET, Kotlin |
| Constrained | Java, Haskell, Swift, Zig, Elixir |
| Difficult | C++, Mojo, Julia |

See `agent-friendly-languages.md` for the per-language reasoning.

## 3. Legacy gravity

Languages whose installed base creates persistent demand independent of greenfield momentum.

| Tier | Languages |
|---|---|
| High | Java, C++, Python, JavaScript/TypeScript |
| Moderate | .NET (C#), Go, Swift (Apple platforms) |
| Low | Rust, Kotlin, Haskell, Elixir, Zig, Julia |
| Negligible | Mojo |

Legacy gravity is asymmetric. It makes a language harder to displace, but it does not protect a language from becoming a legacy *liability* if AI-era pressures (verification, safety) erode its strategic position. C++ is the clearest example: high legacy gravity *and* high safety risk produce a fragile incumbent.

## 4. Safety pressure

Where AI-generated change carries unusually high blast radius, languages that prevent or contain those errors are favored.

| Tier | Languages |
|---|---|
| Strong | Rust, Haskell, Kotlin, .NET, Swift |
| Moderate | TypeScript, Go, Java, Elixir, Zig |
| Weak | Python, Julia, Mojo |
| Exposed | C++ |

Safety pressure is increasingly policy-aware, not merely technical. The White House ONCD report (2024), Microsoft Security Response Center analyses (2019), Android security publications (2022), and Chromium memory-safety reports collectively mark memory safety as a structural property regulators and platform owners now actively select for. C++ is the most exposed mainstream language under this lens; Python's exposure is different in kind (runtime errors rather than memory unsafety) but real for production AI-generated systems.

## 5. Abstraction compression

Languages that allow expressing more behavior in fewer lines without compromising clarity.

| Tier | Languages |
|---|---|
| Strong | Haskell, Kotlin, Elixir, TypeScript |
| Moderate | Rust, Swift, .NET, Python, Julia |
| Weak | Go, Java, C++ |
| Mixed | Mojo (designed for compression but unproven), Zig (deliberately low compression for legibility) |

Compression is double-edged. Go's intentional weakness on this lens is part of its agent-friendliness story — there is less hidden behavior an agent must reconstruct from context. Haskell's strength contributes to its verification advantage but raises learning cost for both humans and AI completion.

## Reading across the lenses

No single language wins all five. The strongest cross-lens profiles in this set:

- **Rust.** Strong on verification and safety; moderate on agentic and abstraction; low legacy gravity (offset by greenfield momentum in systems and infrastructure).
- **TypeScript.** Strong on agentic; moderate on verification, safety, and abstraction; high legacy gravity through the JavaScript ecosystem.
- **Kotlin.** Strong on safety and abstraction; moderate on verification and agentic; legacy gravity inherited via JVM interop.
- **Go.** Strong on agentic; moderate on safety; deliberately weak on abstraction; moderate legacy gravity in cloud and infrastructure.

The strongest defensive position (legacy gravity + ecosystem) belongs to Java, Python, and C++ — but C++ is uniquely exposed on the safety lens, making it the most fragile incumbent in the set.

## Where the lenses disagree

Three cases where the lenses pull in different directions are worth flagging:

- **Python.** Maximum legacy gravity and ecosystem; weak verification; weak safety. The framework's central question for Python is whether AI-era pressure on verification erodes the moat faster than gradual typing rebuilds it.
- **Haskell.** Maximum verification; weak agentic; weak legacy gravity. Strong static structure does not transfer into AI-era dominance without operability and ecosystem.
- **Mojo.** Designed for the future but currently weak on every lens except potential. The lens analysis is a useful counterfactual: what if AI-native design were sufficient by itself? The current evidence says it is not.

## Implications for portfolio thinking

For a team selecting languages across a portfolio of AI-era projects, this lens analysis suggests:

- **Default for greenfield application work.** TypeScript or Kotlin — strong on agentic and abstraction with reasonable safety.
- **Default for systems, infrastructure, security-sensitive.** Rust — pays the operability cost for verification and safety gains.
- **Default for data, AI/ML, scripting.** Python — accepting the verification gap but leveraging ecosystem.
- **Default for fault-tolerant distributed systems.** Elixir — ecosystem cost accepted for runtime properties no other language matches.
- **Default for very large existing estates.** Maintain incumbents (Java, C# on .NET, C++ where present) and apply AI-era pressure incrementally — modernization, memory-safety migration, gradual typing.

No language is a default for *everything*. The framework's central output is that AI-era language choice becomes more domain-sensitive, not less.
