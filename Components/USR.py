

from GroupTortureProject.Components.Init import Init

class usr(Init):

    """
    The following class simulates the electrical component Universal Shift Register (USR)
    Its job is too ..
    """
    def __init__(self , name, clk, interior_seq):
        """
        This initialization method ...
        @:param (name):
        @:param (clck):
        @:param (intrior_seq):
        """
        super().__init__(name)
        self.interior_seq = interior_seq
        self.clk = clk
        self.result = 0

    """    
      The following take the incoming list(interior_seq) of binary number and shift these to
      right to be received by another list(exterior_seq) of 
    """

    def Output(self, exterior_n):
        self.exterior_n = exterior_n[0]
        method = exterior_n[1]
        if self.clk:
            if method == 0:
                self.shift_serial(self.interior_seq, self.exterior_n)

            if method == 1:
                self.interior_seq.reverse()
                self.shift_serial(self.interior_seq, self.exterior_n)
                self.interior_seq.reverse()

            if method == 2:
                self.interior_seq = self.exterior_n
                print(self.interior_seq)
                self.interior_seq = self.result

            elif(method>2):
                #raise Exception("The function is not valid")
                raise ValueError("The function is not valid")

    def shift_serial(self, input1, input2):
        input1.insert(0, input2)
        self.result = input1.pop()
