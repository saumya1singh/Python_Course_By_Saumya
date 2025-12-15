print("welcome to Auction Program")

Auction = {}

while True:
    name = input("What's your name? \n").title().strip()
    bid = int(input("what's your bid? ₹\n"))
    Auction[name] = bid
    # print("\n" *18)       #to hide others name and bid(optional)
    
    other_bidders = input("Are there any other bidder? Type 'Yes' or 'No':\n ").lower()
    if other_bidders == "no":
        break

winner = max(Auction, key = Auction.get)
print(f"The winner is {winner} with a bid of ₹{Auction[winner]}")