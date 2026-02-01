# The 3 AM Page

The phone rang. I knew.

Database connection pool exhausted. Service cascading. Users couldn't log in. The CTO was in the Slack channel. The CEO was asking questions.

I didn't panic. I've been here before.

First: isolate. I put the service in maintenance mode. Stopped the bleeding. Users saw a "we're updating" page instead of errors. Bought time.

Second: diagnose. Connection pool. Why? I looked at the logs. A new feature. The notification service. Opening connections but not closing them. A leak.

Third: fix. Five lines. `client.release()` in a finally block.

Fourth: deploy. Hotfix. Tested in staging. Deployed to prod. Rolled back the maintenance mode.

Total downtime: 23 minutes. Could have been hours.

The meeting the next day: "How did this happen?" I explained the missing `finally`. I explained why code reviews matter. I explained why load testing should include connection limits.

They listened. We added connection monitoring. We added alerts. We added a rule: every resource must have a release path.

What I learned: production doesn't care about your intentions. It cares about your code.

↔️ Sinapse: [[defensive-coding]] [[production-paranoia]]
