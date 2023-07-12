import requests
import sys
from time import sleep
import json

IMG_URL = "https://images.ygoprodeck.com/images/cards/"

if __name__ == "__main__":

    assert len(sys.argv) > 1, "Must call with set names from https://ygoprodeck.com/packs/"
    with open("res/db/sets2cards.json", "r") as f:
        for line in f:
            sets = json.loads(line)

        for sname in sys.argv[1:]:
            try:
                cards = sets[sname]
            except KeyError:
                print("Set [", sname, "] is not in the database. Refer to https://ygoprodeck.com/packs/ for set name. Capitalization and formatting matters for now. Sorry!")
                continue
            
            print("Set has", len(cards), "cards")
            print("Downloading card data and images...")

            num_downloaded = 0
            print(num_downloaded, "/", len(cards), end="\r")

            for i, card in enumerate(cards):
                # rate limit per https://ygoprodeck.com/api-guide/
                if i % 20 == 19:
                    sleep(1)

                try:
                    img = requests.get(card["card_images"][0]["image_url"])
                except KeyError:
                    print("Could not find image data for", card["name"])
                    continue
                except Exception as e:
                    print(e)
                    continue

                with open("res/img/" + str(card["id"]) + ".jpg", "wb+") as img_file:
                    img_file.write(img.content)

                num_downloaded += 1

                print(num_downloaded, "/", len(cards), end="\r")
            print()
            print("Done!")


