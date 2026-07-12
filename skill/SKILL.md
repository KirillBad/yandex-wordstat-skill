---
name: yandex-wordstat
description: Use Yandex Wordstat API to research Yandex search demand, query popularity, trends, regional distribution, and related queries when planning commercial websites, SEO structure, landing pages, content plans, or market demand validation.
---

# Yandex Wordstat

Use the bundled CLI scripts to retrieve Wordstat data and interpret it according to the user's goal.

## Scripts

- `scripts/get_top.py` — get popular and related queries for the last 30 days.
- `scripts/get_dynamics.py` — get query frequency over time.
- `scripts/get_regions_distribution.py` — get query frequency distribution by region for the last 30 days.
- `scripts/get_regions_tree.py` — get the tree of supported regions and their IDs.

## Running scripts

Run from the skill root (the directory containing this `SKILL.md`):

```bash
uv --project scripts run scripts/SCRIPT_NAME.py [ARGS] [OPTIONS]
```

Before using a script for the first time, or when its arguments are unclear, inspect its CLI interface:

```bash
uv --project scripts run scripts/SCRIPT_NAME.py --help
```

Script results are written as JSON to stdout. Diagnostics and errors are written to stderr.

## Workflow

1. Choose the smallest set of scripts needed for the user's request.
2. Inspect --help when the required arguments or options are unknown.
3. Run the selected scripts.
4. Interpret the returned data and answer the user's actual question. Do not return raw JSON unless the user requests it.
5. When comparing phrases or regions, preserve the query parameters used so the results remain comparable.

## Regions

Treat an available region alias as an exact city, not as a shortcut for its
parent administrative region. Prefer an exact alias when it matches the user's
wording. Query the regions tree only when no matching alias exists:

```bash
uv --project scripts run scripts/get_regions_tree.py
```

Then pass the numeric region ID directly:

```bash
uv --project scripts run scripts/SCRIPT_NAME.py --region 208
```

## Credentials

The scripts require these environment variables:

- `YANDEX_WORDSTAT_API_KEY`
- `YANDEX_CLOUD_FOLDER_ID`

If a script reports that any required environment variable is missing, stop immediately. Tell the user which variable is missing and ask them to configure it before retrying.

Never ask the user to paste secret values into the chat. Ask them to set the variables in the environment where the agent runs.
