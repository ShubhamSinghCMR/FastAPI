from threading import Lock
from typing import Set

_blacklist: Set[str] = set()
_lock = Lock()


def add_token_to_blacklist(token: str):
    with _lock:
        _blacklist.add(token)


def is_token_blacklisted(token: str) -> bool:
    with _lock:
        return token in _blacklist
