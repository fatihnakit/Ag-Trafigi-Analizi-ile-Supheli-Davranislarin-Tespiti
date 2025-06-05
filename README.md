<div align="center">
  <img src="https://img.shields.io/github/languages/count/fatihnakit/Projem?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/fatihnakit/Projem?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/fatihnakit/Projem?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/fatihnakit/Projem?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
</div>

## 📌 Project Name / Proje Adı
Ağ Trafiği Analizi ve Güvenlik Tehditlerinin Belirlenmesi

## 📝 A brief, engaging description of your project / Projenizin kısa ve ilgi çekici bir açıklaması
Bu projede yerel ağda toplanan veri trafiği analiz edilerek potansiyel güvenlik tehditleri (DDoS, port tarama, olağandışı IP trafiği) belirlenmiştir. Wireshark ile alınan `.pcap` dosyaları Python kullanılarak incelenmiş, sonuçlar görselleştirilmiş ve güvenlik açısından yorumlanmıştır.

---

## ✨ Features / Özellikler
- **Paket Analizi:** Pcap dosyası üzerinden IP, port ve protokol analizleri yapılır.  
- **Şüpheli Trafik Tespiti:** Çok sayıda istek yapan IP’ler ve olağandışı port kullanımları belirlenir.  
- **Grafiksel Raporlama:** Matplotlib ile veri görselleştirmesi yapılır.  
- **Kullanıcı Dostu Script:** Komut satırı argümanları ile kolay çalıştırma imkanı.  
- **Yorumlu Kod Yapısı:** Öğrencilere ve araştırmacılara uygun açıklamalar içerir.  


---

## 🛤️ Roadmap / Yol Haritası

Projeye ait plan ve geliştirme aşamaları için lütfen [ROADMAP.md](ROADMAP.md) dosyasına göz atın.


---


  ## 🔬 Research / Araştırmalar
  
  | Topic / Başlık             | Link                                 | Description / Açıklama                                      |
  |---------------------------|--------------------------------------|--------------------------------------------------------------|
  | Wireshark Analizi         | researchs/wireshark-analysis.md      | Wireshark ile pcap toplama ve protokol bazlı çözümleme      |
  | Scapy ile Trafik Okuma    | researchs/scapy-usage.md             | Python'da Scapy ile pcap dosyalarının işlenmesi              |
  | Şüpheli IP Tespiti        | researchs/ip-detection.md            | Trafikte anormal davranan IP’lerin belirlenmesi              |


---

## ⚙️ Installation / Kurulum


### Clone the Repository / Depoyu Klonlayın:
```bash
git clone https://github.com/fatihnakit/Projem.git
cd Projem
```
Set Up Virtual Environment / Sanal Ortam Kurulumu (Önerilir):
```
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
```
Install Dependencies / Bağımlılıkları Yükleyin:
```
pip install -r requirements.txt

```
▶️ Usage / Kullanım
Run the project / Projeyi çalıştırın:

python main.py --input data/traffic.pcap --output results.txt

Steps / Adımlar:
data/ klasörüne analiz edilecek .pcap dosyasını koyun.

Script'i yukarıdaki gibi çalıştırın.

results.txt içinde analiz sonuçlarını görüntüleyin.

graphs/ klasöründe otomatik oluşturulan grafiklere bakın.



---

🤝 Contributing / Katkıda Bulunma
Topluluk katkılarına açığız! Katkıda bulunmak için:

1-Bu projeyi fork'layın

2-Fork'u klonlayın:
```
git clone git@github.com:YOUR_USERNAME/Projem.git
```
3-Yeni bir branch oluşturun:
```
git checkout -b feature/your-feature
```
4-Değişiklikleri commit’leyin ve push edin

5-Pull request gönderin

6-Kodlama kurallarına uyun (bkz: CONTRIBUTING.md)
---

📄 License / Lisans

MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına göz atabilirsiniz.

---

📬 Contact / İletişim

Sorularınız veya önerileriniz için:
- **E-posta**: fatihnakit@gmail.com
- **GitHub**: [fatihnakit](https://github.com/fatihnakit)



---

*Replace placeholders (e.g., YOUR_USERNAME/YOUR_REPO) with your project details.*
