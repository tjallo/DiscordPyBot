# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = get_top_artists_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast
from uuid import UUID


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ArtistAttr:
    rank: int

    @staticmethod
    def from_dict(obj: Any) -> 'ArtistAttr':
        assert isinstance(obj, dict)
        rank = int(from_str(obj.get("rank")))
        return ArtistAttr(rank)

    def to_dict(self) -> dict:
        result: dict = {}
        result["rank"] = from_str(str(self.rank))
        return result


@dataclass
class Image:
    size: str
    text: str

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        assert isinstance(obj, dict)
        size = from_str(obj.get("size"))
        text = from_str(obj.get("#text"))
        return Image(size, text)

    def to_dict(self) -> dict:
        result: dict = {}
        result["size"] = from_str(self.size)
        result["#text"] = from_str(self.text)
        return result


@dataclass
class Artist:
    attr: ArtistAttr
    mbid: UUID
    url: str
    playcount: int
    image: List[Image]
    name: str
    streamable: int

    @staticmethod
    def from_dict(obj: Any) -> 'Artist':
        assert isinstance(obj, dict)
        attr = ArtistAttr.from_dict(obj.get("@attr"))
        mbid = UUID(obj.get("mbid"))
        url = from_str(obj.get("url"))
        playcount = int(from_str(obj.get("playcount")))
        image = from_list(Image.from_dict, obj.get("image"))
        name = from_str(obj.get("name"))
        streamable = int(from_str(obj.get("streamable")))
        return Artist(attr, mbid, url, playcount, image, name, streamable)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@attr"] = to_class(ArtistAttr, self.attr)
        result["mbid"] = str(self.mbid)
        result["url"] = from_str(self.url)
        result["playcount"] = from_str(str(self.playcount))
        result["image"] = from_list(lambda x: to_class(Image, x), self.image)
        result["name"] = from_str(self.name)
        result["streamable"] = from_str(str(self.streamable))
        return result


@dataclass
class TopartistsAttr:
    page: int
    total: int
    user: str
    per_page: int
    total_pages: int

    @staticmethod
    def from_dict(obj: Any) -> 'TopartistsAttr':
        assert isinstance(obj, dict)
        page = int(from_str(obj.get("page")))
        total = int(from_str(obj.get("total")))
        user = from_str(obj.get("user"))
        per_page = int(from_str(obj.get("perPage")))
        total_pages = int(from_str(obj.get("totalPages")))
        return TopartistsAttr(page, total, user, per_page, total_pages)

    def to_dict(self) -> dict:
        result: dict = {}
        result["page"] = from_str(str(self.page))
        result["total"] = from_str(str(self.total))
        result["user"] = from_str(self.user)
        result["perPage"] = from_str(str(self.per_page))
        result["totalPages"] = from_str(str(self.total_pages))
        return result


@dataclass
class Topartists:
    artist: List[Artist]
    attr: TopartistsAttr

    @staticmethod
    def from_dict(obj: Any) -> 'Topartists':
        assert isinstance(obj, dict)
        artist = from_list(Artist.from_dict, obj.get("artist"))
        attr = TopartistsAttr.from_dict(obj.get("@attr"))
        return Topartists(artist, attr)

    def to_dict(self) -> dict:
        result: dict = {}
        result["artist"] = from_list(lambda x: to_class(Artist, x), self.artist)
        result["@attr"] = to_class(TopartistsAttr, self.attr)
        return result


@dataclass
class GetTopArtists:
    topartists: Topartists

    @staticmethod
    def from_dict(obj: Any) -> 'GetTopArtists':
        assert isinstance(obj, dict)
        topartists = Topartists.from_dict(obj.get("topartists"))
        return GetTopArtists(topartists)

    def to_dict(self) -> dict:
        result: dict = {}
        result["topartists"] = to_class(Topartists, self.topartists)
        return result


def get_top_artists_from_dict(s: Any) -> GetTopArtists:
    return GetTopArtists.from_dict(s)


def get_top_artists_to_dict(x: GetTopArtists) -> Any:
    return to_class(GetTopArtists, x)
