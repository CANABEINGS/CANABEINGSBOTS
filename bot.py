from telegram import Update, InlineKeyboardButton, InlineKeyboardMarku>
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7641749973:AAHlZReWYPR3D55IEzZgyePZaJLC2VBbQ5g"

WELCOME_TEXT = """Welcome to CANA — Culture And New Assets

A new wave of ownership. Mint OG NFTs and join our community redefinin>

Instructions:

Mint your OG NFT to gain access

Join the community on Telegram, X, and Discord

Follow project updates on the CANA website"""

IMAGE_URL = "https://i.imgur.com/jNGP9gh.png"

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("CANA WEBSITE", url="https://canabeings.>
        [InlineKeyboardButton("MINT OG NFTs", url="https://canabeings.>
        [InlineKeyboardButton("Telegram Channel", url="https://t.me/ca>
         InlineKeyboardButton("Follow X", url="https://twitter.com/CAN>
        [InlineKeyboardButton("Join Discord", url="https://discord.gg/rGZtz8NF/>
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=IMA>

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
