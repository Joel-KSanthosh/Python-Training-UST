
from library_module import Book,Library,LibraryUser
from itertools import count

class Main:
    def __init__(self):
        self.library = Library()
        self.user_count = count(1, 1)
        self.book_count = count(1, 1)


    def main(self):
        print("User details : ")
        name = input("Enter user name : ")
        user = LibraryUser(self.user_count.__next__(),name)
        while True:
            print("[1]. Add Book\t[2]. Remove Book\t[3]. Search Book\t[4]. Display All Books\t[5]. Borrow Book\t"
                  "[6]. Return Book\t[7]. Exit")
            choice = int(input("Enter a choice : "))
            match choice:
                case 1:
                        title = input("Enter the book title : ")
                        author = input("Enter the book author : ")
                        book = Book(self.book_count.__next__(),title,author)
                        print(self.library.add_book(book))
                case 2:
                        book_id = int(input("Enter the book Id to delete : "))
                        print(self.library.remove_book(book_id))
                case 3:
                        title = input("Enter book title to search : ")
                        print(self.library.search_book(title))
                case 4:
                        books : list = list(self.library.display_all_books())
                        books.sort()
                        for book in books:
                            print("Options --> [1]. Next\t[2]. Exit")
                            try:
                                option = int(input("Choose an option : "))
                                if option == 1:
                                    print(book)
                                elif option == 2:
                                    break
                            except ValueError:
                                print("Enter a valid choice : ")
                                break
                        print("------END------")
                        print()


                case 5:
                        book_id = int(input("Enter the book Id to borrow : "))
                        print(user.borrow_book(self.library,book_id))
                case 6:
                        book_id = int(input("Enter the book Id to return : "))
                        print(user.return_book(self.library,book_id))
                case 7:
                        exit()
                case _:
                        print("Enter a valid choice : ")

if __name__ == '__main__':
    func = Main()
    func.main()
# if __name__ == '__main__':
#     run_library = Main()
#     run_library.main()
#         # book1 = Book(user_count.__next__(),"Harry Potter","J K Rowling")
#         # book