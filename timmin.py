number = input("nhap mot so bat ky: ")
def timmin(number):
    result = number[0]
    for num in number:
        if result > num:
            result = num
    return result
print("so nho nhat la: ", timmin(number)) 