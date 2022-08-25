chieucao = int(input("nhap chieu cao: "))
cannang = int(input("nhap can nang: "))
bmi = cannang/(chieucao**2)
if bmi >40:
    print("beo phi cap do 3")
elif bmi>=35:
    print("beo phi cap do 2")
elif bmi>=30:
    print("beo phi cap do 1")
elif bmi>=25:
    print("thua can")
elif bmi>=18.5:
    print("binh thuong")
elif bmi>=17:
    print("gay cap do 1")
elif bmi>=16:
    print("gay cap do 2")
elif bmi<16:
    print("gay cap do 1")