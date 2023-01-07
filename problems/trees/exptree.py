class Int:
    def __init__(self, n):
        self.n = n

    def is_const(self):
        return True

    def num_nodes(self):
        return 1

    def eval(self):
        return self.n

    def __str__(self):
        return str(self.n)


class Plus:
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def is_const(self):
        return False

    def num_nodes(self):
        return 1 + self.op1.num_nodes() + self.op2.num_nodes()

    def eval(self):
        op1_value = self.op1.eval()
        op2_value = self.op2.eval()

        return op1_value + op2_value

    def __str__(self):
        op1_str = str(self.op1)
        op2_str = str(self.op2)

        return f"({op1_str} + {op2_str})"


class Times:
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def is_const(self):
        return False

    def num_nodes(self):
        return 1 + self.op1.num_nodes() + self.op2.num_nodes()

    def eval(self):
        op1_value = self.op1.eval()
        op2_value = self.op2.eval()

        return op1_value * op2_value

    def __str__(self):
        op1_str = str(self.op1)
        op2_str = str(self.op2)

        return f"({op1_str} * {op2_str})"


if __name__ == "__main__":

    # Sample expression tree for (2 + (3 * 5))
    op1 = Int(2)
    op2 = Times(Int(3), Int(5))
    expt = Plus(op1, op2)

    print(f"{expt} = {expt.eval()}")