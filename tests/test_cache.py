from src.cache_manager import CacheManager

CacheManager.init()

CacheManager.save_lrc(
    "那些花儿",
    "范玮琪",
    323,
    "[00:00]测试歌词"
)

content = CacheManager.load_lrc(
    "那些花儿",
    "范玮琪",
    323
)

print(content)