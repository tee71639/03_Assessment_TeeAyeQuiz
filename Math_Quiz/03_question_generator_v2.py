import random
import operator

def randomCalc():
       for i in range(0, 15):
              ops = {'+':operator.add,
                     '-':operator.sub,
                     '*':operator.mul,
                     '/':operator.truediv}
              num1 = random.randint(0,12)
              num2 = random.randint(1,10)   # don't sample 0's to protect against divide-by-zero
              op = random.choice(list(ops.keys()))
              answer = ops.get(op)(num1,num2)
              question = int(input('What is {} {} {}?\n'.format(num1, op, num2)))
              if question == answer:
                     print("correct\n")
              else:
                     print("incorrect\n")

randomCalc()