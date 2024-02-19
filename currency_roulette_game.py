import requests
import random

def get_money_interval(random_num):
    url = 'https://v6.exchangerate-api.com/v6/a39b33c03b950ade242c69fa/latest/USD'
    response = requests.get(url)
    data = response.json()
    ils_rate = data['conversion_rates']['ILS']
    correct_answer = round((ils_rate * random_num))
    return correct_answer

def get_guess_from_user(random_num):
    user_guess = None
    while True:
        user_guess = input("how much is " + str(random_num) + " Dollar in ILS?" + "\n")
        try:
            user_guess = int(user_guess)
            break
        except:
            print("input is invalid!, choose again")
    return user_guess

def compare_results(system_num, user_num, difficulty):
    if user_num in range(system_num-(10-difficulty), system_num+(10-difficulty)+1):
        user_win = True
    else:
        user_win = False
    return user_win

def play(difficulty):
    random_num = random.randint(1, 100)
    system_num = get_money_interval(random_num)
    user_num = get_guess_from_user(random_num)
    win = compare_results(system_num, user_num, difficulty)
    print("did yon win? - " + str(win))
    return win

