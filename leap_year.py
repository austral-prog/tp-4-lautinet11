def leap_year():
    año = int(input("Ingrese un año: "))
    a = año%400
    b = año%4
    c = año/100
    if (b == 0 and c != 0) or a == 0:
        print(f"El año {año} es bisiesto")   
    else:
        print(f"El año {año} no es bisiesto")
