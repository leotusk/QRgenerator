import qrcode
import time
import keyboard
import os


학번 = input() #s21***
이름 = input() #이름 세글자
파일이름 = input() + ".png" #저장되는 파일이름(3209***)

while True:
    시간 = time.time()
    # Esc 키가 눌릴 때까지 QR 코드 생성
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    리스트2 = 학번+이름+str(시간)
    qr.add_data(리스트2)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(파일이름)
    print(img)

    # 5초간 대기 후 QR 코드 지우기
    time.sleep(5)
    os.remove(파일이름)
    print("갱신하였습니다")

    # Esc 키가 눌리면 종료
    if keyboard.is_pressed("esc"):
        print("갱신을 종료합니다")
        break