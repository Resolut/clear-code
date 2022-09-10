# Ясный код Урок 11

# 1
# Для переменной 'file_id' завёл отдельный метод для ее получения

# @dp.message_handler(state=Kasko.prepare_scan_process, content_types=['photo', 'document'])
# def get_file_id(message: Message):
#     file_id = None
#     if message.content_type == 'photo':
#         file_id = message.photo[-1].file_id
#     elif message.content_type == 'document':
#         file_id = message.document.file_id
#
#     return file_id
#
#
# @dp.message_handler(state=Kasko.scan_process, content_types=['photo', 'document'])
# async def get_docs_process(message: Message, state: FSMContext):
#
#     #  перенёс этот блок в отдельный метод 'get_file_id' (см. выше)
#     file_id = None
#     if message.content_type == 'photo':
#         file_id = message.photo[-1].file_id
#     elif message.content_type == 'document':
#         file_id = message.document.file_id
#
#     file_id = get_file_id(message)
#
#     if file_id is not None:
#         async with state.proxy() as data:
#             if 'doc_count' not in data.keys():
#                 data['doc_count'] = 1
#             else:
#                 data['doc_count'] += 1
#             key = "document_id" + "_" + str(data['doc_count'])
#             data[key] = file_id
#         < некоторый код >
#         await bot.download_file_by_id(destination=destination, file_id=file_id)


# 2
# Перенес сообщения и шаблон текста по обработке заявки в отдельные константы
# в область видимости на уровень выше,
# т.к. эти сообщения и шаблон могут быть повторно использованы
# ORDER_FORM_TEMPLATE_MESSAGE = f"Проверьте введённые данные:"
#                               f"\nИмя: <b>{data['first_name']}</b>"
#                               f"\nТип страхования: <b>{data['insurance_type']}</b>"
#                               f"\nНомер телефона: <b>{data['phone']}</b>"
#                               f"\nДата рождения: <b>{data['birthdate']}</b>"
#                               f"\nДата начала действия полиса: <b>{data['police_start_date']}</b>"
#                               f"\nРегион регистрации авто: <b>{data['register_region']}</b>"
#                               f"\nСтаж вождения: <b>{data['driving_age']} лет</b>"
#                               f"\nТип субъекта: <b>{data['entity']}</b>"
#                               f"\nМарка автомобиля: <b>{data['make_car']}</b>"
#                               f"\nМодель автомобиля: <b>{data['model_car']}</b>"
#                               f"\nГод выпуска автомобиля: <b>{data['release_year']}</b>"
#                               f"\nПробег автомобиля: <b>{data['mileage']} км</b>"
#                               f"\nМощность двигателя: <b>{data['engine_power']} л.с.</b>"
#
# ORDER_THANKS_MESSAGE = "Документы получены, спасибо!"
# ORDER_CONFIRM_MESSAGE = "Данные указаны верно ?"

# @dp.message_handler(lambda message: message.text.lower() == "да", state=Kasko.scan_process)
# async def scan_docs_process(message: Message, state: FSMContext):
#     remove_markup = ReplyKeyboardRemove()
#     await message.answer(ORDER_THANKS_MESSAGE, reply_markup=remove_markup)
#     cur_state = await state.get_state()
#     data = await state.get_data()
#
#     await bot.send_message(
#         message.chat.id,
#         text=ORDER_FORM_TEMPLATE_MESSAGE
#     )
#     # Confirm ReplyKeyboardMarkup
#     await message.answer(ORDER_CONFIRM_MESSAGE, reply_markup=kb.inline_edit)
#     await Kasko.check.set()


# 3
# Перенёс выполнение запроса к базе данных в отдельный метод,
# сгруппировав в нём все обращения к объекту базы 'db'

# def execute_sql_query(db, dif_columns, sql_insert, values):
#     with db.open():
#         with db.cursor as cursor:
#             if len(dif_columns) > 0:
#                 # добавить новые столбцы в таблицу
#                 columns_template = " ".join(
#                     ["ADD {} TEXT,".format(column) for column in dif_columns]).rstrip(",")
#                 sql_add_columns = "ALTER TABLE orders {}".format(columns_template)
#                 print("Запрос добавления столбцов: ", sql_add_columns)
#                 cursor.execute(sql_add_columns)
#             cursor.execute(sql_insert, values)
#             db.connection.commit()
#
# @dp.message_handler(lambda message: message.text.lower() == "нет", state=Kasko.add_driver)
# async def finish_order(message: Message, state: FSMContext):
#     < некоторый код перед выполнением запроса >
#     execute_sql_query(db, dif_columns, sql_insert, values)
#     < код отправки уведомления пользователю об успешной отравке >


