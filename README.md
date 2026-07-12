# Yandex Wordstat Skill

An [Agent Skill](https://agentskills.io/) for researching Yandex search demand with the Yandex Wordstat API.

Use it to retrieve and interpret:

- query popularity and related queries;
- search-demand dynamics and seasonality;
- regional demand distribution;
- Wordstat region identifiers.

## Requirements

- [uv](https://docs.astral.sh/uv/)
- Yandex Wordstat API credentials

Set the credentials in the environment where your agent runs:

[How to get API KEY](https://aistudio.yandex.ru/docs/ru/search-api/quickstart/)
[How to get folder id](https://yandex.cloud/en/docs/resource-manager/operations/folder/get-id)

```bash
export YANDEX_WORDSTAT_API_KEY="your-api-key"
export YANDEX_CLOUD_FOLDER_ID="your-folder-id"
```

## Install with `npx skills`

The [`skills`](https://github.com/vercel-labs/skills) CLI detects the skill in this repository and installs it for the agents you select:

```bash
npx skills add KirillBad/yandex-wordstat-skill
```

## Usage

Ask for Wordstat research in natural language. The agent should load the skill automatically when it is relevant.

Examples:

```text
Проверь спрос на ремонт кофемашин в Самаре и покажи связанные запросы.
```

```text
Сравни частотность запроса «доставка цветов» по Москве,
Екатеринбургу и Новосибирску.
```

```text
Покажи динамику спроса на кондиционеры за последние два года
и найди сезонный пик.
```
