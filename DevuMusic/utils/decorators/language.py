# Creator Or Dev @HYPER_AD13 | @SHINING_OFF <Found On telegram>
# Found on github < https://github.com/ItsmeHyper13 >.


from strings import get_string
from DevuMusic.misc import SUDOERS
from DevuMusic.utils.database import (get_lang, is_commanddelete_on,
                                       is_maintenance)


def language(mystic):
    async def wrapper(_, message, **kwargs):
        if await is_maintenance() is False and message.from_user.id not in SUDOERS:
            return await message.reply_text(
                "Bot is under maintenance. Please wait for some time..."
            )
        if await is_commanddelete_on(message.chat.id):
            try:
                await message.delete()
            except:
                pass
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, message, language)

    return wrapper


def languageCB(mystic):
    async def wrapper(_, CallbackQuery, **kwargs):
        if (
            await is_maintenance() is False
            and CallbackQuery.from_user.id not in SUDOERS
        ):
            return await CallbackQuery.answer(
                "Bot is under maintenance. Please wait for some time...",
                show_alert=True,
            )
        try:
            language = await get_lang(CallbackQuery.message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, CallbackQuery, language)

    return wrapper


def LanguageStart(mystic):
    async def wrapper(_, message, **kwargs):
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, message, language)

    return wrapper
