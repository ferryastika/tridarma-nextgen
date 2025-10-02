# tridharma-nextgen
Kode ini mensimulasikan aliran data dalam sistem Tridharma Perguruan Tinggi, menghitung metrik, memvisualisasikan hasilnya, dan memberikan analisis.
Nilai awal dari 'Supply'  (Pendidikan, Penelitian, Pengabdian) mengalir melalui sistem, menghasilkan 'Output',  memenuhi 'Demand', dan memicu 'Kolaborasi' serta 'Rekognisi'.  Terdapat feedback loop di mana kolaborasi dan kapasitas kembali memperkuat pilar supply,  menciptakan siklus yang dinamis. Sebelum anda mulai masuk ke dalam kode ini, ada baiknya anda membaca file PDF berjudul :"Tridharma NextGen Perguruan Tinggi yang Berdampak"
---Ferry Astika S---

_______________________________________________________

### **Output Eksekusi Kode**

```text
=== SIMULASI DATA FLOW TRIDHARMA ===

--- Iterasi 1 ---
P1: 10.00 → 6.80
P2: 8.00 → 4.60
P3: 7.00 → 4.10
CGrad: 0.00 → 1.65
Proto: 0.00 → 1.32
Policy: 0.00 → 1.19
DUDI: 5.00 → 2.50
ACAD: 4.00 → 2.00
PUB: 3.00 → 1.50
COL: 0.00 → 2.20
REC: 0.00 → 0.00
CAREER: 0.00 → 0.00
CAP: 6.00 → 1.00
ADMIN: 4.00 → 2.00
ALIGN: 0.00 → 0.00

📊 METRICS Iterasi 1:
    Total Supply: 15.50
    Total Demand: 6.00
    Score Kolaborasi: 2.20
    Score Rekognisi: 0.00
    ⚠️  Supply Berlebih (Over-supply)

--- Iterasi 2 ---
P1: 6.80 → 4.41
P2: 4.60 → 2.76
P3: 4.10 → 2.51
CGrad: 1.65 → 2.00
Proto: 1.32 → 1.66
Policy: 1.19 → 1.48
DUDI: 2.50 → 2.08
ACAD: 2.00 → 1.09
PUB: 1.50 → 0.81
COL: 2.20 → 2.29
REC: 0.00 → 0.74
CAREER: 0.00 → 0.00
CAP: 1.00 → -0.25
ADMIN: 2.00 → 0.81
ALIGN: 0.00 → 0.00

📊 METRICS Iterasi 2:
    Total Supply: 9.68
    Total Demand: 3.98
    Score Kolaborasi: 2.29
    Score Rekognisi: 0.74
    ⚠️  Supply Berlebih (Over-supply)

--- Iterasi 3 ---
P1: 4.41 → 3.29
P2: 2.76 → 2.07
P3: 2.51 → 1.95
CGrad: 2.00 → 1.87
Proto: 1.66 → 1.66
Policy: 1.48 → 1.50
DUDI: 2.08 → 1.83
ACAD: 1.09 → 0.80
PUB: 0.81 → 0.49
COL: 2.29 → 2.11
REC: 0.74 → 1.11
CAREER: 0.00 → 0.19
CAP: -0.25 → -0.53
ADMIN: 0.81 → 0.12
ALIGN: 0.00 → 0.30

📊 METRICS Iterasi 3:
    Total Supply: 7.32
    Total Demand: 3.11
    Score Kolaborasi: 2.11
    Score Rekognisi: 1.11
    ⚠️  Supply Berlebih (Over-supply)

--- Iterasi 4 ---
P1: 3.29 → 2.45
P2: 2.07 → 1.73
P3: 1.95 → 1.67
CGrad: 1.87 → 1.70
Proto: 1.66 → 1.67
Policy: 1.50 → 1.51
DUDI: 1.83 → 1.61
ACAD: 0.80 → 0.65
PUB: 0.49 → 0.32
COL: 2.11 → 2.01
REC: 1.11 → 1.40
CAREER: 0.19 → 0.32
CAP: -0.53 → -0.32
ADMIN: 0.12 → -0.22
ALIGN: 0.30 → 0.52

📊 METRICS Iterasi 4:
    Total Supply: 5.85
    Total Demand: 2.58
    Score Kolaborasi: 2.01
    Score Rekognisi: 1.40
    ⚠️  Supply Berlebih (Over-supply)

--- Iterasi 5 ---
P1: 2.45 → 1.93
P2: 1.73 → 1.52
P3: 1.67 → 1.47
CGrad: 1.70 → 1.58
Proto: 1.67 → 1.64
Policy: 1.51 → 1.51
DUDI: 1.61 → 1.45
ACAD: 0.65 → 0.57
PUB: 0.32 → 0.24
COL: 2.01 → 1.94
REC: 1.40 → 1.57
CAREER: 0.32 → 0.51
CAP: -0.32 → -0.05
ADMIN: -0.22 → -0.49
ALIGN: 0.52 → 0.76

📊 METRICS Iterasi 5:
    Total Supply: 4.92
    Total Demand: 2.26
    Score Kolaborasi: 1.94
    Score Rekognisi: 1.57
    ⚠️  Supply Berlebih (Over-supply)

--- Iterasi 6 ---
P1: 1.93 → 1.62
P2: 1.52 → 1.41
P3: 1.47 → 1.36
CGrad: 1.58 → 1.50
Proto: 1.64 → 1.61
Policy: 1.51 → 1.50
DUDI: 1.45 → 1.33
ACAD: 0.57 → 0.52
PUB: 0.24 → 0.19
COL: 1.94 → 1.89
REC: 1.57 → 1.68
CAREER: 0.51 → 0.65
CAP: -0.05 → 0.14
ADMIN: -0.49 → -0.66
ALIGN: 0.76 → 0.94

📊 METRICS Iterasi 6:
    Total Supply: 4.39
    Total Demand: 2.05
    Score Kolaborasi: 1.89
    Score Rekognisi: 1.68
    ⚠️  Supply Berlebih (Over-supply)

--- Iterasi 7 ---
P1: 1.62 → 1.40
P2: 1.41 → 1.33
P3: 1.36 → 1.29
CGrad: 1.50 → 1.44
Proto: 1.61 → 1.59
Policy: 1.50 → 1.50
DUDI: 1.33 → 1.25
ACAD: 0.52 → 0.48
PUB: 0.19 → 0.16
COL: 1.89 → 1.86
REC: 1.68 → 1.76
CAREER: 0.65 → 0.76
CAP: 0.14 → 0.25
ADMIN: -0.66 → -0.77
ALIGN: 0.94 → 1.08

📊 METRICS Iterasi 7:
    Total Supply: 4.02
    Total Demand: 1.89
    Score Kolaborasi: 1.86
    Score Rekognisi: 1.76
    ⚠️  Supply Berlebih (Over-supply)

--- Iterasi 8 ---
P1: 1.40 → 1.25
P2: 1.33 → 1.28
P3: 1.29 → 1.24
CGrad: 1.44 → 1.40
Proto: 1.59 → 1.57
Policy: 1.50 → 1.49
DUDI: 1.25 → 1.18
ACAD: 0.48 → 0.46
PUB: 0.16 → 0.14
COL: 1.86 → 1.83
REC: 1.76 → 1.82
CAREER: 0.76 → 0.85
CAP: 0.25 → 0.33
ADMIN: -0.77 → -0.84
ALIGN: 1.08 → 1.18

📊 METRICS Iterasi 8:
    Total Supply: 3.78
    Total Demand: 1.78
    Score Kolaborasi: 1.83
    Score Rekognisi: 1.82
    ⚠️  Supply Berlebih (Over-supply)

=== ANALISIS KESEHATAN SISTEM ===
Efektivitas Kolaborasi: 1.00
Efisiensi Supply: 0.80
Efisiensi Administratif: 3.51
```

