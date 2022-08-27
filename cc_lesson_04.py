# Ясный код. Урок 4. Именование булевых переменных

# 7.1
# 7.1.1 is_changeable -> allow_changes
# 7.1.2 is_exists -> exists
# 7.1.3 is_resizable -> can_resize
# 7.1.4 not_checked_by_filter -> checked_by_filter
# 7.1.5 has_no_bill_data -> contain_bill_data

# 7.2
# 7.2.1
# proc = Popen(['python', auth_script], stdout=PIPE, stderr=STDOUT)
# fail = False # переменную можно переименовать в типичную 'error'
# while True:
#     line = proc.stdout.readline()
#     data = line.decode('utf-8').strip()
#     result = re.search('#[0-9]+', data)
#     if data == '' and proc.poll() is not None:
#         fail = True

# 7.2.2
# while is_repeat_game:
#     <...> код реализации игры
#     while game.get_tries() > 0:
#         <...> код для обработки ходов игрока и компьютера
#         if game.is_win(): # переменную можно переименовать в 'game.done'
#            print(f"Поздравляем!!! Вы отгадали слово с {game.get_max_tries()-game.get_tries()} попыток(-и).")

# 7.3
# infile файл с логами, которые нужно проверить на соответствие CEF формату
# infile - параметр функции
# for line in infile:
#     parsed = {}
#     final_parsed = {}
#     tokens = re.split(r'(?<!\\)\|', line)
#     extension = ''
#     if len(tokens) == 8:
#         extension = tokens[7]
#     if len(tokens) > 8:
#         sys.stderr.write("Parsing error\n")
#         sys.exit(1)
#     parsed['CEFVersion'] = tokens[0].split('CEF:')[1]
#     parsed['DeviceVendor'] = tokens[1]
#     parsed['DeviceProduct'] = tokens[2]
#     parsed['DeviceVersion'] = tokens[3]
#     parsed['SignatureID'] = tokens[4]
#     parsed['Name'] = tokens[5]
#     parsed['Severity'] = tokens[6]

#     for k in parsed: 'k' лучше переименовать в более читаемую для ключа переменную cef_key
#         <...> здесь следует большая логика проверки ключей в логах
#               поэтому легче помнить какие именно ключи проверяются

# 7.4
# 7.4.1
# Для объектов класса поиска можно задать переменные статуса начала окончания поиска
# class Search():
#     self.begin = False
#     self.end = False
#
#     def make_indexing(self):
#         <...> реализация индексации поиска

#     def start_search(self):
#         self.begin = True
#         <...> реализация запуска поиска
#
#      def break_search():
#          self.end = True
#          <...> реализация прерывания счетчика

# 7.4.2
# использование start end для начальных и конечного индексов
# в сообщении с отсеканием первого служебного символа
# def _get_description(message):
#     start = 1
#     end = message.find('" ', start)
#
#     if end == -1:
#         end = len(message)
#
#     return message[start:end]

# 7.5
# 7.5.1
# в этом участке кода 'temp' лучше переименовать в 'history_grouped'
# if type(history) != dict:
#     history["number"] = 1
#     temp = history.groupby("source_bases")["number"].count().reset_index()
#     source_info = dict(zip(temp["source_bases"].to_list(), temp["number"].to_list()))

# 7.5.2
# Здесь словарь следует также переименовать в 'user_profile'
#     tmp = {}
#
#     for e in entity:
#         data = None
#
#         if isinstance(e, models.Report):
#             data = [([e], e.profiles.copy())]
#         elif isinstance(e, models.ExecProfile):
#             if e.reports:
#                 data = [(e.reports.copy(), [e])]
#         elif isinstance(e, models.ReportDelivery):
#             if e.profile.reports:
#                 data = [(e.profile.reports.copy(), [e.profile])]
#         elif isinstance(e, models.ReportSchedule):
#             if e.profile.reports:
#                 data = [(e.profile.reports.copy(), [e.profile])]
#         elif isinstance(e, models.User):
#             data = [(p.reports.copy(), [p]) for p in e.profiles if p.reports]
#
#         if data:
#             user_id = data[0][0][0].user_id
#             <...>
#             tmp[user_id] = tmp.get(user_id, {})
#             tmp[user_id][language] = tmp[user_id].get(language, {})
#             tmp[user_id][language][r] = tmp[user_id][language].get(r, set())
#             tmp[user_id][language][r].add(p)
#
#     for u in tmp.values():
#         for p in u.values():
#             for (r, ps) in p.items():
#                 for x in result:
#                     same = False
#
#                     if len(x[1]) == len(ps):
#                         same = True
#
#                         for y in ps:
#                             if y not in x[1]:
#                                 same = False
#
#                                 break
#
#                     if same:
#                         x[0].append(r)
#
#                         break
#                 else:
#                     result.append(([r], ps))
#
#     return result
