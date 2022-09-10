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
