from getpass import getpass
import time
from helper_module2 import *
# from IPython.display import clear_output
# from IPython.display import Image
# from IPython.display import display

class Sign_in:
    def __init__(self):
        login= login()
        register= register()
        self.login = login
        self.register = register
    
    
    def login(email):
        #clear_output()
        password=getpass("Password: ")
        user = Auth.login_user(email, password) 
        return user
    
        
        
    def register():
        #clear_output()
        print("Registration:")
        email = input("Email: ")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        password = getpass("Password: ")
        
        user_dict={
            "email":email,
            "first_name":first_name,
            "last_name":last_name,
            "password":password
        }
      
    

class Display_book:
    def __init__(self):
        self.display_book_short = book_short

        def display_book_short(book):
            print(f"{book['id']} \t| {book['title'][:50].ljust(50)} | \t{book['subject']}")
        book_short= display_book_short()

#         def display_book_long(book):
#             cover = Image(url=book['img'])
#             display(cover)
#             print(f'''
# Title:\t {book['title']}
# Author: {book['author']}
# Pages:\t {book['pages']}
# Subject: {book['subject']}
# Summary: {book['summary']}
# ''')


class ReadingList():
    def __init__(self):
        self.reading_list=[]
        
    def add_book(self, book):
        if book not in self.reading_list:
            self.reading_list.append(book)
    
    def remove_book(self, book):
        self.reading_list.remove(book)
    
    def empty(self):
        self.reading_list=[]
    
    def show_book_list(self):
        #clear_output()
        if not self.reading_list:
            print("Your reading list is empty")
        for book in self.reading_list:
            print(f'''
{"="*50}            
\n
Title:\t {book['title']}
Book ID: {book['id']}
Author:\t {book['author']}
Subject: {book['subject']}
Summary: {book['summary']}
\n
{"="*50}            
\n
''')

class Get_book():
    def __init__(self):
        get_books = get_books()
        get_category_list = get_category_list()
        get_book_by_category = get_book_by_category()
        get_single_book = get_single_book()
       
        self.get_books= get_books
        self.get_category_list= get_category_list
        self.get_book_by_category= get_book_by_category
        self.get_single_book= get_single_book

    def get_books():
        books = requests.get(url+endpoint_book)
        return books.json()['books']


    def get_category_list(books):
        return {book['subject'].title() for book in books}
    

    def get_book_by_category(books, category):
        return list(filter(lambda book: book['subject'].title()==category.title(),books))
    

    def get_single_book(book_id):
        single_book = requests.get(url+endpoint_book +'/'+str(book_id))
        return single_book.json()
    


def browse_books(books, reading_list, subject=None):
    while True:
        #clear_output()
        print(f'''
Welcome to the Book Browser
You are viewing {subject if subject else 'all'} books
[ID] \t| {"[TITLE]".ljust(50)} | [SUBJECT]
        ''')
        if subject:
            books=Get_book.get_book_by_category(books, subject)
        for book in books:
            Display_book.display_book_short(book)

        selection = input("Select you book by ID [BACK to back out]")
        if selection.lower()=='back':
            return
        elif selection.isnumeric() and int(selection) in map(lambda book: book['id'], books):
            selection=int(selection)
            while True:
                print(f'''
You Selected: {list(filter(lambda book: book['id'] == selection, books))[0]['title']}
1. Add Book To Reading List
2. View More Information
3. Go Back
4. Go To Main Menu
''')
                action = input("Action: ")
                if action =="1":
                    reading_list.add_book(list(filter(lambda book: book['id']==selection, books))[0])
                    print("As you wish")
                    time.sleep(1)
                    break
                elif action =="2":
                    #clear_output()
                    Display_book.display_book_long(list(filter(lambda book: book['id']==selection, books))[0])
                    input("Press Enter To Continue")
                elif action=="3":
                    break
                elif action=="4":
                    return
                    
        else:
            print("Invalid ID")
            time.sleep(2)
            continue