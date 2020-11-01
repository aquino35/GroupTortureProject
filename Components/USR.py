from Components.BaseComponent import BaseComponent


class usr(BaseComponent):
    """
        Description:
        This is the Universal Shift Register (USR) component class of the digital system.
        The USR has four operations which are the following: shift to the left,
        shift to the right, parallel load and idle. Shift to the left would take the incoming value(one value)
        and add this value to the left side of the list and pop out the last values of it. Same concept applies
        to the shift to the right, just the reverse function. The parallel function would take four new values
        and replace the interior values of the universal shift register. Finally in the idle state no changes
        occur. This operation can only happen when the clock value is one, and while in zero no operation would
        occur.
        This method receive an list, the first values represent the new values to be added to the list.
        The second and third values of the list decided the operation of the Universal shift register.
        The fourth to the seventh values represent the new for values to load on the Universal shift register.
        The last value receive the clock value.
        ValueErrors: A USR Object must have 8 input values.
    """

    def __init__(self, name, interior_seq=[None, None, None, None]):
        """
            Description:
            This initialization method ...
            @:param (name): name of the component provided by the user
            @:param (intrior_seq): initial value of the universal state register
        """
        super().__init__(name)
        self.interior_seq = interior_seq
        # self.clk = clk

    """    
      The following take the incoming list(interior_seq) of binary number and shift these to
      right to be received by another list(exterior_seq) of 
    """

    def Output(self, exterior_n):
        """
        Description:
        @:param(exterior_n): List of eight values use to operate the USR
        """
        self.checked = False
        self.checkInputErrors(exterior_n)
        self.exterior_n = exterior_n[0]
        self.clk = exterior_n[7]
        method = exterior_n[1:3]
        parallel_load = exterior_n[3:7]
        if self.clk == 1:
            if method == [0, 0]:
                self.shift_serial(self.interior_seq, self.exterior_n)

            if method == [0, 1]:
                self.interior_seq.reverse()
                self.shift_serial(self.interior_seq, self.exterior_n)
                self.interior_seq.reverse()

            if method == [1, 0]:
                self.interior_seq = parallel_load
                # print(self.interior_seq)
                self.result = self.interior_seq

            elif method == [1, 1]:
                self.result= self.interior_seq  # stays idle
        else:
            return self.result
            #raise Exception("Usr not operating")

    def shift_serial(self, input1, input2):
        input1.insert(0, input2)
        self.result = input1.pop()

    def output(self):
        return self.result, 'Current Registry:', self.interior_seq

    def checkInputErrors(self, inputs):
        if not self.checked:
            length = len(inputs)
            if length < 8 or length > 8:
                raise Exception("A USR object must have 8 inputs")
            else:
                self.checked = True
