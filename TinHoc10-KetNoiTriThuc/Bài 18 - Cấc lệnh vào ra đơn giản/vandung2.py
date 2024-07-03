a = float(input("Nhập số thực dương a: "))
b = float(input("Nhập số thực dương b: "))
c = float(input("Nhập số thực dương c: "))

# chu vi
p = a + b + c

#dien tich
s = ( p * (p - a) * (p - b) * (p - c)  )  ** 0.5

print("Chu vi tam giac la: ", p)
print("Dien tich tam giac la: ", s)
