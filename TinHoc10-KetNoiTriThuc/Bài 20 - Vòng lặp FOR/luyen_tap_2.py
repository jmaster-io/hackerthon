"""
Tính tích của dãy số 1 x 2 x 3 x .... x n
"""
#Nhập số tự nhiên n vào bàn phím
n  = int(input("Nhập số tự nhiên n: "))

# tích ban đầu là 1 
tich = 1

# lặp dãy số từ 1 đến n
for k in range(1, n + 1):   # 1 .... n
    tich = tich * k  # nhân và gán lại biến tích

#in kết quả ra màn hình
print(tich)
