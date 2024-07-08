#nhap n từ bàn phím là số tự nhiên
n = int(input("Nhập số tự nhiên n: "))

#đếm số ước số của n từ 1 tới n (KHÔNG bao gồm n)
count = 0  # bat dau la 0

for k in range(1, n):  # k < n
    if n % k == 0:  # n chia hết cho k => k là ước của n
        count = count + 1   # tăng đếm lên 1 và gán lại count
        
print(count)  #in trên 1 dòng với tham số end
