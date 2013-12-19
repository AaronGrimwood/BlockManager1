import sqlite3

def issue_menu():
    print("Select which field you would like to update")
    print("    1: Update Issue")
    print("    2: Update Issue Date")
    print("    3: Update Issue State")
    print("    4: Update All")


def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected: "))
            if 0<= choice <=4:
                option_valid = True
                print (choice)
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
            return choice

def get_IssueID():
    IssueID = input("Please select an Issue by ID: ")
    return IssueID

def get_Issue():
    Issue = input("Please input Issue details: ")
    return Issue

def get_Issue_Date():
    Issue_Date = input("Please enter Issue Date: ")

def get_Issue_State():
    Issue_State = input("Please enter (Select) Issue State: ")

def update_Issue(data):
    with sqlite3.connect("Block Manager.db") as db:
        cursor = db.cursor()
        sql = "update Issue set Issue=? where IssueID=?"
        cursor.execute(sql,data)
        db.commit()



def update_all(data):
    with sqlite3.connect("Block Manager.db") as db:
        cursor = db.cursor()
        sql = "update Issue set Issue=?, Issue_Date=?, Issue_State=? where IssueID=?"
        cursor.execute(sql,data)
        db.commit()
        
if __name__ == "__main__":
    issue_menu()
    choice = get_menu_choice()
    IssueID = get_IssueID()

    if choice==1:
        Issue=get_Issue()
        

    
    data = ("Latte",2.45,1)
    update_all(data)
 
