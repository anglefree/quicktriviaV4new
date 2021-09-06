
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
import os
import sys


HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\n• Iam A Bot Project made by @Sadlife\n# my group @quicktrivia\n• I Can Manage Group VC's\n\n• Hit /help to know about available commands.</b>"
HELP = """
🎧 <b>I Can Play Musics On VoiceChats 🤪</b>

🎶 **Common Commands**:by @Sadlife56 or aditya
• `/song` __Download Song from youtube__
• `/play`  __Play song you requested__
• `/help` __Show help for commands__
• `/dplay` __Play song you requested via deezer__
• `splay` __Play song you requested via jio saavn__
• `/ytplay` __Play song directly from youtube server__
• `/search` __Search video songs links__
• `/current` __Show now playing__
• `/playlist` __Show now playing list__
• `/video` __Downloads video song quickly__
🎶 **Admin Commands**:*aditya, tushar, lucky, harsh, utkarsh, sg*
• `/player`  __Open music player settings panel__
• `/pause` __Pause song play__
• `/skip` __Skip next song__
• `/resume`  __Resume song play__
• `/userbotjoin`  __Invites assistant to your chat__
• `/end` __Stops music play__
• `/admincache` __Refresh list of admins with vc power__
© Powered By 
[ __@quicltrivia || @Sadlife56__ ]
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
       [
                InlineKeyboardButton('📢 Updates', url='https://t.me/v4updates'),
                InlineKeyboardButton('💬 Support', url='https://t.me/v4updatesdiscussion')
                ],[
                InlineKeyboardButton('🤖 Developer', url='https://t.me/aboutmeaditya'),
                InlineKeyboardButton('🎧 Chats', url='https://t.me/quicktrivia')
                ],[
                InlineKeyboardButton('📜 Source Code 📜', url='https://telegra.ph/file/776826cc26ba5897a9ec2.mp4'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/cd1c80751b6c75a655b1d.jpg", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
                InlineKeyboardButton('📢 Updates', url='https://t.me/v4updates'),
                InlineKeyboardButton('💬 Support', url='https://t.me/v4updatesdiscussion')
                ],[
                InlineKeyboardButton('🤖 Developer', url='https://t.me/aboutmeaditya'),
                InlineKeyboardButton('🎧 Chats', url='https://t.me/quicktrivia')
                ],[
                InlineKeyboardButton('📜 Source Code 📜', url='https://telegra.ph/file/776826cc26ba5897a9ec2.mp4'),
       ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/cd1c80751b6c75a655b1d.jpg", caption=HELP, reply_markup=reply_markup)
    await message.delete()
