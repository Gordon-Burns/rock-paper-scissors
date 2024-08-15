import random


def record_result(value):
    with open("results.txt", "a") as file:
        file.write(value)
        file.write('\n')
        file.close()


def outcome(user_choice, machines_choice):
    if user_choice == machines_choice:
        value = 'tie'
        record_result(value)
        return "Its a tie"
    elif user_choice == 'Rock' and machines_choice == 'Paper':
        value = "program"
        record_result(value)
        return "I Win !!"
    elif user_choice == 'Paper' and machines_choice == 'Rock':
        value = "user"
        record_result(value)
        return "You Win !!"
    elif user_choice == 'Rock' and machines_choice == 'Scissors':
        value = "user"
        record_result(value)
        return "You Win !!"
    elif user_choice == 'Scissors' and machines_choice == 'Rock':
        value = "program"
        record_result(value)
        return "I Win !!"
    elif user_choice == 'Paper' and machines_choice == 'Scissors':
        value = "program"
        record_result(value)
        return "I Win !!"
    elif user_choice == 'Scissors' and machines_choice == 'Paper':
        value = "user"
        record_result(value)
        return "You Win !!"
    else:
        return "Result not Programmed"


def play():
    choices = ['Rock', 'Paper', 'Scissors']

    print(f'Please choose your weapon from the available options:')
    for i in choices:
        print(i)

    user_choice = input("Which is your choice \n")
    machines_choice = random.choice(choices)

    print(f"You chose {user_choice} and I chose {machines_choice}")
    return user_choice, machines_choice


def collect_stats():
    with open("results.txt","r") as file:

        content = file.readlines()
        ties = 0
        user = 0
        program = 0
        for i in content:
            i = i.strip()
            if i == "tie":
                ties = ties + 1
            elif i == "user":
                user = user + 1
            else:
                program = program + 1
    file.close()
    stats = f"\nUser wins:{user} \nTies:{ties}\nProgram wins:{program}"
    return stats

