cost = int(input("nhap so tien: "))
if cost >= 150:
    print("tong tien: ", cost-50)
elif cost >=100:
    print("tong tien: ", cost-25)
elif cost >75:
    print("tong tien: ", cost-15)
else:
    print("tong tien: ", cost)