import os
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler, CallbackContext
#функция приветствия при вводе ссылки /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Информация 	📝 ", callback_data='info')],
        [InlineKeyboardButton("Помощь", callback_data='help')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет, я  бот --Т800-- <..😀..>!  ", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # Отвечаем на запрос кнопки

    if query.data == 'info':
        await query.edit_message_text(text="hello")
    elif query.data == 'help':
        await query.edit_message_text(text="help")

async def profile(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    update.message.reply_text(f'Привет, {user.first_name}! Твой ID: {user.id}')

#функция для обработки текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text.lower() #приводим к нижнему регистру

    #проверка на ключевые слова
    if "привет" in user_message:
        await update.message.reply_text("Привет! Как дела, какую оценку получил? ")
    elif "пока" in user_message:
        await update.message.reply_text("До встречи буду ждать тебя")
    elif "как дела" in user_message:
        await update.message.reply_text("Я в порядке, спасибо! А ты?")
    elif "как тебя зовут" in user_message:
        await update.message.reply_text("Меня зовут --Т800-- 🤖 ")
    else:
        await update.message.reply_text(f"Ты сказал {update.message.text}")

#основная функция запуска бота
def main():
    load_dotenv()

    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    #создаем приложение
    application = Application.builder().token(TOKEN).build()

    #добавляем обработчик команд и сообщений
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("profile", profile))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))


    #запускаем бота
    application.run_polling()


if __name__ == '__main__':
    main()




