import os
import re
import asyncio
import logging

from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from states.store import StoreParser
from utils.store_utils import (
    validate_app_url,
    fetch_prices_google,
    fetch_prices_apple,
    check_rate_limit
)

router = Router()

logger = logging.getLogger(__name__)

@router.message(F.text == "🔍 Анализ цен приложений")
async def start_parser(message: types.Message, state: FSMContext):
    await state.set_state(StoreParser.waiting_for_url)
    await message.answer(
        "Отправьте ссылку на приложение из:\n"
        "• Google Play (https://play.google.com/store/apps/details?id=xxx)\n"
        "• App Store (https://apps.apple.com/xx/app/yyy/idNNNN)"
    )

@router.message(StoreParser.waiting_for_url)
async def process_url(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if not await check_rate_limit(user_id):
        await message.answer(
            "⏳ Вы превысили лимит запросов. Попробуйте снова через минуту."
        )
        await state.clear()
        return

    url = message.text.strip()
    store_type, app_id = await validate_app_url(url)

    if not app_id:
        await message.answer(
            "❌ Неверная ссылка. Пожалуйста, отправьте ссылку на приложение из Google Play или App Store."
        )
        await state.clear()
        return

    try:
        if store_type == "google":
            filepath = await fetch_prices_google(app_id, message, state)
        elif store_type == "apple":
            filepath = await fetch_prices_apple(app_id, message, state)

        else:
            await message.answer(
                "❌ Не удалось определить магазин. Пожалуйста, проверьте ссылку."
            )
            await state.clear()
            return

        if filepath and os.path.exists(filepath):
            await message.answer_document(
                document=FSInputFile(filepath),
                caption="📄 Ваш отчет готов!"
            )
        else:
            await message.answer(
                "❌ Произошла ошибка при обработке. Попробуйте снова позже."
            )
    except Exception as e:
        logger.exception("Error processing URL")
        await message.answer(f"❌ Произошла ошибка: {e}")
    finally:
        await state.clear()