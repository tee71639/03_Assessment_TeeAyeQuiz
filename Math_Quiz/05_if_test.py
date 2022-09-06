import operator
import random
difficulty = "easy"

if difficulty == "easy":
    ops = {'+':operator.add,
    '-':operator.sub}
    num1 = random.randint(0, 15)
    num2 = random.randint(1, 15)
    op,fn = random.choice(ops)
    fn(num1, num2)
    # self.question_box.config(text = "{} {} {}".format(num1, [op], num2))

elif difficulty == "normal":
    ops = {'+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv}
    num1 = random.randint(0, 50)
    num2 = random.randint(1, 50)
    op,fn = random.choice(list(ops)())
    answer = fn(num1, num2)
    

else:
    ops = {'*':operator.mul,
    '/':operator.truediv}
    num1 = random.randint(50, 500)
    num2 = random.randint(50, 500)
    op,fn = random.choice(ops())
    fn(num1, num2)        