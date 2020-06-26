from enum import Enum

def compute(mem):
    while True:
        opcode = mem.next_command()
        opcode = OpCode(opcode)
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
    if opcode.opcode == 1:
        return AddOp(opcode)
    elif opcode.opcode == 2:
        return MultOp(opcode)
    elif opcode.opcode == 3:
        return InputOp(opcode)
    elif opcode.opcode == 4:
        return OutputOp(opcode)
    elif opcode.opcode == 99:
        return None
    else:
        raise RuntimeError(f"Unspecified command: {opcode.opcode()}")


class Operation:
    def __init__(self, n_args, opcode):
        self.n_args = n_args
        self.opcode = opcode

    def parse_arg(self, memory, param, value):
        if param == ParameterMode.POSITION:
            return memory.get_value(value)
        elif param == ParameterMode.IMMEDIATE:
            return value
        elif param == ParameterMode.RELATIVE:
            raise RuntimeError("Unimplemented")

    def get_args(self, memory, code):
        p_data = memory.get_count_after_pc(self.n_args)
        p_modes  = [self.opcode.p1, self.opcode.p2, self.opcode.p3]

        if code == 3 or code == 4:
            return p_data[0]
        else:
            args = [
            self.parse_arg(memory, mode, val) 
            for val, mode in zip(p_data, p_modes[:self.n_args])
            ]
            if p_modes[-1].value == 0:
                args.pop()
                args.append(p_data[-1])
                return args #appended last data point to save at said location
            elif p_modes[-1].value == 1:
                args.pop()
                args.append(self.pc - 1) #as 1 is immediate appends position of argument
                return args


            

    # def parse_arg(self, memory, param, value):
    #     if param == ParameterMode.POSITION:
    #         return memory.get_value(value)
    #     elif param == ParameterMode.IMMEDIATE:
    #         return value
    #     elif param == ParameterMode.RELATIVE:
    #         raise RuntimeError("Unimplemented")


class AddOp(Operation):
    def __init__(self, opcode):
        self.code = 1
        super(AddOp, self).__init__(3, opcode)
        
    def run_operation(self, memory):
        val1, val2, save_at = self.get_args(memory, self.code)
        # print(val1, val2, save_at)
        ans = val1+val2
        memory.set_mem(save_at, ans)


class MultOp(Operation):
    def __init__(self, opcode):
        self.code = 2
        super(MultOp, self).__init__(3, opcode)
        
    def run_operation(self, memory):
        val1, val2, save_at = self.get_args(memory, self.code)
        ans = val1*val2
        memory.set_mem(save_at, ans)


class InputOp(Operation):
    def __init__(self, opcode):
        self.code = 3
        super(InputOp, self).__init__(1, opcode)
        
    def run_operation(self, memory):
        save_at = self.get_args(memory, self.code)
        # ans = int(input("Enter the intcode input: "))
        ans = 1
        memory.set_mem(save_at, ans)


class OutputOp(Operation):
    def __init__(self, opcode):
        self.code = 4
        super(OutputOp, self).__init__(1, opcode)

    def run_operation(self, memory):
        ans = self.get_args(memory, self.code)
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

    def get_value(self, location): #take an input saying which mode it's in then get the value accrodingly
        try:
            return self.memory[location]
        except:
            raise RuntimeError(f"Memory location {location} out of bounds")

class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2

class OpCode:
    def __init__(self, opcode_int): # 01101
        self.opcode = opcode_int % 100
        self.p1 = ParameterMode(opcode_int // 100 % 10 % 10)
        self.p2 = ParameterMode(opcode_int // 1000 % 10)
        self.p3 = ParameterMode(opcode_int // 10000)

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
    with open('pair_programming/inputday5.txt', 'r') as in_file:
        program = in_file.read()
    mem = Memory(program)
    output = compute(mem)
    return output

if __name__ == "__main__":
    # print(d2p2())
    print(d5p1()[0])