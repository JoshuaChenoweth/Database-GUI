import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

# MYSQL parameters
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Joshua092003",
    database="warehouse1"
)
# uses the established connection to connect to user login information on the database.
def authenticate_user(username, password):
    if db:
        try:
            cursor = db.cursor()

            # Check if the user is in Guest_User table
            query_guest = "SELECT * FROM Guest_User WHERE Guest_User_Name = %s AND Guest_password = %s"
            cursor.execute(query_guest, (username, password))
            result_guest = cursor.fetchone()

            if result_guest:
                return "guest"

            # Check if the user is in Admin_User table
            query_admin = "SELECT * FROM Admin_User WHERE Admin_User_Name = %s AND Admin_password = %s"
            cursor.execute(query_admin, (username, password))
            result_admin = cursor.fetchone()

            if result_admin:
                return "admin"
            #error handling
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            cursor.close()

    return None
# defines the login process function
def login():
    #gets the username and password from the database
    username = entry_username.get()
    password = entry_password.get()
    # Throws an error if the user tries to submit a login when one or more of the text boxes are blank
    if username == "" or password == "":
        messagebox.showinfo("", "Username and password cannot be blank.")
    else:
        # Authenticate the user against the database
        user_type = authenticate_user(username, password)
        #if the user is a guest they are logged into the traditional main menu
        if user_type == "guest":
            messagebox.showinfo("", "Guest Login successful")
            show_main_menu()
        #if the user is an admin then they are logged into the admin version of the main menu
        elif user_type == "admin":
            messagebox.showinfo("", "Admin Login successful")
            show_main_menu(admin=True)

        else:
            messagebox.showinfo("", "Incorrect username or password")

def show_main_menu(admin=False):
    #creates the main menu 
    for widget in window.winfo_children():
        widget.destroy()

    # segment creates the framework for the main menu's design
    main_menu_frame = tk.Frame(window, padx=400, pady=400, bg='#a6e3e9')  # Set the background color
    main_menu_frame.pack(fill=tk.BOTH, expand=True)

    # Creates the main menu title
    label_menu = tk.Label(main_menu_frame, text="Main Menu", font=("Arial", 25), bg='blue', fg='white')  # Set background and text color
    label_menu.grid(row=0, column=0, columnspan=2, pady=10)

    # below are the buttons for the action pages provided for the user
    btn_insert = tk.Button(main_menu_frame, text="Insert", command=insert_function, width=15, height=2, font=("Arial", 12))
    btn_insert.grid(row=1, column=0, pady=20, padx=(0, 20))

    btn_delete = tk.Button(main_menu_frame, text="Delete", command=remove_function, width=15, height=2, font=("Arial", 12))
    btn_delete.grid(row=1, column=1, pady=20, padx=(20, 0))

    btn_modify = tk.Button(main_menu_frame, text="Modify", command=modify_function, width=15, height=2, font=("Arial", 12))
    btn_modify.grid(row=2, column=0, pady=20, padx=(0, 20))

    btn_search = tk.Button(main_menu_frame, text="Search", command=search_function, width=15, height=2, font=("Arial", 12))
    btn_search.grid(row=2, column=1, pady=20, padx=(20, 0))

    btn_print = tk.Button(main_menu_frame, text="Print", command=print_item_details, width=15, height=2, font=("Arial", 12))
    btn_print.grid(row=3, column=0, pady=20, padx=(0, 20))

    btn_about_us = tk.Button(main_menu_frame, text="About Us", command=about_us, width=15, height=2, font=("Arial", 12))
    btn_about_us.grid(row=4, column=1, pady=20, padx=(20, 0))
    #If the user is a guest they will have access to a button that will allow them to change their password
    if not admin:
        btn_update_password = tk.Button(main_menu_frame, text="Update Password", command=show_update_password_window, width=15, height=2, font=("Arial", 12))
        btn_update_password.grid(row=3, column=1, pady=20, padx=(20, 0))

    # if the user is logged in as an admin then they will have access to the user administration framework to manipulate the guest users
    if admin:
        btn_user_admin = tk.Button(main_menu_frame, text="User Administration", command=user_admin_function, width=15, height=2, font=("Arial", 12))
        btn_user_admin.grid(row=3, column=1, pady=20, padx=(20, 0))

    # Create a label for the "navigation" text
    label_warehouse = tk.Label(main_menu_frame, text="Navigation", font=("Arial", 40, "bold"), bg='blue', fg='yellow')  # Set background and text color
    label_warehouse.grid(row=5, column=0, columnspan=2, pady=20)

    # takes the main menu frame and centers it on the page
    main_menu_frame.pack_propagate(False)
    main_menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def show_update_password_window():
    # Create a new window for updating the guest user's password
    update_password_window = tk.Toplevel(window)
    update_password_window.title("Update Password")
    update_password_window.geometry('800x600')
    update_password_window.configure(bg='#a6e3e9') 

    # Label and Entry for guest username
    label_username = tk.Label(update_password_window, text="Guest Username:")
    label_username.grid(row=0, column=0, padx=200, pady=10)
    entry_username = tk.Entry(update_password_window)
    entry_username.grid(row=0, column=1, padx=10, pady=10)

    # Label and Entry for new password
    label_password = tk.Label(update_password_window, text="New Password:")
    label_password.grid(row=1, column=0, padx=10, pady=10)
    entry_password = tk.Entry(update_password_window, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=10)

    # Button to update password
    btn_update_password = tk.Button(update_password_window, text="Update Password", command=lambda: update_guest_password(entry_username.get(), entry_password.get()))
    btn_update_password.grid(row=2, column=0, padx=10, pady=10)

    # Button to return to the main menu
    btn_return = tk.Button(update_password_window, text="Return to Main Menu", command=update_password_window.destroy)
    btn_return.grid(row=3, column=0, padx=10, pady=10)

    
