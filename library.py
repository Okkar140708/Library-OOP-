class Book:
    # write a constructor to initialize the attributes for Book class
    def __init__ (self, Title, Author, Release_Year, ISBN, Genre, Available_Copies):
        self.Title = Title 
        self.Author = Author
        self.Release_Year = Release_Year
        self.ISBN = ISBN
        self.Genre = Genre
        self.Available_Copies = Available_Copies

    # function to properly display when we print
    def __str__(self) :
        return (f"Title : {self.Title}\n"
                f"Author : {self.Author}"
                f"Release Year: {self.Release_Year}\n"
                f"ISBN: {self.ISBN}\n"
                f"Genre: {self.Genre}\n"
                f"Available Copies: {self.Available_Copies}\n")
    
    # function to compare books based on ISBN
    def __eq__(self, other ):
        if isinstance(other, Book): # check if 'other' is a book instance
            return self.ISBN == other.ISBN
        return False # return False if not 'other' is a book instance

#start the E-Book class
class eBooks(Book):
    # put the same attribute as Book class
    def __init__(self, Title, Author, Release_Year, ISBN, Genre, narrator, Available_Copies = None ):
        super().__init__(Title, Author, Release_Year, ISBN, Genre, Available_Copies)
        self.narrator = narrator
    
    # string representation of ebook
    def __str__(self):
        return super().__str__() + f"\n Narrator: {self.narrator}"

# start the library class
class library:
    # write a constructor to initialize the attributes for library class
    def __init__(self, book_list=None, room_list=None):
        if book_list is None: # start as empty list if none
            book_list = []
        if room_list is None: # start as empty list if none
            room_list = []
        self.book_list = book_list
        self.room_list = room_list
    
    # add a book to library
    def add_book(self,book):
        for added_book in self.book_list:
            if added_book == book:
                added_book.Available_Copies += 1
                print(f"Copies of {book.Title} increased to {added_book.Available_Copies}")
                return
            
        #if book not found add to current list
        self.book_list.append(book)
        print(f"Added {book.Title} to the library with {book.Available_Copies} copies.")
        
    
    # function for search titles
    def search_title(self, title):
        for book in self.book_list:
            if book.Title.lower() == title.lower(): # search for a book by its title
                return str(book)
        return "Book not found!"
        
    # function for search ISBN
    def search_ISBN(self, ISBN):
        for book in self.book_list:
            if book.ISBN == ISBN: # search for a book by its ISBN
                return book
        return "Book not found!"
    
    # function for searching authors
    def search_author(self, Author):
        author_books = [] # create a list for authors's book
        for book in self.book_list: # loop through the books list
            if book.Author == Author: # check if the book's author matches the given author
                author_books.append(book.Title)
                
        if author_books: # check if any book were found
            return author_books
            
        return "Book not found!"
    
    # A __str__ function that displays the list of books the library has in alphabetical order based on title
    def __str__(self):
        sorted_books = sorted(self.book_list, key=lambda book: book.Title)
        return "\n".join([str(book) for book in sorted_books])
        
        

    # A checkout_book function which takes ISBN as input
    def check_out(self, ISBN):
        for book in self.book_list:
            if book.ISBN == ISBN:
                if book.Available_Copies > 0: # check if there is available copy
                    book.Available_Copies -= 1 # decrease the available copy by 1
                    return f"{book.Title} has successfully checked out!!"
                else:
                    return "The book you wanna take out is unavailable!"
                
        return "Book not found!!"
    
    # return function which takes 
    def return_book(self, ISBN):
        for book in self.book_list:
            if book.ISBN == ISBN:
                if book.Available_Copies is not None: # Check if copies exist, avoiding None check
                    book.Available_Copies += 1 # increase the availabe copy by 1
                    return f"{book.Title} has successfully returned!!"
                else:
                    return "Opps. There was an error returning your book!\n Contact our information centre for this issues"
        
        return "Book not found!"
    
    # function to add a room to the list of rooms that can be reserved
    def add_room(self,room):
        self.room_list.append(room)
    
    # function to display a list of all available rooms in the library
    def display_room(self):
        return self.room_list
    
    # a reserved room function which takes a room off the list of possible rooms to be reserved
    def reserve_room(self,room):
        if room in self.room_list:
            self.room_list.remove(room)
            return f"Room {room} has been successfully reserved!"
        else:
            return f"Opps! Room {room} is not available at the moment."
        
    # A unreserve_room function which adds a room back to the list of possible rooms to be reserved
    def unserved_room(self,room):
        if room not in self.room_list:
            self.room_list.append(room)
            return f"Room {room} has been added to the unreserved room list."
        else:
            return f"Invalid!!\nRoom {room} is not reserved"
        
