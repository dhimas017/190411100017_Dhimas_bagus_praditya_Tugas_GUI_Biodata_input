import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QCheckBox

#membuat fungsi utk menentukan layout window
def window_go():
    #inisialisasi pyqt
    app = QApplication(sys.argv)
    window = QWidget()

    textLabel = QLabel(window)
    textLabel.setText("Input Biodata")
    textLabel.setStyleSheet("background-color: #99b8c2; color: red; font : bold; font-size: 30px") #untuk memberi warna background,warna text, menebalkan text dan ukuran font pada text
    textLabel.resize(570, 35) #570(x) untuk panjang text dari kiri ke kanan dan 35(y) lebar text dari atas ke bawah
    textLabel.move(10,10) #letak dari text secara keseluruhan

    #untuk membuat tulisan name sebelum textbox
    namaLabel = QLabel(window) 
    namaLabel.setText("Name")
    namaLabel.move(10,57) #untuk mengatur posisi dari tulisan : 10(x) untuk posisi text dari kiri ke kanan,57(y) posisi text dari atas ke bawah

    #untuk membuat tulisan address sebelum textbox
    alamatLabel = QLabel(window)
    alamatLabel.setText("Address")
    alamatLabel.move(10,85) 

    #untuk membuat tulisan hobby sebelum checkbox
    hobbyLabel = QLabel(window)
    hobbyLabel.setText("Hobby")
    hobbyLabel.move(10,147)

    #untuk membuat tulisan status sebelum radiobox
    statusLabel = QLabel(window)
    statusLabel.setText("status")
    statusLabel.move(10,215)

    #untuk membuat textboxt atau wadah dari inputan user pada bagian nama dan address
    textbox = [None]*10
    baris = 25 
    for i in range(3): # looping 3x berarti akan ada 3 textbox
        baris = baris + 30
        textbox[i] = QLineEdit(window)
        textbox[i].move(57,baris)
        textbox[i].resize(523, 20)

    #untuk membuat cekbox (berbentuk kotak) yaitu untuk memberi pilihan kepada user dengan mengklik box tersebut. nb : semua data/pilihan dicekbox dapat diklik/dicentang 
    chekbox1 = QCheckBox(window)
    chekbox2 = QCheckBox(window)
    chekbox3 = QCheckBox(window)
    chekbox1.setText("makan")
    chekbox2.setText("tidur")
    chekbox3.setText("main")
    chekbox1.move(57,146)
    chekbox2.move(57,166)
    chekbox3.move(57,186)

    #untuk membuat radiobox (berbentuk lingkaran) yaitu untuk memberi pilihan kepada user dengan mengklik box tersebut. nb : hanya salah satu data saja yang bisa dipilh/diklik pada radiobox
    radiobutton1 = QRadioButton(window)
    radiobutton2 = QRadioButton(window)
    radiobutton3 = QRadioButton(window)
    radiobutton1.setText("pelajar")
    radiobutton2.setText("pegawai")
    radiobutton3.setText("mahasiswa")
    radiobutton1.move(57, 216)
    radiobutton2.move(57, 236)
    radiobutton3.move(57, 256)

    #menentukan ukuran window, + title dan menampilkan
    window.setGeometry(100, 100, 600, 400)
    window.setWindowTitle("PyQt5 Example")
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
   window_go()