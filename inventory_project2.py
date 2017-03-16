import sqlite3   
import csv      
import os       
import datetime 

conn= sqlite3.connect('inventory.db') 
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
    print("[8] Asset Value")
    print("[9] Print")
    print("[10] Category value")
    print("[11] Item Value")
    
    print("[q] Quit.")

    user_input = input("What would you like to do? ")
    return int(user_input) if user_input.isdigit() else user_input

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuff(iid REAL ,name TEXT,description TEXT,total_amt REAL,cost REAL,dateadd DATETIME,status TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS stats(iid REAL ,name TEXT,cost REAL,dateadd DATE,status TEXT)")

def add_item():
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
    
def dele():
    c.execute("SELECT iid,name,description FROM stuff ") 
    for row in c.fetchall():
        print (row)
    value=input('Id of Item to Delete:')
    c.execute("DELETE FROM stuff WHERE iid=?;",(value,))
    conn.commit()
    print("Item has been deleted")

def item_list():
    c.execute("SELECT iid,name,status FROM stuff")
    for row in c.fetchall():
        print (row)

def checkout():
    c.execute("SELECT iid,name FROM stuff WHERE status='in'")
    for row in c.fetchall():
        print (row)
    value=input("Enter Item ID: ")
    c.execute("UPDATE stuff SET status = 'out' WHERE iid=?;",(value,))    
    conn.commit()
    c.execute("INSERT INTO stats (iid  ,name ,cost ,dateadd ,status ) SELECT iid  ,name ,cost ,dateadd ,status FROM stuff WHERE iid=?;",(value,))     
    conn.commit()
    
def checkin():
    c.execute("SELECT iid,name FROM stuff WHERE status='out'")
    for row in c.fetchall():
        print (row)
    value=input("Enter Item ID: ")
    c.execute("UPDATE stuff SET status = 'in' WHERE iid=?;",(value,))
    conn.commit()
    c.execute("INSERT INTO stats (iid  ,name ,cost ,dateadd ,status ) SELECT iid  ,name ,cost ,dateadd ,status FROM stuff WHERE iid=?;",(value,))        
    conn.commit()        
    
def item_view():
    value=input('id:')
    c.execute("SELECT iid,name ,status,dateadd FROM stats  WHERE iid=?;",(value,))
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
    c.execute("SELECT SUM(cost*total_amt) FROM stuff ")
    conn.commit()
    print(":Asset Value :")
    for row in c.fetchall():
        print (row)
    
def itemvaluecategory():
    value=input('Descrption of item:')
    c.execute("SELECT SUM(cost*total_amt) FROM stuff WHERE description=?;",(value,))
    conn.commit()
    print(":Asset Value :")
    for row in c.fetchall():
        print (row)

def itemvalue():
    value=input('Name of item:')
    value2=input('Descrption of item:')
    c.execute("SELECT cost FROM stuff WHERE name=? AND description=?;",(value,value2,))
    conn.commit()
    print(":Item Value :")
    for row in c.fetchall():
        print (row)        
    
             
def prnt(data):
    f=open('gist.csv')
    with f:
        f.write(data)
   
choice =''
display_title_bar()   
while choice != 'q':    
    
    choice = get_user_choice()
    
      
    display_title_bar()
    if choice == 1:
         add_item()
    elif choice == 2:
         dele()
    elif choice == 3:
         item_list()
    elif choice == 4:
         checkout()
    elif choice == 5:
         checkin()
    elif choice == 6:
         item_view()   
    elif choice == 7:
        search()
    elif choice == 8:
        assetvalue ()
    elif choice == 9:
        prnt()
    elif choice==10:
        itemvaluecategory()
    elif choice==11:
        itemvalue()
    
    elif choice == 'q':
        print("\n Have a nice day :)")
    else:
        print("\n Please select a value from the menu .\n")            
    
    
            

create_table()


