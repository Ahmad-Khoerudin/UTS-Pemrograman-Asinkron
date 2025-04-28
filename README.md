Penjelasan Kode:

Fungsi check_website:

1. Menggunakan aiohttp untuk melakukan request HTTP asinkron

2. Mengembalikan URL dan status code (atau pesan error jika gagal)

Fungsi log_to_file:

1. Menyimpan log ke file log.txt secara asinkron

2. Dipisahkan sebagai fungsi terpisah untuk modularitas

Fungsi monitor_websites:

1. Membuat sesi HTTP asinkron

2. Dalam infinite loop:

        Membuat timestamp

        Menjalankan pengecekan semua website secara paralel menggunakan asyncio.gather

        Mencetak dan menyimpan hasilnya

        Memberikan alert (bunyi dan visual) jika website down (status ≠ 200)

        Menunggu 10 detik sebelum pengecekan berikutnya
   
Fitur Tambahan:

1. Alert dengan bunyi (\a) dan visual ketika website down

2. Penanganan Ctrl+C untuk menghentikan program dengan graceful

3. Logging ke file terpisah
