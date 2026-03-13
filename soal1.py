import matplotlib.pyplot as plt

nilai = []
for i in range(10):
    n = float(input(f"Masukkan nilai ke-{i+1}: "))
    nilai.append(n)
    
nilai_tertinggi = max(nilai)
nilai_terendah = min(nilai)
rata_rata = sum(nilai) / len(nilai)

lulus = 0
tidak_lulus = 0

for n in nilai:
    if n >= 60:
        lulus += 1
    else:
        tidak_lulus += 1
        
print("\nHasil Analisis Nilai")
print("Nilai tertinggi :", nilai_tertinggi)
print("Nilai terendah  :", nilai_terendah)
print("Rata-rata       :", rata_rata)
print("Jumlah lulus    :", lulus)
print("Jumlah tidak lulus :", tidak_lulus)

plt.figure(figsize=(5,4))
plt.bar(["Tertinggi", "Terendah"], [nilai_tertinggi, nilai_terendah], color=["green","red"])
plt.title("Perbandingan Nilai Tertinggi dan Terendah")
plt.ylabel("Nilai")
plt.show()

plt.figure(figsize=(5,4))
plt.pie([lulus, tidak_lulus], labels=["Lulus", "Tidak Lulus"], autopct="%1.1f%%", colors=["blue","orange"])
plt.title("Persentase Kelulusan Mahasiswa")
plt.show()
    