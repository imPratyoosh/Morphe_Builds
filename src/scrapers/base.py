from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path

from bs4 import BeautifulSoup

from src.core.network import NetworkManager


def parse_html(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "html.parser")

@dataclass(slots=True, frozen=True)
class AppMetadata:
    pkg_name: str
    versions: list[str]

@dataclass(slots=True, frozen=True)
class DownloadResult:
    path: Path
    is_bundle: bool = False

class BaseScraper(ABC):
    def __init__(self, net: NetworkManager) -> None:
        self.net = net

    @abstractmethod
    def fetch_metadata(self, url: str) -> AppMetadata:
        pass

    @abstractmethod
    def download(self, url: str, version: str, dest: Path, arch: str, dpi: str) -> DownloadResult:
        pass