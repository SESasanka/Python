
lib = {"Harry Potter": 3, "The Hobbit": 2, "Pride and Prejudice": 5}

option = ["1", "2", "3", "4", "5", "6"]


def menu():
    print("Option 1 All Books are View")
    print("Option 2 Total Books Count")
    print("Option 3 Add New Book")
    print("Option 4 Borrow Book")
    print("Option 5 Return Book")
    print("Option 6 All Books and Qty View")


menu()
while True:

    option = input("Enter your option: ")

    def allBookView():

        for name in lib:
            print(f"{name}")

    def totalBooks():
        count = 0
        x = list(lib.values())
        for i in x:
            count += i
        print(f"Total Books are {count}")

    def addNewBook():
        while True:
            newBook = str(
                input("Add New Book (if new book add finished, Enter 0 ) : "))
            newBookQty = int(
                input("Add New Book Qty (if new book add Qty finished, Enter 0 ) : "))
            if newBook == str(0) and newBookQty == int(0):
                break
            lib.update({newBook: newBookQty})
            continue

    def getBooks():
        while True:
            nameBook = str(input("Enter Borrow Book Name : "))

            if nameBook in lib:
                borrow = int(input("Enter QTY : "))

                if borrow <= lib[nameBook]:
                    lib[nameBook] -= borrow
                    print(f"Borrowing process successful {borrow} books ")
                else:
                    print("Thre are no copies available right now")
                    nameBook = str(input("Enter Book Name : "))
                    borrow = int(input("Enter QTY : "))
                    if borrow <= lib[nameBook]:
                        lib[nameBook] -= borrow

            else:
                print("Sorry this book is not available in the library")

            for name, qty in lib.items():
                print(f"{name} : {qty}")

            if nameBook in lib:
                break

    def giveBooks():
        nameBook = str(input("Enter Return Book Name : "))
        if nameBook in lib:
            lib[nameBook] += 1
            print("Return book")
        else:
            print("Not Available")

        for name, qty in lib.items():
            print(f"{name} : {qty}")

    def allBooksAndQty():
        for name, qty in lib.items():
            print(f"{name} : {qty}")

    if option == "1":
        allBookView()
    if option == "2":
        totalBooks()
    if option == "3":
        addNewBook()
    if option == "4":
        getBooks()
    if option == "5":
        giveBooks()
    if option == "6":
        allBooksAndQty()
        break
