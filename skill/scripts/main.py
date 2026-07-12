import os
from dataclasses import dataclass
import typer
from rich.console import Console

_API_KEY = "YANDEX_WORDSTAT_TOKEN"
_FOLDER_ID = "YANDEX_CLOUD_FOLDER_ID"

app = typer.Typer(add_completion=False)
err_console = Console(stderr=True)


@dataclass(frozen=True, slots=True)
class Settings:
    api_key: str
    folder_id: str


def get_settings() -> Settings:
    missing = [name for name in (_API_KEY, _FOLDER_ID) if not os.getenv(name)]

    if missing:
        err_console.print(
            "Configuration error: required environment "
            f"{'variables are' if len(missing) > 1 else 'variable is'} "
            f"not set: {', '.join(missing)}."
        )
        raise typer.Exit(code=2)

    return Settings(api_key=os.environ[_API_KEY], folder_id=os.environ[_FOLDER_ID])
