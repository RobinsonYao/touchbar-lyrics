from src.netease_provider import NeteaseProvider


def main():

    song = NeteaseProvider.find_best_match(
        "三百六十五里路",
        "赵鹏"
    )

    print()
    print(song["id"])
    print(song["name"])
    print(song["artists"][0]["name"])
    print()


if __name__ == "__main__":
    main()