def insert_function():
    # Create a new window for item insertion
    insert_window = tk.Toplevel(window)
    insert_window.title("Insert Item")
    insert_window.geometry('800x600') 
    insert_window.configure(bg='#a6e3e9') 
      # Set the background color to baby blue


    # Label and Entry for item ID
    label_item_id = tk.Label(insert_window, text="Item ID:")
    label_item_id.grid(row=1, column=0,padx=200, pady=10)
    entry_item_id = tk.Entry(insert_window)
    entry_item_id.grid(row=1, column=1, padx=10, pady=10)

    # Label and Entry for item name
    label_item_name = tk.Label(insert_window, text="Item Name:")
    label_item_name.grid(row=2, column=0, padx=10, pady=10)
    entry_item_name = tk.Entry(insert_window)
    entry_item_name.grid(row=2, column=1, padx=10, pady=10)

    # Label and Entry for supplier ID
    label_supplier_id = tk.Label(insert_window, text="Supplier ID:")
    label_supplier_id.grid(row=3, column=0, padx=10, pady=10)
    entry_supplier_id = tk.Entry(insert_window)
    entry_supplier_id.grid(row=3, column=1, padx=10, pady=10)

    # Label and Entry for height
    label_height = tk.Label(insert_window, text="Height:")
    label_height.grid(row=4, column=0, padx=10, pady=10)
    entry_height = tk.Entry(insert_window)
    entry_height.grid(row=4, column=1, padx=10, pady=10)

    # Label and Entry for weight
    label_weight = tk.Label(insert_window, text="Weight:")
    label_weight.grid(row=5, column=0, padx=10, pady=10)
    entry_weight = tk.Entry(insert_window)
    entry_weight.grid(row=5, column=1, padx=10, pady=10)

    # Label and Entry for stored time
    label_stored_time = tk.Label(insert_window, text="Stored Time:")
    label_stored_time.grid(row=6, column=0, padx=10, pady=10)
    entry_stored_time = tk.Entry(insert_window)
    entry_stored_time.grid(row=6, column=1, padx=10, pady=10)

    # Label and Entry for type of item
    label_type_of_item = tk.Label(insert_window, text="Type of Item:")
    label_type_of_item.grid(row=7, column=0, padx=10, pady=30)
    entry_type_of_item = tk.Entry(insert_window)
    entry_type_of_item.grid(row=7, column=1, padx=10, pady=10)

    # Label and Entry for storage condition
    label_storage_condition = tk.Label(insert_window, text="Storage Condition:")
    label_storage_condition.grid(row=8, column=0, padx=10, pady=10)
    entry_storage_condition = tk.Entry(insert_window)
    entry_storage_condition.grid(row=8, column=1, padx=10, pady=10)

    # Buttons for return to main menu and submit
    btn_return = tk.Button(insert_window, text="Return to Main Menu", command=insert_window.destroy)
    btn_return.grid(row=9, column=0, padx=10, pady=10)

    btn_submit = tk.Button(insert_window, text="Submit", command=lambda: submit_insert(entry_item_id.get(), entry_item_name.get(), entry_supplier_id.get(), entry_height.get(), entry_weight.get(), entry_stored_time.get(), entry_type_of_item.get(), entry_storage_condition.get()))
    btn_submit.grid(row=10, column=0, padx=10, pady=10)




