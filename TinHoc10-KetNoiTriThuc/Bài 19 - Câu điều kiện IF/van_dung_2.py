"""
Năm n là năm nhuận nếu thỏa mãn một trong hai điều kiện:
Chia hết cho 400.
Chia hết cho 4 nhưng không chia hết cho 100.
"""
# Nhập năm cần kiểm tra
n = int(input("Nhập năm dương: "))

#Chia hết cho 400.
if n % 400 == 0:
      print(n, "là năm nhuận.")
else:
    #Chia hết cho 4 nhưng không chia hết cho 100.
    if n % 4 == 0 and n % 100 != 0:
        print(n, "là năm nhuận.")
    else:
        print(n, "không là năm nhuận.")
