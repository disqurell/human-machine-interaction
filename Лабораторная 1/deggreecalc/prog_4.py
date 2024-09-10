import tkinter as tk
from tkinter import ttk


def convert_temperature(event=None):
    try:
        # Проверяем, в каком формате была введена температура
        if entry_type.get() == "Фаренгейт":
            input_temp = float(entry_fahrenheit.get())
            celsius = (input_temp - 32) / 1.8
            kelvin = celsius + 273.15

            entry_celsius.delete(0, tk.END)
            entry_kelvin.delete(0, tk.END)
            entry_fahrenheit.delete(0, tk.END)

            entry_celsius.insert(0, f"{celsius:.2f}")
            entry_kelvin.insert(0, f"{kelvin:.2f}")
            entry_fahrenheit.insert(0, f"{input_temp:.2f}")

            # entry_fahrenheit.insert(0, input_temp)

        elif entry_type.get() == "Цельсий":
            input_temp = float(entry_celsius.get())
            fahrenheit = input_temp * 1.8 + 32
            kelvin = input_temp + 273.15
            # entry_celsius.insert(0, input_temp)

            entry_celsius.delete(0, tk.END)
            entry_kelvin.delete(0, tk.END)
            entry_fahrenheit.delete(0, tk.END)

            entry_celsius.insert(0, f"{input_temp:.2f}")
            entry_fahrenheit.insert(0, f"{fahrenheit:.2f}")
            entry_kelvin.insert(0, f"{kelvin:.2f}")

        elif entry_type.get() == "Кельвин":
            input_temp = float(entry_kelvin.get())
            celsius = input_temp - 273.15
            fahrenheit = celsius * 1.8 + 32

            entry_celsius.delete(0, tk.END)
            entry_kelvin.delete(0, tk.END)
            entry_fahrenheit.delete(0, tk.END)

            entry_celsius.insert(0, f"{celsius:.2f}")
            entry_fahrenheit.insert(0, f"{fahrenheit:.2f}")
            entry_kelvin.insert(0, f"{input_temp:.2f}")

    except ValueError:
        entry_celsius.delete(0, tk.END)
        entry_fahrenheit.delete(0, tk.END)
        entry_kelvin.delete(0, tk.END)
        entry_celsius.insert(0, "Ошибка")
        entry_fahrenheit.insert(0, "Ошибка")
        entry_kelvin.insert(0, "Ошибка")


def on_entry_fahrenheit(event):
    entry_type.set("Фаренгейт")
    convert_temperature(event)


def on_entry_celsius(event):
    entry_type.set("Цельсий")
    convert_temperature(event)


def on_entry_kelvin(event):
    entry_type.set("Кельвин")
    convert_temperature(event)


# Создаем основное окно приложения
root = tk.Tk()
root.title("Температурный Конвертер")

# Вложенная переменная типа предназначения
entry_type = tk.StringVar(value="Цельсий")  # Устанавливаем по умолчанию как "Цельсий"

# Поля для отображения результатов
ttk.Label(root, text="Цельсий:").grid(column=0, row=1)
entry_celsius = ttk.Entry(root, width=10)
entry_celsius.grid(column=1, row=1)

ttk.Label(root, text="Фаренгейт:").grid(column=0, row=2)
entry_fahrenheit = ttk.Entry(root, width=10)
entry_fahrenheit.grid(column=1, row=2)

ttk.Label(root, text="Кельвин:").grid(column=0, row=3)
entry_kelvin = ttk.Entry(root, width=10)
entry_kelvin.grid(column=1, row=3)

# Привязываем клавишу "Enter" к каждому полю
entry_fahrenheit.bind("<Return>", on_entry_fahrenheit)
entry_celsius.bind("<Return>", on_entry_celsius)
entry_kelvin.bind("<Return>", on_entry_kelvin)

# Можно задать размер окна
root.geometry("400x150")

# Запускаем главное событие
root.mainloop()