def submit_insert(item_id, item_name, supplier_id, height, weight, stored_time, type_of_item, storage_condition):
    # function is defined for actually inserting information into the database
    if db:
        try:
            cursor = db.cursor()
            query = "INSERT INTO Item (Item_ID, Item_Name, Supplier_ID, Height, Weight, Stored_Time, type_of_item, Storage_Condition) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (item_id, item_name, supplier_id, height, weight, stored_time, type_of_item, storage_condition)
            cursor.execute(query, values)
            db.commit()
            messagebox.showinfo("", "Item inserted successfully.")
            #accesses the data provided from the user and creates an insert into query for the database 
        #error handling
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showinfo("", "Failed to insert item.")

        finally:
            cursor.close()
    else:
        messagebox.showinfo("", "Database connection error.")
def remove_function():
    # Create a new window for item removal
    remove_window = tk.Toplevel(window)
    remove_window.title("Remove Item")
    remove_window.geometry('800x600') 
    remove_window.configure(bg='#a6e3e9')  

    # Uses item_ID to locate specific item for removal
    label_item_id = tk.Label(remove_window, text="Item ID:")
    label_item_id.grid(row=0, column=0, padx=200, pady=10)
    entry_item_id = tk.Entry(remove_window)
    entry_item_id.grid(row=0, column=1, padx=10, pady=10)

    # Buttons for return to main menu and remove
    btn_return = tk.Button(remove_window, text="Return to Main Menu", command=remove_window.destroy)
    btn_return.grid(row=1, column=0, padx=10, pady=10)

    btn_remove = tk.Button(remove_window, text="Remove Item", command=lambda: submit_remove(entry_item_id.get()))
    btn_remove.grid(row=2, column=0, padx=10, pady=10)

def submit_remove(item_id):
    # Function is defined and created for the submit removal button
    if db:
        try:
            cursor = db.cursor()
            query = "DELETE FROM Item WHERE Item_ID = %s"
            cursor.execute(query, (item_id,))
            db.commit()
            messagebox.showinfo("", "Item removed successfully.")
            #Uses the item ID provided from the user to locate the item it coorelates with and remove it
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showinfo("", "Failed to remove item.")
        #error handling
        finally:
            cursor.close()
    else:
        messagebox.showinfo("", "Database connection error.")
