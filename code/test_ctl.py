# Python program to create a set containing square of all numbers from 1 to 6.

class Ctl_test:
    set_inp = {x for x in range(1, 70)}
    lis_out = []

    def get_next_inp_tst(self):
        if len(self.set_inp) == 0 : return None
        next_inp= self.set_inp.pop()
        print (next_inp)
        return next_inp
    # def test1():
    #     while len(self.set_inp) > 0:
    #         get_next_inp()

    def set_next_out_tst(self,value):
        self.lis_out.append(value)



