# Ясный код Урок 11

# 1
# Сравнение на пустой список, как недопустимое значение, можно упростить

# было
# if re.findall(r"^\d+$", input) != []:
#     command = "numbers"
# стало
# if re.findall(r"^\d+$", input):
#     command = "numbers"


# 2
# Некорректная проверка завершения и перезапуска процесса

# было
# if process.exitcode:  # wtf?
#     process.join()
#
#     if process.exitcode > 0:  # internal error
#         log.error("%s return %d", process.name, process.exitcode)
#         self.restart(item)
#
#     else:  # exitcode < 0 => killed
#         log.error("%s killed by signal %d", process.name, process.exitcode)
#         self.restart(item)
#
# else:  # normal exit
#     log.info("%s complete", process.name)

# стало
# process.join()
#
# if process.exitcode > 0:  # internal error
#     log.error("%s return %d", process.name, process.exitcode)
#     self.restart(item)
#
# elif process.exitcode < 0:  # => killed
#     log.error("%s killed by signal %d", process.name, process.exitcode)
#     self.restart(item)
#
# log.info("%s complete", process.name)


# 3
# Очень соблазнительно использовать однобуквенное имя для файла - 'f',
# может произойти конфликт имен из внешней области видимости.
# Переименовал для большего соответствия типу объекта файла

# def chown(tar_file: tarfile.TarInfo) -> tarfile.TarInfo:
#     <..> какой то код работы по работе с файлом

# 4
# Неправильное использование аргументов (через определение глобальной переменной) другим модулем,
# передаваемых при запуске модуля как исполняемого файла
# отказался полностью от использования этой глобальной переменной

# def main():
#     global args # -> удалил переменную ибо в ней не было смысла
#     args = parse_args()
#     args.op()
#
#
# if __name__ == "__main__":
#     main()


# 5
# Переменная цикла никак не используется, для этой цели в python есть '_'
# было
# for line in file:
#     num_errors += 1

# стало
# for _ in log_file:
#     num_errors += 1


# 6
# инициализация списка с объявлением неиспользуемой в цикле переменной 'i', так же заменил на '_'
# result = [0 for i in range(0, paged.pager.pages)]


# 7
# в цикле используется класс Session State, наследуемый от enum.IntEnum,

# {bit.name: 1 for bit in SessionState if state & bit} for sid, state in excluded

# Для реализации протокола Iterable у него отсутствовало переопределение метода __iter__.
# Добавил в класс SessionState переопределение этого метода.


# 8
# лишняя инициализация словаря limits, его можно опустить
# в блоке try он в любом из веток условий случае будет инициализирован

# def get_limits(args: argparse.Namespace) -> dict:
#     defaults = config.system["defaults"]
#     limits = {}  # удалил эту инициализацию
#     try:
#         if args.date:
#             d = dp.parse(args.date)
#             limits = {key: d for key in defaults}
#         elif args.months:
#             d = (datetime.now() - relativedelta(months=args.months)).date()
#             limits = {key: d for key in defaults}
#         else:
#             limits = {
#                 key: (datetime.now() - relativedelta(months=val)).date()
#                 for key, val in defaults.items()
#             }
#     except ValueError:
#         raise argparse.ArgumentTypeError("argument type is not valid")
#
#     limits["all"] = date.today() + relativedelta(days=1)
#     limits["tl"] = config.system["keep_tl_events"]
#     return limits


# 9
# Инициализация поля 'errors' класса IncidentsController происходила в других методах класса,
# перенес инициализацию в __init__

# class IncidentsController:
#     def __init__(self, params):
#         super().__init__("IncidentsControllerIterator")
#
#         self.ds = Incident(g.db)
#         self.id = params.get("id")
#         self.errors = errors
#
#     def check_incident(self, data):
#         errors = schemas.IncidentSchema().validate(data)
#
#         if errors:
#             # self.errors = errors # перенес инициализацию в __init__
#
#             return False
#
#         return True


# 10
# Исправил отсутствие инициализации родительского класса в дочернем классе
# class addressesController(BaseController):
#     def __init__(self, params):
#         super().__init__() # добавил инициализацию полей базового класса
#         self.id = params.get("id")
#         self.ds = ClientAddress(g.db)


# 11
# Переменная message может быть не проинициализирована,
# если ни одно из условий не окажется истинным.
# Добавил дефолтное сообщение в ветке else

# def _delete(self, data):
#     try:
#         if isinstance(data, models.Group):
#             message = "Group deleted: group={}".format(data.name)
#         elif isinstance(data, models.GroupUnit):
#             message = "Group : group={}".format(data.group.name)
#         elif isinstance(data, models.GroupAnotherUnit):
#             message = "Group : group={}".format(data.group.name)
#         elif isinstance(data, models.GroupOthers):
#             message = "Group : group={}".format(data.group.name)
#         elif isinstance(data, models.SystemGroupLdap):
#             message = "Group : group={}".format(data.group.name)
#         else:
#             message = 'Group: not detect'
#
#         self.ds.delete_item(data)
#
#         logger.error(
#             dict(
#                 s_user=current_user.username,
#                 dst=get_server_ip(),
#                 rt=datetime.datetime.now(),
#                 msg=message,
#             ),
#         )


# 12
# Лишняя инициализация словаря, можно сразу проинициализировать словарь нужными ключами

# было
# <...>
# info = {}
#
# info["id"] = str(user.id)
# info["name"] = user.name
# info["description"] = user.description
# info["identifier"] = user.identifier
# info["role_id"] = user.role_id

# result.append(info)
# < продолжение кода>

# стало
# info = {"id": str(user.id),
#         "name": user.name,
#         "description": user.description,
#         "identifier": user.identifier,
#         "role_id":  user.role_id,
# }
# < продолжение кода>


# 13
# Параметр метода на самом деле не используется, а локальная переменная названа таким же именем.
# создается иллюзия, что параметр используется внутри функции
# удалил неиспользуемый параметр
# def _build_change_lists(data, groups): # удалил 'groups' из сигнатуры метода
#     <...>
#     domains, servers, groups = LdapEntityBuilder(flask.g.db).build_entity_lists(data)
#     < .. далее по коду используется локальная переменная 'groups' .. >


# 14
#  параметр 'order' вложенной функции переопределяет переменную внешней функции,
#  переименовал ее в 'order_kind', так как она активно используется далее по коду

# def build(self):
#     order = self.params.get("orderby", "target")
#
#     def get_accounts(value, source, _max, order_kind):
#         if order_kind == "incident_impact":
#             order_kind = "incident_impact"
#         elif order_kind == "incident_count":
#             order_kind = "incident_count"
#         else:
#             order_kind = "session_id"


# 15
# перенес ближе к использованию и упростил инициализацию переменной 'records'
#     def to_csv(self):
#         records = []
#         <... много строк промежуточного кода, где 'records' никак не используется>
#         records.append("key,value\n")
#         <.. далее по коду 'records' уже используется >

# стало
# def to_csv(self):
#           <... много строк промежуточного кода где 'records' никак не используется>
#           records = ["key,value\n"]
#           <.. далее по коду 'records' уже используется >
