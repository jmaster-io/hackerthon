"""
Tính tổng dãy số  S = 1^3 + 2^3 + 3^3 + .... + n^3
"""
#Nhập số tự nhiên n vào bàn phím
n  = int(input("Nhập số tự nhiên n: "))

# tong S ban đầu là 0 
S = 0

# lặp dãy số từ 1 đến n
for k in range(1, n + 1):   # 1 .... n
    S = S + k**3  # cộng S với số k ^ 3 và gán lại biến S

#in kết quả ra màn hình
print(S)
