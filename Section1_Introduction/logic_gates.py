""" Logic Gates Circuit Builder """


class LogicGate:
    """ Logic Gate class """

    def __init__(self, n):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    """ Binary Gate class """

    def __init__(self, n):
        super().__init__(n)
        self.pin_A = None
        self.pin_B = None

    def get_pin_A(self):
        if self.pin_A == None:
            return int(
                input("Enter Pin A input for gate {} --> ".format(self.get_label()))
            )
        else:
            return self.pin_A.get_from().get_output()

    def get_pin_B(self):

        if self.pin_B == None:
            return int(
                input("Enter Pin B input for gate {} --> ".format(self.get_label()))
            )
        else:
            return self.pin_B.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin_A == None:
            self.pin_A = source

        elif self.pin_B == None:
            self.pin_B = source

        else:
            print("Cannot connect: No Empty Pins Available on this Gate")


class AndGate(BinaryGate):
    """ AND Gate class """

    def __init__(self, n):
        super().__init__(n)

    def perform_gate_logic(self):
        a = self.get_pin_A()
        b = self.get_pin_B()

        if a and b:
            return 1

        else:
            return 0


class OrGate(BinaryGate):
    """ OR Gate class """

    def __init__(self, n):
        super().__init__(n)

    def perform_gate_logic(self):
        a = self.get_pin_A()
        b = self.get_pin_B()

        if a or b:
            return 1

        else:
            return 0


class NandGate(AndGate):
    """ NAND Gate class """

    def perform_gate_logic(self):
        if super().perform_gate_logic():
            return 0
        else:
            return 1


class NorGate(OrGate):
    """ NOR Gate class """

    def perform_gate_logic(self):
        if super().perform_gate_logic():
            return 0
        else:
            return 1


class XorGate(BinaryGate):
    """ XOR Gate class """

    def __init__(self, n):
        super().__init__(n)

    def perform_gate_logic(self):
        a = self.get_pin_A()
        b = self.get_pin_B()

        if (a and b) or (not a and not b):
            return 0

        else:
            return 1


class XnorGate(XorGate):
    """ XNOR Gate class """

    def perform_gate_logic(self):
        if super().perform_gate_logic():
            return 0
        else:
            return 1


class UnaryGate(LogicGate):
    """Unary Gate class """

    def __init__(self, n):
        super().__init__(n)
        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(
                input("Enter Pin input for gate {} --> ".format(self.get_label()))
            )
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot connect: No Empty Pins Available on this Gate")


class NotGate(UnaryGate):
    """ NOT Gate class """

    def __init__(self, n):
        super().__init__(n)

    def perform_gate_logic(self):
        a = self.getPin()
        if a:
            return 0
        else:
            return 1


class Connector:
    """ Connector class with Has-A relationship with 2 from and to gates """

    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate

        to_gate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate


def main():
    g5 = NandGate("G5")
    print(g5.get_output())

    g6 = NorGate("G6")
    print(g6.get_output())

    g7 = XorGate("G7")
    print(g7.get_output())

    g8 = XnorGate("G8")
    print(g8.get_output())


if __name__ == "__main__":
    main()
