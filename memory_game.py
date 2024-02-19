import random
import time
import os

def generate_sequence(difficulty):
    list1 = []
    for index in range(1, difficulty+1):
        random_num = random.randint(1, 100)
        random_num = str(random_num)
        list1.insert(index-1, random_num)
    print(list1)
    os.system("cls")
    time.sleep(0.7)
    return list1

def get_list_from_user(difficulty):
    list2 = []
    for index in range(1, difficulty + 1):
        user_input = input("enter the number in index = " + str(index) + "\n")
        list2.insert(index-1, user_input)
    return list2

def is_list_equal(system_list, user_list, difficulty):
    user_win = True
    for index in range(1, difficulty + 1):
        if system_list[index-1] != user_list[index-1]:
            user_win = False
            break
    return user_win

def play(difficulty):
    system_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    win = is_list_equal(system_list, user_list, difficulty)
    print("did yon win? - " + str(win))
    return win