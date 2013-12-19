import sqlite3

def get_Issue_data():
    Issue=input("Please enter your issue details: ")
    Issue_Date=input("Please enter the Issue Date: ")
    Issue_State=input("Please enter (select) Issue State: ")

    return Issue, Issue_Date, Issue_State

def insert_Issue_data(values):
    with sqlite3.connect("Block Manager.db") as db:
        cursor = db.cursor()
        sql = "insert into Issue(Issue,Issue_Date, Issue_State) values (?,?,?)"#do not need to insert productID, ?=placeholde
        cursor.execute(sql,values)
        db.commit()
if __name__ =="__main__":

    Issue, Issue_Date, Issue_State = get_Issue_data()
    Issue = (Issue, Issue_Date,Issue_State)
    insert_Issue_data(Issue)
