import json
import sys
import requests

CARDS_URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
SETS_URL = "https://db.ygoprodeck.com/api/v7/cardsets.php"

if __name__ == "__main__":
    print("Downloading cards from", CARDS_URL, end="...")
    sys.stdout.flush()
    resp = requests.get(url=CARDS_URL)
    if not resp:
        print()
        print("Couldn't download data. Check your internet connection")
        print(resp)
        raise "BAD"
    cards = resp.json()
    print("SUCCESS")

    with open("./res/db/cards.json", "w+") as f:
        f.write(json.dumps(cards))

    print("Downloading sets data from", SETS_URL, end="...")
    sys.stdout.flush()
    resp = requests.get(url=SETS_URL)
    if not resp:
        print()
        print("Couldn't download data. Check your internet connection")
        print(resp)
        raise "Network Error"
    print("SUCCESS")
    sets = resp.json()

    with open("./res/db/sets.json", "w+") as f:
        f.write(json.dumps(sets))

    
