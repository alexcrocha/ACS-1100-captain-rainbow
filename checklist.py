import os

colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
clothes = ["left shoe", "right shoe", "pants", "belt", "top", "mask", "cape"]

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
    checklist[index] = "√" + checklist[index]


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
    elif option == "c":
        clear()
        print("Mark an item Complete")
        item_index = index_validation()
        mark_complete(item_index)
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

    list_all_items()


# test()

running = True

while running:
    clear()
    selection = user_input(
        "Select one of the following options:\nA to Add to the list\nR to Read the list\nU to Update the list\nD to Delete from the list\nC to mark an item Complete\nL to List all items\nQ to exit\n"
    )
    running = select(selection)
