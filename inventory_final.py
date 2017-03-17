import sqlite3   
import csv      
import os       
import datetime 
from tabulate import tabulate
from termcolor import colored, cprint
from colorama import init


init()



conn= sqlite3.connect('inventory.db') 
c=conn.cursor()                     
def display_title_bar():           
                        
    os.system('cls')               
              
    print("\t**********************************************")  
    print("\t---     Inventory management system        ---")
    print("\t**********************************************")






def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS `inventory` (
	`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`name`	TEXT NOT NULL,
	`description`	TEXT NOT NULL,
	`quantity`	INTEGER NOT NULL,
	`cost`	REAL NOT NULL,
	`dateadded`	DATETIME NOT NULL,
	`status`	TEXT NOT NULL
);''')
    c.execute('''CREATE TABLE IF NOT EXISTS `statistics` (
	`ID`	INTEGER NOT NULL,
	`name`	TEXT NOT NULL,
	`dateadded`	DATE NOT NULL,
	`status`	TEXT NOT NULL,
	PRIMARY KEY(`ID`)
);''')
def add_item():
    print("Please Enter the following")
    ID         =input ('ID:')
    name       =input ('Item Name: ')
    description=input ('Item Descrpition: ')
    quantity   =input ('Quantity: ')
    cost       =input ('Item Cost: ')
    dateadded   =datetime.datetime.now()
    status     =input ('Status:')
    c.execute("INSERT INTO inventory  VALUES (?,?,?,?,?,?,?);",  
              (ID,name,description,quantity,cost,dateadded,status))
    conn.commit()
    print("Item added")

        
def remove_item():
    c.execute("SELECT ID,name,description FROM inventory ") 
    all_items = []
    for row in c.fetchall():
        item_details = []
        item_details.append(row[0])
        item_details.append(row[1])
        
        all_items.append(item_details)
    headers = ["Id", "Name"]
    print(colored(tabulate(all_items, headers, tablefmt="grid"),'yellow'))
    conn.commit()
    value=input('Item ID:')
    c.execute("DELETE FROM inventory WHERE ID=?;",(value,))
    conn.commit()
    
   

def item_list():
    c.execute("SELECT ID,name,status FROM inventory")
    all_items = []
    for row in c.fetchall():
        item_details = []
        item_details.append(row[0])
        item_details.append(row[1])
        item_details.append(row[2])
        all_items.append(item_details)
    headers = ["Id", "Name","Status"]
    print(colored(tabulate(all_items, headers, tablefmt="grid"),'yellow'))

def checkout():
    c.execute("SELECT ID,name,status FROM inventory WHERE status='in'")
    print("Items available for checkout")
        
    all_items=[]
    for row in c.fetchall():
        item_details = []
        item_details.append(row[0])
        item_details.append(row[1])
        item_details.append(row[2])
        all_items.append(item_details)
    headers = ["Id", "Name","Status"]
    print(colored(tabulate(all_items, headers, tablefmt="grid"),'yellow'))

    value=input("Enter Item ID: ")
    c.execute("UPDATE inventory SET status = 'out' WHERE ID=?;",(value,))    
    conn.commit()
    c.execute("INSERT INTO statistics (ID  ,name ,dateadded ,status ) SELECT ID  ,name  ,dateadded ,status FROM inventory WHERE ID=?;",(value,))     
    conn.commit()
    
def checkin():
    c.execute("SELECT ID,name,status FROM inventory WHERE status='out'")
    print("Items available for checkin")
        
    all_items=[]
    for row in c.fetchall():
        item_details = []
        item_details.append(row[0])
        item_details.append(row[1])
        item_details.append(row[2])
        all_items.append(item_details)
    headers = ["Id", "Name","Status"]
    print(colored(tabulate(all_items, headers, tablefmt="grid"),'yellow'))
        
    value=input("Enter Item ID: ")
    c.execute("UPDATE inventory SET status = 'in' WHERE ID=?;",(value,))
    conn.commit()
    c.execute("INSERT INTO statistics (ID  ,name  ,dateadded,status ) SELECT ID  ,name ,dateadded ,status FROM inventory WHERE ID=? ;",(value,))        
    conn.commit()        
    
def item_log():
    value=input('Item ID:')
    c.execute("SELECT ID,name ,status,dateadded FROM statistics  WHERE ID=?;",(value,))
    conn.commit()
    all_items=[]
    for row in c.fetchall():
        item_details = []
        item_details.append(row[0])
        item_details.append(row[1])
        item_details.append(row[2])
        item_details.append(row[3])
        all_items.append(item_details)
    headers = ["Id", "Name","Status","Date"]
    print(colored(tabulate(all_items, headers, tablefmt="grid"),'yellow'))
    
def search():
    value=input('Name of item:')
    c.execute("SELECT * FROM inventory WHERE name=?;",(value,))
    all_items=[]
    for row in c.fetchall():
        item_details = []
        item_details.append(row[0])
        item_details.append(row[1])
        item_details.append(row[2])
        item_details.append(row[3])
        item_details.append(row[4])
        item_details.append(row[5])
        all_items.append(item_details)
    headers = ["Id", "Name","Description","Cost","Status","Date Added"]
    print(colored(tabulate(all_items, headers, tablefmt="grid"),'yellow'))

def total_assets():
    c.execute("SELECT SUM (cost*quantity)FROM inventory")
    all_items=[]
    for row in c.fetchall():
        item_details = []
        item_details.append(row[0])
        all_items.append(item_details)
    headers = ["Total Asset Value"]
    print(colored(tabulate(all_items, headers, tablefmt="grid"),'yellow'))
    
       
    
def value_by_category():
    value=input('Descrption of item:')
    c.execute("SELECT SUM(cost*quantity) FROM inventory WHERE description=?;",(value,))
    all_items=[]
    for row in c.fetchall():
        item_details = []
        item_details.append(row[0])
        
        all_items.append(item_details)
    headers = ["Total Cost"]
    print(colored(tabulate(all_items, headers, tablefmt="grid"),'yellow'))
    conn.commit()
    
def item_value():
    value=input('Name of item:')
    value2=input('Descrption of item:')
    c.execute("SELECT cost FROM inventory WHERE name=? AND description=?;",(value,value2,))
    all_items=[]
    for row in c.fetchall():
        item_details = []
        item_details.append(row[0])
        
        all_items.append(item_details)
    headers = ["Total Cost"]
    print(colored(tabulate(all_items, headers, tablefmt="grid"),'yellow'))
    


      

create_table()          


