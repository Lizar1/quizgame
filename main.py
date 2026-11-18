from data import Data

SCENES = {key.lower(): value for key, value in Data.items()}
START = "bedroom"

room = START

while True:
    scene = SCENES[room.lower()]
    print()

    if isinstance(scene, str):
        print(scene)
        if room == "victory":
            print("*** VICTORY ***")
        else:
            print("*** GAME OVER ***")

        print("1) Start over   2) Exit")
        if input("> ") == "1":
            room = START
            continue
        print("Thanks for playing!")
        break

    print(scene["text"])
    actions = scene["Actions"]
    for i in range(len(actions)):
        print(f"{i + 1}) {actions[i][0]}")

    choice = input("> ")
    if choice.isdigit() and 1 <= int(choice) <= len(actions):
        room = actions[int(choice) - 1][1]
    else:
        print("Please type one of the numbers above.")