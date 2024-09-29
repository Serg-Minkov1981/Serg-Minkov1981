import pygame
import random

# Инициализация Pygame
pygame.init()

# Задание размеров экрана и создание окна
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Matrix Code")

# Определение цветов
BLACK = (255, 0, 255)
GREEN = (0, 255, 0)

# Установка шрифта
font_size = 19
font = pygame.font.SysFont('Courier', font_size)

# Количество столбцов (вычисляется на основе ширины экрана и размера шрифта)
columns = SCREEN_WIDTH // font_size

# Создание списка для отслеживания позиций символов
drops = [random.randint(-SCREEN_HEIGHT // font_size, 0) for _ in range(columns)]

# Главный цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение экрана чёрным цветом с легкой прозрачностью для создания эффекта затухания
    screen.fill((100, 15, 50, 100), special_flags=pygame.BLEND_RGBA_SUB)

    # Отображение символов
    for i in range(columns):
        # Генерация случайного символа
        char = chr(random.randint(60, 130))
        text = font.render(char, True, GREEN)

        # Вычисление позиции для отображения символа
        x = i * font_size
        y = drops[i] * font_size

        # Отображение символа
        screen.blit(text, (x, y))

        # Плавное перемещение символов вниз
        drops[i] += 1

        # Сброс позиции символа, если он достиг конца экрана
        if drops[i] * font_size > SCREEN_HEIGHT:
            drops[i] = random.randint(-10, 0)  # Начинаем новую линию

    # Обновление экрана
    pygame.display.flip()

    # Задержка для замедления скорости падения символов
    pygame.time.delay(150)

# Завершение работы Pygame
pygame.quit()
