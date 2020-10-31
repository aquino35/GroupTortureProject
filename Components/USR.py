from Components.BaseComponent import BaseComponent


class usr(BaseComponent):
    """
        Description:
        The following class simulates the electrical component Universal Shift Register (USR)
        Its job is too ..

    """

    def __init__(self, name, interior_seq=[None, None, None, None]):
        """
            Description:
            This initialization method ...
            @:param (name):
            @:param (clck):
            @:param (intrior_seq):
        """
        super().__init__(name)
        self.interior_seq = interior_seq
        # self.clk = clk

    """    
      The following take the incoming list(interior_seq) of binary number and shift these to
      right to be received by another list(exterior_seq) of 
    """

    def Output(self, exterior_n):

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
