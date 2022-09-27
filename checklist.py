import os
import random

colours = [
    "\x1B[38;2;244;53;69mred",
    "\x1B[38;2;250;137;1morange",
    "\x1B[38;2;250;215;23myellow",
    "\x1B[38;2;0;186;113mgreen",
    "\x1B[38;2;0;194;222mblue",
    "\x1B[38;2;0;65;141mindigo",
    "\x1B[38;2;95;40;121mviolet",
]

clothes = ["left shoe", "right shoe", "pants", "belt", "shirt", "mask", "cape"]

checklist = list()


def create(item):
    checklist.append(item)


def read(index):
    return checklist[index]


def update(index, item):
    checklist[index] = item


def destroy(index):
    checklist.pop(index)


def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1


def mark_complete(index):
    checklist[index] = "√ " + checklist[index]


# * Add function that un-checks a checked item in the list.
def unmark_complete():
    index = 0
    valid_indexes = []
    for list_item in checklist:
        if "√" in list_item:
            print("{} {}".format(index, list_item))
            valid_indexes.append(index)
        index += 1
    if len(valid_indexes) > 0:
        valid_index = False
    else:
        print("There are no completed items")
        input("Press Enter to continue...")
        return
    while valid_index == False:
        item_index = int(input("Index Number? > "))
        if item_index in valid_indexes:
            valid_index = True
            checklist[item_index] = checklist[item_index][2:]
        else:
            print(f"Index not valid")


def generate_combination():
    if len(clothes) > 0:
        random_colour = random.choice(colours)
        colours.remove(random_colour)
        random_clothing = random.choice(clothes)
        clothes.remove(random_clothing)
        create(f"{random_colour} {random_clothing}\u001b[0m")
    else:
        print("Wardrobe is full")
        input("Press Enter to continue...")


def generate_wardrobe():
    if len(clothes) > 0:
        while len(clothes) > 0:
            generate_combination()
        list_all_items()
        input("Press Enter to continue...")
    else:
        print("Wardrobe is full")
        input("Press Enter to continue...")


def index_validation():
    list_all_items()
    valid_index = False
    while valid_index == False:
        item_index = int(input("Index Number? > "))
        if len(checklist) > item_index:
            valid_index = True
        else:
            print(f"Index has to be lower than {len(checklist)}")
    return item_index


def clear():
    os.system("cls||clear")


def select(option):
    if option == "a":
        clear()
        print("Add to the list")
        create(input("Input item > "))
    elif option == "r":
        clear()
        print("Read the list")
        item_index = index_validation()
        print(read(item_index))
        input("Press Enter to continue...")
    elif option == "u":
        clear()
        print("Update the list")
        item_index = index_validation()
        item = input("Which item would you like to add? > ")
        update(item_index, item)
    elif option == "g":
        clear()
        print("Generate an item combination")
        generate_combination()
    elif option == "w":
        clear()
        print("Generate whole Wardrobe")
        generate_wardrobe()
    elif option == "m":
        clear()
        print("Mark an item complete")
        item_index = index_validation()
        mark_complete(item_index)
    elif option == "n":
        clear()
        print("Mark a completed item Not complete")
        unmark_complete()
    elif option == "l":
        clear()
        print("List all items")
        list_all_items()
        input("Press Enter to continue...")
    elif option == "d":
        clear()
        print("Delete from the list")
        item_index = index_validation()
        destroy(item_index)
    elif option == "q":
        return False
    return True


def user_input(prompt):
    user_input = input(prompt).lower()
    return user_input


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))

    select("c")

    list_all_items()

    select("r")

    select("g")

    select("w")

    list_all_items()


# test()

running = True

while running:
    clear()
    # Weird indentation below due to """ terminal output
    # I am not a fan of it, I will probably do it differently next time
    selection = user_input(
        """Select an option:
A to Add to the list
R to Read the list
U to Update the list
D to Delete from the list
G to Generate an item combination
W to generate whole Wardrobe
M to mark an item Complete
N to mark a completed item Not complete
L to List all items
Q to Quit
> """
    )
    running = select(selection)
