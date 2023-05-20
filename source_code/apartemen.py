from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, lantai):
        super().__init__("Apartemen", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.lantai = lantai

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_lantai(self):
        return self.lantai
    
    def get_detail(self):
        return str(super().get_summary()) + "\nNama Pemilik: " + self.get_nama_pemilik() + "\nLantai: " + str(self.get_lantai())