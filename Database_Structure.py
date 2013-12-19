import sqlite3

def create_table(db_name, table_name, sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result=cursor.fetchall()
        keep_table=True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it (y/n): ".format(table_name))
            if response == "y":
                keep_table=False
                print("The {0} table will be recreated - all existing data will be lost".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept")
        else:
            keep_table= False
        if not keep_table:
            cursor.execute(sql)
            db.commit()



if __name__ == "__main__":
    db_name = "Block Manager.db"
    sqlBlock = """create table Block
                 (Block_ID integer,
                 Block_ManagerID integer,
                 Block_Name text,
                 Address1 text,
                 Address2 text,
                 Town_City text,
                 County text,
                 Postcode text,
                 FYStart text,
                 NoSpaces integer,
                 primary key (Block_ID),
                 foreign key (Block_ManagerID)
                 references BlockManager(Block_ManagerID))"""
    sqlIssue = """create table Issue
                (IssueID integer,
                Issue text,
                Issue_Date text,
                Issue_State text,
                primary key (IssueID))"""
    sqlTenant = """create table Tenant
                (Tenant_ID integer,
                Tenant_Surname text,
                Tenant_Forname text,
                Tenant_Numberinteger,
                Tenant_Title text,
                Tenant_Email text,
                primary key (Tenant_ID))"""
    sqlLeaseholder="""create table Leaseholder
                    (Leaseholder_ID integer,
                    Leaseholder_Address text,
                    Leaseholder_Surname text,
                    Leaseholder_Forname text,
                    Leaseholder_Number integer,
                    Leaseholder_Title text,
                    Leaseholder_Email text,
                    primary key(Leaseholder_ID))"""
    sqlContractor = """create table Contractor
                    (Contractor_ID integer,
                    Contractor_Forname text,
                    Contractor_Surname text,
                    Contractor_Title text,
                    Contractor_Number integer,
                    Contractor_Postcode text,
                    Contractor_Address1 text,
                    Contractor_Address2 text,
                    Contractor_Town_City text,
                    Contractor_County text,
                    Contractor_Email text,
                    Contractor_SortCode integer,
                    Contractor_Account_Number integer,
                    Services text,
                    primary key (Contractor_ID))"""
    sqlBlockManager = """create table BlockManager
                        (Block_ManagerID integer,
                         Block_Manager_Name text,
                         Block_Manager_Number integer,
                         primary key (Block_ManagerID))"""
    sqlBlockContracts = """create table BlockContracts
                        (BlockContracts_ID integer,
                        Contractor_ID integer,
                        primary key(BlockContracts_ID),
                        foreign key(Contractor_ID)
                        references Contractor(Contractor_ID))"""
    sqlUnits = """create table Units
                (Unit_ID integer,
                Tenant_ID integer,
                Leaseholder_ID integer,
                Unit_Name text,
                primary key(Unit_ID),
                foreign key(Tenant_ID) references Tenant(Tenant_ID),                
                foreign key(Leaseholder_ID) references Leaseholder(Leaseholder_ID))"""

    sqlIssueUnit = """create table IssueUnit
                    (IssueUnit_ID integer,
                    Unit_ID integer,
                    Block_ID integer,
                    Issue_ID integer,
                    primary key(IssueUnit_ID),
                    foreign key(Unit_ID)references Units(Unit_ID),
                    foreign key(Block_ID)references Block(Block_ID),
                    foreign key(Issue_ID)references Issue(Issue_ID))"""


    create_table(db_name,"Block Manager", sqlBlockManager) 
    create_table(db_name,"Block", sqlBlock)
    create_table(db_name,"Issue", sqlIssue)
    create_table(db_name,"Contractor", sqlContractor)
    create_table(db_name,"BlockContracts", sqlBlockContracts)   
    create_table(db_name,"Leaseholder", sqlLeaseholder)
    create_table(db_name,"Tenant", sqlTenant)
    create_table(db_name,"Units", sqlUnits)
    create_table(db_name,"IssueUnit", sqlIssueUnit)









