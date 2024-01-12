from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

token = '6178558816:AAHsxxMVe8I8-3QlbaqoIovqazmVDsQiXi4'
bot_username = '@soccer_gle_bot'


# Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello there thanks for chatting. Lets see what I can do")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Help command")


async def custom(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Custom command")


# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'hello' in processed:
        return "Hey there"
    if 'how are you' in processed:
        return "Good and you?"
    if 'howdy' in processed:
        return "Howdy duty"
    return "Idk"

async def handle_message(update:Update, context:ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # For handling groups you have to write @soccer-gle-bot to send DM
    if message_type == 'group':
        if bot_username in text:
            new_text:str = text.replace(bot_username, '').strip()
            response:str = handle_response(new_text)
        else:
            return
    else:
        response:str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(token).build()

    # Commands
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('custom', custom))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)