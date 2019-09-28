var_a = input("Bitte geben Sie eine Zahl ein:")
var_b = input("Bitte geben Sie eine weitere Zahl ein:")
operation = input("Nun geben Sie eines der Operationszeichen (+, -, /, *) ein:")




if operation == "+":
    print(int(var_a) + int(var_b))
elif operation == "-":
    print(int(var_a)-int(var_b))
elif operation == "/":
    print(int(var_a)/int(var_b))
elif operation == "*":
    print(int(var_a)*int(var_b))