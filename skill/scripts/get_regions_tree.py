import json
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from main import get_settings, app, err_console
import typer
from rich import print


@app.command()
def main() -> None:
    settings = get_settings()

    request = Request(
        "https://searchapi.api.cloud.yandex.net/v2/wordstat/getRegionsTree",
        data=json.dumps({"folderId": settings.folder_id}).encode("utf-8"),
        headers={
            "Authorization": f"Api-Key {settings.api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urlopen(request, timeout=10) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as error:
        message = error.read().decode("utf-8")
        err_console.print(f"Yandex API returned HTTP {error.code}: {message}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
