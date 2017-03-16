import sqlite3   
import csv      
import os       
import datetime 
from tabulate import tabulate
from termcolor import colored, cprint
from colorama import init

init()



conn= sqlite3.connect('inventry.db') 
c=conn.cursor()                     
def display_title_bar():           
                        
    os.system('cls')               
              
    print("\t**********************************************")  
    print("\t---------        Welcome To        -----------")
    print("\t---     Inventory management system        ---")
    print("\t**********************************************")



def get_user_choice():         
    
    print("[1] Add New Item.") 
    print("[2] Delete Item.")
    print("[3] Item List.")
    print("[4] Checkout")
    print("[5] Checkin")
    print("[6] Item View")
    print("[7] Search")
    print("[q] Quit.")

    user_input = input("What would you like to do? ")
    return int(user_input) if user_input.isdigit() else user_input
    # return user_input
    


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuff(iid REAL not NULL, name TEXT not NULL, description TEXT not NULL, total_amt REAL ,cost REAL,dateadd DATETIME,status TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS stats(iid REAL ,name TEXT,cost REAL,dateadd DATE,status TEXT)")

def add_item():
    print("Please Enter the following")
    iid        =input ('ID:')
    name       =input ('Item Name: ')
    description=input ('Item Descrpition: ')
    total_amt  =input ('Total Amout: ')
    cost       =input ('Item Cost: ')
    dateadd    =datetime.datetime.now()
    status     =input ('Status:')
    c.execute("INSERT INTO stuff  VALUES (?,?,?,?,?,?,?);",  
              (iid,name,description,total_amt,cost,dateadd,status))
    conn.commit()
    print("Item been added")
    
def remove_item():
    c.execute("SELECT iid,name,description FROM stuff ") 
    for row in c.fetchall():
        print (row)
    value=input('Id of Item to Delete:')
    c.execute("DELETE FROM stuff WHERE name=?;",(value))
    conn.commit()
    print("Item has been deleted")

def item_list():
    c.execute("SELECT iid,name,status FROM stuff")
    all_items = []
    for row in c.fetchall():
        item_details = []
        item_details.append(row[0])
        item_details.append(row[1])
        item_details.append(row[2])
        all_items.append(item_details)
    headers = ["Id", "Name","Status"]
    print(colored(tabulate(all_items, headers, tablefmt="grid"),'green'))

def checkout():
    c.execute("SELECT iid,name FROM stuff WHERE status='in'")
    for row in c.fetchall():
        print (row)
    value=input("Enter Item ID: ")
    c.execute("UPDATE stuff SET status = 'out' WHERE name=?;",(value,))    
    conn.commit()
    c.execute("INSERT INTO stats (iid  ,name ,cost ,dateadd ,status ) SELECT iid  ,name ,cost ,dateadd ,status FROM stuff WHERE iid=?;",(value,))     
    conn.commit()
    
def checkin():
    c.execute("SELECT iid,name FROM stuff WHERE status='out'")
    for row in c.fetchall():
        print (row)
    value=input("Enter Item ID: ")
    c.execute("UPDATE stuff SET status = 'in' WHERE name=?;",(value,))
    conn.commit()
    c.execute("INSERT INTO stats (iid  ,name ,cost ,dateadd ,status ) SELECT iid  ,name ,cost ,dateadd ,status FROM stuff WHERE iid=?;",(value,))        
    conn.commit()        
    
def item_view():
    value=input('id:')
    c.execute("SELECT iid,name ,status,dateadd FROM stats  WHERE name=?;",(value,))
    conn.commit()
    print("Your Item ")
    for rows in c.fetchall():
        print(rows)

def search():
    value=input('Name of item:')
    c.execute("SELECT * FROM stuff WHERE name=?;",(value,))
    conn.commit()
    print("Found items ")
    for row in c.fetchall():
       
        print(row)

def assetvalue():
    c.execute("SELECT SUM (cost*total_amt)FROM STUFF")
    conn.commit()
    print(":Assert Value")
    for row in c.fetchall():
        print(row)

def itemvaluecategory():
   value=input ("descreption of item:")
   c.execute("SELECT SUM (cost*")        



            
#   choice = ''
        
# display_title_bar()   
# while choice != 'q':    
    
#     choice = get_user_choice()
    
    
#     # display_title_bar()
#     if choice == 1:
#          add_item()
#     elif choice == 2:
#          dele()
#     elif choice == 3:
#          item_list()
#     elif choice == 4:
#          checkout()
#     elif choice == 5:
#          checkin()
#     elif choice == 6:
#          item_view()   
#     elif choice == 7:
#         search()
  
#     elif choice == 'q':
#         print("\n Have a nice day :)")
#     else:
#         print("\n Please select a value from the menu .\n")            
    
    
            

create_table()


