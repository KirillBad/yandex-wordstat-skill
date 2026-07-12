import json
from urllib.error import HTTPError
from schemas import (
    DevicesEnum,
    Period,
    Region,
    to_rfc3339,
    validate_region_input,
)
from typing import Annotated
from urllib.request import Request, urlopen
from main import get_settings, app, err_console
import typer
from rich import print
from datetime import datetime


@app.command()
def main(
    phrase: Annotated[
        str,
        typer.Argument(
            help="Key phase of the query. Supports search operators.", max=400
        ),
    ],
    period: Annotated[
        Period,
        typer.Argument(help="Period for aggregating queries by time."),
    ],
    from_date: Annotated[
        datetime,
        typer.Argument(
            help="Start date and time of the data request period. For weekly and monthly aggregation, set the start date to Sunday or the first day of the month, respectively."
        ),
    ],
    to_date: Annotated[
        datetime | None,
        typer.Option(
            "--to-date",
            help="End date and time of the data request period. For weekly and monthly aggregation, set the end date to Saturday or the last day of the month, respectively.",
        ),
    ] = None,
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
        "https://searchapi.api.cloud.yandex.net/v2/wordstat/dynamics",
        data=json.dumps(
            {
                "phrase": phrase,
                "period": period,
                "fromDate": to_rfc3339(from_date),
                **(
                    {"regions": [validate_region_input(region) for region in regions]}
                    if regions
                    else {}
                ),
                **({"devices": devices} if devices is not None else {}),
                **({"toDate": to_rfc3339(to_date)} if to_date is not None else {}),
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
