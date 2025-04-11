def leap_year():
    año = int(input("Ingrese un año: "))
    a = año%400
    b = año%4
    if a == 0 or b ==0:
        print(f"El año {año} es bisiesto") 
    else:
        print(f"El año {año} no es bisiesto")
