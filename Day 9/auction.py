# from replit import clear
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
restart = True

bidders = {}
def bid_list(name, bid):
    bidders[name] = bid

while restart:
    name = input("Enter the bidder's name: ")
    bid = int(input("How much are you going to bid? "))
    bid_list(name, bid)
    choice = input("Is there anyone else who wants to bid? Type 'y' for yes and 'n' for no. ").lower()
    if choice == "y":
        restart = True
        os.system('cls||clear')
    elif choice == "n":
        restart = False

max = 0
highest = ""
for people in bidders:
    if max == 0:
        max = bidders[people]
    if bidders[people] > max:
        max = bidders[people]
        highest = people

print(f"The highest bidder is {highest}.")