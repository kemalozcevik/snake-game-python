import turtle
import time
import random

# 1. Ekran Ayarları
wn = turtle.Screen()
wn.title("Yılan Oyunu")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# 2. Yılanın Kafası
kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape("square")
kafa.color("white")
kafa.penup()
kafa.goto(0, 0)
kafa.direction = "stop"
yeni_yon = "stop"

# 3. Yem Nesnesi
yem = turtle.Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("red")
yem.penup()
yem.goto(0, 100)

# Kuyruk parçalarını tutacak liste
kuyruklar = []

# Skor, Hız ve Duraklatma Değişkenleri
puan = 0
en_yuksek_puan = 0
hiz = 0.1
duraklatildi = False

# Skor Tablosu Nesnesi
yazici = turtle.Turtle()
yazici.speed(0)
yazici.shape("square")
yazici.color("white")
yazici.penup()
yazici.hideturtle()
yazici.goto(0, 260)
yazici.write(f"Skor: {puan}  En Yüksek: {en_yuksek_puan}", align="center", font=("Courier", 18, "normal"))

# 4. Yön Fonksiyonları
def yukari_git():
    global yeni_yon
    if not duraklatildi and kafa.direction != "down":
        yeni_yon = "up"

def asagi_git():
    global yeni_yon
    if not duraklatildi and kafa.direction != "up":
        yeni_yon = "down"

def saga_git():
    global yeni_yon
    if not duraklatildi and kafa.direction != "left":
        yeni_yon = "right"

def sola_git():
    global yeni_yon
    if not duraklatildi and kafa.direction != "right":
        yeni_yon = "left"

# Duraklat / Devam Et Fonksiyonu (Space)
def duraklat_degistir():
    global duraklatildi
    duraklatildi = not duraklatildi
    yazici.clear()
    if duraklatildi:
        yazici.goto(0, 260)
        yazici.color("white")
        yazici.write(f"Skor: {puan}  En Yüksek: {en_yuksek_puan}  [DURAKLATILDI]", align="center", font=("Courier", 16, "bold"))
    else:
        yazici.goto(0, 260)
        yazici.color("white")
        yazici.write(f"Skor: {puan}  En Yüksek: {en_yuksek_puan}", align="center", font=("Courier", 18, "normal"))
    wn.update()

# Yemi Güvenli Konumlandırma
def yem_konumlandir():
    while True:
        rx = random.randint(-260, 260)
        ry = random.randint(-260, 260)
        yem.goto(rx, ry)
        
        # Kafa veya kuyruk üzerine denk gelirse yeniden konum seç
        if yem.distance(kafa) < 20:
            continue
        
        cakisma = False
        for parca in kuyruklar:
            if yem.distance(parca) < 20:
                cakisma = True
                break
        
        if not cakisma:
            break

# Oyunu Sıfırlama ve Ortada Skor Gösterme Fonksiyonu
def oyunu_sifirla(yanma_sebebi=""):
    global puan, hiz, yeni_yon, duraklatildi
    
    # Bir engele çarparak yandıysa ortada uyarı bas
    if yanma_sebebi != "":
        yazici.clear()
        yazici.goto(0, 30)
        yazici.color("red")
        yazici.write("OYUNU KAYBETTINIZ!", align="center", font=("Courier", 24, "bold"))
        yazici.goto(0, -20)
        yazici.color("white")
        yazici.write(f"Skorunuz: {puan}", align="center", font=("Courier", 18, "normal"))
        
        # Ekranı anında zorla tazele ve 2 saniye beklet
        wn.update()
        time.sleep(2)

    # Durumları sıfırla
    kafa.goto(0, 0)
    kafa.direction = "stop"
    yeni_yon = "stop"
    duraklatildi = False
    
    for parca in kuyruklar:
        parca.goto(1000, 1000)
    kuyruklar.clear()

    puan = 0
    hiz = 0.1

    # Skor tablosunu tepeye eski yerine al
    yazici.clear()
    yazici.goto(0, 260)
    yazici.color("white")
    yazici.write(f"Skor: {puan}  En Yüksek: {en_yuksek_puan}", align="center", font=("Courier", 18, "normal"))
    wn.update()

# Manuel Q ile sıfırlama
def tusa_basarak_sifirla():
    oyunu_sifirla(yanma_sebebi="")

# 5. Klavye Dinleme
wn.listen()
wn.onkeypress(yukari_git, "w")
wn.onkeypress(asagi_git, "s")
wn.onkeypress(saga_git, "d")
wn.onkeypress(sola_git, "a")

wn.onkeypress(yukari_git, "Up")
wn.onkeypress(asagi_git, "Down")
wn.onkeypress(saga_git, "Right")
wn.onkeypress(sola_git, "Left")

wn.onkeypress(tusa_basarak_sifirla, "q")
wn.onkeypress(tusa_basarak_sifirla, "Q")
wn.onkeypress(duraklat_degistir, "space")

# 6. Hareket Mekaniği
def hareket():
    global yeni_yon
    kafa.direction = yeni_yon

    if kafa.direction == "up":
        y = kafa.ycor()
        kafa.sety(y + 20)
    elif kafa.direction == "down":
        y = kafa.ycor()
        kafa.sety(y - 20)
    elif kafa.direction == "right":
        x = kafa.xcor()
        kafa.setx(x + 20)
    elif kafa.direction == "left":
        x = kafa.xcor()
        kafa.setx(x - 20)

# 7. Duvar Kontrolü
def duvar_kontrolu():
    if kafa.xcor() > 290 or kafa.xcor() < -290 or kafa.ycor() > 290 or kafa.ycor() < -290:
        oyunu_sifirla(yanma_sebebi="duvar")

# 8. Ana Oyun Döngüsü
try:
    while True:
        wn.update()
        
        # Duraklatıldıysa döngüyü işletme
        if duraklatildi:
            time.sleep(0.1)
            continue

        # Duvar Kontrolü
        duvar_kontrolu()

        # Yem Yeme Kontrolü
        if kafa.distance(yem) < 20:
            yem_konumlandir()

            # Yeni kuyruk parçası üret
            yeni_kuyruk = turtle.Turtle()
            yeni_kuyruk.speed(0)
            yeni_kuyruk.shape("square")
            yeni_kuyruk.color("gray")
            yeni_kuyruk.penup()
            kuyruklar.append(yeni_kuyruk)

            # Hızlandır
            if hiz > 0.03:
                hiz -= 0.003

            # Skoru artır
            puan += 10
            if puan > en_yuksek_puan:
                en_yuksek_puan = puan
            yazici.clear()
            yazici.goto(0, 260)
            yazici.color("white")
            yazici.write(f"Skor: {puan}  En Yüksek: {en_yuksek_puan}", align="center", font=("Courier", 18, "normal"))

        # Kuyrukları Kaydırma
        for i in range(len(kuyruklar) - 1, 0, -1):
            x = kuyruklar[i - 1].xcor()
            y = kuyruklar[i - 1].ycor()
            kuyruklar[i].goto(x, y)

        if len(kuyruklar) > 0:
            x = kafa.xcor()
            y = kafa.ycor()
            kuyruklar[0].goto(x, y)

        # Kafayı Hareket Ettir
        hareket()

        # Kendi Kuyruğuna Çarpma Kontrolü
        for parca in kuyruklar:
            if parca.distance(kafa) < 20:
                oyunu_sifirla(yanma_sebebi="kuyruk")
                break

        time.sleep(hiz)

except (turtle.Terminator, turtle.TclError):
    pass