# 4
# перенес переменные из метода в константы и в область видимости выше, на уровень модуля,
# чтобы при его импорте зависимые библиотеки прописывались в системную переменную PATH:
# import site
# IS_PYPY = hasattr(sys, "pypy_version_info")
# IS_JYTHON = sys.platform.startswith("java")
# if IS_JYTHON:
#     site_packages = os.path.join(base, "Lib", "site-packages")
# elif IS_PYPY:
#     site_packages = os.path.join(base, "site-packages")
# else:
#     <сделать что то другое>

# site.addsitedir(site_packages) # метод добавит пути до библиотек в PATH


# 5
# Вынес в отдельный метод 'get_parsed_records' блок обработки записей сессий и прокси
#
# def consume():
#     pattern = re.compile(r"session_id=[\"'](\S{10})[\"']")
#
#     for string in sys.stdin.buffer:
#         line = decode_string(string)
#
#         try:
#             < блок ниже вынесен в отдельный метод >
#             rec = Parser(line)
#             rec._parse_metadata()
#
#             if rec.rec_type in ["SSH Session", "RDP Session", "VNC Session"]:
#                 < большой код обработки записей сессий использующий rec>
#             elif rec.rec_type in ["sshproxy", "rdpproxy"]:
#                 < код обработки записей с прокси использующий rec>
#             else:
#                 < код обработки нераспознанных протоколов >
#             < конец блока >

#             get_parsed_records(line)
#
#         except ValueError as e:
#             try:
#                 < попытка трассировки ошибки >
#             except Exception:
#                 < запись в лог об ошибке>


# 6
# В методе 'run' контроллера большой блок кода создающий и подготавливающий к использованию
# объект отчета (report).
# Вынес этот блока кода в отдельный метод '_build_report'

# class ReportTemplatesController(object):
#     def _build_report():
#         report_class = self._report_class()
#         report = report_class(g.db, preview=True)
#
#         result, self.errors = report.load.params(request.form)
#
#         if self.errors:
#             flash_errors(self.errors)
#         else:
#             report.prepare_params(result)
#             report.build()
#             report.suppress_lines()
#         return report
#
#     def run(self):
#         report._build_report()
#         params = report.dump_params(result)
#
#         template, report_data = report.show()


# 7
# В методе создания пользователя 'create' сгруппировал команды,
# обновляющие форму перед отрисовкой ее на фронтенде.
# Вынес в отдельный метод 'prepare_user_form'

# def prepare_user_form(self):
#     form = BaseForm()
#     form.obj.force_change_pwd = True
#     form.obj.password_expires_at = self._get_expiration_date()
#     form.obj.account_expires_at = self._get_expiration_date("account")
#     return form
#
# def create(self):
#     if request.method == "GET":
#         self.prepare_user_form()
#
#         return render_template("users/new.html", f=form.obj, action="new")


# 8
# Сгруппировал в отдельный метод 'draw_charts' команды для построения графика
# для переданных данных
#  def draw_chart(index, counts):
#         ws_chart = pygal.StackedBar(pygal_config)
#
#         ws_chart.y_labels_major = [10, 100, 1000, 10000, 100000]
#         ws_chart.x_labels = index
#         ws_chart.height = 400
#
#         ws_chart.add(_("Sessions"), counts["data"]["sessions"].to_list())
#         ws_chart.add(_("Events"), counts["data"]["events"].to_list())
#
#         inc_chart = pygal.StackedBar(pygal_config)
#
#         inc_chart.y_labels_major = [10, 100, 1000, 10000, 100000]
#         inc_chart.x_labels = index
#         inc_chart.height = 400

# def _get_stats(self, params):
#     < код получения index и counts >
#     draw_chart(index, counts)


# 9 сгруппировал в отдельный метод 'init_pygal_config'
# настройку файла конфигурации для отрисовки графика

