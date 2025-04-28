"Nama: Ahmad Khoerudin"
"NIM: 122203003"
"Mata Kuliah: Pemrograman Asinkron"
"Tugas: Pertemuan 7 - UTS"

import asyncio
import aiohttp
from datetime import datetime
import sys

# Daftar website yang akan dimonitor
WEBSITES = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.python.org",
    "https://www.openai.com",
    "https://www.example.com",
    "https://www.thiswebsitedoesnotexistforsure.com"
]

async def check_website(session, url):
    """Mengecek status sebuah website secara asinkron"""
    try:
        async with session.get(url, timeout=10) as response:
            status = response.status
            return url, status
    except Exception as e:
        return url, f"Error: {str(e)}"

async def log_to_file(message):
    """Menyimpan log ke file log.txt"""
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

async def monitor_websites():
    """Fungsi utama untuk memonitor website"""
    async with aiohttp.ClientSession() as session:
        while True:
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            print(f"\n{timestamp} Memeriksa status website...")
            
            tasks = [check_website(session, url) for url in WEBSITES]
            results = await asyncio.gather(*tasks)
            
            for url, status in results:
                message = f"{timestamp} {url} - Status: {status}"
                print(message)
                await log_to_file(message)
                
                # Cek jika status bukan 200
                if status != 200:
                    alert = f"{timestamp} {url} - SITE DOWN! Status: {status}"
                    print("\a" + "!"*50)  # Bunyi alert dan visual alert
                    print("!"*10 + " SITE DOWN! " + "!"*10)
                    print(alert)
                    print("!"*50)
                    await log_to_file("ALERT: " + alert)
            
            # Tunggu 10 detik sebelum pengecekan berikutnya
            await asyncio.sleep(10)

if __name__ == "__main__":
    print("Aplikasi Monitoring Website Asinkron")
    print(f"Memantau {len(WEBSITES)} website setiap 10 detik")
    print("Tekan Ctrl+C untuk menghentikan")
    print("Log disimpan di log.txt")
    
    try:
        asyncio.run(monitor_websites())
    except KeyboardInterrupt:
        print("\nMonitoring dihentikan oleh pengguna")
        sys.exit(0)
