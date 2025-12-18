from typing import List
from typing import Any
from dataclasses import dataclass

# https://restcountries.com/v3.1/name/Poland
import json
@dataclass
class Ara:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Ara':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Ara(_official, _common)

@dataclass
class Bre:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Bre':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Bre(_official, _common)

@dataclass
class CapitalInfo:
    latlng: List[float]

    @staticmethod
    def from_dict(obj: Any) -> 'CapitalInfo':
        _latlng = [.from_dict(y) for y in obj.get("latlng")]
        return CapitalInfo(_latlng)

@dataclass
class Car:
    signs: List[str]
    side: str

    @staticmethod
    def from_dict(obj: Any) -> 'Car':
        _signs = [.from_dict(y) for y in obj.get("signs")]
        _side = str(obj.get("side"))
        return Car(_signs, _side)

@dataclass
class Ces:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Ces':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Ces(_official, _common)

@dataclass
class CoatOfArms:
    png: str
    svg: str

    @staticmethod
    def from_dict(obj: Any) -> 'CoatOfArms':
        _png = str(obj.get("png"))
        _svg = str(obj.get("svg"))
        return CoatOfArms(_png, _svg)

@dataclass
class Currencies:
    PLN: PLN

    @staticmethod
    def from_dict(obj: Any) -> 'Currencies':
        _PLN = PLN.from_dict(obj.get("PLN"))
        return Currencies(_PLN)

@dataclass
class Cym:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Cym':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Cym(_official, _common)

@dataclass
class Demonyms:
    eng: Eng
    fra: Fra

    @staticmethod
    def from_dict(obj: Any) -> 'Demonyms':
        _eng = Eng.from_dict(obj.get("eng"))
        _fra = Fra.from_dict(obj.get("fra"))
        return Demonyms(_eng, _fra)

@dataclass
class Deu:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Deu':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Deu(_official, _common)

@dataclass
class Eng:
    f: str
    m: str

    @staticmethod
    def from_dict(obj: Any) -> 'Eng':
        _f = str(obj.get("f"))
        _m = str(obj.get("m"))
        return Eng(_f, _m)

@dataclass
class Est:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Est':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Est(_official, _common)

@dataclass
class Fin:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Fin':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Fin(_official, _common)

@dataclass
class Flags:
    png: str
    svg: str
    alt: str

    @staticmethod
    def from_dict(obj: Any) -> 'Flags':
        _png = str(obj.get("png"))
        _svg = str(obj.get("svg"))
        _alt = str(obj.get("alt"))
        return Flags(_png, _svg, _alt)

@dataclass
class Fra:
    f: str
    m: str
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Fra':
        _f = str(obj.get("f"))
        _m = str(obj.get("m"))
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Fra(_f, _m, _official, _common)

@dataclass
class Gini:
    2018: float

    @staticmethod
    def from_dict(obj: Any) -> 'Gini':
        _2018 = float(obj.get("2018"))
        return Gini(_2018)

@dataclass
class Hrv:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Hrv':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Hrv(_official, _common)

@dataclass
class Hun:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Hun':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Hun(_official, _common)

@dataclass
class Idd:
    root: str
    suffixes: List[str]

    @staticmethod
    def from_dict(obj: Any) -> 'Idd':
        _root = str(obj.get("root"))
        _suffixes = [.from_dict(y) for y in obj.get("suffixes")]
        return Idd(_root, _suffixes)

@dataclass
class Ind:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Ind':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Ind(_official, _common)

@dataclass
class Ita:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Ita':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Ita(_official, _common)

@dataclass
class Jpn:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Jpn':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Jpn(_official, _common)

@dataclass
class Kor:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Kor':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Kor(_official, _common)

@dataclass
class Languages:
    pol: str

    @staticmethod
    def from_dict(obj: Any) -> 'Languages':
        _pol = str(obj.get("pol"))
        return Languages(_pol)

