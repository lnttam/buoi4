temp =0
def sosanh(num1,num2,num3):
    if num2<num1 and num2<num3:
        temp = num1
        num1 = num2
        num2 = temp
    elif num3<num1 and num3<num2:
        temp = num1
        num1 = num3
        num3 = temp
    if num3<num2:
        temp = num2
        num2 = num3
        num3 = temp
    return(num1, num2, num3)

so1 = int(input("nhap so thu 1: "))
so2 = int(input("nhap so thu 2: "))
so3 = int(input("nhap so thu 3: "))

print(sosanh(so1,so2,so3))