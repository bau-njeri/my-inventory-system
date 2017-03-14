import sqlite3
import csv
import os
import codecs
import datetime

conn= sqlite3.connect('inventory.db')
c=conn.cursor()
def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('cls')
              
    print("\t**********************************************")
    print("\t***  Inventory management system           ***")
    print("\t**********************************************")



def get_user_choice():
    # Let users know what they can do.
    print("[1] All Items Available.")
    print("[2] Add New Item.")
    print("[3] Delete Item.")
    print("[4] Show specific item")
    print("[5] Search")
    print("[6] Reset")
    print ("[7] Checkout")
    print("[q] Quit.")

    return input("What would you like to do? ")

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS inventory(iid REAL ,name TEXT,description TEXT,total_amt REAL,cost REAL,dateadd DATETIME,status TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS checkin(iid REAL ,name TEXT,cost REAL,dateadd DATETIME,status TEXT))")
    c.execute("CREATE TABLE IF NOT EXISTS checkout(iid REAL ,name TEXT,cost REAL,dateadd DATETIME,status TEXT))")
def read_from_db():
    c.execute("SELECT iid,name,status FROM inventory")
    for row in c.fetchall():
        print (row)
def add_item():
    iid= input('ID:')
    name=input('Item Name: ')
    description=input('Item Descrpition: ')
    total_amt=input('Total Amout: ')
    cost=input('Item Cost: ')
    dateadd=2016-3-14
    status=input('Status:')
    c.execute("INSERT INTO inventory  VALUES (?,?,?,?,?,?,?);",
              (iid,name,description,total_amt,cost,dateadd,status))        
    conn.commit()
    print("Item been added")
    
def item_view():
    value=input('id:')
    c.execute("SELECT * FROM inventory WHERE iid=?;",(value,))
    
    conn.commit()
    print("Your Item ")
    for row in c.fetchall():
        print(row)

def search():
    value=input('Name of item:')
    c.execute("SELECT * FROM inventory WHERE name=?;",(value,))
    
    conn.commit()
    print("Found items ")
    for row in c.fetchall():
       
        print(row)
def checkout():
    c.execute("SELECT iid,name FROM inventory WHERE status='checkedin'")
    for row in c.fetchall():
        print (row)
    value=input("ur: ")
    c.execute("INSERT INTO checkout (iid  ,name ,cost ,dateadd ,status ) SELECT iid  ,name ,cost ,dateadd ,status FROM inventory WHERE iid=?;",(value,))        
    conn.commit()
    for row in c.fetchall():
        print (row)  
       


    
def dele():
    value=input('id:')
    c.execute("DELETE FROM inventory WHERE iid=?;",(value,))
    
    conn.commit()
    print("Item has been removed")

def drop():
    c.execute("DELETE FROM inventory")
    
    conn.commit()
    print("Everything has been removed")


            
          


choice = ''
display_title_bar()
while choice != 'q':    
    
    choice = get_user_choice()
    
    # Respond to the user's choice.
    display_title_bar()
    if choice == 1:
        read_from_db()
    elif choice == 2:
        add_item()
    elif choice == 3:
        dele()
    elif choice == 4:
        item_view()
    elif choice == 5:
        search()
    elif choice == 6:
        drop()
    elif choice==7:
        checkout()
    elif choice == 'q':
        
        print("\n Have a nice day")
    else:
        print("\Please select a number from the menu.\n")            
    
    
            

create_table()

#read_from_db()
#c.close()
#conn.close()
