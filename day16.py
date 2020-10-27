'''Advent of code 2019 day 16'''

from collections import deque

def apply_pattern(signal, pattern):
    new_signal = []
    for index, value in enumerate(signal.signal):
        pattern.make_pattern(index)
        pattern.fit_to_signal(signal.signal)
        ans = [
            x*y for x, y in zip(signal.signal, pattern.fitted_pattern)
        ]
        new_signal.append(last_digit(sum(ans)))
    return "".join(new_signal)

def last_digit(number): #returns last digit
    number = str(abs(number))
    number = list(number)
    return number.pop()

def sets_to_answer(message_start=5979187, len_input=650, repeats=10000):
    into_set1 = 5979187 % 650
    # print(into_set1)
    into_set2 = into_set1 + 8
    # print(into_set2)
    return  repeats - (message_start//len_input) - 1
#801 sets back from the firsst 650 and then 5979187 % 650 into it is the starting letter


class Signal():
    def __init__(self, signal):
        self.signal = list(signal)
        self.parse()

    def parse(self):
        output = [int(x) for x in self.signal]
        self.signal = deque(output)


class Pattern():
    def __init__(self, pattern):
        self.pattern = pattern
        self.parse()
    
    def parse(self):
        output = [int(x) for x in self.pattern.split(",")]
        self.pattern = deque(output)

    def fit_to_signal(self, signal):
        final_pattern = deque()
        while len(final_pattern) < len(signal):
            final_pattern.extend(self.current_pattern)
        while len(final_pattern) > len(signal):
            final_pattern.pop()
        self.fitted_pattern = final_pattern

    def make_pattern(self, sig_index):
        new_pattern = deque()
        for value in range(len(self.pattern)):
            for _ in range(sig_index + 1):
                new_pattern.append(self.pattern[value])
        new_pattern.append(new_pattern.popleft())
        self.current_pattern = new_pattern
        

def d16p1():
    with open("inputday16.txt", "r") as f:
        sig = f.read()
    # print(len(sig))
    # signal = Signal(sig)
    signal = Signal(sig)
    pattern = Pattern("0,1,0,-1")
    desired_phase = 1
    count = 0
    while count < desired_phase:
        new_signal = apply_pattern(signal, pattern)
        signal = Signal(new_signal)
        count += 1
    return new_signal[-8:]

def d16p2():
    with open("inputday16.txt", "r") as f:
        sig = f.read()
    # signal = Signal(sig*2)
    signal = Signal(sig)
    heck = len(signal.signal)
    pattern = Pattern("0,1,0,-1")
    amount_to_add = sets_to_answer()
    desired_phase = 1
    count = 0
    while count < desired_phase:
        new_signal = apply_pattern(signal, pattern)
        signal = Signal(new_signal)
        count += 1
        print(count)
    a = new_signal[-1950:-1300], new_signal[-1300:-650], new_signal[-650:]
    with open("test.txt", "a") as f:
        f.write(str(a) + "\n")
    # mid_ans = []
    # for num in chunk[487:495]:
    #     mid_ans.append(last_digit(int(num) + 5))
    # return "".join(mid_ans)


#5979187 idea it seems that every 2 repeats sets one set of the input from back to front
# so assuming that holds then at 10000 repeats the last 50000 sets of input are set
#and then what else i noticed was that the difference between the first one set and the next one
#is that you just add 1 to each individual digit but the amount changes
if __name__ == "__main__":
    # print(d16p1())
    # print(sets_to_answer())
    # print(d16p2())