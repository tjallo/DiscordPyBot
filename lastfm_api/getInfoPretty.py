# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome_from_dict(json.loads(json_string))
import json
from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


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
class Registered:
    unixtime: int
    text: int

    @staticmethod
    def from_dict(obj: Any) -> 'Registered':
        assert isinstance(obj, dict)
        unixtime = int(from_str(obj.get("unixtime")))
        text = from_int(obj.get("#text"))
        return Registered(unixtime, text)

    def to_dict(self) -> dict:
        result: dict = {}
        result["unixtime"] = from_str(str(self.unixtime))
        result["#text"] = from_int(self.text)
        return result


@dataclass
class User:
    playlists: int
    playcount: int
    gender: str
    name: str
    subscriber: int
    url: str
    country: str
    image: List[Image]
    registered: Registered
    type: str
    age: int
    bootstrap: int
    realname: str

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        playlists = int(from_str(obj.get("playlists")))
        playcount = int(from_str(obj.get("playcount")))
        gender = from_str(obj.get("gender"))
        name = from_str(obj.get("name"))
        subscriber = int(from_str(obj.get("subscriber")))
        url = from_str(obj.get("url"))
        country = from_str(obj.get("country"))
        image = from_list(Image.from_dict, obj.get("image"))
        registered = Registered.from_dict(obj.get("registered"))
        type = from_str(obj.get("type"))
        age = int(from_str(obj.get("age")))
        bootstrap = int(from_str(obj.get("bootstrap")))
        realname = from_str(obj.get("realname"))
        return User(playlists, playcount, gender, name, subscriber, url, country, image, registered, type, age, bootstrap, realname)

    def to_dict(self) -> dict:
        result: dict = {}
        result["playlists"] = from_str(str(self.playlists))
        result["playcount"] = from_str(str(self.playcount))
        result["gender"] = from_str(self.gender)
        result["name"] = from_str(self.name)
        result["subscriber"] = from_str(str(self.subscriber))
        result["url"] = from_str(self.url)
        result["country"] = from_str(self.country)
        result["image"] = from_list(lambda x: to_class(Image, x), self.image)
        result["registered"] = to_class(Registered, self.registered)
        result["type"] = from_str(self.type)
        result["age"] = from_str(str(self.age))
        result["bootstrap"] = from_str(str(self.bootstrap))
        result["realname"] = from_str(self.realname)
        return result


@dataclass
class Welcome:
    user: User

    @staticmethod
    def from_dict(obj: Any) -> 'Welcome':
        assert isinstance(obj, dict)
        user = User.from_dict(obj.get("user"))
        return Welcome(user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["user"] = to_class(User, self.user)
        return result


def welcome_from_dict(s: Any) -> Welcome:
    return Welcome.from_dict(s)


def welcome_to_dict(x: Welcome) -> Any:
    return to_class(Welcome, x)
