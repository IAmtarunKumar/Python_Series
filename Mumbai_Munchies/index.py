
list = [{"id" : 1 , "name" : "Samosa" , "price" : 10} , {"id" : 2 , "name" : "Jalebi" , "price" : 5}]

def showSnakes():
     for i in list:
          print("\nID-"+str(i["id"])  , i["name"]+ " -₹"+ str(i["price"]))
print("\n--------------------------------------------------")
# inputTaking()


def addSnakes():
    id = len(list)+1
    name = input("Enter Your name : ");
    price = input("Enter Your price : ");
    newSnack = {"id" : id , "name" : name , "price" : price}
    list.append(newSnack)
    print("\n----------------------------------------")
    print("New Snakes is added")
    print("----------------------------------------\n")
    inputTaking()


def removeSnakes():
    id = input("Enter Your id : ")

    for i in list:

        if(i["id"]==int(id)):
               
               list.remove(i)
               print("\n--------------------------------------------------")
               print("ID",i["id"],"Item is Removed")
               print("--------------------------------------------------\n")
               break;
        
    inputTaking()
        
        


def updateSnakes():
    id = input("Enter Your id: ")
    for i in list:
        if i["id"] == int(id):
            i["name"] = input("Enter your updated snake's name: ")
            i["price"] = input("Enter Your updated price: ")

            print("\n--------------------------------------------------")
            print("ID",i["id"], "Item is updated")
            print("--------------------------------------------------\n")
            break;
    inputTaking()

        
    



option=""
def inputTaking():
    print("\n-------------------------------------")
    print("Welcome to Mumbai Manchies")
    print("-------------------------------------\n")

    add = "Add a snack to the inventory"
    print("1.",add)
    remove = "Remove a snack from the inventory"
    print("2.",remove)
    update = "Update the availability of a snack"
    print("3.",update)
    show = "Show All Snakesthe availability of a snack"
    print("4.",show)

    option = input("\nPlease Select Your Options : ")
    # return option
    if(option=="1"):
        addSnakes()
        # inputTaking()
    elif(option=="2"):
     removeSnakes()
    #  inputTaking()
    elif(option=="3"):
     updateSnakes()
    #  inputTaking()
    elif(option=="4"):
     showSnakes()
     inputTaking()

inputTaking()
     
  


