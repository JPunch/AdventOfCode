'''Advent of Code 2019 day4'''
# Your puzzle input is 172851-675869

def is_password(password):
    password = [int(i) for i in str(password)]
    double = False
    for index in range(len(password) - 1):
        if password[index] > password[index + 1]:
            return False
        elif len(password) != 6:
            return False
        elif password[index] == password[index + 1]:
            double = True
    if double == True:
        return True
    else:
        return False

def count_password(passrange):
    passrange = passrange.split("-")
    count = 0
    for password in range(int(passrange[0]), int(passrange[1])):
        if is_password(password) == True:
            count += 1
    return count

def extra_password(password):
    password2 = [int(i) for i in str(password)]
    counts = {i:password2.count(i) for i in password2}
    if is_password(password) == True:
        for index in range(len(password2) - 1):
            if password2[index] == password2[index+1]:
                if 2 in counts.values():
                    return True
                else:
                    return False

def count_extrapassword(passrange):
    passrange = passrange.split("-")
    count = 0
    for password in range(int(passrange[0]), int(passrange[1])):
        if extra_password(password) == True:
            count += 1
    return count

if __name__ == "__main__":
    # print(is_password(111111))
    # print(is_password(223450))
    # print(is_password(123789))
    # print(count_password("172851-675869"))
    # extra_password(111122)
    print(count_extrapassword("172851-675869"))