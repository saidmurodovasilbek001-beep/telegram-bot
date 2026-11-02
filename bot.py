from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "BOT_TOKENINGNI_SHU_YERGA_QOY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salom! Men sizning botingizman. 😊\n"
        "Menga savol yoki misol yuboring."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Buyruqlar:\n/start - Boshlash\n/help - Yordam\n"
        "Hisoblash uchun misol yuboring."
    )

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    try:
        result = eval(text, {"__builtins__": {}}, {})
        await update.message.reply_text(f"Javob: {result}")
    except:
        await update.message.reply_text("Xabaringizni oldim! 😊")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
