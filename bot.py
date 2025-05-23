from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7641749973:AAHlZReWYPR3D55IEzZgyePZaJLC2VBbQ5g"  # Replace with your real token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("CANA WEBSITE", url="https://canabeings.github.io/cana/")],
        [InlineKeyboardButton("MINT OG NFTs", url="https://canabeings.github.io/OG-NFT-COLLECTION-/")],
        [
            InlineKeyboardButton("Telegram Channel", url="https://t.me/canabeing"),
            InlineKeyboardButton("Follow X", url="https://twitter.com/CANA_BEINGS")
        ],
        [InlineKeyboardButton("Join Discord", url="https://discord.gg/rGZtz8NF")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo="https://i.imgur.com/7v5S5hU.png",  # Direct link from imgur
        caption=(
            "Welcome to CANA — Culture And New Assets\n\n"
            "A new wave of ownership. Mint OG NFTs and join our community redefining Education and culture through Web3.\n\n"
            "**Instructions:**\n"
            "• Mint your OG NFT to gain access\n"
            "• Join the community on Telegram, X, and Discord\n"
            "• Follow project updates on the CANA website"
        ),
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
