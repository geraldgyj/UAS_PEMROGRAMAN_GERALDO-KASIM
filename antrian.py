import time
from collections import deque

class SistemAntrian:
    def __init__(self):
        self.antrian = deque()  
        self.waktu_mulai = {}   
        self.waktu_selesai = []  

    def tambah_nasabah(self, nama, kategori):
        
        self.antrian.append({"nama": nama, "kategori": kategori})
        print(f"Nasabah {nama} (Kategori: {kategori}) ditambahkan ke antrian.")

    def proses_nasabah(self):
        if not self.antrian:
            print("Tidak ada nasabah dalam antrian.")
            return

        
        
        nasabah = self.antrian.popleft()
        nama = nasabah["nama"]
        kategori = nasabah["kategori"]
        
        print(f"Melayani nasabah {nama} (Kategori: {kategori})...")
        waktu_pelayanan = 2  
        self.waktu_mulai[nama] = time.time()
        time.sleep(waktu_pelayanan)  
        waktu_selesai = time.time()
        
        
        self.waktu_selesai.append(waktu_selesai - self.waktu_mulai[nama])
        print(f"Nasabah {nama} selesai dilayani dalam {waktu_selesai - self.waktu_mulai[nama]:.2f} detik.")

    def tampilkan_statistik(self):
        if not self.waktu_selesai:
            print("Belum ada data pelayanan.")
            return

        rata_rata_waktu = sum(self.waktu_selesai) / len(self.waktu_selesai)
        print(f"\n--- Statistik Pelayanan ---")
        print(f"Jumlah Nasabah Dilayani: {len(self.waktu_selesai)}")
        print(f"Rata-rata Waktu Pelayanan: {rata_rata_waktu:.2f} detik")


if __name__ == "__main__":
    sistem = SistemAntrian()

    while True:
        print("\nMenu:")
        print("1. Tambah Nasabah")
        print("2. Proses Nasabah")
        print("3. Tampilkan Statistik")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            nama = input("Masukkan nama nasabah: ")
            kategori = input("Masukkan kategori (Reguler/Prioritas): ")
            sistem.tambah_nasabah(nama, kategori)
        elif pilihan == "2":
            sistem.proses_nasabah()
        elif pilihan == "3":
            sistem.tampilkan_statistik()
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

