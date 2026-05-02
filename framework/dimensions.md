# Dimensions

> **Native vs ecosystem rule.** *Native* means stewarded by the language team or first-party shipped — language/runtime/standard-library/steward-shipped libraries. The "language steward" is the entity that ships the canonical language toolchain (Microsoft for .NET/C# and TypeScript, Apple for Swift, JetBrains for Kotlin, Dashbit/Plataformatec for Elixir, the Python Software Foundation for Python, the Go team at Google for Go, the Rust Foundation for Rust, OpenJDK / Oracle for Java, the ISO C++ committee with major-vendor compilers for C++). *Ecosystem* is everything else — third-party packages, community libraries, and commercial vendor SDKs not shipped by the language steward. Anthropic's official SDKs, OpenAI's SDKs, LangChain, Pydantic, Zod, Serde, Vercel AI SDK, Newtonsoft.Json, Jackson, llama.cpp, and nlohmann/json are ecosystem, not native — even when first-class for their language.

## Human cognition

Measures how well the language helps humans understand, modify, and reason about programs.

Criteria:

- readability
- conceptual economy
- expressiveness
- local reasoning
- error visibility
- abstraction quality

## Machine cognition

Measures how well the language exposes structure to compilers, analyzers, tools, and AI systems.

Criteria:

- static analyzability
- type-system strength
- syntax regularity
- semantic clarity
- refactorability
- formal reasoning potential

## AI-agent operability

Measures how well autonomous or semi-autonomous AI agents can work with the language.

Criteria:

- fast feedback loops
- error-message quality
- testability
- modularity
- dependency clarity
- code-generation robustness
- repairability

## Runtime and ecosystem

Measures production practicality.

Criteria:

- performance ceiling
- performance predictability
- deployment model
- interop
- library maturity (the libraries a new project needs exist and are usable, not the volume of legacy code in this language)
- ecosystem viability (forward-looking production-readiness: deployment story, observability, integration with non-language systems such as databases, OS, hardware, and accelerators; evaluated as a property a greenfield project can lean on today, distinct from legacy installed-base gravity)
- tooling maturity
- security posture
- concurrency model

## Strategic viability

Measures long-term relevance.

Criteria:

- ecosystem velocity
- institutional support
- learning curve
- talent availability
- backward compatibility
- governance quality
- AI-training representation
- future fit

## AI-systems native

Measures what the language/runtime/standard library/language-steward-shipped libraries provide directly for AI integration. Native means shipped by the language steward — Microsoft for .NET (Semantic Kernel, Microsoft.Extensions.AI, ONNX Runtime .NET), Apple for Swift (Core ML, Create ML, MLX), JetBrains for Kotlin (kotlinx-serialization, Kotlin MCP SDK), Dashbit/Plataformatec-adjacent for Elixir (Bumblebee, Nx). External community SDKs (LangChain, Anthropic SDKs, OpenAI SDKs, Pydantic) are scored under `ai_systems_ecosystem`, not here.

Criteria:

- steward_shipped_runtime (first-party AI/ML inference and modeling runtime, e.g. ONNX Runtime .NET, Core ML, MLX, Bumblebee/Nx)
- steward_shipped_agent_framework (first-party agent/orchestration framework, e.g. Semantic Kernel, Microsoft.Extensions.AI)
- steward_shipped_protocol_support (first-party MCP / function-calling / tool-protocol surface)
- steward_shipped_provider_clients (first-party LLM client libraries shipped by the language steward, distinct from external commercial SDKs)
- standard_library_ai_surface (any AI-relevant primitives in the standard library or core platform)

## AI-systems ecosystem

Measures the depth of the third-party / community / commercial-third-party ecosystem the language relies on for AI integration. This is where Anthropic and OpenAI SDKs, LangChain ports, MCP SDKs published outside the language steward, vector-store clients, Pydantic, Zod, Vercel AI SDK, llama.cpp bindings, and observability integrations live for most languages.

Criteria:

- llm_provider_sdks (Anthropic, OpenAI, Google client SDKs not shipped by the language steward)
- agent_frameworks_external (LangChain, LangChain.js, LangChain4j, LlamaIndex, AutoGen)
- protocol_sdks_external (MCP, A2A, OpenAI function-calling SDKs published outside the language steward)
- inference_runtime_bindings (llama.cpp bindings, ONNX bindings outside steward, candle, etc.)
- vector_store_clients (Pinecone, Weaviate, Qdrant, Chroma, pgvector clients)
- streaming_messaging (Kafka, NATS, Pub/Sub clients used by AI pipelines)
- observability (OpenTelemetry, structured logging integrations)
- embedding_pipeline_support (third-party embedding generation, vector ingestion)

## Structured-output native

Measures schema-validated parsing, types-to-schema generation, and pattern-match exhaustiveness provided by the language/stdlib/steward libraries. Native examples include System.Text.Json + JsonSchemaExporter (.NET), Codable (Swift stdlib), encoding/json + struct tags (Go stdlib), kotlinx-serialization (Kotlin — JetBrains-stewarded), Java records + Bean Validation (Jakarta-stewarded). Pydantic, Zod, Serde, Jackson, Newtonsoft.Json, Hibernate Validator, FluentValidation, ozzo-validation, validator/v10, and Ecto are scored under `structured_output_ecosystem`.

Criteria:

- stdlib_schema_validation (declarative schema-validated parsing in the standard library or steward-shipped library)
- stdlib_json_schema_generation (native types -> JSON Schema autogeneration shipped by the language steward)
- compile_time_contract_safety (how strongly the type system protects the boundary between LLM output and program code, using only steward-shipped facilities)
- pattern_match_exhaustiveness (closed-hierarchy + exhaustive-match reasoning at the language level)
- llm_tool_call_typing_native (steward-shipped tool-call argument typing — Semantic Kernel function calling, Microsoft.Extensions.AI structured outputs, etc.)

## Structured-output ecosystem

Measures the third-party / community / commercial ecosystem for the type/data layer between LLM output and program logic: Pydantic, Zod, ArkType, Instructor, Outlines, Vercel AI SDK structured outputs, Newtonsoft.Json, Jackson, FluentValidation, FastEndpoints, validator/v10, ozzo-validation, serde + schemars, Hibernate Validator, Ecto changesets, instructor_ex, nlohmann/json.

Criteria:

- ecosystem_schema_validation (Pydantic, Zod, ArkType, Jackson, serde, Ecto, validator/v10, Hibernate Validator, FluentValidation)
- ecosystem_json_schema_generation (zod-to-json-schema, schemars, Pydantic model_json_schema, Newtonsoft schema export)
- llm_tool_call_typing_ecosystem (Instructor, Vercel AI SDK structured outputs, LangChain/LangChain4j AI Services tool typing)
- constrained_generation (JSON-schema-constrained decoding / guided generation: Outlines, llama.cpp GBNF, JSON-mode wrappers)
- structured_output_libraries (LLM-specific structured-output libraries: Instructor, instructor_ex, Vercel AI SDK structured outputs, LangChain output parsers)
- runtime_validation_libraries (third-party runtime validation: Pydantic v2, Zod, FluentValidation, Hibernate Validator, ozzo-validation)

## Ecosystem dependency risk

Measures the backer-mix and resilience of the load-bearing dependencies the language relies on for its AI-systems, structured-output, and runtime/ecosystem position. **Higher score = lower risk = better.** A language whose AI/SO surface rests on language-steward-shipped or major-commercial-vendor backed libraries scores high; a language whose load-bearing dependencies are single-maintainer OSS or under-funded community projects scores low.

Anchors:

- 5.0 — almost all load-bearing dependencies backed by the language steward or major commercial vendors with sustained investment.
- 4.0 — mix of language-stewards and well-funded commercial vendors; few single-maintainer single-points-of-failure.
- 3.0 — healthy mix but with notable single-points-of-failure (a critical library with one primary maintainer).
- 2.0 — heavy reliance on small community projects or under-funded maintainers; bus-factor risk material.
- 1.0 — critical capability rests on near-abandoned or single-maintainer projects.

Criteria:

- backer_mix (the proportion of load-bearing dependencies backed by language stewards or major commercial vendors versus single-maintainer or under-funded community projects)
- bus_factor (number of active maintainers on each load-bearing dependency)
- funding_durability (commercial backing, foundation hosting, or paid-maintenance plans)
- single_points_of_failure (specific load-bearing dependencies with one primary maintainer)
- substitutability (whether a load-bearing dependency could be replaced without rewriting the AI/SO surface)
