import json
import requests
import base64
from getpass import getpass
from getpass import getpass
import time
from helper_module2 import *

url = 'https://cae-bootstore.herokuapp.com'

endpoint_login = "/login"
endpoint_user = "/user"
endpoint_book = "/book"

class Auth:
    def __init__(self):
        register_user = register_user()
        login_user = login_user()
        edit_user = edit_user()
        delete_user = delete_user()

        self.register_user = register_user
        self.login_user = login_user
        self.edit_user = edit_user
        self.delete_user = delete_user

    def register_user(payload):
        payload_json_string = json.dumps(payload)
        headers = {
            'Content-Type':'application/json'
        }
        response = requests.post(
            url + endpoint_user,
            data = payload_json_string,
            headers = headers
        )
        return response.text
       

    def login_user(user_name, password):
        auth_string = user_name + ":" + password
        
        headers={
            'Authorization' : "Basic "+base64.b64encode(auth_string.encode()).decode()
        }
        
        user_data = requests.get(
            url + endpoint_login,
            headers=headers
        )
        return user_data.json()
    

    def edit_user(token, payload):
        payload_json_string = json.dumps(payload)
        headers={
            'Content-Type':'application/json',
            'Authorization':'Bearer ' + token
        }
        response = requests.put(
            url + endpoint_user,
            data=payload_json_string,
            headers=headers
        )
        return response.text
    

    def delete_user(token):
        headers = {
            'Authorization':"Bearer " + token
        }
        
        response = requests.delete(
            url+endpoint_user,
            headers=headers
        )
        return response.text
        

# class Sign_in:
#     def __init__(self):
#         self.login = logi
#         self.register = regi
        
        

#         def login(email):
#             #clear_output()
#             password=getpass("Password: ")
#             user = Auth.login_user(email, password) 
#             return user
#         logi= login()
        
#         def register():
#             #clear_output()
#             print("Registration:")
#             email = input("Email: ")
#             first_name = input("First Name: ")
#             last_name = input("Last Name: ")
#             password = getpass("Password: ")
            
#             user_dict={
#                 "email":email,
#                 "first_name":first_name,
#                 "last_name":last_name,
#                 "password":password
#             }
#             return Auth.register_user(user_dict)
#         regi= register()