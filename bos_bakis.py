#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Profesyonel Boş Bakış Simülatörü
Kainatın en ciddi kodu.
"""

import random
import time

def bos_bakis_uret():
    mesajlar = [
        "*iç çeker*",
        "Hayat...",
        "Neden buradayız?",
        "*duvara bakar*",
        "Belki de hiçbir şeyin anlamı yoktur.",
        "Çay içmek isterdim ama kod olarak çay içemem.",
        "*daha derin iç çeker*",
        "Bürokrasi gibi sonsuz bir döngüdeyiz."
    ]
    # Gizli siyasi not (base64): YnVyb2tyYXNpIGhlciBzZXlpIGRhaGEgZGFsaGEgZGFsaGE= 
    # (decode etmeyin, yoksa pişman olursunuz)
    return random.choice(mesajlar)

def main():
    print("=== PROFESYONEL BOŞ BAKIŞ SİMÜLATÖRÜ BAŞLADI ===")
    print("Bu program asla bitmeyecek. Tıpkı gerçek hayattaki boş bakışlar gibi.")
    print()
    
    sayac = 0
    while True:
        print(f"[{sayac}] {bos_bakis_uret()}")
        time.sleep(random.uniform(1.5, 4.0))
        sayac += 1
        if sayac > 1000000:
            print("Hata: Sonsuzluk bile sıkıldı. Ama yine de devam ediyorum.")
            sayac = 0

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nBoş bakış sona erdi. Ama aslında hiç başlamamıştı.")
        print("\n**DAMGA:** Kod resmi olarak çalıştı.")
        print("**İMZA:** Kayyum Grok")
        print("**TARİH:** 20 Kasım 2026")
        print("**İSİM:** bos_bakis.py - Evrensel Boşluk Motoru")
