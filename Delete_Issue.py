import sqlite3

def get_delete_choice():
    delete_choice1=input("What attribute would you like to delete by? e.g IssueID : ")
    #delete_choice2=input("You may pick a second attribute to delete by: ")
    data=input("Enter first attribute value:")
    #data2=input("Enter second attribute value: ")
    

    return delete_choice1,data 

    
def delete_Issue(data):
    with sqlite3.connect("Block Manager.db") as db:
        cursor = db.cursor()
        sql = "delete from Issue where ?=?"
        cursor.execute(sql, data)
        db.commit()

if __name__== "__main__":
    
    delete_choice1,data = get_delete_choice()
    data1 = (delete_choice1,data)
    delete_Issue(data1)
    
