from aiogram import Router, F, html
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from keyboards.food_keyboard import food_keyboard
from keyboards.sizes_keyboard import sizes_keyboard

from middlewares.GetAllTitlesAndSizesMiddleWare import GetAllTitlesAndSizesMiddleware

from states.food_states import OrderFood


router = Router()
router.message.filter()
router.message.middleware(GetAllTitlesAndSizesMiddleware())


@router.message(StateFilter(OrderFood), Command('cancel'))
@router.message(F.text.lower().startswith('cancel'))
async def cancel_ordering(message: Message, state: FSMContext):
    await message.reply('Canceled!', reply_markup=ReplyKeyboardRemove())
    await state.clear()


@router.message(Command("food"), StateFilter(None))
async def send_food_titles(message: Message, all_titles: set[str], state: FSMContext):
    await message.answer(
        "Choose food, please", reply_markup=food_keyboard(all_titles=all_titles)
    )
    await state.set_state(OrderFood.choosing_food_title)


@router.message(OrderFood.choosing_food_title)
async def send_food_sizes(
    message: Message, 
    all_titles: set[str], 
    state: FSMContext, 
    all_sizes: set[str]
):
    if message.text not in all_titles:
        await message.answer(
            "Please click the button, don't write it yourself!",
            reply_markup=food_keyboard(all_titles=all_titles),
        )
        return

    await state.update_data(chosen_food=message.text)
    await message.answer(
        "And now please choose the size of your meal ^_^",
        reply_markup=sizes_keyboard(all_sizes),
    )

    await state.set_state(OrderFood.choosing_food_size)


@router.message(OrderFood.choosing_food_size)
async def send_food_sizes(
    message: Message, 
    all_sizes: set[str],
    state: FSMContext
):
    if message.text not in all_sizes:
        await message.answer(
            "Please click the button, don't write it yourself!",
            reply_markup=sizes_keyboard(all_sizes=all_sizes),
        )
        return

    chosen_food = await state.get_data()


    await message.answer(
        f'Your have choosen {chosen_food['chosen_food']} size: {message.text.lower()}.\n\n'
        f'{html.bold("Order was created. Please, wait!")}',
        reply_markup=ReplyKeyboardRemove(),
        parse_mode='HTML'
    )

    await state.clear()