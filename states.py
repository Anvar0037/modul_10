from aiogram.fsm.state import StatesGroup, State

class ProductStatesGroup(StatesGroup):
    title = State()
    price = State()
    photo = State()