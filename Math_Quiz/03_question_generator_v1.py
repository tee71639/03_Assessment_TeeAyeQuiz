import random

number_one = random.randrange(1, 15)
number_two = random.randrange(1, 15)
answer = number_one + number_two
question = ("{} + {} = ?".format(number_one, number_two))
print(question)