def modify_function():
    # Create a new window for item modification
    modify_item_window = tk.Toplevel(window)
    modify_item_window.title("Modify Item")
    modify_item_window.geometry('800x600')
    modify_item_window.configure(bg='#a6e3e9') 

    # Label and Entry for item ID to be modified
    label_item_id_modify = tk.Label(modify_item_window, text="Item ID to Modify:")
    label_item_id_modify.grid(row=0, column=0, padx=200, pady=10)
    entry_item_id_modify = tk.Entry(modify_item_window)
    entry_item_id_modify.grid(row=0, column=1, padx=10, pady=10)

    # Label and Entry for new item name
    label_new_item_name = tk.Label(modify_item_window, text="New Item Name:")
    label_new_item_name.grid(row=1, column=0, padx=10, pady=10)
    entry_new_item_name = tk.Entry(modify_item_window)
    entry_new_item_name.grid(row=1, column=1, padx=10, pady=10)

    # Label and Entry for new supplier ID
    label_new_supplier_id = tk.Label(modify_item_window, text="New Supplier ID:")
    label_new_supplier_id.grid(row=2, column=0, padx=10, pady=10)
    entry_new_supplier_id = tk.Entry(modify_item_window)
    entry_new_supplier_id.grid(row=2, column=1, padx=10, pady=10)

    # Label and Entry for new height
    label_new_height = tk.Label(modify_item_window, text="New Height:")
    label_new_height.grid(row=3, column=0, padx=10, pady=10)
    entry_new_height = tk.Entry(modify_item_window)
    entry_new_height.grid(row=3, column=1, padx=10, pady=10)

    # Label and Entry for new weight
    label_new_weight = tk.Label(modify_item_window, text="New Weight:")
    label_new_weight.grid(row=4, column=0, padx=10, pady=10)
    entry_new_weight = tk.Entry(modify_item_window)
    entry_new_weight.grid(row=4, column=1, padx=10, pady=10)

    # Label and Entry for new stored time
    label_new_stored_time = tk.Label(modify_item_window, text="New Stored Time (YYYY-MM-DD HH:mm:ss):")
    label_new_stored_time.grid(row=5, column=0, padx=10, pady=10)
    entry_new_stored_time = tk.Entry(modify_item_window)
    entry_new_stored_time.grid(row=5, column=1, padx=10, pady=10)

    # Label and Entry for new type of item
    label_new_type_of_item = tk.Label(modify_item_window, text="New Type of Item:")
    label_new_type_of_item.grid(row=6, column=0, padx=10, pady=10)
    entry_new_type_of_item = tk.Entry(modify_item_window)
    entry_new_type_of_item.grid(row=6, column=1, padx=10, pady=10)

    # Label and Entry for new storage condition
    label_new_storage_condition = tk.Label(modify_item_window, text="New Storage Condition:")
    label_new_storage_condition.grid(row=7, column=0, padx=10, pady=10)
    entry_new_storage_condition = tk.Entry(modify_item_window)
    entry_new_storage_condition.grid(row=7, column=1, padx=10, pady=10)

    # Buttons for return to main menu and modify
    btn_return_modify = tk.Button(modify_item_window, text="Return to Main Menu", command=modify_item_window.destroy)
    btn_return_modify.grid(row=8, column=0, padx=10, pady=10)

    btn_modify = tk.Button(modify_item_window, text="Modify Item", command=lambda: submit_modify_item(entry_item_id_modify.get(), entry_new_item_name.get(), entry_new_supplier_id.get(), entry_new_height.get(), entry_new_weight.get(), entry_new_stored_time.get(), entry_new_type_of_item.get(), entry_new_storage_condition.get()))
    btn_modify.grid(row=9, column=0, padx=10, pady=10)

def submit_modify_item(item_id_modify, new_item_name, new_supplier_id, new_height, new_weight, new_stored_time, new_type_of_item, new_storage_condition):
    # creates a function for the modfication submission, and utilizes the info provided from the user as constructors
    if db:
        try:
            cursor = db.cursor()
            query = "UPDATE Item SET Item_Name = %s, Supplier_ID = %s, Height = %s, Weight = %s, Stored_Time = %s, type_of_item = %s, Storage_Condition = %s WHERE Item_ID = %s"
            values = (new_item_name, new_supplier_id, new_height, new_weight, new_stored_time, new_type_of_item, new_storage_condition, item_id_modify)
            cursor.execute(query, values)
            db.commit()
            messagebox.showinfo("", "Item modified successfully.")
        # Takes the info provided by the user and modfies the item and its qualities based off the user input
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showinfo("", "Failed to modify item.")
        #error handling
        finally:
            cursor.close()
    else:
        messagebox.showinfo("", "Database connection error.")

