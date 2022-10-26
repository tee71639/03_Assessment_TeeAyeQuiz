import random
import operator

# Division only experiment...
def randomCalc():
       for i in range(0, 15):
              ops = {
                     '/':operator.truediv}
              num1 = random.randint(0,12)
              num2 = random.randint(1,12)   # don't sample 0's to protect against divide-by-zero
              op = random.choice(list(ops.keys()))
              answer = ops.get(op)(num1,num2)
              question = int(input('What is {} {} {}?\n'.format(num1, op, num2)))
              if question == answer:
                     print("correct\n")
              else:
                     print("incorrect\n")

while True:
       randomCalc() 