import os
import time
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Функция для выключения компьютера
def shutdown():
    if os.name == 'nt':  # Для Windows
        os.system('shutdown /s /f /t 0')
    else:  # Для Linux и MacOS
        os.system('shutdown now')

# Функция для расчета времени и выключения
def schedule_shutdown():
    shutdown_time_str = entry_time.get()
    try:
        # Преобразование времени из строки в объект datetime
        shutdown_time = datetime.now().replace(
            hour=int(shutdown_time_str.split(":")[0]),
            minute=int(shutdown_time_str.split(":")[1]),
            second=0,
            microsecond=0
        )
        current_time = datetime.now()
        difference = (shutdown_time - current_time).total_seconds()

        if difference > 0:
            # Ожидание до указанного времени
            messagebox.showinfo("Ожидание", f"Компьютер выключится через {int(difference)} секунд.")
            root.after(int(difference * 1000), shutdown)
        else:
            messagebox.showerror("Ошибка", "Указанное время уже прошло.")
    except (ValueError, IndexError):
        messagebox.showerror("Ошибка", "Введите корректное время в формате ЧЧ:ММ.")

# Создание графического интерфейса
root = tk.Tk()
root.title("Выключение ПК по расписанию")

# Метка для ввода времени
label = tk.Label(root, text="Введите время выключения (ЧЧ:ММ):")
label.pack(padx=20, pady=10)

# Поле ввода времени
entry_time = tk.Entry(root)
entry_time.pack(padx=20, pady=10)

# Кнопка для подтверждения
button = tk.Button(root, text="Запланировать выключение", command=schedule_shutdown)
button.pack(padx=20, pady=20)

# Запуск окна
root.mainloop()
