import json

if __name__ == "__main__":

    cards = {}
    sets2cards = {}
    # load .json to data
    with open("./res/db/fetched.json", "r") as f:
        for line in f:
            cards = json.loads(line)["data"]

    no_set_count = 0

    for card in cards:
        try:
            for card_set in card["card_sets"]:
                set_code = card_set["set_name"]
                if not set_code in sets2cards:
                    sets2cards[set_code] = []

                card_no_set = card.copy()
                del card_no_set["card_sets"]

                sets2cards[set_code].append(card_no_set)
        except KeyError:
            no_set_count += 1

    print("#sets= ", len(sets2cards))
    print("Found sets for", (len(cards) - no_set_count), "cards out of", len(cards), "cards")

    with open("./res/db/sets2cards.json", "w+") as f:
        f.write(json.dumps(sets2cards))

    sets = {}
    with open("./res/db/sets.json") as f:
        for line in f:
            sets = json.loads(line)

    print("Gathered cards for", len(sets2cards), "sets out of", len(sets), "known")

    for s in sets:
        sname = s["set_name"]
        if not sname in sets2cards:
            print("Set [", sname, "] is not in the database")
            continue

        if len(sets2cards[sname]) < s["num_of_cards"]:
            print("Set [", sname, "] only has", len(sets2cards[sname]), "out of", s["num_of_cards"], "known")



