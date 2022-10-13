while True:
    so = input("nhap 2 so nguyen bat ki: ")
    x = so.split()
    start = int(x[0])
    end = int(x[1])
    if start > end:
        print("so bat dau phai be hon so ket thuc")
    else: 
        break

for i in range(start, end+1):
    if i%5==0 and i%3==0:
        print(i,"FizzBuzz")
    elif i%5==0:
        print(i,"Buzz")
    elif i%3==0:
        print(i,"Fizz")
    else :
        print(i)
    i+=1