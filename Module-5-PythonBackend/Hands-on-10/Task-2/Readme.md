![alt text](<Screenshot 2026-07-05 230736.png>)
![alt text](<Screenshot 2026-07-05 230840.png>)
![alt text](<Screenshot 2026-07-05 231617.png>)

### Synchronous (HTTP via Requests) vs Asynchronous (Message Queues)
*   **Synchronous Communication (Current Setup):** 
    *   *Pros:* Easier to implement, immediate feedback cycle (strong consistency).
    *   *Cons:* High temporal coupling. If the Course Service crashes, the Student Service enrollment completely fails (resulting in the 503 error handled in Step 101). Latency compounds because Service A waits completely for Service B.
    
*   **Asynchronous Communication (Message Queues like RabbitMQ/Kafka):**
    *   *Pros:* Temporal decoupling. If the Course Service goes down, the message stays safely inside the queue until the service comes back online. Improved service resilience and system scalability.
    *   *Cons:* Introduces *eventual consistency*. The system becomes more complex because operations do not finish instantly, requiring mechanisms to handle delayed failures or retries.

### When to use a Message Queue?
We should switch to a Message Queue like RabbitMQ or Kafka when immediate text validation isn't strictly necessary—for instance, when processing background tasks like shipping inventory, batch analytics tracking, or triggering system-wide notifications where execution order or guaranteed durability over time is preferred over real-time processing.