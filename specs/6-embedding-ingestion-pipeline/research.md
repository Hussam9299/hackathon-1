# Research: Embedding Ingestion Pipeline

This document summarizes the research conducted to resolve ambiguities in the implementation plan.

## 1. Performance Goals

**Decision**: The primary performance goal will be to maximize throughput (pages processed per second) while keeping latency for a single page under a reasonable threshold (e.g., 5 seconds). A specific target of 10 pages per second will be the initial goal.

**Rationale**: For an ingestion pipeline, especially for bulk processing, throughput is more critical than low latency for individual items. The goal is to process the entire website in a reasonable amount of time.

**Alternatives considered**: Prioritizing low latency, but this is more relevant for real-time applications, not bulk ingestion.

## 2. Scope and Scale

**Decision**: The initial scope is a single Docusaurus website with up to 1,000 pages. The system should be designed to be easily adaptable for more sites in the future.

**Rationale**: Starting with a clear, limited scope allows for a focused initial implementation. Designing for future extension (e.g., by making the source URL configurable) is a good practice.

**Alternatives considered**: Building a generic multi-site crawler from the start, but this would add unnecessary complexity to the initial version.

## 3. Best Practices for Cohere Embeddings

**Decision**: 
- Use `input_type="search_document"` for the documents being indexed.
- Choose the `embed-english-v3.0` model as the content is in English.
- Use a dimensionality of 1024.
- Pre-process and chunk the documents before sending them to the API.

**Rationale**: These decisions align with Cohere's official recommendations for semantic search use cases. Smart chunking is crucial for RAG performance.

**Alternatives considered**: Using other models, but `embed-english-v3.0` is a strong choice for English content.

## 4. Best Practices for Qdrant

**Decision**:
- Use the HTTP client for the implementation.
- Use Cosine similarity as specified in the constraints.
- Attach metadata (source URL, chunk number) to each vector.
- Use bulk upload methods for initial ingestion.
- Store vectors on disk to manage memory usage.

**Rationale**: These are standard practices for using Qdrant in a production-like environment. Bulk uploads are much more efficient for ingestion.

**Alternatives considered**: In-memory storage, but this could be an issue with large datasets.

## 5. Best Practices for Web Crawling

**Decision**:
- Use `requests` to fetch HTML and `BeautifulSoup` to parse it.
- Start with a sitemap if available to discover all URLs.
- Implement a delay between requests to avoid overwhelming the server.
- Focus on extracting only the main content of the pages.
- Handle potential errors like broken links gracefully.

**Rationale**: This is a standard and robust stack for simple web crawling tasks. Respecting the target server is crucial for any crawler.

**Alternatives considered**: Using a more complex framework like Scrapy, but that is overkill for this project's scope.

## 6. `uv` for Environment Management

**Decision**: Use `uv` to create and manage the virtual environment and dependencies for the project.

**Rationale**: `uv` is a modern, fast, and easy-to-use tool that simplifies Python project management. It is a good choice for a new project.

**Alternatives considered**: Using `venv` and `pip` directly, but `uv` provides a better developer experience.
