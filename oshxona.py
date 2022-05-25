# """
#  This is a echo bot.
#  It echoes any incoming text messages.
#  """

import logging
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardMarkup, \
    KeyboardButton

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from aiogram.types import ContentTypes

from aiogram.dispatcher.filters.builtin import Command, CommandStart, CommandHelp, CommandPrivacy

API_TOKEN = '5393119606:AAEvq47054L-IssiiUti8wNU7uSuPqLyr5c'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

menu_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ovqatlar', callback_data='Ovqatlar'),
            InlineKeyboardButton(text='Napitki', callback_data='Napitki')
        ],
        [
            InlineKeyboardButton(text='Kanstovar', callback_data='Kanstovar'),
            InlineKeyboardButton(text='Xoztovar', callback_data='Xoztovar')
        ]
    ],
)



ovqat_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Somsa', callback_data="Somsa"),
            InlineKeyboardButton(text='Manti', callback_data='Manti')
        ],
        [
            InlineKeyboardButton(text='Osh', callback_data="Osh"),
            InlineKeyboardButton(text='Norin', callback_data="Norin")
        ],
        [
            InlineKeyboardButton(text='Shashlik', callback_data="Shashlik"),
            InlineKeyboardButton(text='Orqaga', callback_data='Orqaga')
        ]
    ]
)



xoztovar_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Fen', callback_data="Fen"),
            InlineKeyboardButton(text='Termometr', callback_data='Termometr'),
            InlineKeyboardButton(text='Mix', callback_data='Mix')

        ],
        [
            InlineKeyboardButton(text='Qulf', callback_data='Qulf'),
            InlineKeyboardButton(text='Chelak', callback_data='Chelak'),
            InlineKeyboardButton(text='Sement', callback_data='Sement')
        ],
        [
            InlineKeyboardButton(text='Ohak', callback_data='Ohak'),
            InlineKeyboardButton(text='Shlakoblok', callback_data='Shlakoblok'),
            InlineKeyboardButton(text='Drel', callback_data='Drel'),
        ],
        [
            InlineKeyboardButton(text='Bolgarka', callback_data='Bolgarka'),
            InlineKeyboardButton(text='Orqaga', callback_data='Orqaga')
        ]
    ]
)

kanstovar_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ruchka', callback_data='Ruchka'),
            InlineKeyboardButton(text='Qalam', callback_data='Qalam'),
            InlineKeyboardButton(text='Daftar', callback_data='Daftar'),
        ],
        [
            InlineKeyboardButton(text='Bloknot', callback_data='Bloknot'),
            InlineKeyboardButton(text='O`chirg`ich', callback_data='O`chirg`ich'),
            InlineKeyboardButton(text='Flomaster', callback_data='Flomaster')
        ],
        [
            InlineKeyboardButton(text='Kley', callback_data='Kley'),
            InlineKeyboardButton(text='Sirkul', callback_data='Sirkul'),
            InlineKeyboardButton(text='Chizg`ich', callback_data='Chizg`ich'),
        ],
        [
            InlineKeyboardButton(text='Lupa', callback_data='Lupa'),
            InlineKeyboardButton(text='Orqaga', callback_data='Orqaga')
        ]
    ],
)



napitki_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Hydrolife', callback_data='Hydrolife'),
            InlineKeyboardButton(text='Asu', callback_data='Asu')
        ],
        [
            InlineKeyboardButton(text='Coca-cola', callback_data='Coca-cola'),
            InlineKeyboardButton(text='Pepsi', callback_data='Pepsi')
        ],
        [
            InlineKeyboardButton(text='Ice-tea', callback_data='Ice-tea'),
            InlineKeyboardButton(text='Fuse-tea', callback_data='Fuse-tea')
        ],
        [
            InlineKeyboardButton(text='Fanta', callback_data='Fanta'),
            InlineKeyboardButton(text='Fensi', callback_data='Fensi')
        ],
        [
            InlineKeyboardButton(text='Montella', callback_data='Montella'),
            InlineKeyboardButton(text='Nestle', callback_data='Nestle')
        ],
        [
            InlineKeyboardButton(text='Orqaga', callback_data='Orqaga')
        ]
    ]
)


