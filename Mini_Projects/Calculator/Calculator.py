print("Calculator.Trust the process. It's all about Calculation.")
print("Type 'exit' to quit.")

while True:
    expression = input("Enter Your Calculation: ")

    if expression.lower() == 'exit':
        print("GoodBye!")
        break

    try:
        result = eval(expression)
        print("Result:", result)
    except:
        print("Invalid expression, try again.")
        