import math

a = float(input("nhap canh 1 = "))
b = float(input("nhap canh 2 = "))
c = float(input("nhap canh 3 = "))
s = (a+b+c)/2
dientich = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("dien tich tam giac = ", dientich)