@dataclass
class Maps:
    googleMaps: str
    openStreetMaps: str

    @staticmethod
    def from_dict(obj: Any) -> 'Maps':
        _googleMaps = str(obj.get("googleMaps"))
        _openStreetMaps = str(obj.get("openStreetMaps"))
        return Maps(_googleMaps, _openStreetMaps)

@dataclass
class Name:
    common: str
    official: str
    nativeName: NativeName

    @staticmethod
    def from_dict(obj: Any) -> 'Name':
        _common = str(obj.get("common"))
        _official = str(obj.get("official"))
        _nativeName = NativeName.from_dict(obj.get("nativeName"))
        return Name(_common, _official, _nativeName)

@dataclass
class NativeName:
    pol: Pol

    @staticmethod
    def from_dict(obj: Any) -> 'NativeName':
        _pol = Pol.from_dict(obj.get("pol"))
        return NativeName(_pol)

@dataclass
class Nld:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Nld':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Nld(_official, _common)

@dataclass
class Per:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Per':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Per(_official, _common)

@dataclass
class PLN:
    symbol: str
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'PLN':
        _symbol = str(obj.get("symbol"))
        _name = str(obj.get("name"))
        return PLN(_symbol, _name)

@dataclass
class Pol:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Pol':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Pol(_official, _common)

@dataclass
class Por:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Por':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Por(_official, _common)

@dataclass
class PostalCode:
    format: str
    regex: str

    @staticmethod
    def from_dict(obj: Any) -> 'PostalCode':
        _format = str(obj.get("format"))
        _regex = str(obj.get("regex"))
        return PostalCode(_format, _regex)

@dataclass
class Root:
    name: Name
    tld: List[str]
    cca2: str
    ccn3: str
    cioc: str
    independent: bool
    status: str
    unMember: bool
    currencies: Currencies
    idd: Idd
    capital: List[str]
    altSpellings: List[str]
    region: str
    subregion: str
    languages: Languages
    latlng: List[int]
    landlocked: bool
    borders: List[str]
    area: int
    demonyms: Demonyms
    cca3: str
    translations: Translations
    flag: str
    maps: Maps
    population: int
    gini: Gini
    fifa: str
    car: Car
    timezones: List[str]
    continents: List[str]
    flags: Flags
    coatOfArms: CoatOfArms
    startOfWeek: str
    capitalInfo: CapitalInfo
    postalCode: PostalCode

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _name = Name.from_dict(obj.get("name"))
        _tld = [.from_dict(y) for y in obj.get("tld")]
        _cca2 = str(obj.get("cca2"))
        _ccn3 = str(obj.get("ccn3"))
        _cioc = str(obj.get("cioc"))
        _independent =
        _status = str(obj.get("status"))
        _unMember =
        _currencies = Currencies.from_dict(obj.get("currencies"))
        _idd = Idd.from_dict(obj.get("idd"))
        _capital = [.from_dict(y) for y in obj.get("capital")]
        _altSpellings = [.from_dict(y) for y in obj.get("altSpellings")]
        _region = str(obj.get("region"))
        _subregion = str(obj.get("subregion"))
        _languages = Languages.from_dict(obj.get("languages"))
        _latlng = [.from_dict(y) for y in obj.get("latlng")]
        _landlocked =
        _borders = [.from_dict(y) for y in obj.get("borders")]
        _area = int(obj.get("area"))
        _demonyms = Demonyms.from_dict(obj.get("demonyms"))
        _cca3 = str(obj.get("cca3"))
        _translations = Translations.from_dict(obj.get("translations"))
        _flag = str(obj.get("flag"))
        _maps = Maps.from_dict(obj.get("maps"))
        _population = int(obj.get("population"))
        _gini = Gini.from_dict(obj.get("gini"))
        _fifa = str(obj.get("fifa"))
        _car = Car.from_dict(obj.get("car"))
        _timezones = [.from_dict(y) for y in obj.get("timezones")]
        _continents = [.from_dict(y) for y in obj.get("continents")]
        _flags = Flags.from_dict(obj.get("flags"))
        _coatOfArms = CoatOfArms.from_dict(obj.get("coatOfArms"))
        _startOfWeek = str(obj.get("startOfWeek"))
        _capitalInfo = CapitalInfo.from_dict(obj.get("capitalInfo"))
        _postalCode = PostalCode.from_dict(obj.get("postalCode"))
        return Root(_name, _tld, _cca2, _ccn3, _cioc, _independent, _status, _unMember, _currencies, _idd, _capital, _altSpellings, _region, _subregion, _languages, _latlng, _landlocked, _borders, _area, _demonyms, _cca3, _translations, _flag, _maps, _population, _gini, _fifa, _car, _timezones, _continents, _flags, _coatOfArms, _startOfWeek, _capitalInfo, _postalCode)

