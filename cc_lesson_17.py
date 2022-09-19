# Ясный код. Урок 17

# 1
# Шумные комменатрии, удалил (строки 7, 10, 14, 17)

# if not args.infile.isatty():
#     # interactive device
#     infile = args.infile
# else:
#     # open the file here
#     infile = open(args.infile, 'r')
#
# if input_file:
#     # passed file
#     infile = open(input_file, 'r')
#
# # close input file if one was opened
# if args.infile.isatty():
#     infile.close()


# 2
# Первый комментарий (строка 27) действительно поясняет содержимое списка 'd',
# а во втором (29) нет необходимости, т.к. это ясно из кода

# with dbopen(str(path / "idx")) as idx:
#     # list of tuples (offset, length)
#     d = [tuple(map(int, idx[key].split(b":"))) for key in idx.keys()]
#     # sort by offset
#     return sorted(d, key=lambda x: x[0])


# 3
# Нелокальная информация или точнее риторический 'to do' вопрос :)
# удалил его, т.к. ответ на этот вопрос содержится в вызывающем коде

# TODO should we yield Path objects?
# def items(self, relative: bool = False) -> t.Generator[str, None, None]:
#     import glob
#
#     for item in glob.iglob(str(self.base_path / "*/*/*")):
#         if relative:
#             yield os.path.relpath(item, str(self.base_path))
#         else:
#             yield item


# 4
# Лишняя информация, шум, удалил комментарий в стр. 53

# def __next_token(self, delim=" "):
#     token = None
#     idx = self.line.find(delim)  # находим индекс первого пробела в строке
#     <...>


# 5
# Бессмысленный комментарий (стр. 61), из кода и так очевидно,
# что проверяется тип поля с атрибутами

# check type
# if self.attrs.type not in self.event_types:
#     log.critical('UNKNOWN EVENT TYPE: "%s"', self.attrs.type)
#     raise ValueError('UNKNOWN EVENT TYPE: "{}"'.format(self.attrs.type))


# 6
# Открытый вопрос (стр. 78), оформил его в виде todo
# for obj in objs:
#     try:
#         serialized = json.dumps(obj, default=encoder, separators=(",", ":"), sort_keys=True)
#     except TypeError as ex:
#         log.error("Cannot serialize object: %r", obj)
#         if strict:
#             raise ex
#         else:
#             continue
#     yield serialized, obj  # return only serialized without obj???


# 7
# Слишком общий "todo" (стр.84)
# Дополнил его, что необходимо добавить дополнительные имена сервисов

# # TODO should be refactored
# def _get_service(self, svc):
#     return svc if svc else "RDP"


# 8
# Закомментированный код (99-106),
# удалил его и объединил первые два условия

# class Encoder(json.JSONEncoder):
#     def default(self, val):
#         if isinstance(val, (datetime.datetime, datetime.date, datetime.timedelta)):
#             return str(val)
#         elif isinstance(val, uuid.UUID):
#             return str(val)
# #        elif isinstance(val, np.integer):
# #            return int(val)
# #        elif isinstance(val, np.floating):
# #            return float(val)
# #        elif isinstance(val, np.bool_):
# #            return bool(val)
# #        elif isinstance(val, np.ndarray):
# #            return val.tolist()
#         else:
#             try:
#                 return super(Encoder, self).encode(val)
#             except Exception:
#                 log.exception("Could not serialize type %s", type(val))
#                 return str(val)


# 9
# Вместо почти неприметного (бормочущего) комментария (стр. 118) добавил docstring к классу

# class AnomalyConfigFTDSchema(AnomalyConfigSchema):  # file transfer detector
#     factor = ma.fields.Float()
#     low_loads = ma.fields.Integer(required=True, validate=ma.validate.Range(min=0))
#     medium_loads = ma.fields.Integer(required=True, validate=ma.validate.Range(min=0))
#     high_loads = ma.fields.Integer(required=True, validate=ma.validate.Range(min=0))
#     period = ma.fields.Integer(required=True, validate=ma.validate.Range(min=0))


# 10
# Перенёс комментарий (стр. 129), оформив его в docstring метода

# send restart command for the list of services
# def restart_services(services: set) -> None:
#     if services:
#         msg = dict(job="ProcMgr", params=dict(action="restart", proc=list(services)))
#
#         qmgr.submit(
#             json.dumps(msg, default=db.Encoder().default, ensure_ascii=False).encode(),
#             "job.{}".format("restart"),
#             "jobrunner"
#         )


# 11
# Избыточный комментарий docstring, удалил, т.к. метод не нуждается в пояснениях

# def remove_file(file: str) -> None:
#     """safely delete file"""
#     try:
#         os.remove(file)
#     except OSError as ex:
#         log.error("{} was not to be removed, {}".format(file, ex))


# 12
# Нелокальный комментарий (стр. 156), относящийся к другому участку кода
# Перенёс его в нужное место (перед строкой 161)

# certificate_file = os.path.join(unpacked, "certificate")
# # install process client certificate
# <блок кода, не связанный с процессом установки сертификата>
# <... другой блок кода ...>
# <... ещё один блок ...>
# <блок кода где происходит установка сертификата>


# 13
# Бессмысленные комментарии (стр. 173, 174) для бессмысленного метода,
# код которого никогда не выполнится, удалил метод

# def update_node(directory: str) -> None:
#     file = os.path.join(directory, "node")
#
#     data = read_json(file)
#
#     if False:  # ......... "node" update needed
#         # ......... update "node"
#
#         write_json(file, data)


# 14
# Избыточный комментарий
# Код метода не требует очевидного комментария в виде docstring, удалил его
# def config_file(_id: str, config: str) -> str:
#     """return config file path"""
#     return os.path.join(config, _id, config_name)


# 15
# Бесполезный комментарий, шум. Удалил

# files
# base = Path(st.base(sid))
