#-*- coding:utf-8-*-

stdChar = ['<', '>', '+', '-', '[', ']', ',', '.']
expandChar = {
    'notes': ['#'],
    'num': [str(n) for n in range(1, 10)],
}


class Stack():
    def __init__(self):
        self.__stack = []

    def sin(self, pc: int):
        self.__stack.append(pc)

    def sout(self):
        if len(self.__stack) == 0:
            return 0
        else:
            self.__stack.pop(-1)
            return 1

    def get(self):
        return self.__stack[-1]


class Tape():
    def __init__(self):
        self.__tape = [0]
        self.__ptr = 0

    def set(self, num):
        self.__tape[self.__ptr] = num

    def get(self):
        return self.__tape[self.__ptr]

    def add(self, num: int = 1):
        self.__tape[self.__ptr] += num

    def minus(self, num: int = 1):
        if self.__tape[self.__ptr] - num < 0:
            raise RuntimeError("Zero - Error")
        self.__tape[self.__ptr] -= num

    def advance(self, step: int = 1):
        if self.__ptr + step >= len(self.__tape):
            for _ in range(self.__ptr + step + 1 - len(self.__tape)):
                self.__ptr += 1
                self.__tape.append(0)
        else:
            self.__ptr += step

    def deadvance(self, step: int = 1):
        if self.__ptr - step < 0:
            raise RuntimeError("Zero < Error")
        self.__ptr -= step

    def show(self):
        print('p:', self.__ptr, self.__tape)


class BF():
    def __init__(self, code: str):
        self.__code = code
        self.__pc = 0
        self.__tape = Tape()
        self.__bracketStack = Stack()

    def run(self):
        while self.__pc < len(self.__code):
            self.parse(self.__code[self.__pc])
            self.__pc += 1
        self.__tape.show()

    def gotoAdvance(self):
        self.__pc += 1
        while self.__pc < len(self.__code):
            if self.__code[self.__pc] == '[':
                self.__bracketStack.sin(self.__pc)
            elif self.__code[self.__pc] == ']':
                if self.__bracketStack.sout() == 0:
                    break
            else:
                pass
            self.__pc += 1

    def gotoDeadvance(self, ):
        self.__pc -= 1
        while self.__pc > 0:
            if self.__code[self.__pc] == ']':
                self.__bracketStack.sin(self.__pc)
            elif self.__code[self.__pc] == '[':
                if self.__bracketStack.sout() == 0:
                    break
            else:
                pass
            self.__pc -= 1

    def parse(self, char):
        if char not in stdChar:
            pass
        if char == '<':
            self.__tape.deadvance()
        elif char == '>':
            self.__tape.advance()
        elif char == '+':
            self.__tape.add()
        elif char == '-':
            self.__tape.minus()
        elif char == ',':
            inputChar = ord((input("Inpute ASCII Char:") + '\n')[0])
            self.__tape.set(inputChar)
        elif char == '.':
            print(chr(self.__tape.get()))
        elif char == '[':
            if self.__tape.get() == 0:
                self.gotoAAdvance()
        elif char == ']':
            if self.__tape.get() != 0:
                self.gotoDeadvance()
code = '++++++++++ [ >+++++++ >++++++++++ >+++ >+ <<<<- ] >++. >+. +++++++.. +++. >++. <<+++++++++++++++. >. +++. ------. --------. >+. >.'
bf = BF(code)
bf.run()
