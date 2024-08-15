from functions import outcome, play, collect_stats
print("Do you want to \n 1)Play \n 2)See who wins more? \n")
menu = input()
if menu == "1":
    user_choice, machines_choice = play()
    print(outcome(user_choice, machines_choice))
else:
    print(collect_stats())

