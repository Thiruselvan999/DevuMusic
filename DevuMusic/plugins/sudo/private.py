# Creator Or Dev @HYPER_AD13 | @SHINING_OFF <Found On telegram>
# Found on github < https://github.com/ItsmeHyper13 >.

from pyrogram import filters
from pyrogram.types import Message

import config
from strings import get_command
from DevuMusic import app
from DevuMusic.misc import SUDOERS
from DevuMusic.utils.database import (add_private_chat,
                                       get_private_served_chats,
                                       is_served_private_chat,
                                       remove_private_chat)
from DevuMusic.utils.decorators.language import language

AUTHORIZE_COMMAND = get_command("AUTHORIZE_COMMAND")
UNAUTHORIZE_COMMAND = get_command("UNAUTHORIZE_COMMAND")
AUTHORIZED_COMMAND = get_command("AUTHORIZED_COMMAND")


@app.on_message(filters.command(AUTHORIZE_COMMAND) & SUDOERS)
@language
async def authorize(client, message: Message, _):
    if config.PRIVATE_BOT_MODE != str(True):
        return await message.reply_text(_["pbot_12"])
    if len(message.command) != 2:
        return await message.reply_text(_["pbot_1"])
    try:
        chat_id = int(message.text.strip().split()[1])
    except:
        return await message.reply_text(_["pbot_7"])
    if not await is_served_private_chat(chat_id):
        await add_private_chat(chat_id)
        await message.reply_text(_["pbot_3"])
    else:
        await message.reply_text(_["pbot_5"])


@app.on_message(filters.command(UNAUTHORIZE_COMMAND) & SUDOERS)
@language
async def unauthorize(client, message: Message, _):
    if config.PRIVATE_BOT_MODE != str(True):
        return await message.reply_text(_["pbot_12"])
    if len(message.command) != 2:
        return await message.reply_text(_["pbot_2"])
    try:
        chat_id = int(message.text.strip().split()[1])
    except:
        return await message.reply_text(_["pbot_7"])
    if not await is_served_private_chat(chat_id):
        return await message.reply_text(_["pbot_6"])
    await remove_private_chat(chat_id)
    return await message.reply_text(_["pbot_4"])


@app.on_message(filters.command(AUTHORIZED_COMMAND) & SUDOERS)
@language
async def authorized(client, message: Message, _):
    if config.PRIVATE_BOT_MODE != str(True):
        return await message.reply_text(_["pbot_12"])
    m = await message.reply_text(_["pbot_8"])
    text = _["pbot_9"]
    chats = await get_private_served_chats()
    served_chats = [int(chat["chat_id"]) for chat in chats]
    count = 0
    co = 0
    msg = _["pbot_13"]
    for served_chat in served_chats:
        try:
            title = (await app.get_chat(served_chat)).title
            count += 1
            text += f"{count}:- {title[:15]} [{served_chat}]\n"
        except Exception:
            title = _["pbot_10"]
            co += 1
            msg += f"{co}:- {title} [{served_chat}]\n"
    if co == 0:
        return await m.edit(_["pbot_11"]) if count == 0 else await m.edit(text)
    if count == 0:
        await m.edit(msg)
    else:
        text = f"{text} {msg}"
        return await m.edit(text)