# @dp.message_handler(content_types=ContentTypes.TEXT)
# async def start_handler(message: types.Message):
#     await message.answer('Siz matn jonatdingiz')
#
#
# @dp.message_handler(content_types=ContentTypes.STICKER)
# async def start_handler(message: types.Message):
#     await message.answer('Siz stiker jonatdingiz')
#
# @dp.message_handler(content_types=ContentTypes.VOICE)
# async def start_handler(message: types.Message):
#     await message.answer('Siz audioxabar jonatdingiz')
#
#
# @dp.message_handler(content_types=ContentTypes.AUDIO)
# async def start_handler(message: types.Message):
#     await message.answer('Siz musiqa jonatdingiz')
#
#
# @dp.message_handler(content_types=ContentTypes.VIDEO_NOTE)
# async def start_handler(message: types.Message):
#     await message.answer('Siz videoxabar jonatdingiz')
#
#
# @dp.message_handler(content_types=ContentTypes.ANIMATION)
# async def start_handler(message: types.Message):
#     await message.answer('Siz gif jonatdingiz')
#
#
# @dp.message_handler(content_types=ContentTypes.DOCUMENT)
# async def start_handler(message: types.Message):
#     await message.answer('Siz dokument jonatdingiz')
#
#
#
# @dp.message_handler(content_types=ContentTypes.LOCATION)
# async def start_handler(message: types.Message):
#     await message.answer('Siz lokatsiya jonatdingiz')



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    # """
    # This handler will be called when user sends `/start` or `/help` command
    # """

    await message.answer(f"Salom {message.from_user.full_name}")
    await message.answer('Tanlang:', reply_markup=menu_inline)

@dp.callback_query_handler(text='Orqaga')
async def send_orqaga(message: types.Message):
    await message.answer('Tanlang', reply_markup=menu_inline)


@dp.callback_query_handler(text='Ovqatlar')
async def send_ovqat(message: types.Message):
    await message.answer("Menyu:", reply_markup=ovqat_inline)



@dp.callback_query_handler(text=['Somsa'])
async def send_somsa(message: CallbackQuery):
    await message.answer('Go`shtli somsaning narxi 5 750 so`m.\nKartoshkali somsaning narxi 3 750 so`m.')


@dp.callback_query_handler(text=['Shashlik'])
async def send_shashlik(message: types.CallbackQuery):
    await message.answer('Qiymaning narxi 10 000 so`m.\nJazzning narxi 8 500 so`m.')


@dp.callback_query_handler(text=['Osh'])
async def send_osh(message: CallbackQuery):
    await message.answer('Oshning narxi 25 000 so`m.')


@dp.callback_query_handler(text=['Manti'])
async def send_manti(message: CallbackQuery):
    await message.answer('Mantinig narxi(1 dona) 3 000 so`m.')


@dp.callback_query_handler(text=['Norin'])
async def send_norin(message: CallbackQuery):
    await message.answer('Norinning narxi(1kg) 60 000 so`m.')


@dp.callback_query_handler(text=['Xoztovar'])
async def send_tovar(message: CallbackQuery):
    await message.answer('Tovarning nomini kiriting va narxini biling.\nTovarlar:', reply_markup=xoztovar_inline)


@dp.callback_query_handler(text='Fen')
async def send_mix(message: CallbackQuery):
    await message.answer('Fenning narxi 157 450 so`m.')


@dp.callback_query_handler(text='Termometr')
async def send_termometr(message: CallbackQuery):
    await message.answer('Plastmassa termometrning narxi 3 950 so`m.')


@dp.callback_query_handler(text='Mix')
async def send_mix(message: CallbackQuery):
    await message.answer('Mixning narxi(1 dona) 500 so`m.')


@dp.callback_query_handler(text='Qulf')
async def send_qulf(message:CallbackQuery):
    await message.answer(
        'Velosiped uchun qulfning narxi(kichkina) 14 000 so`m,\nVelosiped uchun qulfning narxi(o`rtacha) 18 450 so`m,\nVelosiped uchun qulfning narxi(katta) 19 450 so`m.')


@dp.callback_query_handler(text='Chelak')
async def send_chelak(message: CallbackQuery):
    await message.answer('Chelakning narxi 19 950 so`m.')


#
@dp.callback_query_handler(text='Sement')
async def send_sement(message: CallbackQuery):
    await message.answer('Sementning narxi(1kg) 750 so`m.')


@dp.callback_query_handler(text='Ohak')
async def send_ohak(message: CallbackQuery):
    await message.answer('Ohakning narxi(1kg) 800 so`m.')


@dp.callback_query_handler(text='Shlakoblok')
async def send_shlakoblok(message: CallbackQuery):
    await message.answer('Shlakoblokning narxi(1dona) 1 750 so`m.')


@dp.callback_query_handler(text='Drel')
async def send_drel(message: CallbackQuery):
    await message.answer('Drelning narxi 300 000 so`m.')


@dp.callback_query_handler(text='Bolgarka')
async def send_bolgarka(message: CallbackQuery):
    await message.answer('Bolgarkaning narxi 350 000 so`m.')


@dp.callback_query_handler(text='Kanstovar')
async def send_kanstovar(message: CallbackQuery):
    await message.answer('Kanstovarning nomini kiriting:', reply_markup=kanstovar_inline)


@dp.callback_query_handler(text='Ruchka')
async def send_ruchka(message: CallbackQuery):
    await message.answer('Ko`k ruchkaning narxi 2 000 so`m,\nYashil ruchkaning narxi 2 500 so`m.')


@dp.callback_query_handler(text='Qalam')
async def send_qalam(message: CallbackQuery):
    await message.answer('Qalamning narxi 1 500 so`m.')


