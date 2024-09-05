from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def message(update: Update, context: CallbackContext):
    # Get the text sent by the user
    user_message = update.message.text
    
    # Reply with the same text or a custom message
    update.message.reply_text("Write your feedback by using commands /feedback")

# Функция для записи отзыва в файл
def record_feedback(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    feedback = ' '.join(context.args)
    user = update.message.from_user
    message_time = update.message.date  # This is a datetime object
    
    # Format the date and time as a string
    formatted_time = message_time.strftime('%Y-%m-%d %H:%M:%S')
    
    # Запись отзыва в файл
    with open('Paws&Tails Feedback.txt', 'a', encoding='utf-8') as file:
        file.write(f"Date: {formatted_time}, User ID: {user_id}, Username: {username}, Feedback: {feedback}\n")

def main():
    # Вставьте свой токен ниже
    updater = Updater("7248837612:AAE2HLYk7GJSKnQ2wzJJMPZPgrUrwFMJFxE", use_context=True)
    dispatcher = updater.dispatcher

    # Обработчик команды /feedback
    dispatcher.add_handler(CommandHandler("feedback", record_feedback))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message))
    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
