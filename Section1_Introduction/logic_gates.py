""" Logic Gates Circuit Builder """


class LogicGate(object):
    """Logic gate class.
    
    Args: 
        n (str): Logic gate label description

    Attributes:
        label (str): Logic gate label description
        output (any): Output of the logic gate
    """

    def __init__(self, n):
        """LogicGate __init__ method.
        
        Args:
            n (str): Logic gate label description

        Attributes:
            label (str): Logic gate description
            output (any): Output of the logic gate
        """
        self.label = n
        self.output = None

    def get_label(self):
        """Gets the description from the logic gate.
        
        Returns:
            str: description of the logic gate
        """
        return self.label

    def get_output(self):
        """Gets the output from the logic gate.
        
        Returns:
            (bool): Boolean value of the logic gate operation
        """
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    """Binary gate class.
    
    Args: 
        n (str): Logic gate label description

    Attributes:
        pin_A (LogicGate): Logic gate reference
        pin_B (LogicGate): Logic gate reference
    """

    def __init__(self, n):
        """Binnary gate __init__ method
        
        Args:
            n (str): Logic gate label description
        """
        super().__init__(n)
        self.pin_A = None
        self.pin_B = None

    def get_pin_A(self):
        """Returns pin A logic gate reference.
        
        Returns:
            (LogicGate): Returns pin A logic gate
        """
        if self.pin_A == None:
            return int(
                input("Enter Pin A input for gate {} --> ".format(self.get_label()))
            )
        else:
            return self.pin_A.get_from().get_output()

    def get_pin_B(self):
        """Returns pin B logic gate reference.
        
        Returns:
            (LogicGate): Returns pin B logic gate
        """
        if self.pin_B == None:
            return int(
                input("Enter Pin B input for gate {} --> ".format(self.get_label()))
            )
        else:
            return self.pin_B.get_from().get_output()

    def set_next_pin(self, source):
        """Sets pin reference for the current logic gate.

        If pin A is available, set reference for it.
        If pin A is occupied, set reference for pin B. 
        If bot references are occupied, print a message
        
        Args:
            source (LogicGate): Logic gate reference 
        """
        if self.pin_A == None:
            self.pin_A = source

        elif self.pin_B == None:
            self.pin_B = source

        else:
            print("Cannot connect: No Empty Pins Available on this Gate")


class AndGate(BinaryGate):
    """AND gate class
    
    Args:
        n (str): Logic gate label description
    """

    def __init__(self, n):
        """AND gate __init__ method
        
        Args:
            n (str): Logic gate label description
        """
        super().__init__(n)

    def perform_gate_logic(self):
        """Performs logic operation for the AND gate
        
        Returns:
            bool: True or False value result from the operation
        """
        a = self.get_pin_A()
        b = self.get_pin_B()

        if a and b:
            return 1

        else:
            return 0


class OrGate(BinaryGate):
    """OR gate class
    
    Args:
        n (str): Logic gate label description
    """

    def __init__(self, n):
        """OR gate __init__ method
        
        Args:
            n (str): Logic gate label description
        """
        super().__init__(n)

    def perform_gate_logic(self):
        """Performs logic operation for the OR gate
        
        Returns:
            bool: True or False value result from the operation
        """
        a = self.get_pin_A()
        b = self.get_pin_B()

        if a or b:
            return 1

        else:
            return 0


class NandGate(AndGate):
    """NAND gate class
    
    Args:
        n (str): Logic gate label description
    """

    def __init__(self, n):
        """NAND gate __init__ method
        
        Args:
            n (str): Logic gate label description
        """
        super().__init__(n)

    def perform_gate_logic(self):
        """Performs logic operation for the OR gate
        
        Returns:
            bool: True or False value result from the operation
        """
        if super().perform_gate_logic():
            return 0
        else:
            return 1


class NorGate(OrGate):
    """NOR gate class
    
    Args:
        n (str): Logic gate label description
    """

    def __init__(self, n):
        """NOR gate __init__ method
        
        Args:
            n (str): Logic gate label description
        """
        super().__init__(n)

    def perform_gate_logic(self):
        """Performs logic operation for the OR gate
        
        Returns:
            bool: True or False value result from the operation
        """
        if super().perform_gate_logic():
            return 0
        else:
            return 1


class XorGate(BinaryGate):
    """XOR gate class
    
    Args:
        n (str): Logic gate label description
    """

    def __init__(self, n):
        """XOR gate __init__ method
        
        Args:
            n (str): Logic gate label description
        """
        super().__init__(n)

    def perform_gate_logic(self):
        """Performs logic operation for the OR gate
        
        Returns:
            bool: True or False value result from the operation
        """
        a = self.get_pin_A()
        b = self.get_pin_B()

        if (a and b) or (not a and not b):
            return 0

        else:
            return 1


class XnorGate(XorGate):
    """XNOR gate class
    
    Args:
        n (str): Logic gate label description
    """

    def __init__(self, n):
        """XNOR gate __init__ method
        
        Args:
            n (str): Logic gate label description
        """
        super().__init__(n)

    def perform_gate_logic(self):
        """Performs logic operation for the OR gate
        
        Returns:
            bool: True or False value result from the operation
        """
        if super().perform_gate_logic():
            return 0
        else:
            return 1


class UnaryGate(LogicGate):
    """Unary gate class
    
    Args:
        n (str): Logic gate label description
    """

    def __init__(self, n):
        """Unary gate __init__ method
        
        Args:
            n (str): Logic gate label description
        """
        super().__init__(n)
        self.pin = None

    def get_pin(self):
        """Gets the pin output from the unary gate
        
        Returns:
            bool: True or False value from the pin output 
        """
        if self.pin == None:
            return int(
                input("Enter Pin input for gate {} --> ".format(self.get_label()))
            )
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        """Sets the next pin for the unary gate output
        
        Args:
            source (LogicGate): Logic gate to connect to
        """
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot connect: No Empty Pins Available on this Gate")


class NotGate(UnaryGate):
    """NOT gate class
    
    Args:
        n (str): Logic gate label description
    """

    def __init__(self, n):
        """NOT gate __init__ method
        
        Args:
            n (str): Logic gate label description
        """
        super().__init__(n)

    def perform_gate_logic(self):
        """Performs logic operation for the NOT gate
        
        Returns:
            bool: True or False value result from the operation
        """
        a = self.get_pin()
        if a:
            return 0
        else:
            return 1


class Connector(object):
    """Connect class for logic gates.

    This connector class allows logic gates to join their outputs and inputs. 
    This class Has-A relationship with 2 logic gates: 'from' and 'to'.
    
    Args: 
        from_gate (LogicGate): Starting logic gate
        to_gate (LogicGate): Ending logic gate

    Attributes: 
        from_gate (LogicGate): Starting logic gate
        to_gate (LogicGate): Ending logic gate

    """

    def __init__(self, from_gate, to_gate):
        """Connect __init__ method
        
        Args:
            from_gate (LogicGate): Starting logic gate
            to_gate (LogicGate): Ending logic gate
        """
        self.from_gate = from_gate
        self.to_gate = to_gate

        to_gate.set_next_pin(self)

    def get_from(self):
        """Gets the starting logic gate from the connector
        
        Returns:
            LogicGate: Starting logic gate from the connector
        """
        return self.from_gate

    def get_to(self):
        """Gets the ending logic gate from the connector
        
        Returns:
            LogicGate: Ending logic gate from the connector
        """
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
