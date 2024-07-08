"""
Siêu thị áp dụng mức giá bán cam theo hai loại:
Dưới 5kg: 12.000 đồng/kg
5kg trở lên: 10.000 đồng/kg
"""
# Nhập số lượng cam mua
so_luong = float(input("Nhập số lượng cam mua (kg): "))

# giá bán cam theo hai loại:
gia_ban = 0 

# Dưới 5kg: 12.000 đồng/kg
if so_luong < 5:
    gia_ban = 12000
    
else:  #5kg trở lên: 10.000 đồng/kg
    gia_ban = 10000

# Tính toán số tiền phải trả
tong_tien = so_luong * gia_ban

# Hiển thị kết quả
print("Số tiền phải trả cho", so_luong, "kg cam là: ", round(tong_tien) , "đồng")

