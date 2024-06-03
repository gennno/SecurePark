import cv2
import pickle
import cvzone
import numpy as np
import requests

# Konfigurasi Firebase
firebase_url = 'https://fir-dec23-default-rtdb.firebaseio.com'  # Ubah ke tabel yang benar
firebase_auth = 'AIzaSyCB2w7nDJ2jiU2C_CSLhwG2FHOtEzymAG4'  # Ganti dengan secret key/auth token Anda

# Video feed
cap = cv2.VideoCapture(1)  # Gunakan indeks kamera yang sesuai (0 atau 1)

# Muat posisi parkir
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except FileNotFoundError:
    posList = []
    print("File CarParkPos tidak ditemukan. Memulai dengan daftar kosong.")

width, height = 65, 110

# Menambahkan penamaan untuk posisi parkir
parking_spot_names = [6, 7, 8, 9, 10]

def send_to_firebase(data):
    url = f'{firebase_url}/slots6_10.json?auth={firebase_auth}'
    response = requests.put(url, json=data)
    if response.status_code == 200:
        print('Data berhasil dikirim ke Firebase')
    else:
        print(f'Gagal mengirim data ke Firebase: {response.status_code}, {response.text}')

def check_parking_space(imgPro):
    spaceCounter = 0
    slots6_10 = {}  # Dictionary untuk menyimpan status parkir

    for idx, pos in enumerate(posList):
        x, y = pos
        img_crop = imgPro[y:y + height, x:x + width]
        count = cv2.countNonZero(img_crop)
        cvzone.putTextRect(img, str(count), (x, y + height - 1), scale=1.3, thickness=1, offset=0, colorR=(255, 50, 0))

        if count < 6900:  # Ubah pixel pengukur kotak
            color = (0, 0, 255)  # Merah
            thickness = 3
            spaceCounter += 1
            status = "terisi"
        else:  # Jika kosong
            color = (0, 255, 0)  # Hijau
            thickness = 2
            status = "tersedia"

        # Print status ruang parkir ke CMD
        spot_name = parking_spot_names[idx] if idx < len(parking_spot_names) else f"{idx + 1}"
        print(f"Ruang parkir {spot_name} di posisi {pos} adalah {status} dengan count {count}")

        # Update status parkir dalam dictionary
        slots6_10[spot_name] = status

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(img, f"Spot {spot_name}: {status}", (x, y - 10), scale=1, thickness=1, offset=0, colorR=color)

    # Update status parkir ke Firebase
    send_to_firebase(slots6_10)

    cvzone.putTextRect(img, f'Terisi: {spaceCounter}/{len(posList)}', (100, 400), scale=5, thickness=5, offset=10, colorR=(255, 50, 0))
    # Print status total ruang parkir ke CMD
    print(f'Total Ruang Parkir Kosong: {spaceCounter}/{len(posList)}')


while True:
    success, img = cap.read()  # Baca frame dari webcam
    if not success:
        print("Gagal mengambil gambar dari webcam. Keluar...")
        break

    # Konversi ke skala abu-abu dan aplikasikan Gaussian blur
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 1)

    # Terapkan threshold adaptif
    img_threshold = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY, 25, 16)
    img_median = cv2.medianBlur(img_threshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    img_dilate = cv2.dilate(img_median, kernel, iterations=1)

    # Periksa ruang parkir pada gambar yang diproses
    check_parking_space(img_dilate)

    # Tampilkan feed video dari webcam dan gambar yang diproses
    cv2.imshow("Webcam", img)

    # Keluar dari loop saat 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bebaskan tangkapan dan tutup semua jendela OpenCV
cap.release()
cv2.destroyAllWindows()
