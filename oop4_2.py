class NhanVien:
    def __init__(self, ten, luongcb, hesoluong, luongmax):
        self.__tenNhanVien = ten
        self.__luongCoBan = luongcb
        self.__heSoLuong = hesoluong
        self.__luongMax = luongmax
    def get__tenNhanVien(self):
        return self.__tenNhanVien
    def set__tenNhanVien(self, ten):
        self.__tenNhanVien = ten
    def get__luongCoBan(self):
        return self.__luongCoBan
    def set__luongCoBan(self, luongcb):
        self.__luongCoBan = luongcb
    def get__heSoLuong(self):
        return self.__heSoLuong
    def set__heSoLuong(self, hesoluong):
        self.__heSoLuong = hesoluong
    def get__luongMax(self):
        return self.__luongMax
    def set__luongMax(self, luongmax):
        self.__luongMax = luongmax
    def tinh_luong(self):
        luong = self.__luongCoBan * self.__heSoLuong
        if luong > self.__luongMax:
            print("cong ty khong co du tien de tra luong cho nhan vien ", self.__tenNhanVien)
            return False
        else:
            print("congtycothetraluongduchonhanvien", self.__tenNhanVien)
            return True
    def tang_Luong (self,delta):
        heSoLuongMoi = self.__heSoLuong + delta
        luongMOi = self.__luongCoBan *heSoLuongMoi
        if luongMoi > self.__luongMax:
            print ("cong ty khong tra luong du cho nhan vien ", self.__tenNhanVien)
            return False 
        else :
            print("nhan vien nhan duoc tien", self.__tenNhanVien)
            return True
    def inTTin ( self ):
        print ("_"* 30)
        print(f"Ten Nhan Vien: {self.__tenNhanVien}")
        print(f"Luong Co Ban: {self.__luongCoBan}")
        print(f"He So Luong: {self.__heSoLuong}")
        print(f"Luong Max: {self.__luongMax}")
        print ("#"*30)
        