# def init_pygal_config():
#     pygal_config = pygal.Config(fill=False, interpolate=None)
#
#     pygal_config.disable_xml_declaration = True
#     pygal_config.show_minor_y_labels = False
#     pygal_config.show_minor_x_labels = False
#     pygal_config.x_labels_major_every = 3
#     pygal_config.truncate_label = -1
#     pygal_config.style = pygal.style.DefaultStyle(label_font_size=14)
#
#     pygal_config.css.append(get_pygal_css_path())


# 10
# В метод передаётся список exclude, который может быть изменен в процессе выполнения функции
# Внутри метода завел tuple, в который копирую данные из списка и работаю дальше уже с ним.

# def _load(self, params, exclude=[]):
#     excluded = tuple(exclude)
#     if params.get("mail"):
#         params = self._process_mail_credentials(params)
#     data, self.errors = sch.GeneralConfigurationSchema(exclude=excluded).load(params)
#     return data


# 11
# Перенёс в отдельный метод init_incident инициализацию пустыми значениями объекта 'incident'

# class IncidentController(object):
#     def init_incident(self):
#         incident = type("", (), {})()
#         incident.session = type("", (), {})()
#         incident.session.user = ""
#         incident.session.device = ""
#         incident.session.proxy_ip = ""
#         incident.session.client_ip = ""
#
#     def index(self):
#         self.init_incident()
#         <далее код использующий incident>
#         return render_template("incidents/index.html", incident=incident)


# 12
# Сузил область видимости списка, из уровня модуля перенес в единственную функцию,
# где этот список используется

# def create_archive():
#     tables = [
#         "deliveries",
#         "incident_history",
#         "incidents",
#         "people",
#         "permissions",
#         "reports",
#         "restriction_groups",
#         "role_permission",
#         "role_restriction_group",
#         "roles",
#         "schedules",
#         "search_results",
#         "targets",
#         "users",
#     ]

#     for t in tables:
#         selected = select([m.Base.metadata.tables[t]])
#         < запись метаданных в выбранное поле >


# 13
# Вынес в отдельный метод запись свойств для аккаунта администратора
# def update_admin():
#     admin = sess.query(User).filter(User.username == "admin").first()
#     new_password = (
#         generate_password_hash(args.password) if args.password else DEFAULT_ADMIN_PWD
#     )
#
#     if admin:
#         admin.password = new_password
#         admin.force_change_pwd = True
#         admin.blocked = False
#         admin.account_expires_at = None
#         admin.password_expires_at = None
#         admin.login_attempts = 0
#     else:
#         create_user(is_admin=True)

# try:
#     with session_scope() as sess:
#         update_admin()
#         sess.add(admin)
# except SQLAlchemyError as ex:
#     log.exception(ex)
#     print("Cannot change 'admin' account: {}".format(ex), file=sys.stderr)
#     return 1


# 14
# Сузил область видимости переменной, перенёс список системных команд
# из модуля в единственную функцию, которая его использует
# def run_cmd_by_user(user):
#     sysinfo_commands = [
#             "/bin/hostname",
#             ["/bin/ip", "addr"],
#             ["/bin/ip", "link"],
#             "/bin/date",
#             "/usr/bin/uptime",
#             ["/bin/cat", "/proc/cpuinfo"],
#             ["/bin/cat", "/proc/meminfo"],
#             ["/bin/cat", "/proc/vmstat"],
#             ["/bin/cat", "/proc/loadavg"],
#             ["/bin/bash", "-c", "ulimit", "-a"],
#     ]
#
#     sysinfo_data = "Run as user: {}\n\n".format(user) if user else ""
#
#     for cmd in sysinfo_commands:
#         cmd_name = str.join(" ", cmd) if isinstance(cmd, list) else cmd
#         sysinfo_data += "[ {} ] {}\n".format(cmd_name, "-" * (80 - len(cmd_name) + 5))
#
#         try:
#             cmd_data = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         except OSError as err:
#             print("Cannot exec {}: {}".format(cmd, err), file=sys.stderr)
#             continue


# 15
# Назвал переменную 'hash' и не смог использовать стандартный python метод hash,
# из наложения областей видимости.
# переименовал переменную в 'hash'

# hash = hash(path) -> file_hash = hash(path)
