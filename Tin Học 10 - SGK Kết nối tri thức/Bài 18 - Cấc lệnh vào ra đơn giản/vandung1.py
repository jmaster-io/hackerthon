# Giả sử ss là số giây cần chuyển đổi
ss = int(input("Nhập vào số giây" ))
#Sử dụng các hằng số cho số giây trong một ngày, giờ và phút
NGAY = 86400
GIO = 3600
PHUT = 60
#Tính số ngày, giờ, phút và giây
ngay = ss // NGAY
ss = ss % NGAY
gio = ss // GIO
ss = ss % GIO
phut = ss // PHUT
giay = ss % PHUT
#In kết quả ra màn hình
print(ngay, "ngày", gio, "giờ", phut, "phút", giay, "giây")
