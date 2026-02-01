# Postgres vs Mongo

The argument that lasted three days.

Serban wanted Mongo. "Flexible schema," he said. "Move fast." He'd read a blog post. Everyone was using Mongo. It was web scale.

I pushed back. Hard.

"What kind of data do we have?" I asked.

"Users, posts, relationships..."

"Relationships. That's the key word. Users have posts. Posts have comments. Comments have authors. That's a graph, not a document. With Postgres, we get foreign keys, constraints, transactions. With Mongo, we get... hope."

He didn't want to hear it. "But Mongo is faster!"

"For writes, maybe. For complex queries? For ensuring data integrity? We're building a social platform. Consistency matters more than raw speed."

Day two: I built a prototype. Showed him the query to find "friends of friends who liked this post." Postgres: one join, 12ms. Mongo: aggregation pipeline, 340ms, and it returned duplicates.

Day three: He conceded. We chose Postgres.

Six months later: a migration would have corrupted data in Mongo. Postgres constraints caught it. He thanked me.

↔️ Sinapse: [[the-null-pointer-hunt]] [[schema-design]]