@dataclass
class Rus:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Rus':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Rus(_official, _common)

@dataclass
class Slk:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Slk':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Slk(_official, _common)

@dataclass
class Spa:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Spa':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Spa(_official, _common)

@dataclass
class Srp:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Srp':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Srp(_official, _common)

@dataclass
class Swe:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Swe':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Swe(_official, _common)

@dataclass
class Translations:
    ara: Ara
    bre: Bre
    ces: Ces
    cym: Cym
    deu: Deu
    est: Est
    fin: Fin
    fra: Fra
    hrv: Hrv
    hun: Hun
    ind: Ind
    ita: Ita
    jpn: Jpn
    kor: Kor
    nld: Nld
    per: Per
    pol: Pol
    por: Por
    rus: Rus
    slk: Slk
    spa: Spa
    srp: Srp
    swe: Swe
    tur: Tur
    urd: Urd
    zho: Zho

    @staticmethod
    def from_dict(obj: Any) -> 'Translations':
        _ara = Ara.from_dict(obj.get("ara"))
        _bre = Bre.from_dict(obj.get("bre"))
        _ces = Ces.from_dict(obj.get("ces"))
        _cym = Cym.from_dict(obj.get("cym"))
        _deu = Deu.from_dict(obj.get("deu"))
        _est = Est.from_dict(obj.get("est"))
        _fin = Fin.from_dict(obj.get("fin"))
        _fra = Fra.from_dict(obj.get("fra"))
        _hrv = Hrv.from_dict(obj.get("hrv"))
        _hun = Hun.from_dict(obj.get("hun"))
        _ind = Ind.from_dict(obj.get("ind"))
        _ita = Ita.from_dict(obj.get("ita"))
        _jpn = Jpn.from_dict(obj.get("jpn"))
        _kor = Kor.from_dict(obj.get("kor"))
        _nld = Nld.from_dict(obj.get("nld"))
        _per = Per.from_dict(obj.get("per"))
        _pol = Pol.from_dict(obj.get("pol"))
        _por = Por.from_dict(obj.get("por"))
        _rus = Rus.from_dict(obj.get("rus"))
        _slk = Slk.from_dict(obj.get("slk"))
        _spa = Spa.from_dict(obj.get("spa"))
        _srp = Srp.from_dict(obj.get("srp"))
        _swe = Swe.from_dict(obj.get("swe"))
        _tur = Tur.from_dict(obj.get("tur"))
        _urd = Urd.from_dict(obj.get("urd"))
        _zho = Zho.from_dict(obj.get("zho"))
        return Translations(_ara, _bre, _ces, _cym, _deu, _est, _fin, _fra, _hrv, _hun, _ind, _ita, _jpn, _kor, _nld, _per, _pol, _por, _rus, _slk, _spa, _srp, _swe, _tur, _urd, _zho)

@dataclass
class Tur:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Tur':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Tur(_official, _common)

@dataclass
class Urd:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Urd':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Urd(_official, _common)

@dataclass
class Zho:
    official: str
    common: str

    @staticmethod
    def from_dict(obj: Any) -> 'Zho':
        _official = str(obj.get("official"))
        _common = str(obj.get("common"))
        return Zho(_official, _common)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
