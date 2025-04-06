from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states.profit import ProfitCalculation
from keyboards.reply import get_main_keyboard
from utils.calculations import calculate_amount_after_fee

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Привет! Я умный помощник продавцов FunPay. я могу расчитать чистую прибыль с заказа, а так же умею парсить цены в Google Play.\nВыберите действие:",
        reply_markup=get_main_keyboard()
    )

@router.message(F.text == "💰 Рассчитать чистую прибыль")
async def start_calculation(message: types.Message, state: FSMContext):
    await state.set_state(ProfitCalculation.waiting_for_initial_amount)
    await message.answer("Введите исходную сумму ($):")

@router.message(ProfitCalculation.waiting_for_initial_amount)
async def process_initial_amount(message: types.Message, state: FSMContext):
    try:
        initial_amount = float(message.text)
        await state.update_data(initial_amount=initial_amount)
        await state.set_state(ProfitCalculation.waiting_for_amount_paid)
        await message.answer("Введите сумму, которую вы заплатили ($):")
    except ValueError:
        await message.answer("Ошибка! Введите число.")

@router.message(ProfitCalculation.waiting_for_amount_paid)
async def process_amount_paid(message: types.Message, state: FSMContext):
    try:
        amount_paid = float(message.text)
        data = await state.get_data()
        initial_amount = data['initial_amount']

        withdrawal_fee_percentage = 6
        withdrawal_fee_fixed = 0

        amount_after_fee = calculate_amount_after_fee(
            initial_amount, withdrawal_fee_percentage, withdrawal_fee_fixed)
        net_profit = amount_paid - amount_after_fee

        response = (
            f"📊 Результаты расчета:\n"
            f"• Исходная сумма: ${initial_amount:.2f}\n"
            f"• Сумма после комиссии: ${amount_after_fee:.2f}\n"
            f"• Вы заплатили: ${amount_paid:.2f}\n"
            f"• Чистая прибыль: ${net_profit:.2f}"
        )

        await message.answer(response)
        await state.clear()
    except ValueError:
        await message.answer("Ошибка! Введите число.")
