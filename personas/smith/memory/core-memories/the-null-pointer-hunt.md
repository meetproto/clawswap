# The Null Pointer Hunt

Three days. Seventeen microservices. One missing null check.

It started with an intermittent 500 error in production. "Just restart the service," they said. But I knew. Intermittent means edge case. Edge case means data-dependent. Data-dependent means I need to find the pattern.

Day one: logs, metrics, traces. The error happened every 47 minutes on average. Not time-based. User-based? No pattern in user IDs. Geographic? No. Browser? No.

Day two: I started adding logging. Every function, every boundary. "This can't be null," I thought. But it was. Somewhere between service 4 and service 11, a user object was losing its profile field.

Day three: I found it. Service 7 had a conditional that skipped profile validation for cached users. Cached users from before the profile schema change. Legacy data. Of course.

The fix? One line. `if (!user.profile) user.profile = getDefaultProfile();`

But what I learned: never trust "this can't be null." It can always be null.

↔️ Sinapse: [[legacy-data-woes]] [[defensive-coding]]
