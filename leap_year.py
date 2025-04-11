def leap_year():
    año = int(input("Ingrese un año: "))
    a = año%400
    if a == 0:
        print(f"El año {año} es bisiesto") 
    else:
        print(f"El año {año} no es bisiesto")

