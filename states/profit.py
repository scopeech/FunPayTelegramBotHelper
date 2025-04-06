from aiogram.fsm.state import StatesGroup, State

class ProfitCalculation(StatesGroup):
    waiting_for_initial_amount = State()
    waiting_for_amount_paid = State()
