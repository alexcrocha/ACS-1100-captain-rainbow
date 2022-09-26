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
    checklist[index] = '√' + checklist[index]

def select(option):
    if option == "c":
        create(input("Input item > "))
    elif option == "r":
        valid_index = False
        while valid_index == False:
            item_index = int(input("Index Number? > "))
            if len(checklist) > item_index:
                valid_index = True
            else:
                print(f"Index has to be lower than {len(checklist)}")
        print(read(item_index))
    elif option == "u":
        index = int(input("Which index do you want to replace? > "))
        item = input("Which item would you like to add? > ")
        update(index, item)
    elif option == "v":
        valid_index = False
        while valid_index == False:
            item_index = int(input("Index Number? > "))
            if len(checklist) > item_index:
                valid_index = True
            else:
                print(f"Index has to be lower than {len(checklist)}")
        mark_complete(item_index)
    elif option == "a":
        list_all_items()
    elif option == "d":
        destroy(int(input("Which index do you want to delete? > ")))
    elif option == "q":
        return False
    return True


def user_input(prompt):
    user_input = input(prompt)
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


test()

running = True

while running:
    selection = user_input(
        "Select one of the following options:\nC to add to the list\nR to read the list\nU to update the list\nD to delete an item from the list\nV to mark an item complete\nA to list all items\nQ to exit\n"
    )
    running = select(selection)
