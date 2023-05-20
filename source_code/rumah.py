from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, luas_tanah):
        super().__init__("Rumah", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.luas_tanah = luas_tanah

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_luas_tanah(self):
        return self.luas_tanah
    
    def get_detail(self):
        return str(super().get_summary()) + "\nNama Pemilik: " + self.get_nama_pemilik() + "\nLuas Tanah: " + str(self.get_luas_tanah()) + " m^2"