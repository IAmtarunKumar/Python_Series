menu = [
    {"dish_id": 1, "dish_name": "Margherita Pizza", "price": 12.99, "availability": True},
    {"dish_id": 2, "dish_name": "Pasta Carbonara", "price": 10.99, "availability": True},
    {"dish_id": 3, "dish_name": "Chicken Tikka Masala", "price": 15.49, "availability": False},
    # Add more dishes here
]

orderList = []


def showMenu():
    for i in menu:
        print(f"{i['dish_id']} {i['dish_name']} ₹{i['price']} availability-{i['availability']}")



def add_dish():
    new_dish_id = len(menu)+1
    new_dish_name = input("Enter the dish name: ")
    new_price = input("Enter the dish price: ")
    new_availability = input("Enter availibility (True/False): ")
    new_dish = {
       "dish_id" : new_dish_id,
       "dish_name" : new_dish_name,
       "price" : new_price,
       "availability" : new_availability 
    }
    menu.append(new_dish)
    # print(menu)
    print("New Item added in Menu with ID",new_dish_id)


def remove_dish():
    remove_id = input("Enter item ID: ")
    for i in menu:
        if(str(i["dish_id"]))==(remove_id):
            menu.remove(i)
            print(menu)
            break;


def update_dish():
    update_id = input("Enter item ID: ")
    for i in menu:
        if(str(i["dish_id"])==update_id):
            i["availability"] = input("Enter Updated Availability: ")
            print(menu)
            break;


def order():
    name = input("Enter Customer Name: ")
    
    order_dish_id = input("Enter Order Dish ID (1,2,3..): ")
    # print(order_dish_id)
    dish_list = order_dish_id.split(",")
    order_id = len(orderList)+1
    item_not_avilable = []
    avl_dish=[]
    # print(dish_list)
    for i in dish_list:
        for item in menu:
            if(str(i)==str(item['dish_id']) and item['availability']):
                avl_dish.append(i)
            
                
            

    
    newOrder = {"order_id" : order_id, 
                "Customer_Name" : name,
                "Order_Dish_ID" : avl_dish,
                "Status"  : "Order is Placed"}
    
    orderList.append(newOrder)

    # print("available dish ID" , avl_dish , "and Not available dish ID" , item_not_avilable)
    # print(orderList)
    print("Your Order is Placed")
    # print(orderList)
    # print(item_not_avilable)


def Order_Status():
    status_order_id = input("Enter Order ID: ")
    for i in orderList:
        # print(i)
        if(str(i["order_id"])== str(status_order_id)):
            i["Status"] = input("Enter Updated Order Status: ")
            print("\nOrder Status is Updated\n")
            break;

def show_all_orders():
    item_avl = len(orderList)
    if(item_avl>0):
        for item in orderList:
            print(f"ORDER_ID-{item['order_id']} CUSTOMER_NAEM-{item['Customer_Name']} ORDERED_DISH_ID-{item['Order_Dish_ID']} STATUS-{item['Status']}")
    else:
        print("\nEmpty order list....\n")



def Exit():
    print("\n Thank You.... \n")






def main():
    def printMenu():
        print("--------------------------------")
        print("{{     Zomato Chronicles      }}")           
        print("--------------------------------")

        print("\n1. Show Dishes")
        print("2. Add Dish Into Menu")
        print("3. Remove Dish from Menu")
        print("4. Update Dish Avalibility in Menu")
        print("5. Show Order Lists")
        print("6. Take New Order from Customer")
        print("7. Update Order Status")
        print("8. Exit\n")

        option = input("Select Your Option: ")
        return option

    option=printMenu()
    if(option=="1"):
        showMenu()
        main()
    elif(option=="2"):
        add_dish()
        main()
    elif(option=="3"):
        remove_dish()
        main()
    elif(option=="4"):
        update_dish()
        main()
    elif(option=="5"):
        show_all_orders()
        main()
    elif(option=="6"):
        order()
        main()
    elif(option=="7"):
        Order_Status()
        main()
    
    elif(option=="8"):
        Exit()
    else:
        print("Invalid Option")

main()
    
    







