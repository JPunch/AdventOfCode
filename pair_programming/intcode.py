def compute(mem):
    while True:
        opcode = mem.next_command()

        # Create opcode handling object
        operation = opcode_factory(opcode)

        if operation is None:
            break

        # Mutate memory
        operation.run_operation(mem)
        # end step

    return mem.memory

def parse_string(mem_string):
    return [int(num) for num in mem_string.strip().split(",")]

def opcode_factory(opcode):
    if opcode == 1:
        return AddOp()
    elif opcode == 2:
        return MultOp()
    elif opcode ==3:
        return InputOp()
    elif opcode ==4:
        return OutputOp()
    elif opcode == 99:
        return None
    else:
        raise RuntimeError("Unspecified command")


class Operation:
    def __init__(self, n_args):
        self.n_args = n_args

    def get_args(self, memory):
        return memory.get_count_after_pc(self.n_args)


class AddOp(Operation):
    def __init__(self):
        self.code = 1
        super(AddOp, self).__init__(3)
        
    def run_operation(self, memory):
        ref1, ref2, save_at = self.get_args(memory)
        val1 = memory.get_value(ref1)
        val2 = memory.get_value(ref2)
        ans = val1+val2
        memory.set_mem(save_at, ans)


class MultOp(Operation):
    def __init__(self):
        self.code = 2
        super(MultOp, self).__init__(3)
        
    def run_operation(self, memory):
        ref1, ref2, save_at = self.get_args(memory)
        val1 = memory.get_value(ref1)
        val2 = memory.get_value(ref2)
        ans = val1*val2
        memory.set_mem(save_at, ans)


class InputOp(Operation):
    def __init__(self):
        self.code = 3
        super(InputOp, self).__init__(1)
        
    def run_operation(self, memory):
        save_at = self.get_args(memory)
        ans = input("Enter the intcode input")
        memory.set_mem(save_at, ans)


class OutputOp(Operation):
    def __init__(self):
        self.code = 4
        super(OutputOp, self).__init__(1)

    def run_operation(self, memory):
        ans = self.get_args(memory)
        print(ans)


class Memory:
    def __init__(self, memory):
        self.memory = parse_string(memory)
        self.pc = 0

    def next_command(self):
        if self.pc < len(self.memory):
            return self.memory[self.pc]
        else:
            raise RuntimeError(f"Memory location {self.pc} out of bounds")
    
    def get_count_after_pc(self, n_args):
        arg_start_id = self.pc + 1
        args = self.memory[arg_start_id : arg_start_id + n_args]
        self.pc += n_args + 1
        return args

    def set_mem(self, location, value):
        try:
            self.memory[location] = value
        except:
            raise RuntimeError(f"Memory location {location} out of bounds")

    def get_value(self, location):
        try:
            return self.memory[location]
        except:
            raise RuntimeError(f"Memory location {location} out of bounds")


def d2p1():
    with open('inputday2.txt', 'r') as in_file:
        program = in_file.read()
    mem = Memory(program)
    mem.set_mem(1, 12)
    mem.set_mem(2, 2)
    output = compute(mem)
    print(output[0])

def d2p2():
    with open('inputday2.txt', 'r') as in_file:
        program = in_file.read()
    for i in range(100):
        for j in range(100):
            mem = Memory(program)
            mem.set_mem(1, i)
            mem.set_mem(2, j)
            ans = compute(mem)[0]
            if ans == 19690720:
                return (100*i + j)

def d5p1():
    pass

if __name__ == "__main__":
    print(d2p2())