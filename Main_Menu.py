from Flat_Class import *
from Block_Class import *

# Main program
def display_main_menu():
    print("Issue Manager)
    print("     1: View Issue")
    print("     2: Add Issue")
    print("     3: Edit Issue")

    print("Blocks")
    print("     4: View all blocks")
    print("     5: Add New Block")
    print("     6: Edit Block")

    print("REPORTS")
    print("     7:Creat Works order")
    print("     8:Financial Reports")#link to a diary of finances via a block selection

    print("Contractors")
    print("     9:View Contractors")
    print("    10:Add Contractors")
    print("    11:Edit Contractors")
    print("    12:Delete Contractors")

    print("DOCS")
    print("    13:DocType3")
    print("    14:DocType4")

    print("HELP/TRAIN")
    print("    15: User Manual")
    print("    16: Contact System Support")
    print("    17: User Training")

def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected: "))
            if 0<= choice <=18:## needs to change when being used for dropdowns
                option_valid = True
                print (choice)
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
            return choice

def block_dropdown_menu():
    print ("1:Select Block")
    print ("2:Search Owners Names")
    choice2=int(input("option Selected: "))

def manage():
    display_main_menu()
    choice = get_menu_choice()
#Diary
    if choice==1:
        pass
    elif choice==2:
        pass
    elif choice==3:
        pass

#Transactions
    elif choice==4:
        pass
    elif choice==5:
        pass
    elif choice==6:
        pass
#reports
    elif choice==7:
        pass
    elif choice==8:
        pass
#Blocks
    elif choice== 9:
        choice2=1
        if choice2==1:
            #print all block reports
            #NEED EDIT LATER WITH FOR LOOP!
            display_main_menu()
            
        elif choice==2:
            pass
    else:
        pass
    
def main():
    manage()

if __name__== "__main__":
    main()
