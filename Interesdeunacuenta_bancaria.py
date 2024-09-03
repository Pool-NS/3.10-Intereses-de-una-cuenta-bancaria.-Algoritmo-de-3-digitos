import tkinter as tk
from tkinter import messagebox

def calcular_saldo():
    try:
        saldo = float(entrada_saldo.get())
        if saldo < 10000.00:
            saldo = saldo * (1 + 0.03)
        else:
            saldo = saldo * (1 + 0.04)
        resultado.set(f"Saldo final: {saldo:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Saldo")
ventana.geometry("300x150")

# Variables
resultado = tk.StringVar()

# Crear y colocar widgets
tk.Label(ventana, text="Ingrese el saldo actual:").pack(pady=10)
entrada_saldo = tk.Entry(ventana)
entrada_saldo.pack()

tk.Button(ventana, text="Calcular Saldo", command=calcular_saldo).pack(pady=10)

tk.Label(ventana, textvariable=resultado).pack()

# Iniciar el loop de la interfaz gráfica
ventana.mainloop()