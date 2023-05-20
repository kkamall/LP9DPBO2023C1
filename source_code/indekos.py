from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, harga):
        super().__init__("Indekos")
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.harga = harga

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    def get_harga(self):
        return self.harga

    def get_detail(self):
        return str(super().get_summary()) + "\nNama Pemilik: " + self.get_nama_pemilik() + "\nNama Penghuni: " + self.get_nama_penghuni() + "\nHarga: Rp. " + str(self.get_harga()) 