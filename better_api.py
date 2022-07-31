from helper_module import *
from helper_module2 import *
from getpass import getpass
import time
# from helper_module2 import *
# from IPython.display import clear_output
# from IPython.display import Image
# from IPython.display import display


def main():
    reading_list = ReadingList()
    
    
    
    while True:
        #clear_output()
        print("Welcome to the Bookstore")
        email = input("Type your email to login or Type `register` to Register ")
        if email == 'register':
            success_register=Sign_in.register()
            if success_register:
                print("You have successfully registered")
                continue
        elif email.lower() == "quit":
            print("Goodbye")
            break
        else:
            try:
                Sign_in.login(email)
            except:
                print("Invalid Username/Password combo")
                time.sleep(2)
                continue
        # First Scene of our app (above)
        while True:
            #lear_output()
            print("""
Welcome to the Repository            
You can:            
1. Browse All Books
2. Browse Book by Category
3. View Reading List
4. Remove Book From Reading List
5. Delete A User
6. Edit User
7. Quit     
""")
            command = input("Select your Fate: ")
            if command == "1":
                browse_books(Get_book.get_books, reading_list)
            elif command == "2":
                while True:
                    print(" | ".join(Get_book.get_category_list(Get_book.get_books)))
                    cat = input("Category: ").title()
                    if cat in Get_book.get_category_list(Get_book.get_books):
                        browse_books(Get_book.get_books, reading_list, cat)
                        break
                    print("Invalid Category")
                    time.sleep(2)
                    continue
            elif command == "3":
                reading_list.show_book_list()
                input("Press Enter To Return")
                continue
            elif command == "4":
                while True:
                    #clear_output()
                    reading_list.show_book_list()
                    garbage = input("What book ID would you like to remove? [BACK to back out]")
                    if garbage.lower() == "back":
                        break
                    elif garbage.isnumeric() and int(garbage) in map(lambda book: book['id'], reading_list.reading_list):
                        reading_list.remove_book(list(filter(lambda book: book['id']==int(garbage), reading_list.reading_list))[0])
                        print(f'{garbage} has been removed')
                        time.sleep(2)
                        break
                    else:
                        print(f'{garbage} is not in your collection')
                        time.sleep(2)
                        break
                continue
            elif command == "5":
                while True:
                    #clear_output()
                    print("You have have chosen to delete a user")             
                    Auth.delete_user(Sign_in.register)
                    break
            elif command == "6":
                while True:
                    #clear_output()
                    print("You have have chosen to edit a user")             
                    Auth.edit_user(Sign_in.register)
                    break
                                    
            elif command == "7":
                print("Goodbye")
                break
            else:
                print("Invalid Selection")
                time.sleep(2)
                continue
        break

main()