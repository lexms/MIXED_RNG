# NIM : 10116370
# Nama : Alexander M S
# Kelas : MOSI-8

class GenerateRandomNumber:
    def __init__(self):
        self.a = 231
        self.c = 721
        self.m = 1693
        self.n = 2
        self.z0 = 10116370
        self.count = 300

    def mix_RNG_formula(self, Zi_minus_1):
        a_pow_n = pow(self.a,self.n)

        temp_Z = (  ( a_pow_n * Zi_minus_1 )+( (a_pow_n-1)/(self.a-1) * self.c )  )

        return temp_Z % self.m

    def uniform_generate(self, zi):
        return zi / self.m

    def RNG_mix(self):
        _list = []
        for i in range(0,self.count):
            if i == 0:
                #Zi-1 = Z0
                zi = self.mix_RNG_formula(self.z0)
                u = self.uniform_generate(zi)
                _list.append({'Zi-1': self.z0, 'Zi':zi,'U': u})
            elif i > 0:
                Zi_minus_1 = self.mix_RNG_formula(_list[i-1]['Zi-1']) 
                zi = self.mix_RNG_formula(Zi_minus_1)
                u = self.uniform_generate(zi)
                _list.append({'Zi-1': Zi_minus_1, 'Zi':zi,'U': u})
                
        return _list

    def RNG_print(self):
        _list = self.RNG_mix()
        print('No.\t |     Zi-1      |      Zi       |       Ui      |')
        print('-----------------------------------------------')
        for i in range(0,len(_list)):
            print("{}\t | {:.4f} \t | {:.4f} \t | {:.4f} \t |".format(i+1, _list[i]['Zi-1'], _list[i]['Zi'], _list[i]['U']))


test = GenerateRandomNumber()

test.RNG_print()

