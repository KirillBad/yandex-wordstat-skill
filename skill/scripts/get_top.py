import json
from urllib.error import HTTPError
from schemas import DevicesEnum, Region, validate_region_input
from typing import Annotated
from urllib.request import Request, urlopen
from main import get_settings, app, err_console
import typer
from rich import print


@app.command()
def main(
    phrase: Annotated[
        str,
        typer.Argument(
            help="Key phase of the query. Supports search operators.", max=400
        ),
    ],
    num_phrases: Annotated[
        int,
        typer.Option(
            "--num-phrases",
            min=1,
            max=2000,
            help="Number of phrases in the response.",
        ),
    ] = 50,
    regions: Annotated[
        list[str] | None,
        typer.Option(
            "--region",
            help="Region alias. Can be passed multiple times. If ommited queries from all regions are taken into account.",
            metavar=f"[{'|'.join(region.value for region in Region)}]|REGION_ID",
        ),
    ] = None,
    devices: Annotated[
        list[DevicesEnum] | None,
        typer.Option(
            "--device",
            help="List of device types used to send the query. Can be passed multiple times. If ommited all devices used",
        ),
    ] = None,
) -> None:
    settings = get_settings()

    request = Request(
        "https://searchapi.api.cloud.yandex.net/v2/wordstat/topRequests",
        data=json.dumps(
            {
                "phrase": phrase,
                "numPhrases": num_phrases,
                **(
                    {"regions": [validate_region_input(region) for region in regions]}
                    if regions
                    else {}
                ),
                **({"devices": devices} if devices is not None else {}),
                "folderId": settings.folder_id,
            }
        ).encode("utf-8"),
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
