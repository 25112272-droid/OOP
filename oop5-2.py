class nhanVien:
    
    def __init__( self, maNhanVien, tenNhanVien, namSinh, diaChi, heSoluong, luongToiDa):
        self.maNhanVien = maNhanVien
        self.tenNhanVien = tenNhanVien
        self.namSinh = namSinh
        self.diaChi = diaChi
        self.heSoLuong = heSoluong
        if self.heSoLuong < 0:
            raise ValueError("he so khong ton tai")
        else:
            self.heSoLuong = heSoluong
        self.luongToiDa = luongToiDa
    def tinhLuong(self):
        # cho luong co ban la 10000000
        return 10000000 * self.heSoLuong
class CongTacVien (nhanVien):
    def __init__ (self,maNhanVien, tenNhanVien, namSinh, diaChi, heSoluong, luongToiDa, thoiHanHopDong, khoanPhuCap):
        super().__init__(maNhanVien, tenNhanVien, namSinh, diaChi, heSoluong, luongToiDa)
        self.thoiHanHopDong = thoiHanHopDong
        if thoiHanHopDong in ["3 thang", "6 thang", "12 thang"]:
            print (f"Thời hạn hợp đồng của công tác viên {self.tenNhanVien} là {self.thoiHanHopDong}")
        else:
            raise ValueError("Thời hạn hợp đồng không hợp lệ")
        self.khoanPhuCap = khoanPhuCap
    def tinhLuong(self):
        return super().tinhLuong() + self.khoanPhuCap
class nhanVienChinhThuc (nhanVien):
    def __init__ (self,maNhanVien, tenNhanVien, namSinh, diaChi, heSoluong, luongToiDa, viTriCongViec):
        super().__init__(maNhanVien, tenNhanVien, namSinh, diaChi, heSoluong, luongToiDa)
        self.viTriCongViec = viTriCongViec
    def tinhLuong (self):
        return super().tinhLuong()
class truongPhong (nhanVien):
    def __init__ (self,maNhanVien, tenNhanVien, namSinh, diaChi, heSoluong, luongToiDa, ngayBatDauQuanLy, khoanPhuCapTruongPhong):
        super().__init__(maNhanVien, tenNhanVien, namSinh, diaChi, heSoluong, luongToiDa)
        self.ngayBatDauQuanLy = ngayBatDauQuanLy
        self.khoanPhuCapTruongPhong = khoanPhuCapTruongPhong
    def tinhLuong(self):
        return super().tinhLuong() + self.khoanPhuCapTruongPhong

# Example 
if __name__ == "__main__":
    congTacVien1 = CongTacVien("CTV001", " nguyen van a", 1999, "Ha Nam", 0.8, 2000000, "12 thang", 4000000)
    print(f"Luong cua cong tac vien 1: {congTacVien1.tinhLuong()}")
