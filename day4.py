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
    password = [int(i) for i in str(password)]
    if is_password(password) == True:
        for index in range(len(password) - 1):
            if password[index] == password[index+1] 
            #make dictionary of all letters of doubled and then if the total count of one is true the password is True

if __name__ == "__main__":
    # print(is_password(111111))
    # print(is_password(223450))
    # print(is_password(123789))
    print(count_password("172851-675869"))