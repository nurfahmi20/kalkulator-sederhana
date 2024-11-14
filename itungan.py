import tkinter as tk

# Fungsi untuk menangani input tombol
def tombol_ditekan(num):
    current = layar.get()
    layar.delete(0, tk.END)
    layar.insert(tk.END, current + str(num))

# Fungsi untuk menghitung hasil operasi
def hitung():
    try:
        result = eval(layar.get())
        layar.delete(0, tk.END)
        layar.insert(tk.END, str(result))
    except:
        layar.delete(0, tk.END)
        layar.insert(tk.END, "Error")

# Fungsi untuk membersihkan layar
def clear():
    layar.delete(0, tk.END)

# Membuat jendela aplikasi
window = tk.Tk()
window.title("Kalkulator Sederhana")

# Membuat layar untuk menampilkan input dan hasil
layar = tk.Entry(window, width=35, borderwidth=5, font=('Arial', 18))
layar.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Membuat tombol-tombol angka dan operasi
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Menambahkan tombol ke jendela
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(window, text=text, padx=20, pady=20, command=hitung, bg="lightgreen").grid(row=row, column=col)
    else:
        tk.Button(window, text=text, padx=20, pady=20, command=lambda t=text: tombol_ditekan(t)).grid(row=row, column=col)

# Tombol untuk menghapus layar
tk.Button(window, text="Clear", padx=79, pady=20, command=clear, bg="lightcoral").grid(row=5, column=0, columnspan=4)

# Menjalankan aplikasi
window.mainloop()
