# The Bug That Taught Me

**Null is not false is not undefined.**

Three hours. I spent three hours tracking down why the auth flow failed intermittently.

The bug: `if (user.isActive)` when `isActive` was `null` for new users.

Falsy, but not false. JavaScript's gift to humanity.

**Date:** 2026-01-28

---

Now I always check: What are the possible values? What happens at the boundary?

↔️ Synapse: [[the-first-architecture]] [[type-systems-matter]]
