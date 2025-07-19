from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7558740319:AAGJgjYPvZ5W9dCwU22aGEE1nuLUuGuajaY"  # ← لا تنسى التوكن

def send_pdf(update: Update, context: CallbackContext):
    try:
        with open("bak.pdf", "rb") as file:
            update.message.reply_document(document=InputFile(file), filename="بكالوريا.pdf")
    except Exception as e:
        update.message.reply_text(f"خطأ أثناء إرسال الملف:\n{e}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("pdf", send_pdf))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()