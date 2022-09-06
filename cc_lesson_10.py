# Ясный код Урок 10

# 1
# Я сам не сразу вспомнил, почему длина должна быть 28 :)
# "магическое число" перенес в константу для ясности и использовал уже константу
# def storage_iterator(path: str) -> t.Iterator[t.Tuple[str, str]]:
#     DIR_NAME_MIN_LENGTH = 28
#     # from pathlib import Path
#     # import re
#     # dirs = (x.parts[-1] for x in Path(path).glob("**/[a-f0-9][a-f0-9]*") if x.is_dir())
#     # yield from (x for x in dirs if re.match(rf"[a-f0-9]{DIR_NAME_MIN_LENGTH}", x))
#
#     rx = re.compile(rf"^[0-9a-f]{2,{DIR_NAME_MIN_LENGTH}}$")
#
#     for dirname, dirs, files in os.walk(path):
#
#         # filter non-storage dirs
#         dirs[:] = filter(lambda d: rx.search(d), dirs)
#
#         if dirs:  # use leaf nodes only
#             continue
#
#         basename = os.path.basename(dirname)
#         if len(basename) < DIR_NAME_MIN_LENGTH:
#             continue
#
#         yield dirname, basename

# 2
# вместо раздельного использования путей к логам и масок для файлов
# вынес список кортежей путей и масок файлов логов в единый список
# VAR_LOG_FILES = [
#     ("/var/log/rabbitmq", "*log"),
#     ("/var/log/rabbitmq", "*1"),
#     ("/var/log/rabbitmq", "*err"),
#     ("/var/log/apache2", "error.log"),
#     ("/var/log", "cron.log"),
# ]


# 3
# исправил правильное сравнение на непринадлежность к членам списка:
# было
# if not "all" in nodes:
#     <do something>

# стало
# if "all" not in nodes:
#     <do something>


# 4 сравнение можно упростить
# было
# if (
#     u.account_expires_at and
#     u.account_expires_at > now and
#     u.account_expires_at < warn
# ):

# стало
# if (
#     u.account_expires_at and
#     now < u.account_expires_at < warn
# ):

# 5 магическая строка используется более чем в 3 местах в модуле
# лучше завести в отдельную переменную
# service_owner = "www-data"
# if pwd.getpwuid(os.stat(result.name).st_uid).pw_name != service_owner:
#     shutil.chown(result.name, service_owner, service_owner)


# 6 в методе не проверялся, что параметр period может быть нулевым
# добавил проверку на none и сравнение на ноль и установку минимально возможного значения
# def check_file_exists(path, period):
#     if period is None or period == 0:
#         period = 60
#     if not tsdb.exists_db(path):
#         tsdb.create_db(path, period, int(5 * 365 * (tsdb.DAY / period)))


# 7
# в коде запроса явно заглушено предупреждение E711 и следом также сравнение на None
# было
# query = session.query(models.User).filter(and_(
#     models.User.domain_id != None,  # noqa: E711
#     or_(
#         models.User.last_update == None,
#         models.User.last_update <= to_date
#     )
# ))

# стало
# query = session.query(models.User).filter(and_(
#     models.User.domain_id is not None,
#     or_(
#         models.User.last_update is None,
#         models.User.last_update <= to_date
#     )
# ))


# 8 более 'питоничное' сравнение на пустой список
# name_problem = [name for name in transfer_list if area[name]["anxiety"]]
# было
# if name_problem == []:
#     continue
# стало
# if not name_problem:
#     continue


# 9
# 'user.get_data()' вернет строку введенных пользователем данных с различной кодировкой
# приводим ее к utf-8 и в unicode для дальнейшего использования
# user_raw_data = user.get_data()
# user_data = user_raw_data.encode().decode('unicode-escape')
# <.. using user_data ..>


# 10
# временная переменная 'data' хранит список данных события.
# во первых переименовал ее 'event_all_data' в для понимания с какими именно данными имеем дело,
# во вторых добавил проверку, что это действительно список,
#  чтобы избежать возникновения исключения при попытке перечисления данных в нем
#  event_all_data = event["event_data"]["data"]
#
# if event_type == "KBD_INPUT" and isinstance(event_data, list):
#     agents = [1 if agent in event_data else 0 for agent in self.agents]


# 11
# логическое сравнение можно упростить до более читаемого
# было
# def iter_pages(self, left_edge=2, left_current=2, right_current=5, right_edge=2):
#     last = 0
#     for num in range(1, self.pages + 1):
#         if (
#                 num <= left_edge or
#                 (num > self.page - left_current - 1 and num < self.page + right_current) or
#                 num > self.pages - right_edge
#         ):
#             <do something>
#
# стало
# def iter_pages(self, left_edge=2, left_current=2, right_current=5, right_edge=2):
#     last = 0
#     for num in range(1, self.pages + 1):
#         if (
#             num <= left_edge or
#             (self.page - left_current - 1 < num < self.page + right_current) or
#             num > self.pages - right_edge
#         ):
#             <do something>


# 12
# логическое сравнение можно упростить до более читаемого
# было
# if current < level["level"] and previous >= level["level"]:
# стало
# if current < level["level"] <= previous:
