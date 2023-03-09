user_input = input("Hi ,would you  like to start an order or show us the restaurant's contact in formation : ")
cart_list =[]
san_price = {
    "king mo": 100,
    "old shcool": 110,
    "choloze blue cheese": 115,
    "animal style": 120
                    }
if user_input == "contact us":
    print("the phone number is: 01156897456 , and the address is : cairo ")
elif user_input == "order":
    order_list = ["beef burger" , "chicken burger"]
    for order in order_list:
        print(order)
    order_type = input("which one do you prefer ?")
    if order_type in order_list :
        sandwiches_list =["king mo" ,"old shcool","choloze blue cheese","animal style"]
        for san in sandwiches_list:
            print(san)
        order_san = input("which one do you prefer ?")
        if order_san in sandwiches_list:
            cart_list.append(order_san)
            price_of_oneorder = san_price.get(order_san) + ((14/100)  * san_price.get(order_san))
            print(price_of_oneorder)
        else:
            print("Error ! ")






















