"""
Tính tổng dãy số từ 0 đến n
Sau đó bình phương tổng tính được
"""
#Nhập số tự nhiên n vào bàn phím
n  = int(input("Nhập số tự nhiên n: "))

#Tổng ban đầu là 0
S = 0

# lặp dãy số từ 0 đến n
for k in range(n + 1):   # 0 1 .... n
    S = S + k  #cộng với số k trong dãy và gán lại cho S

#in a màn hình với bình phương tổng S
print(S * S)
