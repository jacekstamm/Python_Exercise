def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def divine(a, b):
    return a / b


def power(a, b):
    return a ** b


def calculator():
    database = []
    print("Wybierz działanie które chcesz wykonać:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęgowanie")

    choice = input("Wpisz co wybrałeś: (1/2/3/4/5): ")

    num1 = float(input("Wpisz pierwszą liczbę: "))
    num2 = float(input("Wpisz drugą liczbę: "))

    last = process(choice, num1, num2)

    save = input("Czy chcesz zapisać swoje ostatnie działanie? Y/N: ")

    if save == "Y" or save == "y":
        database.append(last)

    print("Jakie chcesz teraz działanie wykonać?")
    print("1. Chcę coś obliczyc jeszcze raz.")
    print("2. Wyświetl ostatnie zapisane działanie")
    print("3. Zakończ program")
    again = input("Które działanie wybierasz? 1/2/3: ")

    if again == "1":
        calculator()
    elif again == "2":
        for record in database:
            print(record)
            calculator()
    elif again == "3":
        print("Do zobaczenia!")
        return


def process(choice, num1, num2):
    if choice == "1":
        print(num1, " + ", num2, " = ", add(num1, num2))
        return str(num1) + "+" + str(num2) + "=" + str(add(num1, num2))
    elif choice == "2":
        print(num1, " - ", num2, " = ", substract(num1, num2))
        return str(num1) + "-" + str(num2) + "=" + str(substract(num1, num2))
    elif choice == "3":
        print(num1, " * ", num2, " = ", multiplication(num1, num2))
        return str(num1) + "*" + str(num2) + "=" + str(multiplication(num1, num2))
    elif choice == "4":
        try:
            print(num1, " / ", num2, " = ", divine(num1, num2))
            return str(num1) + "/" + str(num2) + "=" + str(divine(num1, num2))
        except ZeroDivisionError:
            print("Nie dziel przez zero!!!")
    elif choice == "5":
        print(num1, "^", num2, " = ", power(num1, num2))
        return str(num1) + "^" + str(num2) + "=" + str(power(num1, num2))


def stop_application():
    print("Dziękujem za skorzystanie z naszego SUPER kalkulatora")
    return None


print("No to jak? Zaczynamy zabawę z matematyką?")
start = input("Y/N: ")

if start == "Y" or start == "y":
    calculator()
elif start == "N" or start == "n":
    stop_application()
