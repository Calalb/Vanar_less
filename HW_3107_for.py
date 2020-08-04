def inputInteger( text ):
    try:
        return  int(input(text))
    except ValueError:
        print("Valoare gresita!")

def contur( text ):
    print()
    print("#" * 89)
    print(text)
    print("#" * 89)

#############################################
start_value = inputInteger("Start: ?")
end_value = inputInteger("End: ?")
#############################################
contur("Diapazon of values")
if start_value > end_value:
    for x in range(start_value, end_value -1, - 1):
     print(x, end = ", ")
else:
    for x in range(start_value, end_value +1):
        print(x, end= ", ")

contur("Divide by 3")
if start_value > end_value:
    for x in range(start_value, end_value -1, -1):
        if x % 3 == 0:
            print(x, end=", ")
else:
    for x in range(start_value, end_value+1):
        if x % 3 == 0:
            print(x, end=", ")

contur("First 5 values")
num = 0
if start_value > end_value:
    for x in range(start_value, end_value -1, -1):
        if x % 3 == 0 and num < 5:
            print(x, end= ", ")
            num +=1
else:
    for x in range(start_value, end_value+1):
        if x % 3 == 0 and num < 5:
            print(x, end= ", ")
            num += 1