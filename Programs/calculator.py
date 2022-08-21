first_num = float(input("Enter first number>>"))
second_num = float(input("Enter second number>>"))
sign = input("Enter Sign [ +, -, *, /, %, // ]: ")

if sign == "+":
    print("The output is ", first_num + second_num)

elif sign == "-":
    print("The output is ", first_num - second_num)

elif sign == "*":
    print("The output is ", first_num * second_num)

elif sign == "/":
    print("The output is ", first_num / second_num)

elif sign == "%":
    print("The output is ", first_num & second_num)

elif sign == "//":
    print("The output is ", first_num // second_num)

else:
    print("Try again, something was wrong.")
