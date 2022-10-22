import random

class DNA: #1
    def __init__(self, chain: str, cchain=''):
        self.chain = chain # первая цепь
        self.cchain = cchain # комплементарная цепь
        for i in range(len(self.chain)):
            if (self.chain[i]!='A') and (self.chain[i]!='T') and (self.chain[i]!='G') and (self.chain[i]!='C'):
                raise Exception('This is not DNA!')        
        for i in range(len(self.chain)):
            if self.chain[i] == 'A':
                self.cchain = self.cchain + 'T'
            if self.chain[i] == 'T':
                self.cchain = self.cchain + 'A'
            if self.chain[i] == 'G':
                self.cchain = self.cchain + 'C'
            if self.chain[i] == 'C':
                self.cchain = self.cchain + 'G'

    #2
    def printdna(self, index : int):     
        print('[', self.chain[index], ',', self.cchain[index], ']')

    #4
    def ligation(self, other) -> 'DNA':
        self.chain += other.chain
        self.cchain += other.cchain
        print('[', self.chain, ',', self.cchain, ']')

    #6
    def multiplication(self, other) -> 'DNA':
        newchain = ''
        newcchain = ''
        if len(self.chain) > len(other.chain):
            for i in range(len(other.chain)):
                if random.choice([0,1]) == 1:
                    newchain += other.chain[i]
                else:
                    newchain += self.chain[i]
            for i in range(len(other.chain), len(self.chain)):
                    newchain += self.chain[i]
        else:
            for i in range(len(self.chain)):
                if random.choice([0,1]) == 1:
                    newchain += other.chain[i]
                else:
                    newchain += self.chain[i]
            for i in range(len(self.chain), len(other.chain)):
                    newchain += other.chain[i]
        for i in range(len(newchain)):
            if newchain[i] == 'A':
                newcchain = newcchain + 'T'
            if newchain[i] == 'T':
                newcchain = newcchain + 'A'
            if newchain[i] == 'G':
                newcchain = newcchain + 'C'
            if newchain[i] == 'C':
                newcchain = newcchain + 'G'
        self.chain = newchain
        self.cchain = newcchain
        print('[', self.chain, ',', self.cchain, ']')

    #7 (учитывается наличие у ДНК и РНК 3' и 5' концов)
    def comparewithrna(self, other) -> str:
        k = 0
        s = 0
        if len(self.chain) != len(other.chain):
            return 'False'
        else:
            for i in range(len(self.chain)):
                if (self.chain[i] != other.chain[i]) and not((self.chain[i] == 'T') and (other.chain[i] == 'U')):
                    k = 1
            for i in range(len(self.cchain)):
                if (self.cchain[len(self.cchain)-i-1] != other.chain[i]) and not((self.cchain[len(self.cchain)-i-1] == 'T') and (other.chain[i] == 'U')):
                    s = 1                
        if k == 1 and s == 1 :
            return 'False'
        else:
            return 'True'

    #8
    # "Вывод print"
    def __str__(self) -> str:
        return f'[{self.chain}, {self.cchain}]'
    
    # "Вывод при вызове в ячейке ноутбука"
    def __repr__(self) -> str:
        return f'[{self.chain}, {self.cchain}]'

####################################################################################################

class RNA: #1
    def __init__(self, chain: str):
        self.chain = chain
        for i in range(len(self.chain)):
            if (self.chain[i]!='A') and (self.chain[i]!='U') and (self.chain[i]!='G') and (self.chain[i]!='C'):
                raise Exception('This is not RNA!')

    #2    
    def printrna(self, index : int):
        print(self.chain[index])

    #3
    def complementdna(self):
        dnachain1 = ''
        dnachain2 = ''
        for i in range(len(self.chain)):
            if self.chain[i] == 'A':
                dnachain1 = dnachain1 + 'T'
            if self.chain[i] == 'U':
                dnachain1 = dnachain1 + 'A'
            if self.chain[i] == 'G':
                dnachain1 = dnachain1 + 'C'
            if self.chain[i] == 'C':
                dnachain1 = dnachain1 + 'G'
        for i in range(len(dnachain1)):
            if dnachain1[i] == 'A':
                dnachain2 = dnachain2 + 'T'
            if dnachain1[i] == 'T':
                dnachain2 = dnachain2 + 'A'
            if dnachain1[i] == 'G':
                dnachain2 = dnachain2 + 'C'
            if dnachain1[i] == 'C':
                dnachain2 = dnachain2 + 'G'
        dnahelix = [dnachain1, dnachain2]
        print(dnahelix)

    #4
    def ligation(self, other) -> 'RNA':
        self.chain += other.chain
        print(self.chain)

    #5
    def multiplication(self, other) -> 'RNA':
        newchain = ''
        if len(self.chain) > len(other.chain):
            for i in range(len(other.chain)):
                if random.choice([0,1]) == 1:
                    newchain += other.chain[i]
                else:
                    newchain += self.chain[i]
            for i in range(len(other.chain), len(self.chain)):
                    newchain += self.chain[i]
        else:
            for i in range(len(self.chain)):
                if random.choice([0,1]) == 1:
                    newchain += other.chain[i]
                else:
                    newchain += self.chain[i]
            for i in range(len(self.chain), len(other.chain)):
                    newchain += other.chain[i]
        self.chain = newchain
        print(self.chain)

    #7 (учитывается наличие у ДНК и РНК 3' и 5' концов)
    def comparewithdna(self, other) -> str:
        k = 0
        s = 0
        if len(self.chain) != len(other.chain):
            return 'False'
        else:
            for i in range(len(self.chain)):
                if (self.chain[i] != other.chain[i]) and not((self.chain[i] == 'U') and (other.chain[i] == 'T')):
                    k = 1
            for i in range(len(self.chain)):
                if (self.chain[i] != other.cchain[len(other.cchain)-i-1]) and not((self.chain[i] == 'U') and (other.cchain[len(other.cchain)-i-1] == 'T')):
                    s = 1                
        if k == 1 and s == 1 :
            return 'False'
        else:
            return 'True'

    #8
    # "Вывод print"
    def __str__(self) -> str:
        return f'{self.chain}'
    
    # "Вывод при вызове в ячейке ноутбука"
    def __repr__(self) -> str:
        return f'{self.chain}'
