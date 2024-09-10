import tkinter as tk
from tkinter import ttk


def convert_from_fahrenheit(event=None):
    try:
        # Считываем температуру из поля ввода Фаренгейта
        input_temp = float(entry_fahrenheit.get())

        # Преобразуем из Фаренгейта в Цельсий
        celsius = (input_temp - 32) / 1.8

        # Обновляем поле Цельсия
        entry_celsius.set(f"{celsius:.2f}")

    except ValueError:
        entry_celsius.set("Ошибка")


def convert_from_celsius(event=None):
    try:
        # Считываем температуру из поля ввода Цельсия
        input_temp = float(entry_celsius.get())

        # Преобразуем из Цельсия в Фаренгейт
        fahrenheit = (input_temp * 1.8) + 32

        # Обновляем поле Фаренгейта
        entry_fahrenheit.set(f"{fahrenheit:.2f}")

    except ValueError:
        entry_fahrenheit.set("Ошибка")


# Создаем основное окно приложения
root = tk.Tk()
root.title("Преобразователь температур")  # Заголовок окна

# Label для указания Фаренгейта
label_fahrenheit = ttk.Label(root, text="Фаренгейт:")
label_fahrenheit.grid(column=0, row=0)

# Строка для ввода температуры в Фаренгейтах
entry_fahrenheit = tk.StringVar()
entry_fahrenheit_entry = ttk.Entry(root, textvariable=entry_fahrenheit, width=10)
entry_fahrenheit_entry.grid(column=1, row=0)
entry_fahrenheit_entry.bind("<Return>", convert_from_fahrenheit)

# Поля для отображения результата в Цельсиях
ttk.Label(root, text="Цельсий:").grid(column=0, row=1)
entry_celsius = tk.StringVar()
entry_celsius_entry = ttk.Entry(root, textvariable=entry_celsius, width=10)
entry_celsius_entry.grid(column=1, row=1)
entry_celsius_entry.bind("<Return>", convert_from_celsius)

# Можно задать размер окна
root.geometry("400x150")

# Запускаем главное событие
root.mainloop()
