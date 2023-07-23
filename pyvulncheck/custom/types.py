from typing import TypedDict, Optional

class Package(TypedDict):
    name: str
    version: str


class VersionKey(TypedDict):
    system: str
    name: str
    version: str


class Advisory(TypedDict):
    id: str


class Link(TypedDict):
    label: str
    url: str


class GetVersionAPIResponse(TypedDict):
    versionKey: list[VersionKey]
    isDefault: bool
    licenses: list[Optional[str]]
    advisoryKeys: list[Advisory]
    links: list[Link]
    publishedAt: str


class GetAdvisioryAPIResponse(TypedDict):
    advisoryKey: Advisory
    url: str
    title: str
    aliases: list[Optional[str]]
    cvss3Score: int
    cvss3Vector: str
    