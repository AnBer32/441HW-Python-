import game
from loader import dp
from aiogram.types import Message


@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    for duel in game.total:
        if message.from_user.id == duel[0]:
            await message.answer('Ты уже начал игру! Играй давай!')
            break
    else:
        # game.new_game = True
        await message.answer(f'Привет, {message.from_user.full_name}'
                             f'Мы будем играть в конфеты. Бери от 1 до 28...')
        my_game = [message.from_user.id, message.from_user.first_name, 150]
        game.total.append(my_game)
