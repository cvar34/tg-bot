import random
def pass_gen(length):
    password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password_1 = ""
    for i in range(length):
        password_1 = password_1 + random.choice(password)
    return password_1