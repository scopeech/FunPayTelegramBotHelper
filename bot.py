import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN
from handlers import profit, store_parser

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

async def main():
    # Инициализация бота и диспетчера
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # Регистрация всех роутеров
    dp.include_router(profit.router)
    dp.include_router(store_parser.router)  # Добавляем новый роутер для парсера

    try:
        # Удаляем все обновления, которые произошли после последнего выключения бота
        await bot.delete_webhook(drop_pending_updates=True)
        logger.info("Бот успешно запущен")
        
        # Запускаем бота
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Произошла ошибка при запуске бота: {e}")
    finally:
        logger.info("Бот остановлен")
        
if __name__ == "__main__":
    try:
        # Запускаем бота в асинхронном режиме
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Бот остановлен пользователем")