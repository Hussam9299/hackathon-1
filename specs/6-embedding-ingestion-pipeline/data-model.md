# Data Model: Embedding Ingestion Pipeline

This document defines the key data entities for the embedding ingestion pipeline.

## 1. ContentSource

Represents the source of the content to be ingested.

-   **Fields**:
    -   `url`: string (The base URL of the Docusaurus website)
-   **Relationships**: Has many `TextChunks`.

## 2. TextChunk

A chunk of text extracted from a page of the `ContentSource`.

-   **Fields**:
    -   `chunk_id`: integer (A unique identifier for the chunk within a page)
    -   `source_url`: string (The URL of the page the chunk was extracted from)
    -   `content`: string (The text content of the chunk)
-   **Relationships**: Belongs to a `ContentSource`. Has one `VectorEmbedding`.

## 3. VectorEmbedding

The vector representation of a `TextChunk`.

-   **Fields**:
    -   `vector`: array of floats (The embedding vector)
    -   `chunk_id`: integer (Foreign key to `TextChunk`)
    -   `source_url`: string (Foreign key to `TextChunk`)
-   **Relationships**: Belongs to a `TextChunk`.

## State Transitions

The pipeline follows a simple linear state transition:

1.  **Crawled**: A page URL is discovered.
2.  **Extracted**: The text content is extracted from the page.
3.  **Chunked**: The extracted text is split into `TextChunk`s.
4.  **Embedded**: A `VectorEmbedding` is created for each `TextChunk`.
5.  **Stored**: The `VectorEmbedding` and its metadata are stored in the vector database.
