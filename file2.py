try:
    num_1, num_2 = eval(input("Enter two numbers, seperated by a comma : "))
    result = num_1 / num_2
    print(("Result is", result))
except ZeroDivisionError:
    print("Division by zero is error")
except SyntaxError:
    print("Comma is missiong.Enter numbers seperated by a comma like this 1,2")
except:
    print("Wrong input")
else:
    ("This will execute no matter what")