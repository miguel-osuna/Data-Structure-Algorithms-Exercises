''' Logic Gates Circuit Builder '''


class LogicGate():
    ''' Logic Gate class '''

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    ''' Binary Gate class '''

    def __init__(self, n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate {} --> ".format(self.getLabel())))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):

        if self.pinB == None:
            return int(input("Enter Pin B input for gate {} --> ".format(self.getLabel())))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source

        elif self.pinB == None:
            self.pinB = source

        else:
            print("Cannot connect: No Empty Pins Available on this Gate")


class AndGate(BinaryGate):
    ''' AND Gate class '''

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a and b:
            return 1

        else:
            return 0


class OrGate(BinaryGate):
    ''' OR Gate class '''

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a or b:
            return 1

        else:
            return 0


class NandGate(AndGate):
    ''' NAND Gate class '''

    def performGateLogic(self):
        if super().performGateLogic():
            return 0
        else:
            return 1


class NorGate(OrGate):
    ''' NOR Gate class '''

    def performGateLogic(self):
        if super().performGateLogic():
            return 0
        else:
            return 1


class XorGate(BinaryGate):
    ''' XOR Gate class '''

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if (a and b) or (not a and not b):
            return 0

        else:
            return 1


class XnorGate(XorGate):
    ''' XNOR Gate class '''

    def performGateLogic(self):
        if super().performGateLogic():
            return 0
        else:
            return 1


class UnaryGate(LogicGate):
    '''Unary Gate class '''

    def __init__(self, n):
        super().__init__(n)
        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate {} --> ".format(self.getLabel())))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot connect: No Empty Pins Available on this Gate")


class NotGate(UnaryGate):
    ''' NOT Gate class '''

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPin()
        if a:
            return 0
        else:
            return 1


class Connector():
    ''' Connector class with Has-A relationship with 2 from and to gates '''

    def __init__(self, fromgate, togate):
        self.fromgate = fromgate
        self.togate = togate

        togate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


if __name__ == "__main__":
    # g1 = AndGate("G1")
    # g2 = AndGate("G2")
    # g3 = OrGate("G3")
    # g4 = NotGate("G4")
    # c1 = Connector(g1, g3)
    # c2 = Connector(g2, g3)
    # c3 = Connector(g3, g4)
    # print(g4.getOutput())

    g5 = NandGate("G5")
    print(g5.getOutput())

    g6 = NorGate("G6")
    print(g6.getOutput())

    g7 = XorGate("G7")
    print(g7.getOutput())

    g8 = XnorGate("G8")
    print(g8.getOutput())
