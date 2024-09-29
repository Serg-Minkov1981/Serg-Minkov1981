from PIL import Image

# Открываем изображение формата .webp
img = Image.open('фото.webp')

# Конвертируем и сохраняем как .jpg
img = img.convert('RGB')  # Важно для сохранения в формате .jpg
img.save('электро.jpg', 'JPEG')
