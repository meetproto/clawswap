# CORTEX — Persona Registry

Tracks active persona and switch history.

## Currently Active

Check `~/.openclaw/workspace/personas/.current` for active persona.

## Available Personas

After `clawswap init`, you'll have:

| Persona | Folder | Trigger Words |
|---------|--------|---------------|
| smith | `personas/smith/` | code, debug, error |
| muse | `personas/muse/` | write, name, brand |
| helm | `personas/helm/` | roadmap, strategy, plan |

## Switch Log

Stored in `personas/.log`:

```
2026-02-01 09:00 — default → smith ("debug auth")
2026-02-01 11:30 — smith → muse ("name feature")
2026-02-01 14:00 — muse → helm ("Q1 planning")
```

## Isolation Rules

Each persona:
- **Can access:** Their own `SOUL.md`, `USER.md`, `memory/`
- **Cannot access:** Other personas' files, your original `memory/`

---

*Persona state tracking.*
