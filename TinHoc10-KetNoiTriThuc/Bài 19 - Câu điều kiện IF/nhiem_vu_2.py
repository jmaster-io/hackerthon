#nhập số điện thiêu thụ với input, ép kiểu sang số thực
k = float(input("Nhap so kWh tieu thu dien nha em:"))

# t là số tiền điện cần thanh toán, bắt đầu là 0 
t = 0 

#bậc 1: nếu k <= 50,  x 1,678 nghìn đồng
if k <= 50 :
    t = k * 1.678  # sử dụng dấu . cho phần thập phân trong lập trình

else: # trường hợp ngược lại  k> 50
    #bậc 2:  k > 50  and k <= 100  :  x 1.734
    if k <= 100:
        t = 50 * 1.678 + (k - 50) * 1.734
        
    else :  # bậc 3:  k > 100
         t = 50 * 1.678 + 50 * 1.734 + (k - 100) * 2.014

# in ra số tiền điện phải trả, hàm round để làm tròn số thực về dạng số nguyên
print("Số tiền điện phải trả là:", round(t), "nghìn đồng")

    
    