### **Visualisasi Grafik Hasil Simulasi**

 detail dari visualisasi yang dihasilkan oleh kode tersebut setelah 8 iterasi

Grafik yang dihasilkan menampilkan jaringan terarah (directed graph) yang merepresentasikan ekosistem Tridharma Perguruan Tinggi.

  * **Tata Letak:** Node-node diatur secara logis dari kiri ke kanan mengikuti alur proses:

      * **Kiri:** Kelompok node 'Supply' (`P1`, `P2`, `P3`) berwarna merah muda.
      * **Tengah Kiri:** Kelompok node 'Output' (`CGrad`, `Proto`, `Policy`) berwarna biru muda.
      * **Tengah:** Node 'Kolaborasi' (`COL`) berwarna oranye dan 'Rekognisi' (`REC`) berwarna jingga.
      * **Tengah Kanan:** Kelompok node 'Demand' (`DUDI`, `ACAD`, `PUB`) berwarna hijau muda.
      * **Kanan:** Kelompok node 'Support System' (`CAREER`, `CAP`) berwarna biru langit dan ungu muda.
      * **Bawah:** Node 'Constraint' dan 'Incentive' (`ADMIN`, `ALIGN`) berwarna pink dan putih.

  * **Ukuran Node:** Ukuran setiap lingkaran node merepresentasikan nilainya (`value`) di akhir simulasi.

      * Node `P1`, `P2`, `P3`, dan `DUDI` yang awalnya besar, kini ukurannya mengecil secara signifikan.
      * Node `COL` (Kolaborasi) dan `REC` (Rekognisi) tumbuh menjadi cukup besar, menunjukkan akumulasi nilai dari interaksi sistem.
      * Node `ADMIN` (Beban Administratif) menjadi sangat kecil, bahkan nilainya negatif, yang direpresentasikan oleh ukuran node minimum.

  * **Warna Panah (Edge):**

      * **Hijau:** Sebagian besar panah berwarna hijau, menandakan hubungan yang saling menguatkan (pengaruh positif, `weight > 0`).
      * **Merah:** Terdapat dua panah berwarna merah yang menunjukkan pengaruh negatif atau penghambat:
        1.  Dari `ADMIN` ke `CAP`: Beban administratif mengurangi kapasitas sumber daya.
        2.  Dari `REC` ke `ADMIN`: Sistem rekognisi yang baik dapat mengurangi beban administratif.

  * **Label:** Setiap node memiliki label yang menunjukkan ID-nya dan nilai akhirnya (misal: `COL\n(1.8)`). Setiap panah juga memiliki label yang menjelaskan sifat hubungan tersebut (misal: "kolaborasi-supply(loop-1)").

Secara keseluruhan, visualisasi menunjukkan bagaimana nilai awal dari 'Supply' (Pendidikan, Penelitian, Pengabdian) mengalir melalui sistem, menghasilkan 'Output', memenuhi 'Demand', dan memicu 'Kolaborasi' serta 'Rekognisi'. Terdapat *feedback loop* di mana kolaborasi dan kapasitas kembali memperkuat pilar supply, menciptakan siklus yang dinamis.
