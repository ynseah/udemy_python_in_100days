from art import logo
print (logo)

bidders = []

def add_new_bidder (bid_name, bid_price):
    new_bidder = {}
    new_bidder["Name"] =  bid_name
    new_bidder["Price"] = bid_price
    bidders.append(new_bidder)

def get_highest_bid ():
    curr_highest_bidder_name = ""
    curr_highest_price = 0
    for dict in bidders:
        #for key in dict:
        if int(dict["Price"]) > int(curr_highest_price):
            curr_highest_bidder_name = dict["Name"]
            curr_highest_price = dict["Price"]
    
    print ("Highest bid is " + curr_highest_bidder_name + " who bidded price is RM" + curr_highest_price)

def get_bidder ():
    name = input("Please enter your name. \nName: ")
    price = input("Price for your bid: ")
    add_new_bidder(name, price)
    

bidding_active = True
while (bidding_active is True):
    get_bidder()
    other_bidder = input("Is there any other bidder?")
    
    if (other_bidder == "No"):
        get_highest_bid()
        print (bidders)
        bidding_active = False
    else:
        print ("clear screen")