def search_function():
    # creates the window for searching
    search_window = tk.Toplevel(window)
    search_window.title("Search Item")
    search_window.geometry('800x600')
    search_window.configure(bg='#a6e3e9') 

    # creates the textboxes and their labels
    label_search_criteria = tk.Label(search_window, text="Item Name:")
    label_search_criteria.grid(row=0, column=0, padx=200, pady=10)
    entry_search_criteria = tk.Entry(search_window)
    entry_search_criteria.grid(row=0, column=1, padx=10, pady=10)

    # button for commiting search
    btn_submit = tk.Button(search_window, text="Search", command=lambda: search_item(entry_search_criteria.get()))
    btn_submit.grid(row=1, column=0, padx= 10, pady=10)

    # Button to return to the main menu
    btn_return = tk.Button(search_window, text="Return to Main Menu", command=search_window.destroy)
    btn_return.grid(row=2, column=0, padx=10, pady=10)

def search_item(search_criteria):
    if db:
        try:
            cursor = db.cursor()
            query = "SELECT * FROM Item WHERE Item_Name = %s"  
            cursor.execute(query, (search_criteria,))
            item_details = cursor.fetchone()
            # performs the query that retireves the search information from our database

            if item_details:
                # Display item details in a messagebox 
                messagebox.showinfo("Item Details", f"Item ID: {item_details[0]}\n"
                                                    f"Item Name: {item_details[1]}\n"
                                                    f"Supplier ID: {item_details[2]}\n"
                                                    f"Height: {item_details[3]}\n"
                                                    f"Weight: {item_details[4]}\n"
                                                    f"Stored Time: {item_details[5]}\n"
                                                    f"Type of Item: {item_details[6]}\n"
                                                    f"Storage Condition: {item_details[7]}")
            else:
                messagebox.showinfo("", "Item not found.")
        # Error handling
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showinfo("", "Failed to retrieve item details.")

        finally:
            cursor.close()
    else:
        messagebox.showinfo("", "Database connection error.")

def print_item_details():

    # Create a new window for printing item details
    print_window = tk.Toplevel(window)
    print_window.title("Print Item Details")
    print_window.geometry('800x600')
    print_window.configure(bg='#a6e3e9') 

    # Label and Entry for item ID
    label_item_id = tk.Label(print_window, text="Item ID:")
    label_item_id.grid(row=0, column=0, padx=200, pady=10)
    entry_item_id = tk.Entry(print_window)
    entry_item_id.grid(row=0, column=1, padx=10, pady=10)

    # Button for submitting and printing item details
    btn_submit = tk.Button(print_window, text="Print Details", command=lambda: print_details(entry_item_id.get()))
    btn_submit.grid(row=1, column=0, padx=10, pady=10)

    # Button to return to the main menu
    btn_return = tk.Button(print_window, text="Return to Main Menu", command=print_window.destroy)
    btn_return.grid(row=2, column=0, padx=10, pady=10)

