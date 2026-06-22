# tests/test_netease.py

from src.netease_provider import NeteaseProvider


result = NeteaseProvider.search_song(
    "三百六十五里路"
)

print(result)