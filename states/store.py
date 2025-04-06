from aiogram.fsm.state import StatesGroup, State

class StoreParser(StatesGroup):
    waiting_for_url = State()
    processing = State()