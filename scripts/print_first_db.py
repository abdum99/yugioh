import json

if __name__ == "__main__":
    with open("./fetched.json", "r") as f:
        for line in f:
            data = json.loads(line)

        print("found this # of cards:", len(data["data"]))

        for i in range(5):
            print(data["data"][i])