# start a Person class
class Person:
    def __init__(self,name,Age,checked_out_book,reserved_room): # initialize the attributes
        self.name = name
        self.Age = Age
        self.checked_out_book = checked_out_book
        self.reserved_room = reserved_room
    
    # a function to diaplay about a person
    def __str__(self):
        return (f"Name : {self.name}\n"
                f"Age: {self.Age}\n"
                f"The book that a reader checked out : {self.checked_out_book}\n"
                f"The room that a reader reserved : {self.reserved_room}")
    
    # a function for checking out a book
    def checkout_book(self,books,library):
        
        # check if a person can only reserve 5 times STILL NEED THIS
        if len(self.checked_out_book) >= 5:
            return "You can not check out more than 5 times!"
        
        # check all required books 
        for book in books:  
            if book in library.book_list: # check for book that user requests in available library book lists
                if book.Available_Copies > 0: # check if there is available book
                    if book.Genre.lower() == 'mature': # check if the genre is mature
                        if self.Age > 16: # check if the reader is over 16
                            book.Available_Copies -= 1 # decrease the copies by 1
                            if book not in self.checked_out_book:
                                self.checked_out_book.append(book) # a kinda list for books that a reader checked out
                                return "You can check out this book!"
                        else:
                            return "You are too young to read this sort of books."
                    else:
                        book.Available_Copies -= 1 # decrease the copies by 1
                        if book not in self.checked_out_book:
                            self.checked_out_book.append(book) # a kinda list for books that a reader checked out
                        return "The book has sucessfully checked out"
                        
                else:
                    return "There is not available copies for the book you requested!"
            else:
                return "Sorry the book you requested is not available in this library"

    # a function that returns a specific book to a specific library
    def returnbook(self, book, library):
        if book in self.checked_out_book:  # check if the person borrowed this book
            if book in library.book_list:  # check if the book is from the library
                book.Available_Copies += 1  # increase the available copies
                self.checked_out_book.remove(book)  # remove the book from the person's borrowed list
                print("You have successfully returned to the library. Thanks for borrowing!")
            else:
                print("The book you are returning does not belong to this library.")
        else:
            print("You did not borrow this book!")

    # A function which reserves a room from a library if there is any available rooms
    def reserve_room_for_people(self,room,library):
        if self.reserved_room is not None: # check if a person has already reserved a room
            print("You can only use one room at one time.")
        else: # if a person has not reserved a room
            if room in library.room_list:
                library.reserve_room(room) # reserve the room using the library's method
                self.reserved_room = room # assign the room to the person
            else:
                print("The room is not available")
    # this function is showing only the first print statement

    # A function which takes off he reservation on a specific room from a specific library
    def unreserve_room_for_people(self,room,library):
        if self.reserved_room is not None:  # Check if the person has a room reserved
            library.unserved_room(self.reserved_room)  # Add the room back to the library's list of available rooms
            print(f"Room {self.reserved_room} has been unreserved.")
            self.reserved_room = None  # Clear the person's reservation
        else:
            print("You don't have any room reserved to unreserve.")

# a sub class, Student from Parent class,Person class
class Student(Person):
    def __init__(self,name,Age,checked_out_book,reserved_room,student_number): # initialize the attributes
        self.name = name
        self.Age = Age
        self.checked_out_book = checked_out_book
        self.reserved_room = reserved_room
        self.student_number = student_number

    def checkout_book(self, books, library):
        # Modify the condition to allow up to 10 books
        if len(self.checked_out_book) > 10:
            return "You can not check out more than 10 times!"

# Create some book instances
book1 = Book("1984", "George Orwell", 1949, "1234567890", "Dystopian", 5)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "1234567891", "Fiction", 3)
book3 = eBooks("The Great Gatsby", "F. Scott Fitzgerald", 1925, "1234567892", "Fiction", "Jake Gyllenhaal", 2)
book4 = Book("Moby Dick", "Herman Melville", 1851, "456789012", "Fiction", 4)
book5 = Book("Pride and Prejudice", "Jane Austen", 1813, "567890123", "Fiction", 1)
book6 = Book("War and Peace", "Leo Tolstoy", 1869, "678901234", "Fiction", 4)


# Create a library instance
my_library = library()

# Add books to the library
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)
my_library.add_book(book4)
my_library.add_book(book5)
my_library.add_book(book6)

# # Display the library's book list
# print(my_library)

# # Search for a book by title
# print(my_library.search_title("1984"))

# # Search for a book by ISBN
# print(my_library.search_ISBN("1234567891"))

# # Search for books by author
# print(my_library.search_author("Harper Lee"))

# Checkout a book and check if caanot borrow 5 books at the time
person = Person("Alice", 20, [], None)
print(person.checkout_book([book6], my_library))
print(person.checkout_book([book5], my_library))
print(person.checkout_book([book4], my_library))
print(person.checkout_book([book3], my_library))
print(person.checkout_book([book2], my_library))
print(person.checkout_book([book1], my_library))

# Display the updated library's book list
print(my_library)

# Return a book
print(person.returnbook(book1, my_library))

# Reserve a room
my_library.add_room("Study Room 1")
person.reserve_room_for_people("Study Room 1", my_library)

# Display reserved room
print(person.reserved_room)

# Unreserve the room
person.unreserve_room_for_people("Study Room 1", my_library)

# Check the status after unreserving the room
print(person.reserved_room)

# Create a Student instance and check out books
student = Student("Bob", 18, [], None, "S123456")
print(student.checkout_book([book2, book3], my_library))

# Attempt to checkout more than allowed books
print(student.checkout_book([book1, book3], my_library))

print("Auf Wiedersehen")