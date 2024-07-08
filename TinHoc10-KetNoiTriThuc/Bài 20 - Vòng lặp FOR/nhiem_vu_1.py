#nhap n từ bàn phím là số tự nhiên
n = int(input("Nhập số tự nhiên n: "))

#tìm ước số của n từ 1 tới n (bao gồm cả n)
for k in range(1, n + 1):    # k <= n
    if n % k == 0 :  # n chia hết cho k => k là ước của n
        print(k, end = " ")  #in trên 1 dòng với tham số end
