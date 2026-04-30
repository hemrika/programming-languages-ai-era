# Haskell

## AI-era hypothesis

Haskell is the natural anchor for the *verification advantage* lens: a pure-functional, strongly typed language whose program structure is deeply legible to formal reasoning. It tests whether AI-era pressure on correctness elevates languages built around type-driven and equational reasoning.

## Strengths

- Pure functional with very strong static typing
- Type-driven development supports machine-checkable contracts
- Powerful abstractions (typeclasses, monads, GADTs)
- Strong basis for formal reasoning and refactoring
- Active research community and tooling investment

## Weaknesses

- Steep learning curve and unfamiliar mental model for many developers
- Lazy evaluation complicates performance reasoning and debugging
- Smaller adoption and AI-training-data footprint
- Build-system fragmentation (Cabal, Stack, Nix)
- Library ecosystem narrower than mainstream alternatives

## Open questions

- Do Haskell's strong types make AI-generated code measurably more verifiable?
- Does laziness hurt or help AI-agent operability in practice?
- Will dependent-types or refinement-types extensions (e.g., Liquid Haskell) become AI-relevant?
