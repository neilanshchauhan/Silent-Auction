import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

def auction ():
    
    name = (input("What is your name?: "))
    bid = int((input("What is your bid?:$ ")))
    choice = (input("Are there any other bidders? Type 'yes' or 'no': ")).lower()

    auction_details = {}
    auction_details[name] = bid
   

    if choice == 'yes':
        os.system('cls')
        auction()
    elif choice == 'no':
        for bidder in auction_details:
            bids = auction_details[bidder]
            highest_bid = 0
            if bids > highest_bid:
                winner = ""
                highest_bid = bids
                winner = bidder
        print(f"The Winner is {winner} with a bid of {bids}!")

### Version-2 Idea = It also tells the user about others bids!

    #     choice_2 = input("Do you want to see others bids? Type 'yes' or 'no: ").lower()
    #     if choice_2 == 'yes':
    #         for k,v in auction_details.items():
    #             print(k, ": ", v)
    #     elif choice_2 == 'no':
    #         print("Have a Nice Day")
    #     else:
    #         print("Wrong Input")

    # else:
    #     print("Wrong Input!!! Try Again.")

auction()