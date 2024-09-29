import tkinter as tk
from tkinter import messagebox


def calculate_p1():
    try:
        # Получение данных для расчета p1
        impulses = float(entry_impulses.get())  # Количество импульсов
        norm = float(entry_norm.get())  # Норма импульсов
        seconds = float(entry_seconds.get())  # Количество секунд

        # Расчет по формуле для p1
        global p1
        p1 = (3600 * impulses) / (norm * seconds)

        # Отображение результата для p1
        result_label_p1.config(text=f"Результат p1: {p1:.2f}")
        calculate_difference()  # Пересчет расхождения, если p2 уже рассчитано
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числовое значение для p1!")


def calculate_p2():
    try:
        # Получение данных для расчета p2
        voltage = float(entry_voltage.get())  # Напряжение
        current = float(entry_current.get())  # Сила тока

        # Расчет по формуле для p2
        global p2
        p2 = (voltage * current) / 100

        # Отображение результата для p2
        result_label_p2.config(text=f"Результат p2: {p2:.2f}")
        calculate_difference()  # Пересчет расхождения, если p1 уже рассчитано
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числовое значение для p2!")


def calculate_difference():
    # Проверяем, что оба значения p1 и p2 уже посчитаны
    if 'p1' in globals() and 'p2' in globals():
        if p1 == 0 and p2 == 0:
            result_label_diff.config(text="Результат: p1 и p2 равны 0")
            return

        # Расчет процента расхождения
        difference = (abs(p1 - p2) / ((p1 + p2) / 2)) * 100
        result_label_diff.config(text=f"Расхождение: {difference:.2f}%")


# Создаем основное окно
root = tk.Tk()
root.title("Расчет p1 и p2 с расхождением")

# --- Первая часть для расчета p1 ---
frame_p1 = tk.Frame(root)
frame_p1.pack(padx=10, pady=10)

# Заголовок для первой части
label_p1 = tk.Label(frame_p1, text="Расчет p1 (импульсы, норма, секунды):")
label_p1.pack()

# Поля для ввода данных для p1
label_impulses = tk.Label(frame_p1, text="Введите количество импульсов:")
label_impulses.pack()
entry_impulses = tk.Entry(frame_p1)
entry_impulses.pack()

label_norm = tk.Label(frame_p1, text="Введите норму импульсов:")
label_norm.pack()
entry_norm = tk.Entry(frame_p1)
entry_norm.pack()

label_seconds = tk.Label(frame_p1, text="Введите количество секунд:")
label_seconds.pack()
entry_seconds = tk.Entry(frame_p1)
entry_seconds.pack()

# Кнопка для расчета p1
calculate_button_p1 = tk.Button(frame_p1, text="Рассчитать p1", command=calculate_p1)
calculate_button_p1.pack()

# Метка для отображения результата p1
result_label_p1 = tk.Label(frame_p1, text="Результат p1:")
result_label_p1.pack()

# --- Вторая часть для расчета p2 ---
frame_p2 = tk.Frame(root)
frame_p2.pack(padx=10, pady=10)

# Заголовок для второй части
label_p2 = tk.Label(frame_p2, text="Расчет p2 (напряжение, сила тока):")
label_p2.pack()

# Поля для ввода данных для p2
label_voltage = tk.Label(frame_p2, text="Введите напряжение (U):")
label_voltage.pack()
entry_voltage = tk.Entry(frame_p2)
entry_voltage.pack()

label_current = tk.Label(frame_p2, text="Введите силу тока (I):")
label_current.pack()
entry_current = tk.Entry(frame_p2)
entry_current.pack()

# Кнопка для расчета p2
calculate_button_p2 = tk.Button(frame_p2, text="Рассчитать p2", command=calculate_p2)
calculate_button_p2.pack()

# Метка для отображения результата p2
result_label_p2 = tk.Label(frame_p2, text="Результат p2:")
result_label_p2.pack()

# --- Общий результат расхождения ---
frame_diff = tk.Frame(root)
frame_diff.pack(padx=10, pady=10)

# Метка для отображения процента расхождения
result_label_diff = tk.Label(frame_diff, text="Расхождение:")
result_label_diff.pack()

# Запуск основного цикла обработки событий
root.mainloop()
