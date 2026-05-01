# Dimensions

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

## AI-systems interoperability

Measures how cleanly the language integrates with the infrastructure a complete AI-era system actually depends on: the data layer, LLM providers, agent frameworks, protocols, inference runtimes, streaming, and observability.

Criteria:

- data_layer_integration (SQL, NoSQL, vector-store clients)
- llm_provider_support (OpenAI, Anthropic, Google SDKs)
- agent_framework_support (LangChain, Semantic Kernel, LlamaIndex, etc.)
- protocol_support (MCP, A2A, OpenAI function-calling)
- inference_runtime_support (ONNX, llama.cpp bindings, local inference)
- streaming_messaging (Kafka, NATS, Pub/Sub)
- observability (OpenTelemetry, structured logging)
- embedding_pipeline_support (embedding generation, vector ingestion)

## Structured-output maturity

Measures how mature the language's ecosystem is for the type/data layer that sits between LLM output and program logic: schema-validated JSON parsing, LLM tool-call argument typing, constrained generation support, type-safe structured outputs from LLM SDKs, and JSON Schema generation from native types.

Criteria:

- schema_validation (declarative schema-validated parsing libraries: Pydantic, Zod, Serde+schemars, Jackson Bean Validation, kotlinx-serialization, System.Text.Json, Codable, Ecto changesets)
- llm_tool_call_typing (type-safe LLM tool-call argument definitions in the official LLM SDKs)
- constrained_generation (JSON-schema-constrained decoding / guided generation: llama.cpp grammars, Outlines, etc.)
- structured_output_libraries (LLM-specific structured-output ergonomics: Instructor, Vercel AI SDK structured outputs, LangChain output parsers, LangChain4j AI Services, Semantic Kernel function calling)
- json_schema_generation (native types -> JSON Schema autogeneration)
- compile_time_contract_safety (how strongly the type system protects the boundary between LLM output and program code)
