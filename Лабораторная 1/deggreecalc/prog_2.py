import tkinter as tk
from tkinter import ttk


def convert_temperature(*args):
    try:
        # Считываем температуру из поля ввода
        input_temp = float(entry_temperature.get())
        # Обнуляем выходные поля
        entry_celsius.delete(0, tk.END)

        # Преобразуем из Фаренгейта в Цельсий
        celsius = (input_temp - 32) / 1.8
        entry_celsius.insert(0, f"{celsius:.2f}")

    except ValueError:
        entry_celsius.delete(0, tk.END)
        entry_celsius.insert(0, "Ошибка")


# Создаем основное окно приложения
root = tk.Tk()
root.title("Преобразователь температур")  # Заголовок окна

# Label для указания Фаренгейта
label_fahrenheit = ttk.Label(root, text="Фаренгейт:")
label_fahrenheit.grid(column=0, row=0)

# Строка для ввода температуры в Фаренгейтах
entry_temperature = tk.StringVar()
entry_temperature.trace_add("write", convert_temperature)

entry_temperature_entry = ttk.Entry(root, textvariable=entry_temperature, width=10)
entry_temperature_entry.grid(column=1, row=0)

# Поля для отображения результата в Цельсиях
ttk.Label(root, text="Цельсий:").grid(column=0, row=1)
entry_celsius = ttk.Entry(root, width=10)
entry_celsius.grid(column=1, row=1)

# Можно задать размер окна
root.geometry("400x150")

# Запускаем главное событие
root.mainloop()
