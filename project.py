class Lib:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def dispBooks(self):
        print(f"LIST OF BOOKS THAT WE HAVE ARE BELOW: {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    Sameer= Lib(['C++', 'THE_ALCHEMIST', 'DBMS_by_NAVATHE', 'PYTHON_Basics', 'ANALYSIS_OF_ALGORITHM'], "SAMEER")

    while(True):
        print(f"{Sameer.name} library welcoms you.Choose the option")
        print("1. Show Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            Sameer.dispxaBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            Sameer.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            Sameer.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            Sameer.returnBook(book)

        else:
            print("Not a valid option")


        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue

