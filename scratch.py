import operator

num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}
userOperator = input("Enter operator: ")
operation = ops[userOperator]
result = operation(int(num1), int(num2))
print(num1 + " " + userOperator + " " + num2 + " = " + str(result))
