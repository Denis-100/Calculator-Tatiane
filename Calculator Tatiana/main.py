print("Это калькулятор, введите 2 числа, а затем выберите операцию")

num1 = 0
num2 = 0
otvet = 0

def input_data():
    global num1, num2
    try:
        num1 = int(input("Введите 1-е число: "))
        num2 = int(input("Введите 2-е число: "))
    except ValueError:
        print("Ошибка, вводите пожалуйста числа")
        input_data()

input_data()

oper = input("Выберите операцию: '+' -' '*' '**' '/' '//' '%' ")


match oper:
    case "+": # Саша
        print("Сложение")
    case "-": # Ярослав
        print("Вычитание")
    case "*":
        otvet = num1 * num2
    case "**":
        # Пример как делать:
        # Было:
        # print("Возведение в степень")
        # ---------------
        # Стало:
        otvet = num1 ** num2
    case "/": # Дима
        otvet = num1 / num2
    case "//": # Никита
        print("Целочисленное деление")
    case "%": # Никита
        print("Остаток от деления")


print(f"{num1} {oper} {num2} = {otvet}")