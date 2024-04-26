import sqlite3
from datetime import datetime, timedelta
from prettytable import PrettyTable

db_connection = sqlite3.connect('database.db')
db = db_connection.cursor()

categories = ["tanulas", "lakhatas", "kozlekedes", "etelek+haztartas", "sport" , "szemelyes", "szorakozas", "utazas", "valtozo1", "valtozo2"]

def main():    
    
    while(True):
        if input("Would you like to add an item? (yes/no)") == "yes":
            add_expense()            
            print("added")

        else: 
            print("1-for this months total \n2-specify range \n3-delete entry by id \n4-list last 5 \n0-exit")
            menu = ''
            while True:
                menu = input("Press a number: ")
                if validate(menu,0,5): break                
            
            # print(menu)
            if int(menu) == 1:
                get_this_month()
                db_connection.commit()
                db_connection.close()
                break
            elif int(menu) == 2:
                print("1 - last month \n2 - last 3 months \n3 - last 6 months \n4 - this year")
                while True:
                    menu2 = input("Press a number: ")
                    if validate(menu,1,5): break
                get_by_time(menu2)
                db_connection.commit()
                db_connection.close()
                break

            elif int(menu) == 3:
                while True:    
                    index = input("Which entry to delete?")
                    if validate(index,0,100000):
                        break
                    else: 
                        print("Not existing id")
                                           
                delete(int(index))
                db_connection.commit()
                db_connection.close()
                break

            elif int(menu) == 4:
                history()
                db_connection.commit()
                db_connection.close()
                break
        
            else:
                db_connection.commit()
                db_connection.close()
                break       
            
    db_connection.close()

def add_expense():
    entry = input("Add an item name: ")
    cost  = input("Cost: ")     
    if validate_cost(cost):           
        while True: 
            category = input("Category: ")
            if validate_category(category):
                break 
            else:        
                print("invalid category")
        current_time = datetime.now().date()
        # print(entry, cost, current_time)                     

        db.execute(
                "INSERT INTO expenses (description, amount, category, timestamp) VALUES(?,?,?,?)",
                (entry,
                cost,
                category,
                current_time
                ))
        db_connection.commit()
    
def history():
    
    table = PrettyTable()
    table.field_names = ["expense_id", "description" , "amount" , "category" , "timestamp" ]
    
    rows = db.execute('SELECT * FROM expenses ORDER BY timestamp DESC LIMIT 5;')

    for row in rows:
        table.add_row(row) 
    
    print(table)


def validate(x,n,m):  
        
    if int(x) in range(n,m):        
        return True
    else:
        print("Not existing menu element")
        return False
        

def validate_cost(cost):
    if int(cost) >= 0:
        # print("val cost")
        return True
    else: 
        print("Please enter a positive number")
        return False
        

def validate_category(category):
    if category in categories:
        return True
    else: 
        print("Category does not exist")
        return False
        
def get_this_month():
    table = PrettyTable()
    table.field_names = ["Category", "Amount" ]
    
    rows = db.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category;')
    for row in rows:
        table.add_row(row) 
    
    sum = db.execute('SELECT SUM(amount) AS SUM FROM expenses;')
    total = sum.fetchone()[0]
    table.add_row(["--------", "--------"])
    table.add_row(["TOTAL", total])
    
    print(table)

def get_by_time(n):
    today = datetime.now().date()    
    first_day = ""
    last_day = ""
    if int(n) == 1:        
        last_day = (today.replace(day=1) - timedelta(days=1))
        first_day = last_day.replace(day=1)
    elif int(n)  == 2:
        first_day = (today.replace(day=1) - timedelta(days=55)).replace(day=1)
        last_day = today
    elif int(n)  == 3: 
        first_day = (today.replace(day=1) - timedelta(days=150)).replace(day=1)
        last_day = today
    elif int(n)  == 4: 
        first_day = today.replace(month=1 , day=1)
        last_day = today

    #print(first_day, last_day)

    # Creating table and represent the table 
    table = PrettyTable()
    table.field_names = ["Category", "Amount" ]
    
    # print(first_day, last_day)
    rows = db.execute('SELECT category, SUM(amount) FROM expenses WHERE timestamp BETWEEN ? AND ? GROUP BY category;', (first_day, last_day))

    for row in rows:
        table.add_row(row) 
    
    sum = db.execute('SELECT SUM(amount) AS SUM FROM expenses WHERE timestamp >= ? AND timestamp <= ?;', (first_day, last_day))
    res = sum.fetchone()
    if res is None:        
        print("No matching data was found.")
    else:   
        total = res[0]      
        table.add_row(["--------", "--------"])
        table.add_row(["TOTAL", total])
    
    print(table)
    

def delete(n):
    db.execute( "DELETE FROM expenses WHERE expense_id=(?)", (int(n),))
            
    if db.rowcount == 1:
        print(f"Done! ID {n} has been deleted.")
        return 0
    else: 
        print("Delete unsuccessful. Could not find item with particular ID.")
        return 0

if __name__ == "__main__":
    main()