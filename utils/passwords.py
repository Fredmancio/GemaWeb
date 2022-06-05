import random


def generate_random_password():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"

    Use_for = lower_case + upper_case + number
    lenght_for_pass = 8
    password = "".join(random.sample(Use_for, lenght_for_pass))
    return password


