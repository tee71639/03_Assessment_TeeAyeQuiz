import random
import operator


def randomCalc():
       score = 0
       for i in range(0, 10):
              ops = {'+':operator.add,
                     '-':operator.sub,
                     '*':operator.mul}
              num1 = random.randint(0,12)
              num2 = random.randint(1,10)   # don't sample 0's to protect against divide-by-zero
              op = random.choice(list(ops.keys()))
              answer = ops.get(op)(num1,num2)
              question = int(input('What is {} {} {}?\n'.format(num1, op, num2)))
              if question == answer:
                     print("correct\n")
                     score = score + 1
              else:
                     print("incorrect\n")

       print("Your score was {}/10".format(score))

randomCalc()