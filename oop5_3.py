class CanBo :
    def __init__(self, ten, tuoi, gioiTinh, diaChi):
        self.hoVaTen = ten
        self.tuoi = tuoi
        self.gioiTinh = gioiTinh
        self.diaChi = diaChi
    
    def loai_Can_Bo (self):
        return "CanBo"
    
    def hien_thi(self):
        print(f"loai can bo: {self.loai_Can_Bo()}")
        print(f"Ho va ten: {self.hoVaTen}")
        print(f"Tuoi: {self.tuoi}")
        print(f" Gioi tinh: {self.gioiTinh}")
        print(f" Dia chi: {self.diaChi}")
class CongNhan (CanBo):
    def __init__( self, ten,tuoi,gioiTinh,diaChi,bac):
        super().__init__(ten,tuoi,gioiTinh,diaChi)
        if not (1 <= bac <=10):
            raise ValueError("Bac 1- 10")
        self.bac = bac
    def loai_Cong_Nhan (self):
        return "CongNhan"
    def hien_thi(self):
        super().hien_thi()
        print(f"bac: {self.bac}")
class KySu (CanBo):
    def __init__ (self, ten,tuoi,gioiTinh,diaChi,nganhDaoTao):
        super ().__init__(ten,tuoi,gioiTinh,diaChi)
        self.nganhDaoTao = nganhDaoTao
    def nganh_Dao_Tao (self):
        return "nganh_Dao_Tao"
    def hien_thi(self):
        super().hien_thi()
        print(f"Nganh dao tao: {self.nganh_Dao_Tao()}")
class NhanVien (CanBo):
    def __init__ (self, ten,tuoi,gioiTinh,diaChi,congViec):
        super ().__init__(ten,tuoi,gioiTinh,diaChi)
        self.congViec = congViec
    def cong_Viec (self):
        return "cong_Viec"
    def hien_thi(self):
        super().hien_thi()
        print(f"Cong viec: {self.cong_Viec()}")
while True:
    print("1. Them can bo moi")
    print("2. Tim kiem theo ho ten")
    print("3. Hien thi thong tin ve cac can bo")
    print("4. Thoat chuong trinh")
    luaChon = input("Nhap lua chon cua ban (1-4):")
    if luaChon == "1":
        loaiCanBo = input ("Nhap loai can bo  :")
        if loaiCanBo == "Cong Nhan":
            ten = input (" nhap ho va ten")
            tuoi = int  (input (" nhap so tuoi"))
            gioiTinh = input (" nhap gioi tinh")
            diaChi = input (" nhap dia chi")
            bac = int (input ("nhap bac (1-10)"))
            congNhan = CongNhan ( ten, tuoi, gioiTinh, diaChi, bac)
        
        elif loaiCanBo == "Ky Su":
            ten = input (" nhap ho va ten")
            tuoi = int  (input (" nhap so tuoi"))
            gioiTinh = input (" nhap gioi tinh")
            diaChi = input (" nhap dia chi")
            nganhDaoTao = input (" nhap nganh dao tao")
            kySu = KySu (ten, tuoi, gioiTinh, diaChi, nganhDaoTao)
           
        elif loaiCanBo == "Nhan Vien":
            ten = input (" nhap ho va ten")
            tuoi = int  (input (" nhap so tuoi"))
            gioiTinh = input (" nhap gioi tinh")
            diaChi = input (" nhap dia chi")
            congViec = input ("nhap cong viec")
            nhanVien = NhanVien (ten, tuoi, gioiTinh, diaChi, congViec)
          
        else:
            print (" khong co loai can bo nay, vui long nhap lai")
            break
    elif luaChon == "2":
        tenCanBo = input (" nhap ho va ten can bo can tim kiem")
        if tenCanBo == CongNhan.hoVaTen:
            CongNhan.hien_thi()
        elif tenCanBo == KySu.hoVaTen:
            KySu.hien_thi()
        elif tenCanBo == NhanVien.hoVaTen:
            NhanVien.hien_thi()
        else:
            print (" khong tim thay ten cua can bo ")
            break
    elif luaChon =="3":
        print (" hien thi thong tin chinh xac ve can bo")
        CongNhan.hien_thi()
        KySu.hien_thi()
        NhanVien.hien_thi()
        break
    elif luaChon == "4":
        print (" thoat chuong trinh")
        break
    else :
        print (" khong co lua chon nay, vui long nhap lai")
        
        
