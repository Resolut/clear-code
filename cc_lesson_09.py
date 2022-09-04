# Ясный код Урок 9

# 1
# Захардкоженное значение токена api бота вынес в глобальную область видимости модуля
# завел в отдельную константу, и создал отдельное поле
# Bot.token('123456789-98765432') -> API_TOKEN = '123456789-98765432'
# Bot.token = API_TOKEN

# 2
# Значение пути к директории хранения различных логов системы перенес в константу,
# поскольку этот путь не будет изменяться
# LOGS_DIR = '/path_to_logs'

# 3
# цвет фона программы - кортеж RGB значений - перенес в константу BG_COLOR
# BG_COLOR = (181, 184, 183)

# 4
# Основные свойства базы данных вынес в конфиг,
# обращение к которым в конечном модуле с подключением к db происходит через константы
# DB_ENGINE = config.system["db"["engine"]
# DB_HOST = config.system["db"]["host"]
# DB_NAME = config.system["db"]["_name"]

# 5
# Словарь параметров поиска событий в открытой сессии не меняется,
# поэтому завел для него отдельную константу
# SEARCH_PARAMETERS = { <...> различные ключи-параметры поиска данных в сессии}

# 6
# Захардкоженное чилсо - Лимит на кол-во скачанных файлов по FTP перенес в константу
# FILE_TRANSFER_COUNT_PER_DAY = 10

# 7
# разбивка событий по группам на 10 минутные интервалы, завел константу вместо просто числа 600
# INTERVAL_IN_SEC = 600
# grouping = func.to_timestamp(func.floor(extract / INTERVAL_IN_SEC) * INTERVAL_IN_SEC)

# 8 параметр значимости ('серъёзности') инцидента завел в конфиг,
# многократное обращение в коде теперь происходит через специально созданную константу
# SEVERITY = config.system["severity_levels"]

# 9
# завел константу - соль для шифрования
# SALT = "adcdefghi"

# 10
# параметры для проверки паролей завел в конфиг,
# а в коде, где используются эти параметры проверки пароля, завел константы:
# MIN_LENGTH = config.app["password_policy"]["min_length"]
# MAX_LENGTH = config.app["password_policy"]["max_length"]
# MIN_LOWERCASE = config.app["password_policy"]["min_lowercase"]
# MIN_UPPERCASE = config.app["password_policy"]["min_uppercase"]
# MIN_DIGITS = config.app["password_policy"]["min_digits"]
# MIN_SPECIAL = config.app["password_policy"]["min_special"]

# 11
# в проверке метода проверки пароля на символы из таблицы ASCII добавил читаемую константу
# LAST_ASCII_SYMBOL = 126
# if ord(c) > LAST_ASCII_SYMBOL:
#     <do something>

# 12
# часто встречающийся 24 часовой период вынес в отдельную константу
# вроде есть специальное слово в английском для суток 'nychthemeron', не решился его использовать :)
# DAY_PERIOD_IN_SEC = 24 * 3600
