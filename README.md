# FunPay Telegram Bot

Этот Telegram-бот предназначен для помощи продавцам FunPay в расчете чистой прибыли и анализе цен приложений в Google Play и App Store.

## Особенности

-   **Расчет чистой прибыли:** Позволяет рассчитать чистую прибыль с заказа, учитывая комиссию.
-   **Анализ цен приложений:** Собирает и анализирует цены приложений из Google Play и App Store в разных странах.

## Начало работы

### Предварительные требования

-   Python 3.7+
-   Библиотека aiogram
-   Библиотека aiohttp

### Установка

1.  Клонируйте репозиторий:

    ```bash
    git clone https://github.com/scopeech/FunPayTelegramBotHelper
    ```

2.  Перейдите в каталог проекта:

    ```bash
    cd FunPayTelegramBotHelper
    ```

3.  Создайте и активируйте виртуальное окружение (рекомендуется):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```

4.  Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

### Настройка

1.  Создайте файл `config.py` в корневом каталоге проекта (если его еще нет).
2.  Добавьте токен вашего Telegram-бота и путь к каталогу отчетов:

    ```python
    # filepath: config.py
    import os
    BOT_TOKEN = "YOUR TELEGRAM BOT TOKEN"
    CONST_PATH = os.path.join(os.path.dirname(__file__), "data", "reports")
    ```

    Замените `"YOUR TELEGRAM BOT TOKEN"` на токен вашего бота, полученный от BotFather в Telegram.

### Использование

1.  Запустите бота:

    ```bash
    python bot.py
    ```

2.  Отправьте команду `/start` боту в Telegram, чтобы начать.
3.  Используйте клавиатуру для выбора действия:
    -   `💰 Рассчитать чистую прибыль`: Рассчитайте чистую прибыль, введя исходную сумму и сумму, которую вы заплатили.
    -   `🔍 Анализ цен приложений`: Отправьте ссылку на приложение из Google Play или App Store, чтобы проанализировать цены.

## Структура файлов

```
├── bot.py              # Основной файл бота
├── config.py           # Файл конфигурации
├── handlers/           # Каталог обработчиков
│   ├── __init__.py
│   ├── profit.py       # Обработчик для расчета прибыли
│   └── store_parser.py # Обработчик для парсинга цен
├── keyboards/          # Каталог клавиатур
│   ├── __init__.py
│   └── reply.py        # Файл с reply-клавиатурами
├── states/             # Каталог состояний FSM
│   ├── __init__.py
│   ├── profit.py       # Состояния для расчета прибыли
│   └── store.py        # Состояния для парсинга цен
├── utils/              # Каталог утилит
│   ├── __init__.py
│   ├── calculations.py # Утилиты для расчетов
│   └── store_utils.py  # Утилиты для работы с магазинами приложений
├── data/               # Каталог для хранения данных
│   └── reports/        # Каталог для отчетов
├── .gitignore          # Файл игнорирования Git
├── README.md           # Этот файл
└── requirements.txt    # Файл зависимостей
```

## Зависимости

-   aiogram
-   aiohttp
-   nest-asyncio
-   python-telegram-bot

Все зависимости перечислены в файле `requirements.txt`.

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT. См. файл `LICENSE` для получения дополнительной информации.
