class Calc:


    def add(self,a,b):
        return a + b
    def minus(self,a,b):
        return a - b
    def mult(self,a,b):
        return a * b
    def div(self,a,b):
        return a / b

    @staticmethod
    def pr(a,b):
        return a % b
    @staticmethod
    def rp(a,b):
        return a**b

cal = Calc()
def input_ask():
    a = int(input('First Number: '))
    b = int(input('Second Number: '))
    return a,b
c = input("+, -, *, /,%,**: ")
if c in ['+','-','*','/','%','**']:
    num1,num2 = input_ask()



    if c == '+':
        print('Result: ',cal.add(num1,num2))
    if c == '-':
        print('Result: ',cal.minus(num1,num2))
    if c == '*':
        print('Result: ',cal.mult(num1,num2))
    if c == '/':
        print('Result: ',cal.div(num1,num2))
    if c == '%':
        ss = input(" можете ли вы заплатить 10 $:")
        if ss == "yes":
            ff = input("Pay 10$: ")
            if ff >= '10':
                print("Thank you",cal.pr(num1,num2))
    if c == '**':
        ss = input("можете ли вы заплатить 10 $: ")
        if ss == "да":
            ff = input("оплати 10$: ")
            if ff >= 10:
                print("спасибо", cal.rp(num1, num2))