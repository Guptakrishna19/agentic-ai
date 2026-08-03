1. Load Balancer
A load balancer distributes incoming requests across multiple API servers. This prevents a single server from becoming overloaded and improves availability.

2. Cache (Redis)
A cache stores frequently requested responses or retrieved document chunks in memory. This reduces latency and decreases repeated database lookups.

3. Separate Vector Database
The vector database is isolated from the application servers. It stores embeddings and performs similarity search efficiently while allowing independent scaling of storage and compute.