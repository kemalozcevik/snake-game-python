<img width="594" height="632" alt="1" src="https://github.com/user-attachments/assets/c27f7fc4-abd6-4711-86a4-ebf376a9fb48" />
# 🐍 Python Turtle - Klasik Yılan Oyunu

Python'ın yerleşik `turtle` modülü kullanılarak sıfırdan geliştirilmiş, grid tabanlı klasik Snake oyunu.

---

## 🚀 Özellikler

- **Grid Tabanlı Hareket:** 20 piksellik adımlarla ızgara hareketi.
- **Kuyruk Takip Algoritması:** Listenin tersten taranmasıyla kafayı takip eden dinamik gövde parçaları.
- **Güvenli Yem Konumlandırma:** Yemin yılan kafası veya gövdesi üzerinde doğmasını engelleyen doğrulama döngüsü.
- **Input Buffer Kilidi:** Tek karede ters yöne art arda basılarak kendi içine dönüp yanmayı engelleyen yön mekanizması.
- **Dinamik Hızlanma:** Skor arttıkça oyun temposunun kademeli olarak yükselmesi.
- **Canlı Skor ve Rekor:** Oturum içi en yüksek skoru hafızada tutan dinamik gösterge.
- **Duraklatma (Pause):** `Space` tuşu ile oyunu dondurma ve sürdürme.
- **Oyun Bitti Ekranı:** Duvara veya kuyruğa çarpıldığında ortada beliren uyarı ve skor ekranı.

---

## 🎮 Kontroller

| Tuş | Eylem |
| :--- | :--- |
| **W / ↑** | Yukarı |
| **S / ↓** | Aşağı |
| **A / ←** | Sola |
| **D / →** | Sağa |
| **Space** | Duraklat / Devam Et |
| **Q** | Oyunu Sıfırla |

---

## 🛠️ Çalıştırma

Harici kütüphane gerektirmez.

```bash
python main.py
