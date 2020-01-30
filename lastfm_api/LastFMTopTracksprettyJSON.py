# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = last_fm_from_dict(json.loads(json_string))

import json
from dataclasses import dataclass
from typing import Any, List, TypeVar, Type, Callable, cast
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ToptracksAttr:
    page: int
    per_page: int
    user: str
    total: int
    total_pages: int

    @staticmethod
    def from_dict(obj: Any) -> 'ToptracksAttr':
        assert isinstance(obj, dict)
        page = int(from_str(obj.get("page")))
        per_page = int(from_str(obj.get("perPage")))
        user = from_str(obj.get("user"))
        total = int(from_str(obj.get("total")))
        total_pages = int(from_str(obj.get("totalPages")))
        return ToptracksAttr(page, per_page, user, total, total_pages)

    def to_dict(self) -> dict:
        result: dict = {}
        result["page"] = from_str(str(self.page))
        result["perPage"] = from_str(str(self.per_page))
        result["user"] = from_str(self.user)
        result["total"] = from_str(str(self.total))
        result["totalPages"] = from_str(str(self.total_pages))
        return result


@dataclass
class Artist:
    url: str
    name: str
    mbid: str

    @staticmethod
    def from_dict(obj: Any) -> 'Artist':
        assert isinstance(obj, dict)
        url = from_str(obj.get("url"))
        name = from_str(obj.get("name"))
        mbid = from_str(obj.get("mbid"))
        return Artist(url, name, mbid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["url"] = from_str(self.url)
        result["name"] = from_str(self.name)
        result["mbid"] = from_str(self.mbid)
        return result


@dataclass
class TrackAttr:
    rank: int

    @staticmethod
    def from_dict(obj: Any) -> 'TrackAttr':
        assert isinstance(obj, dict)
        rank = int(from_str(obj.get("rank")))
        return TrackAttr(rank)

    def to_dict(self) -> dict:
        result: dict = {}
        result["rank"] = from_str(str(self.rank))
        return result


class Size(Enum):
    EXTRALARGE = "extralarge"
    LARGE = "large"
    MEDIUM = "medium"
    SMALL = "small"


@dataclass
class Image:
    size: Size
    text: str

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        assert isinstance(obj, dict)
        size = Size(obj.get("size"))
        text = from_str(obj.get("#text"))
        return Image(size, text)

    def to_dict(self) -> dict:
        result: dict = {}
        result["size"] = to_enum(Size, self.size)
        result["#text"] = from_str(self.text)
        return result


@dataclass
class Streamable:
    fulltrack: int
    text: int

    @staticmethod
    def from_dict(obj: Any) -> 'Streamable':
        assert isinstance(obj, dict)
        fulltrack = int(from_str(obj.get("fulltrack")))
        text = int(from_str(obj.get("#text")))
        return Streamable(fulltrack, text)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fulltrack"] = from_str(str(self.fulltrack))
        result["#text"] = from_str(str(self.text))
        return result


@dataclass
class Track:
    attr: TrackAttr
    duration: int
    playcount: int
    artist: Artist
    image: List[Image]
    streamable: Streamable
    mbid: str
    name: str
    url: str

    @staticmethod
    def from_dict(obj: Any) -> 'Track':
        assert isinstance(obj, dict)
        attr = TrackAttr.from_dict(obj.get("@attr"))
        duration = int(from_str(obj.get("duration")))
        playcount = int(from_str(obj.get("playcount")))
        artist = Artist.from_dict(obj.get("artist"))
        image = from_list(Image.from_dict, obj.get("image"))
        streamable = Streamable.from_dict(obj.get("streamable"))
        mbid = from_str(obj.get("mbid"))
        name = from_str(obj.get("name"))
        url = from_str(obj.get("url"))
        return Track(attr, duration, playcount, artist, image, streamable, mbid, name, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@attr"] = to_class(TrackAttr, self.attr)
        result["duration"] = from_str(str(self.duration))
        result["playcount"] = from_str(str(self.playcount))
        result["artist"] = to_class(Artist, self.artist)
        result["image"] = from_list(lambda x: to_class(Image, x), self.image)
        result["streamable"] = to_class(Streamable, self.streamable)
        result["mbid"] = from_str(self.mbid)
        result["name"] = from_str(self.name)
        result["url"] = from_str(self.url)
        return result


@dataclass
class Toptracks:
    attr: ToptracksAttr
    track: List[Track]

    @staticmethod
    def from_dict(obj: Any) -> 'Toptracks':
        assert isinstance(obj, dict)
        attr = ToptracksAttr.from_dict(obj.get("@attr"))
        track = from_list(Track.from_dict, obj.get("track"))
        return Toptracks(attr, track)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@attr"] = to_class(ToptracksAttr, self.attr)
        result["track"] = from_list(lambda x: to_class(Track, x), self.track)
        return result


@dataclass
class LastFm:
    toptracks: Toptracks

    @staticmethod
    def from_dict(obj: Any) -> 'LastFm':
        assert isinstance(obj, dict)
        toptracks = Toptracks.from_dict(obj.get("toptracks"))
        return LastFm(toptracks)

    def to_dict(self) -> dict:
        result: dict = {}
        result["toptracks"] = to_class(Toptracks, self.toptracks)
        return result


def last_fm_from_dict(s: Any) -> LastFm:
    return LastFm.from_dict(s)


def last_fm_to_dict(x: LastFm) -> Any:
    return to_class(LastFm, x)
