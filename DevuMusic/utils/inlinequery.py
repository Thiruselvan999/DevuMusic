# Creator Or Dev @HYPER_AD13 | @SHINING_OFF <Found On telegram>
# Found on github < https://github.com/ItsmeHyper13 >

from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = [
    InlineQueryResultArticle(
        title="Pᴀᴜsᴇ Sᴛʀᴇᴀᴍ",
        description=f"ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ.",
        thumb_url="https://telegra.ph/file/37d4ea97e97877eb63f93.jpg",
        input_message_content=InputTextMessageContent("/pause"),
    ),
    InlineQueryResultArticle(
        title="Rᴇsᴜᴍᴇ Sᴛʀᴇᴀᴍ",
        description=f"ʀᴇsᴜᴍᴇ ᴄᴜʀʀᴇɴᴛ ᴘᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ.",
        thumb_url="https://telegra.ph/file/4e65d111fdb89809fe94e.jpg",
        input_message_content=InputTextMessageContent("/resume"),
    ),
    InlineQueryResultArticle(
        title="Sᴋɪᴘ Sᴛʀᴇᴀᴍ",
        description=f"sᴋɪᴘ ᴛᴏ ɴᴇxᴛ ᴛʀᴀᴄᴋ. | ꜰᴏʀ sᴘᴇᴄɪꜰɪᴄ ᴛʀᴀᴄᴋ ɴᴜᴍʙᴇʀ: /skip [ɴᴜᴍʙᴇʀ] ",
        thumb_url="https://telegra.ph/file/78189a482f76fdc3f8185.jpg",
        input_message_content=InputTextMessageContent("/skip"),
    ),
    InlineQueryResultArticle(
        title="Eɴᴅ Sᴛʀᴇᴀᴍ",
        description="sᴛᴏᴘ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ.",
        thumb_url="https://telegra.ph/file/eb33b1f0daaecb911d013.jpg",
        input_message_content=InputTextMessageContent("/end"),
    ),
    InlineQueryResultArticle(
        title="Sʜᴜғғʟᴇ Sᴛʀᴇᴀᴍ",
        description="sʜᴜꜰꜰʟᴇ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ʟɪsᴛ.",
        thumb_url="https://telegra.ph/file/a72528b064792e703bef3.jpg",
        input_message_content=InputTextMessageContent("/shuffle"),
    ),
    InlineQueryResultArticle(
        title="Lᴏᴏᴘ Sᴛʀᴇᴀᴍ",
        description="ʟᴏᴏᴘ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ. | ᴜsᴀɢᴇ: /loop [enable|disable]",
        thumb_url="https://telegra.ph/file/895786885daeb9f9978b6.png",
        input_message_content=InputTextMessageContent("/loop 3"),
    ),
    InlineQueryResultArticle(
        title="Sᴇᴇᴋ sᴛʀʀᴀᴍ",
        description="sᴇᴇᴋ ᴛʜᴇ ɢᴏɪɴɢ sᴛʀᴇᴀᴍ ʙʏ ᴀ sᴘᴇғɪᴄ ᴛɪᴍᴇ",
        thumb_url="https://telegra.ph/file/1f2aaf412fd0e6dac1139.png",
        input_message_content=InputTextMessageContent("/seek 10"),
    ),
]
