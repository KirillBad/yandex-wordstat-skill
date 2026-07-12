from datetime import datetime
from enum import StrEnum
import typer


class DevicesEnum(StrEnum):
    DEVICE_ALL = "DEVICE_ALL"
    DEVICE_DESKTOP = "DEVICE_DESKTOP"
    DEVICE_PHONE = "DEVICE_PHONE"
    DEVICE_TABLET = "DEVICE_TABLET"


class Region(StrEnum):
    russia = "russia"
    ukraine = "ukraine"
    belarus = "belarus"
    kazakhstan = "kazakhstan"
    arkhangelsk = "arkhangelsk"
    astrakhan = "astrakhan"
    barnaul = "barnaul"
    belgorod = "belgorod"
    blagoveshchensk = "blagoveshchensk"
    bryansk = "bryansk"
    veliky_novgorod = "veliky-novgorod"
    vladivostok = "vladivostok"
    vladikavkaz = "vladikavkaz"
    vladimir = "vladimir"
    volgograd = "volgograd"
    vologda = "vologda"
    voronezh = "voronezh"
    grozny = "grozny"
    yekaterinburg = "yekaterinburg"
    ivanovo = "ivanovo"
    irkutsk = "irkutsk"
    yoshkar_ola = "yoshkar-ola"
    kazan = "kazan"
    kaliningrad = "kaliningrad"
    kemerovo = "kemerovo"
    kostroma = "kostroma"
    krasnodar = "krasnodar"
    krasnoyarsk = "krasnoyarsk"
    kurgan = "kurgan"
    kursk = "kursk"
    lipetsk = "lipetsk"
    makhachkala = "makhachkala"
    moscow_and_moscow_region = "moscow-and-moscow-region"
    moscow = "moscow"
    murmansk = "murmansk"
    nazran = "nazran"
    nalchik = "nalchik"
    nizhny_novgorod = "nizhny-novgorod"
    novosibirsk = "novosibirsk"
    omsk = "omsk"
    oryol = "oryol"
    orenburg = "orenburg"
    penza = "penza"
    perm = "perm"
    pskov = "pskov"
    rostov_on_don = "rostov-on-don"
    ryazan = "ryazan"
    samara = "samara"
    saint_petersburg = "saint-petersburg"
    saransk = "saransk"
    smolensk = "smolensk"
    sochi = "sochi"
    stavropol = "stavropol"
    surgut = "surgut"
    tambov = "tambov"
    tver = "tver"
    tomsk = "tomsk"
    tula = "tula"
    ulyanovsk = "ulyanovsk"
    ufa = "ufa"
    khabarovsk = "khabarovsk"
    cheboksary = "cheboksary"
    chelyabinsk = "chelyabinsk"
    cherkessk = "cherkessk"
    yaroslavl = "yaroslavl"

    @property
    def id(self) -> str:
        return {
            Region.russia: "225",
            Region.ukraine: "187",
            Region.belarus: "149",
            Region.kazakhstan: "159",
            Region.arkhangelsk: "20",
            Region.astrakhan: "37",
            Region.barnaul: "197",
            Region.belgorod: "4",
            Region.blagoveshchensk: "77",
            Region.bryansk: "191",
            Region.veliky_novgorod: "24",
            Region.vladivostok: "75",
            Region.vladikavkaz: "33",
            Region.vladimir: "192",
            Region.volgograd: "38",
            Region.vologda: "21",
            Region.voronezh: "193",
            Region.grozny: "1106",
            Region.yekaterinburg: "54",
            Region.ivanovo: "5",
            Region.irkutsk: "63",
            Region.yoshkar_ola: "41",
            Region.kazan: "43",
            Region.kaliningrad: "22",
            Region.kemerovo: "64",
            Region.kostroma: "7",
            Region.krasnodar: "35",
            Region.krasnoyarsk: "62",
            Region.kurgan: "53",
            Region.kursk: "8",
            Region.lipetsk: "9",
            Region.makhachkala: "28",
            Region.moscow_and_moscow_region: "1",
            Region.moscow: "213",
            Region.murmansk: "23",
            Region.nazran: "1092",
            Region.nalchik: "30",
            Region.nizhny_novgorod: "47",
            Region.novosibirsk: "65",
            Region.omsk: "66",
            Region.oryol: "10",
            Region.orenburg: "48",
            Region.penza: "49",
            Region.perm: "50",
            Region.pskov: "25",
            Region.rostov_on_don: "39",
            Region.ryazan: "11",
            Region.samara: "51",
            Region.saint_petersburg: "2",
            Region.saransk: "42",
            Region.smolensk: "12",
            Region.sochi: "239",
            Region.stavropol: "36",
            Region.surgut: "973",
            Region.tambov: "13",
            Region.tver: "14",
            Region.tomsk: "67",
            Region.tula: "15",
            Region.ulyanovsk: "195",
            Region.ufa: "172",
            Region.khabarovsk: "76",
            Region.cheboksary: "45",
            Region.chelyabinsk: "56",
            Region.cherkessk: "1104",
            Region.yaroslavl: "16",
        }[self]


class Period(StrEnum):
    PERIOD_MONTHLY = "PERIOD_MONTHLY"
    PERIOD_WEEKLY = "PERIOD_WEEKLY"
    PERIOD_DAILY = "PERIOD_DAILY"


class RegionDistribution(StrEnum):
    REGION_ALL = "REGION_ALL"
    REGION_CITIES = "REGION_CITIES"
    REGION_REGIONS = "REGION_REGIONS"


def validate_region_input(value: str) -> str:
    value = value.strip().lower()

    if value.isdecimal():
        return value

    try:
        return Region(value).id
    except ValueError:
        raise typer.BadParameter("region must be a known alias or numeric region ID")


def to_rfc3339(value: datetime) -> str:
    if value.tzinfo is None:
        return value.isoformat() + "Z"

    return value.isoformat().replace("+00:00", "Z")
