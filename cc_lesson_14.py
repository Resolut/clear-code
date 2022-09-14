# Ясный код. Урок 14

# 1
# Мажорная и Минорная версии интерпретатора Python берётся срезом списка. sys.version[3]
# И хотя этот срез работает, но например для версии Python 3.10 уже случится ошибка.
# Лучше использовать готовые значения из переменной этого же модуля sys

# было
# site_packages = os.path.join(
#     base,
#     "lib",
#     "python{}".format(sys.version[:3]), "site-packages")
#
# стало
# site_packages = os.path.join(
#     base,
#     "lib",
#     "python{}.{}".format(sys.version_info.major, sys.version_info.minor),
#     "site-packages")


# 2
# Список временных периодов не должен быть случайно изменен.

# rows = ["Today", "Week", "Month", "Quarter", "Year", "Total"]

# лучше вместо него использовать кортеж (tuple)

# rows = ("Today", "Week", "Month", "Quarter", "Year", "Total")
# for row in rows:
#     < код использующий временные периоды>


# 3
# ограниченный набор статусов уровней тревоги используется несколькими модулями программы
# thresholds = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

# лучше вывести в отдельный enum класс для использования
# class ThresholdsLevel(enum.Enum):
#     LOW = 0
#     MEDIUM = 1
#     HIGH = 2
#     CRITICAL = 3


# 4
# Можно не использовать индексацию, а воспользоваться возможностями языка по распаковке,
# если элементов в списке заранее известное ограниченное кол-во

# было
# parts = k.split(".")
#
# resource = parts[0]
# selected = parts[1]

# стало
# resource, selected = k.split(".")


# 5
# В данном участке кода вместо использования обычного tuple
# и обращения по индексу для читаемости лучше возвращать именованный кортеж (named tuple)

# было

# def get_user_name():  # вернет кортеж вида
#     < некоторый код получения пользователя >
#     return full_name, display_name, given_name, middle_name, family_name, initials

# def update_person_data(persons: list):
#     user_name = get_user_name()
#     for p in persons:
#         if p.data.get("fullName") != user_name[0]:
#             p.data["fullName"] = user_name[0]
#
#         if p.data.get("displayName") != user_name[1]:
#             p.data["displayName"] = user_name[1]
#
#         if p.data.get("givenName") != user_name[2]:
#             p.data["givenName"] = user_name[2]
#
#         if p.data.get("middleName") != user_name[3]:
#             p.data["middleName"] = user_name[3]
#
#         if p.data.get("familyName") != user_name[4]:
#             p.data["familyName"] = user_name[4]
#
#         < остальная часть кода обновления данных пользователя >

# стало
# LdapUserName = namedtuple('LdapUser', [
#     'full_name',
#     'display_name',
#     'middle_name',
#     'last_name',
#     'initials'])


# def get_user_name() -> LdapUserName:  # вернёт именованные кортеж вида
#     < некоторый код получения имен и инициалов пользователя >
#     full_name = <...>
#     display_name = <...>
#     middle_name = <...>
#     last_name = <...>
#     initials = <...>

#     return LdapUserName(full_name, display_name, middle_name, last_name, initials)


# def update_person_data(persons: list):
#     user_name = get_user_name()
#     for p in persons:
#         if p.data.get("fullName") != user_name.full_name:
#             p.data["fullName"] = user_name.full_name
#
#         if p.data.get("displayName") != user_name.display_name:
#             p.data["displayName"] = user_name.display_name
#
#         if p.data.get("middleName") != user_name.middle_name:
#             p.data["middleName"] = user_name.middle_name
#
#         if p.data.get("lastName") != user_name.last_name:
#             p.data["lastName"] = user_name.last_name
#
#         < остальная часть кода обновления данных пользователя >
