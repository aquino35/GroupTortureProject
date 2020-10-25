

from GroupTortureProject.Components.Init import Init

class usr(Init):
    def __init__(self , name, clk, interior_seq):
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
                print(self.interior_seq)

            if method == 1:
                self.interior_seq.reverse()

                self.shift_serial(self.interior_seq, self.exterior_n)
                self.interior_seq.reverse()
                print(self.interior_seq)

            if method == 2:
                self.interior_seq = self.exterior_n
                print(self.interior_seq)
                self.interior_seq = self.result


        else:
            print("jajajajaj")

    def shift_serial(self, aaa, bbb):

        aaa.insert(0, bbb)
        self.result = aaa.pop()

        print(self.result)