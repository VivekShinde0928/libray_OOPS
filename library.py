# Library
class Library:
    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.lend = {}                    # it is a dict in which book & name tracked to whom it owned at present

    def display_books(self):
        return f"\nAvailable books are {self.list_of_books} in library : {self.library_name}"

    def lend_books(self, book, user):
        if book not in self.lend.keys():
            self.lend.update({book:user})  #**update**
            print('your book updated, now u can take it')
        else:
            print(f"already taken by {self.lend[book]}")

    def add_books(self,book):
        self.list_of_books.append(book)

    def return_books(self,xxx):
        self.lend.pop(xxx)
        self.list_of_books.append(book)


if __name__ == '__main__':
    Vicky = Library(['english', 'maths', 'physics', 'chemistry', 'history', 'biology', 'astronauts'], "VivekLibrary")
    while True:
        user_input = input("Enter 1 to 'Display books', 2 to 'Lend Book', 3 to 'Add book', 4 to 'Return book' :")
        if user_input!='1' and user_input!='2' and user_input!='3' and user_input!='4' :
            print('Please enter correct integer')
            continue
        else:
            user_input = int(user_input)

        if user_input == 1:
            print(Vicky.display_books())

        elif user_input == 2:
            book = input('Enter book name :')
            user = input('Enter your name :')
            Vicky.lend_books(book, user)
            try :
                Vicky.list_of_books.remove(book)
            except:
                print(f"Only available these books : {Vicky.list_of_books}")

        elif user_input == 3:
            add = input("Add book to library ")
            Vicky.add_books(add)

        elif user_input == 4:
            ret = input("which book to return to library :")
            Vicky.return_books(ret)

        else:
            print('\nsomething went wrong')
        # x=''
        while True:
            x=input("Enter 'e' for exit or 'c' to continue :")
            if x == 'e':
                exit()
            elif x == 'c':
                break                            #breaks out of current loop



