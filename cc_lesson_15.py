# Ясный код. Урок 15

# 1
# all_columns = [column['COLUMN_NAME'] for column in db.cursor.fetchall()]
# order_data = await state.get_data()
# columns = order_data.keys()

# проверка и запись всех отсутствующие столбцов в таблицу
# dif_columns = list(set(columns) - set(all_columns))

# with db.cursor as cursor:
#     if len(dif_columns) > 0:
#         columns_template = " ".join(
#             ["ADD {} TEXT,".format(column) for column in dif_columns]).rstrip(",")
#         sql_add_columns = "ALTER TABLE orders {}".format(columns_template)
#         cursor.execute(sql_add_columns)
#         placeholders = ", ".join(['%s'] * len(order_dict))
#         sql_insert = "INSERT INTO %s ( %s ) VALUES ( %s )" % (
#             'orders', columns, placeholders)
#         cursor.execute(sql_insert, values)
#         db.connection.commit()


# 2
# def inititalize_dynamic_settings(self):
#     """Инициализирует настройки, изменяющиеся в ходе игры."""
#     self.ship_speed_factor = 0.75
#     self.bullet_speed_factor = 2
#     self.alien_speed_factor = 0.5
#
#     # fleet_direction = 1 - обозначает движение флота пришельцев вправо; -1 - влево.
#     self.fleet_direction = 1
#
#     # Подсчёт очков
#     self.alien_points = 50
#     <...>


# 3
# def prepare_level(self):
#     """Преобразует уровень в графическое изображение."""
#     self.level_image = self.font.render(
#         str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
#     # Уровень выводится под текущим счетом
#     self.level_rect = self.level_image.get_rect()
#     self.level_rect.right = self.score_rect.right
#     self.level_rect.top = self.score_rect.bottom + 10


# 4
# add the virtual environments site-package to the host python import mechanism
# IS_PYPY = hasattr(sys, "pypy_version_info")
# IS_JYTHON = sys.platform.startswith("java")
# if IS_JYTHON:
#     site_packages = os.path.join(base, "Lib", "site-packages")
# elif IS_PYPY:
#     site_packages = os.path.join(base, "site-packages")
# else:
#     IS_WIN = sys.platform == "win32"
#     if IS_WIN:
#         site_packages = os.path.join(base, "Lib", "site-packages")
#     else:
#         site_packages = os.path.join(
#             base, "lib", "python{}".format(sys.version[:3]), "site-packages"
#         )


# 5
# session = ds.session()
# if not session.empty:
#     # events per hour (in hour to be more precise)
#     session["evtph"] = (
#             session["evtcnt"] / (session["duration"].transform(lambda x: np.ceil(x / 3600) if x else 1))
#     ).round(2)


# 6
# prev = set(sys.path)
#
# # Move the added items to the front of the path, in place
# new = list(sys.path)
# sys.path[:] = [i for i in new if i not in prev] + [i for i in new if i in prev]


# 7
# def is_uuid(value):
#     if isinstance(value, uuid.UUID):
#         return True
#     elif isinstance(value, str):
#         try:
#             result = uuid.UUID(value, version=4)
#             value = value.replace("-", "")
#             # If the uuid_string is a valid hex code,
#             # but an invalid uuid4,
#             # the UUID.__init__ will convert it to a
#             # valid uuid4. This is bad for validation purposes.
#             if result.hex == value:
#                 return True
#             # workaround for 'people' table - uuids there contain '5' as version
#             elif (
#                 result.hex[:12] == value[:12] and
#                 result.hex[13:] == value[13:] and
#                 result.hex[12] == "4" and
#                 value[12] == "5"
#             ):
#                 return True
#         except ValueError:
#             return False
#     return False
