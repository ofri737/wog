import random

def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    print("system number was - " + str(secret_number))
    return secret_number

def get_guess_from_user(difficulty):
    user_guess = None
    while user_guess not in range(1,difficulty+1):
        user_guess = input("geuss my number between 1 to " + str(difficulty) + "\n")
        try:
            user_guess = int(user_guess)
            if user_guess in range(1, difficulty + 1):
                break
            else:
                print("input is not in range, choose again")
        except:
            print("input is invalid!, choose again")
    return user_guess

def compare_results(system_num, user_num):
    if system_num == user_num:
        user_win = True
    else:
        user_win = False
    return user_win

def play(difficulty):
    user_num = get_guess_from_user(difficulty)
    system_num = generate_number(difficulty)
    win = compare_results(system_num, user_num)
    print("did yon win? - " + str(win))
    return win