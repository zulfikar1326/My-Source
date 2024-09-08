import cv2  as cv
import time as tm
import os 



def template():
    templat = """
        ======================================
        PROGRAM MANIPULASI FOTO DENGAN OPEN CV
                    BY ZULFIKAR 
        ======================================
        
        1. Input Foto
        2. Tampilkan foto
        3. Ubah Ukuran Foto
        4. Exit
        """
    print(templat)
      
def readImg(img):
    """Baca img"""
    readImage = cv.imread(img) 
    if readImage.all():
        print("Input berhasil, Tunggu sebentar...")
    else:
        print("Alamat Yang anda masukan Salah!!")
    
    return readImage

def openImage(img):
    """Membuka GUI Image"""
    try:
        viewImage = cv.imshow("Your img",img)
        print(viewImage)
        print("img berhasil Dibuka")
        key = cv.waitKey(0)
        
    except:
        print("Ada Kesalahan Dalam Meluncurkan Proses...2")
        cv.destroyAllWindows() 
        
    return key

def resizeImg(tinggi,lebar,img):
    """Ubah Ukuran img"""
    try:
        addNewData = cv.resize(img,(tinggi,lebar))
        cv.waitKey(0)
        
        print(addNewData)
        return addNewData
    
    except:
        print("Ada kesalahan ketika Prosesing Mohon diulangi")

def saveImage(img):
    """Simpan Img"""
    cv.imwrite('Youtimg.jpg',img)   
    print("img Sudah tersimpan File anda")


def clearTermina():
    """Membersihkan Terminal"""
    os.system('clear')

def timecontrol():
    """Waktu Delay"""
    tm.sleep(3)



if __name__ == "__main__":
    while True:
        print("sabar ya bob Sedang Loading......")
        
        tm.sleep(0.800) # Waktu Delay
        clearTermina()  # Clear Terminal
        
        template()
        
        ofinput1 = input("Opsi : ")
        
        if ofinput1 == '1': # Opsi 1 Input img 
            clearTermina()
            
            print("=== CONTOH ===")
            print("../a/b/c/imganda.jpg")
            
            opsi1 = input("Masukkan Alamat img : ")
            hasilBaca = readImg(opsi1)
            timecontrol()
            
        
        elif ofinput1 == "2":   # Opsi 2 Tampilkan img
            clearTermina()
            timecontrol() 
            
            key = openImage(hasilBaca)
            if key == ord('q'):
                cv.destroyAllWindows()
                timecontrol()
            
        
        elif ofinput1 == "3":   # Opsi 3 Ubah Ukuran img
            clearTermina()
            timecontrol() 
            
            
            inputWidth = int(input("Masukkan Width img   :\t "))
            inputHeight = int(input("Masukkan Height img :\t "))

            hasil = resizeImg(inputWidth,inputHeight,hasilBaca)
            
            try:
                opsiMini = input("Tampilkanimg 1.ya 2.tidak ")
                if opsiMini == "1":
                    tampilkan = openImage(hasil)
                    print("sedang Menyimpan, Tunggu Sebentar...")
                    timecontrol()
                    save = saveImage(hasil)
                    
            except:
                print("Input Salah")

        elif ofinput1 == "4":   # Opsi 4 Keluar dari Apps
            print("input 4")
            clearTermina()
            exit("Program out")
        
        else:
            clearTermina()
            print("Input Salah")
