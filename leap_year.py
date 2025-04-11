def leap_year():
    año = int(input("Ingrese un año: "))
    a = año%400
    b = año%4
    if año < 400 and b == 0:
        print(f"El año {año} es bisiesto")
    if año > 400 and a == 0:
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")
