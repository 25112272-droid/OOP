class nhanvien:
    LUONG_MAX = 20000000000
    def __init__(self, ten, luongcb, hesoluong):
        self.tenNhanVien = ten
        self.__luongCoBan = luongcb
        self.__heSoLuong = hesoluong
    def get_ten(self):
        return self.__tenNhanVien
    def set_ten(self,ten):
        self.__tenNhanVien = ten
    def get_luongCoBan(self):
        return self.__luongCoBan
    def set_luongCoBan(self, luongCoBan):
        self.__luongCoBan = luongCoBan
    def get_heSoLuong(self):
        return self.__heSoLuong
    def set_heSoLuong(self, heSoLuong):
        self.__heSoLuong = heSoLuong
    def tinh_luong (self):
        return  self.__luongCoBan * self.__heSoLuong
    def tang_luong(self, delta):
        self.__luongMoi = self.tinh_luong()+delta
        if self.__luongMoi > self.LUONG_MAX:
            print("cong ty khong du tien de tra luong cho nhan vien", self.__tenNhanVien)
            return False
        else:
            print(" cong ty co the tra luong du cho nhan vien", self .__tenNhanVien)
            return True
    def inTTin(self):
        print("-" * 3)
        print(f"Ten NV: {self.__tenNhanVien}")
        print(f"Luong Co Ban: {self.__luongCoBan}")
        print(f"He So Luong: {self.__heSoLuong}")
        print(f"Tong Luong: {self.tinh_luong()}")
        print("-" * 3)
# Example usage:

nv = nhanvien("Nguyen Van A", 10000000, 2.6)
nv.inTTin() # Xem thông tin.
nv.tang_luong(5000000) # Thử tăng 5 triệu
nv.inTTin() # Xem lại sau khi tăng