#Library Management System

class Library:
    def __init__(self,list,name):
        self.booksList=list
        self.name=name
        self.lendDict={ }
    def displayBooks(self):
        print(f"List of books available in our library {self.name} are")
        for books in self.booksList:
            print(books)

    def addBook(self,book):
        self.booksList.append(book)
        print("Book has been added successfully to the books list")

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book databse has been updated.You can take this book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]} ")

    def returnBook(self,book):
        self.booksList.remove(book)

if __name__ == '__main__':
    library=Library(['ComputerScience','Physics','Maths','Chemistry','English'],"Delhi Public")
    while (True):
        print(f"Welcome to {library.name} Library")
        print("Enter your choice to continue")
        print("1. Display books")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")

        user_choice=int(input())
        if user_choice==1:
            library.displayBooks()
        elif user_choice==2:
            book=input("Enter the name of book you want to lend : ")
            name=input("Enter your name : ")
            library.lendBook(name,book)
        elif user_choice==3:
            book=input("Enter the name of book you want to add : ")
            library.addBook(book)
        elif user_choice==4:
            book = input("Enter the name of book you want to return : ")
            library.returnBook(book)
        else:
            print("Invalid Choice")

        print("Press q to Quit or c to continue")
        user_choice1=" "
        while user_choice1!="q" and user_choice1!="c":
            user_choice1 = input()
            if user_choice1=="q":
                exit()
            elif user_choice1=="c":
                continue