def print_details(item_id):
# creates a function that outlines the functionality for the print button
    if db:
        try:
            cursor = db.cursor()
            query = "SELECT * FROM Item WHERE Item_ID = %s"
            cursor.execute(query, (item_id,))
            item_details = cursor.fetchone()
            # Uses the ID provided by the user to fetch item details then print them
            if item_details:
                # Display item details in a messagebox 
                messagebox.showinfo("Item Details", f"Item ID: {item_details[0]}\n"
                                                    f"Item Name: {item_details[1]}\n"
                                                    f"Supplier ID: {item_details[2]}\n"
                                                    f"Height: {item_details[3]}\n"
                                                    f"Weight: {item_details[4]}\n"
                                                    f"Stored Time: {item_details[5]}\n"
                                                    f"Type of Item: {item_details[6]}\n"
                                                    f"Storage Condition: {item_details[7]}")
            else:
                messagebox.showinfo("", "Item not found.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showinfo("", "Failed to retrieve item details.")
  #Error handling
        finally:
            cursor.close()
    else:
        messagebox.showinfo("", "Database connection error.")

def user_admin_function():
    
    # Create a new window for guest user functions
    guest_window = tk.Toplevel(window)
    guest_window.title("Users")
    guest_window.geometry('800x600')
    guest_window.configure(bg='#a6e3e9') 

    # Label and Entry for user details
    label_user_name = tk.Label(guest_window, text="User Name:")
    label_user_name.grid(row=0, column=0, padx=200, pady=10)
    entry_user_name = tk.Entry(guest_window)
    entry_user_name.grid(row=0, column=1, padx=10, pady=10)

    label_fname = tk.Label(guest_window, text="First Name:")
    label_fname.grid(row=1, column=0, padx=10, pady=10)
    entry_fname = tk.Entry(guest_window)
    entry_fname.grid(row=1, column=1, padx=10, pady=10)

    label_lname = tk.Label(guest_window, text="Last Name:")
    label_lname.grid(row=2, column=0, padx=10, pady=10)
    entry_lname = tk.Entry(guest_window)
    entry_lname.grid(row=2, column=1, padx=10, pady=10)

    label_password = tk.Label(guest_window, text="Password:")
    label_password.grid(row=3, column=0, padx=10, pady=10)
    entry_password = tk.Entry(guest_window, show="*")
    entry_password.grid(row=3, column=1, padx=10, pady=10)

    label_address = tk.Label(guest_window, text="Address:")
    label_address.grid(row=4, column=0, padx=10, pady=10)
    entry_address = tk.Entry(guest_window)
    entry_address.grid(row=4, column=1, padx=10, pady=10)

    label_phone_number = tk.Label(guest_window, text="Phone Number:")
    label_phone_number.grid(row=5, column=0, padx=10, pady=10)
    entry_phone_number = tk.Entry(guest_window)
    entry_phone_number.grid(row=5, column=1, padx=10, pady=10)

    # Buttons for adding and removing users
    btn_add_user = tk.Button(guest_window, text="Add User", command=lambda: add_guest_user(
        entry_user_name.get(), entry_fname.get(), entry_lname.get(),
        entry_password.get(), entry_address.get(), entry_phone_number.get())
    )
    btn_add_user.grid(row=6, column=0, padx=10, pady=10)

    btn_remove_user = tk.Button(guest_window, text="Remove User", command=lambda: remove_guest_user(entry_user_name.get()))
    btn_remove_user.grid(row=7, column=0, padx=10, pady=10)

    # Button to return to the main menu
    btn_return = tk.Button(guest_window, text="Return to Main Menu", command=guest_window.destroy)
    btn_return.grid(row=8, column=0, padx=10, pady=10)

def add_guest_user(user_name, fname, lname, password, address, phone_number):
    # Provides the functionality for the add guest user function
    if db:
        try:
            cursor = db.cursor()
            query = "INSERT INTO Guest_User (Guest_User_Name, Guest_fname, Guest_lname, Guest_password, Guest_address, Guest_Phone_Number) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (user_name, fname, lname, password, address, phone_number))
            db.commit()
            messagebox.showinfo("", "Guest User added successfully.")
        # Gathers the guest user information given by the user and inserts a new user into the guest_User table
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showinfo("", "Failed to add Guest User.")
        #Error handling
        finally:
            cursor.close()
    else:
        messagebox.showinfo("", "Database connection error.")

def remove_guest_user(user_name):
    #Provides the functionality for the removal of a guest user
    if db:
        try:
            cursor = db.cursor()
            query = "DELETE FROM Guest_User WHERE Guest_User_Name = %s"
            cursor.execute(query, (user_name,))
            db.commit()
            messagebox.showinfo("", "Guest User removed successfully.")
        # Does the same thing with the user information, just uses delete instead of insert into
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showinfo("", "Failed to remove Guest User.")
        # Error Handling
        finally:
            cursor.close()
    else:
        messagebox.showinfo("", "Database connection error.")

def admin_user_function():
    # Creates a new window for admin user manipulaiton
    admin_window = tk.Toplevel(window)
    admin_window.title("Admin User Functions")
    admin_window.geometry('800x600')
    admin_window.configure(bg='#a6e3e9') 

    # Label and Entry for user details
    label_user_name = tk.Label(admin_window, text="Admin User Name:")
    label_user_name.grid(row=0, column=0, padx=200, pady=10)
    entry_user_name = tk.Entry(admin_window)
    entry_user_name.grid(row=0, column=1, padx=10, pady=10)

    label_email = tk.Label(admin_window, text="Admin Email:")
    label_email.grid(row=1, column=0, padx=10, pady=10)
    entry_email = tk.Entry(admin_window)
    entry_email.grid(row=1, column=1, padx=10, pady=10)

    label_fname = tk.Label(admin_window, text="First Name:")
    label_fname.grid(row=2, column=0, padx=10, pady=10)
    entry_fname = tk.Entry(admin_window)
    entry_fname.grid(row=2, column=1, padx=10, pady=10)

    label_lname = tk.Label(admin_window, text="Last Name:")
    label_lname.grid(row=3, column=0, padx=10, pady=10)
    entry_lname = tk.Entry(admin_window)
    entry_lname.grid(row=3, column=1, padx=10, pady=10)

    label_password = tk.Label(admin_window, text="Password:")
    label_password.grid(row=4, column=0, padx=10, pady=10)
    entry_password = tk.Entry(admin_window, show="*")
    entry_password.grid(row=4, column=1, padx=10, pady=10)

    label_recovery_email = tk.Label(admin_window, text="Recovery Email:")
    label_recovery_email.grid(row=5, column=0, padx=10, pady=10)
    entry_recovery_email = tk.Entry(admin_window)
    entry_recovery_email.grid(row=5, column=1, padx=10, pady=10)

    # Buttons for adding and removing users
    btn_add_user = tk.Button(admin_window, text="Add User", command=lambda: add_admin_user(
        entry_user_name.get(), entry_email.get(), entry_fname.get(),
        entry_lname.get(), entry_password.get(), entry_recovery_email.get())
    )
    btn_add_user.grid(row=6, column=0, columnspan=2, pady=10)

    btn_remove_user = tk.Button(admin_window, text="Remove User", command=lambda: remove_admin_user(entry_user_name.get()))
    btn_remove_user.grid(row=7, column=0, padx=10, pady=10)

    # Button to return to the main menu
    btn_return = tk.Button(admin_window, text="Return to Main Menu", command=admin_window.destroy)
    btn_return.grid(row=8, column=0, padx=10, pady=10)

def add_admin_user(user_name, email, fname, lname, password, recovery_email):
    #Does the same thing as the guest user functions just manipultes the admin user table instead of the guest user table
    if db:
        try:
            cursor = db.cursor()
            query = "INSERT INTO Admin_User (Admin_User_Name, Admin_Email, Admin_fname, Admin_lname, Admin_Password, Admin_Recovery_Email) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (user_name, email, fname, lname, password, recovery_email))
            db.commit()
            messagebox.showinfo("", "Admin User added successfully.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showinfo("", "Failed to add Admin User.")

        finally:
            cursor.close()
    else:
        messagebox.showinfo("", "Database connection error.")

def remove_admin_user(user_name):
    #Does the same thing as the guest user functions just manipultes the admin user table instead of the guest user table
    if db:
        try:
            cursor = db.cursor()
            query = "DELETE FROM Admin_User WHERE Admin_User_Name = %s"
            cursor.execute(query, (user_name,))
            db.commit()
            messagebox.showinfo("", "Admin User removed successfully.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showinfo("", "Failed to remove Admin User.")

        finally:
            cursor.close()
    else:
        messagebox.showinfo("", "Database connection error.")

def update_password_function():
    ##his function creates the entry buttons and labels for the guest users password manipulation
    update_window = tk.Toplevel(window)
    update_window.title("Update Password")
    update_window.geometry('800x600')
    update_window.configure(bg='#a6e3e9') 

    label_username = tk.Label(update_window, text="Username:")
    label_username.grid(row=0, column=0, padx=200, pady=10)

    entry_username = tk.Entry(update_window)
    entry_username.grid(row=0, column=1, padx=10, pady=10)

    label_password = tk.Label(update_window, text="New Password:")
    label_password.grid(row=1, column=0, padx=10, pady=10)

    entry_password = tk.Entry(update_window, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=10)

    btn_update_password = tk.Button(update_window, text="Update Password", command=lambda: update_guest_password(entry_username.get(), entry_password.get()))
    btn_update_password.grid(row=2, column=0, padx=10, pady=10)

def update_guest_password(guest_user_name, new_password):
    # This funciton provides the actual functionality for the guest user password manipulation
    if db:
        try:
            cursor = db.cursor()

            # Check if the guest user exists
            cursor.execute("SELECT * FROM Guest_User WHERE Guest_User_Name = %s", (guest_user_name,))
            user = cursor.fetchone()

            if user:
                # Update the password for the guest user
                cursor.execute("UPDATE Guest_User SET Guest_Password = %s WHERE Guest_User_Name = %s", (new_password, guest_user_name))
                db.commit()
                messagebox.showinfo("Success", "Password updated successfully!")
            else:
                messagebox.showerror("Error", "Guest user not found.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showerror("Error", f"Database error: {err}")

        finally:
            cursor.close()
    else:
        messagebox.showerror("Error", "Database connection error.")

def about_us():
    about_window = tk.Toplevel(window)
    about_window.title("About Us")
    about_window.geometry('800x600')
    about_window.configure(bg='#a6e3e9') 

        # Large title
    label_title = tk.Label(about_window, text="Database Management Process", font=("Arial", 20, "bold"), pady=10)
    label_title.pack()

    about_text = (
        "Our group was tasked with designing a warehouse management system that allowed for updateable warehouse items through the use of "
        "A python graphical user interface. Our members Annie Lee, Joshua Chenoweth, Nick DiPardo, John Biolo, and Evan Brown first designed a database"
        " from scratch using MySQL. Than constructed a conclusive lab report covering our project. We are all Computer Science students with"
        " Several different focuses studying at Marist College."
        # Add more details about your project as needed
    )

    # Larger text
    label_about = tk.Label(about_window, text=about_text, font=("Arial", 16), wraplength=550, justify=tk.LEFT)
    label_about.pack(padx=20, pady=20)

# Create the main window
window = tk.Tk()
window.title("Warehouse Management System")
window.geometry('1000x1000')
window.configure(bg='#a6e3e9') 

# Load images with Pillow
welcome_image = Image.open("welcome.jpg")
wms_image = Image.open("wms.png")

# Convert images to Tkinter PhotoImage objects
welcome_tk_image = ImageTk.PhotoImage(welcome_image)
wms_tk_image = ImageTk.PhotoImage(wms_image)

# Create labels to display images
label_welcome = tk.Label(window, image=welcome_tk_image)
label_welcome.pack()

label_wms = tk.Label(window, image=wms_tk_image)
label_wms.pack()

# Username label and entry
label_username = tk.Label(window, text="Username:")
label_username.pack()

entry_username = tk.Entry(window)
entry_username.pack()

# Password label and entry
label_password = tk.Label(window, text="Password:")
label_password.pack()

entry_password = tk.Entry(window, show="*")
entry_password.pack()

# creates Login button
button_login = tk.Button(window, text="Login", command=login)
button_login.pack()

# Keep the main window running
window.mainloop()
