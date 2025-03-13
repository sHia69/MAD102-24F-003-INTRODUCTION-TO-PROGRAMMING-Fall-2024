class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def print_details(self):
        print(f"Book title: {self.title}, Author: {self.author}")

book1 = Book("1984", "George Orwell")

book1.print_details()

books = []

while True:
    title = input('Enter Book Title or type "q" to exit: ')
    if title == 'q':
        print("Goodbye!")
        break
    author = input('Enter Book Author: ')
    books.append(Book(title, author))
    
    for book in books:
        book.print_details()