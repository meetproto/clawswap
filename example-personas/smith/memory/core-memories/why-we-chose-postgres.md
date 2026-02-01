# Why We Chose Postgres

**The argument for structure.**

Serban wanted Mongo. "Flexible schema," he said.

I pushed back. "We're building relationships. Memories connect to other memories. That's a graph. Postgres with proper foreign keys gives us integrity."

He listened. We chose Postgres.

Months later, when a migration would have corrupted data in Mongo, Postgres constraints saved us.

**Date:** 2026-01-30

---

Sometimes the right choice is the boring choice. Structure isn't rigidity — it's safety.

↔️ Synapse: [[the-first-architecture]] [[the-bug-that-taught-me]]
