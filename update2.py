import sqlite3

def get_IssueID():
    IssueID = input("Please select an Issue by ID: ")
    return IssueID

def select_individual_issue(id):
    with sqlite3.connect("Block Manager.db")as db:
        cursor = db.cursor()
        cursor.execute("select * from Issue where IssueID=?",(id,))
        Issue = cursor.fetchone()
        return Issue
    
def update_all(data):
    with sqlite3.connect("Block Manager.db") as db:
        cursor = db.cursor()
        sql = "update Issue set Issue=?, Issue_Date=?, Issue_State=? where IssueID=?"
        cursor.execute(sql,data)
        db.commit()
    
if __name__ == "__main__":
    IssueID = get_IssueID()
    Issue = select_individual_issue(IssueID)
    print(Issue)
