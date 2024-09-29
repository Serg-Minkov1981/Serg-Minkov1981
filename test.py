import speech_recognition as sr
import webbrowser
import dgek  # Импортируем наш файл dgek.py

# Оптимизация работы с микрофоном: заранее настроим распознавание шумов
recognizer = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("Слушаю вас...")
        recognizer.adjust_for_ambient_noise(source)  # Настройка на уровень фонового шума (один раз)

        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language='ru-RU')  # Распознавание на русском языке
            print(f"Вы сказали: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
            return None
        except sr.RequestError:
            print("Ошибка соединения с Google API")
            return None


# Функция для обработки команд
def handle_command(command):
    if "привет" in command:
        # Используем кэширование для фразы "Привет! Как ваши дела?"
        dgek.cache_speech("Привет! Как ваши дела?", "hello.mp3")
        dgek.play_cached_speech("hello.mp3")
    elif "как тебя зовут" in command:
        # Используем кэширование для фразы "Меня зовут Помощник."
        dgek.cache_speech("Меня зовут Помощник.", "name.mp3")
        dgek.play_cached_speech("name.mp3")
    elif "открой google" in command:
        dgek.cache_speech("Открываю Google.", "open_google.mp3")
        dgek.play_cached_speech("open_google.mp3")
        webbrowser.open("https://www.google.com")
    elif "выход" in command or "стоп" in command:
        dgek.cache_speech("До свидания!", "goodbye.mp3")
        dgek.play_cached_speech("goodbye.mp3")
        return False
    else:
        dgek.cache_speech("Извините, я не понял команду.", "not_understood.mp3")
        dgek.play_cached_speech("not_understood.mp3")
    return True


# Основная функция работы ассистента
def main():
    # Кэшируем приветственное сообщение
    dgek.cache_speech("Привет! Я ваш голосовой помощник. Чем могу помочь?", "greeting.mp3")
    dgek.play_cached_speech("greeting.mp3")

    try:
        while True:
            command = listen()
            if command:
                if not handle_command(command):
                    break  # Завершение работы программы
    except KeyboardInterrupt:
        dgek.cache_speech("Программа завершена. До свидания!", "interrupt.mp3")
        dgek.play_cached_speech("interrupt.mp3")
        print("Работа программы завершена вручную.")


if __name__ == "__main__":
    main()
