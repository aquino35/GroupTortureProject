from GroupTortureProject.Components.BaseComponent import BaseComponent


class usr(BaseComponent):
    """
    The following class simulates the electrical component Universal Shift Register (USR)
    Its job is too ..
    """

    def __init__(self, name, interior_seq=[None, None, None, None]):
        """
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

        self.exterior_n = exterior_n[0]
        self.clk = exterior_n[7]
        method = exterior_n[1:3]
        parallel_load = exterior_n[3:7]

        if not self.interior_seq == None:
            if self.clk:
                if method == [0, 0]:
                    self.shift_serial(self.interior_seq, self.exterior_n)

                if method == [0, 1]:
                    self.interior_seq.reverse()
                    self.shift_serial(self.interior_seq, self.exterior_n)
                    self.interior_seq.reverse()

                if method == [1, 0]:
                    self.interior_seq = parallel_load
                    # print(self.interior_seq)
                    self.interior_seq = self.result

                elif method == [1, 1]:
                    self.interior_seq = self.result  # stays idle

    def shift_serial(self, input1, input2):
        input1.insert(0, input2)
        self.result = input1.pop()

    def output(self):
        return self.result, 'Current Registry:', self.interior_seq
