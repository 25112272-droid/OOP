class hangHoa:
    def __init__( self, maHang, tenHang, nhaSanXuat, gia):
        self.maHang = maHang
        self.tenHang = tenHang
        self.nhaSanXuat = nhaSanXuat
        self.gia = gia
    def hienThi (self):
        print ("_" * 30)
        print(f"Mã hàng: {self.maHang}")
        print(f"Tên hàng: {self.tenHang}")
        print(f"Nhà sản xuất: {self.nhaSanXuat}")
        print(f"Giá: {self.gia}")
class hangDienMay (hangHoa):
    def __init__(self, maHang, tenHang, nhaSanXuat, gia, thoiGianBaoHanh, dienAp, congSuat):
            super().__init__(maHang, tenHang, nhaSanXuat, gia)
            self.thoiGianBaoHanh = thoiGianBaoHanh
            self.dienAp = dienAp
            self.congSuat = congSuat

    def hienThi(self):
            super().hienThi()
            print(f"Thời gian bảo hành: {self.thoiGianBaoHanh}")
            print(f"Điện áp: {self.dienAp}")
            print(f"Công suất: {self.congSuat}")
class hangSanhSu (hangHoa):
    def __init__(self, maHang, tenHang, nhaSanXuat, gia, loaiNguyenLieu):
        super().__init__(maHang, tenHang, nhaSanXuat, gia)
        self.loaiNguyenLieu = loaiNguyenLieu

    def hienThi(self):
        super().hienThi()
        print(f"Loại nguyên liệu: {self.loaiNguyenLieu}")
class hangThucPham (hangHoa):
    def __init__( self, maHang, tenHang, nhaSanXuat, gia, ngaySanXuat, ngayHetHan):
        super().__init__(maHang, tenHang, nhaSanXuat, gia)
        self.ngaySanXuat = ngaySanXuat
        self.ngayHetHan = ngayHetHan

    def hienThi(self):
        super().hienThi()
        print(f"Ngày sản xuất: {self.ngaySanXuat}")
        print(f"Ngày hết hạn: {self.ngayHetHan}")
        
# Chạy thử chương trình
if __name__ == "__main__":
    # Tạo thử một mặt hàng điện máy
    tu_lanh = hangDienMay("DM01", "Tủ lạnh G", "G", 1200000, "24 tháng", "220V", "120W")
    
    print("--- THÔNG TIN MẶT HÀNG ---")
    tu_lanh.hienThi()