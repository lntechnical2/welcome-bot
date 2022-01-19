from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os

Token =os.environ.get("BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

keyboard = [
                [InlineKeyboardButton("Join iur group", url='https://t.me/meninbluefans')],
                [InlineKeyboardButton("Join our channel", url='https://t.me/INDCRICINFO')]
            ]
buttons = InlineKeyboardMarkup(keyboard)

def start(updater,context):
 updater.message.reply_text('''Hi iam welcome messanger bot 
Add me to your group 
 
 Made with Love ❤️ by @lntechnical

  ''')
def help(updater,context):
 updater.message.reply_text("Add me to your group ")
 

def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(f'Hello {member.full_name} , Welcome to ln support Thank you for Joining  ')

add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
updater.dispatcher.add_handler(add_group_handle)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(CommandHandler('help',help))

updater.start_polling()
updater.idle()
