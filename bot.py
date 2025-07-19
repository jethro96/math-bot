from telegram import Update, ReplyKeyboardMarkup, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "7558740319:AAGJgjYPvZ5W9dCwU22aGEE1nuLUuGuajaY"  # ← عدّل التوكن الحقيقي

# 🟩 start – أول رسالة
def start(update: Update, context: CallbackContext):
    keyboard = [
        ["📘 ابتدائي (قيد التجهيز)", "📗 إعدادي"],
        ["📕 ثانوي", "🎈 ترفيهي"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("أهلاً فيك ببوت شروحات الرياضيات!\nاختر المرحلة يلي بدك ياها:", reply_markup=reply_markup)

# 🟨 الردود
def handle_buttons(update: Update, context: CallbackContext):
    choice = update.message.text

    if choice == "📘 ابتدائي (قيد التجهيز)":
        update.message.reply_text("قسم الابتدائي قيد التجهيز، ترقبونا قريباً!")

    elif choice == "📗 إعدادي":
        keyboard = [["صف سابع (قيد الإنجاز)"],
                    ["صف ثامن (قيد الإنجاز)"],
                    ["صف تاسع (قيد الإنجاز)"],
                    ["⬅️ رجوع"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        update.message.reply_text("اختر الصف الإعدادي:", reply_markup=reply_markup)

    elif choice == "📕 ثانوي":
        keyboard = [["صف عاشر (قيد الإنجاز)"],
                    ["صف حادي عشر (قيد الإنجاز)"],
                    ["📄 بكالوريا"],
                    ["⬅️ رجوع"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        update.message.reply_text("اختر الصف الثانوي:", reply_markup=reply_markup)

    elif choice == "📄 بكالوريا":
        keyboard = [["📂 الجزء الأول", "📂 الجزء الثاني"],
                    ["⬅️ رجوع"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        update.message.reply_text("اختر القسم يلي بدك يا من البكالوريا:", reply_markup=reply_markup)

    elif choice == "📂 الجزء الأول":
        try:
            with open("الوحدة الثانية شرح.pdf", "rb") as file:
                update.message.reply_document(document=InputFile(file), filename="الوحدة الثانية - شرح.pdf")
        except FileNotFoundError:
            update.message.reply_text("⚠️ عذرًا، لم يتم العثور على الملف المطلوب.")

    elif choice == "📂 الجزء الثاني":
        update.message.reply_text("الجزء الثاني قيد التحضير 🛠️")

    elif choice == "🎈 ترفيهي":
        update.message.reply_text("قسم الترفيه ✅")

    elif choice == "⬅️ رجوع":
        start(update, context)

    else:
        update.message.reply_text("الرجاء اختيار خيار من الأزرار.")

# ⚙️ تشغيل البوت
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_buttons))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()