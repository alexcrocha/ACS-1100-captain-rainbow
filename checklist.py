from tabnanny import check


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


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    # print(read(1))


test()


def select(option):
    if option == "c":
        create(input("Which item would you like to add? > "))
    elif option == "r":
        print(read(int(input("Which index? > "))))
    elif option == "u":
        index = int(input("Which index do you want to replace? > "))
        item = input("Which item would you like to add? > ")
        update(index, item)
    elif option == "d":
        destroy(int(input("Which index do you want to delete? > ")))
    elif option == "q":
        return False
    return True


running = True

while running:
    selection = input(
        "Select one of the following options:\nC to add to the list\nR to read the list\nU to update the list\nD to delete an item from the list\nQ to exit\n"
    )
    running = select(selection)
