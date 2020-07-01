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
    signal = Signal(sig)
    pattern = Pattern("0,1,0,-1")
    desired_phase = 100
    count = 0
    while count < desired_phase:
        new_signal = apply_pattern(signal, pattern)
        signal = Signal(new_signal)
        count += 1
    return new_signal[:8]

if __name__ == "__main__":
    print(d16p1())