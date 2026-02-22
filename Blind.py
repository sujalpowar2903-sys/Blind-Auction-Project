import art
print(art.logo)
def find_highest_bidder(biddig_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amp=ount > highedst_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is{winner} with a bid of ${highest_bid}. ")
#Ask the user form input 
bids = {}
# Save data into ditionary {name: price}
#Whther if new bids need to be added
continue_bidding = True 
while continue_bidding:
    name = input("What is your name?: ")
    price =int(input("What is your bid?: "))
    bids[name] = price
    should_continue = input ("Are there any other bidder? type 'yes' or 'no'. \n")
    if should_continue == "no":
        conting_bidding = False
        find_highest_bidder(bids)
    elif should_continue =="yes":
        print("\n" * 20)

#Compare bids in dictionary 