@dp.callback_query_handler(text='Daftar')
async def send_daftar(message: CallbackQuery):
    await message.answer('Daftarning narxi 2 200 so`m.')


@dp.callback_query_handler(text='Bloknot')
async def send_bloknot(message: CallbackQuery):
    await message.answer('Bloknotning narxi(kichkina) 7 000 so`m,\nBloknotning narxi(katta) 10 000 so`m.')


@dp.callback_query_handler(text='O`chirg`ich')
async def send_ochirgich(message: CallbackQuery):
    await message.answer('O`chirg`ichning narxi 4 000 so`m.')


@dp.callback_query_handler(text='Flomaster')
async def send_flomaster(message: CallbackQuery):
    await message.answer('Flomasterlarning narxi 22 000 so`m.')


@dp.callback_query_handler(text='Kley')
async def send_kley(message: CallbackQuery):
    await message.answer('Kleyning narxi 6 000 so`m.')


@dp.callback_query_handler(text='Sirkul')
async def send_sirkul(message: CallbackQuery):
    await message.answer('Sirkulning narxi 14 000 so`m.')


@dp.callback_query_handler(text='Chizg`ich')
async def send_chizgich(message: CallbackQuery):
    await message.answer('Chizg`ichning narxi(20sm) 6 000 so`m.')


@dp.callback_query_handler(text='Lupa')
async def send_lupa(message: CallbackQuery):
    await message.answer('Lupaning narxi 10 000 so`m.')





@dp.callback_query_handler(text='Napitki')
async def send_napitki(message: CallbackQuery):
    await message.answer('Ichmoqchi bo`lgan suvingizni tanlang: ', reply_markup=napitki_inline)

@dp.callback_query_handler(text='Hydrolife')
async def send_hydrolife(message: CallbackQuery):
    await message.answer('Hydrolife:\nGazlanmagan suvning(0.5 l) narxi 1 700 so`m\nGazlanmagan suvning(1 l) narxi 2 500 so`m\nGazlangan suvning(0.5 l) narxi 1 200 so`m\nGazlangan suvning(1 l) narxi 2 200 so`m' )

@dp.callback_query_handler(text='Coca-cola')
async def send_cola(message: CallbackQuery):
    await message.answer('Coca-colaning(0.5 l) narxi 5 000 so`m\nCoca-colaning(1 l) narxi 8 000 so`m\nCoca-colaning(1.5 l) narxi 11 000 so`m')

@dp.callback_query_handler(text='Fanta')
async def send_fanta(message: CallbackQuery):
    await message.answer('Fantaning(0.5 l) narxi 5 000 so`m\nFantaning(1 l) narxi 8 000 so`m\nFantaning(1.5 l) narxi 11 000 so`m')

@dp.callback_query_handler(text='Pepsi')
async def send_pepsi(message: CallbackQuery):
    await message.answer('Pepsining(0.5 l) narxi 5 000 so`m\nPepsining(1 l) narxi 8 000 so`m\nPepsining(1.5 l) narxi 11 000 so`m')

@dp.callback_query_handler(text='Ice-tea')
async def send_icetea(message: CallbackQuery):
    await message.answer('Ice-teaning(0.5 l) narxi 4 000 so`m\nIce-teaning(1.25 l) narxi 6 800 so`m')

@dp.callback_query_handler(text='Fuse-tea')
async def send_fusetea(message: CallbackQuery):
    await message.answer('Fuse-teaning(0.5 l) narxi 5 000 so`m\nFuse-teaning(1.25 l) narxi 8 000 so`m')

@dp.callback_query_handler(text='Asu')
async def send_asu(message: CallbackQuery):
    await message.answer('Asuning(0.5l) narxi 3 500 so`m\nAsuning(1 l) narxi 6 000 so`m')

@dp.callback_query_handler(text='Montella')
async def send_montella(message: CallbackQuery):
    await message.answer('Montella:\nGazlanmagan suvning(0.5 l) narxi 1 700 so`m\nGazlanmagan suvning(1 l) narxi 2 500 so`m\nGazlangan suvning(0.5 l) narxi 1 200 so`m\nGazlangan suvning(1 l) narxi 2 200 so`m')

@dp.callback_query_handler(text='Nestle')
async def send_nestle(message: CallbackQuery):
    await message.answer('Nestle:\nGazlanmagan suvning(0.5 l) narxi 1 700 so`m\nGazlanmagan suvning(1 l) narxi 2 500 so`m\nGazlangan suvning(0.5 l) narxi 1 200 so`m\nGazlangan suvning(1 l) narxi 2 200 so`m')

@dp.callback_query_handler(text='Fensi')
async def send_fensi(message: CallbackQuery):
    await message.answer('Fensining(0.5 l) narxi 2 000 so`m\nFensining(1.5 l) narxi 4 700 so`m')


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer('Xato')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
















