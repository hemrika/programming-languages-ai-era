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
