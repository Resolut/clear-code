# Ясный код. Урок 7

# 5.1 incidents_count -> get_total_incidents_count
# метод возвращает общее кол-во инцидентов в системе

# 5.2  метод 'index' ничего не индексирует, а только изменяет формат даты в списке поля frames
#      поэтому следует переименовать: index -> reformat_time_for_each_frame()
#      def index(self, time_format="%Y-%m-%d %H:%M:%S"):
#          return [a.strftime(time_format) for a in self.frames]

# 5.3  метод класса Dashboard возвращает словарь с количеством посетителей, событий и сессий,
#      а не статистику нескольких объектов
#      top_stats -> get_target_counts

# 5.4  Event имеет метод 'get_list', который на самом деле возвращает словарь с событиями и кол-вом страниц
#      get_list -> get_all_events_and_pages

# 5.5 Incident имеет метод get_item с параметром id, отличная идея отразить это в названии метода,
#     т.к. объект класса можно получить и например по имени инцидента
#     get_item(self, id): -> get_item_by_id


# 5.6 Класс Person имеет метод получения строки из таблицы в бд нужно переименовать его в читабельный вид с глаголом:
#     row_nmbr - get_row_number

# 5.7 Класс Session имеет метод _get_filtered_data получения отобранных объектов сессий
#     метод назван слишком абстрактно
#       _get_filtered_data -> get_session_by_filter

# 5.8 class User имеет целых ворох абстрактных названий item, можно сократить названия:

#     def get_item(self, id): -> get_by_id
#     def get_list(self, params={}): -> get_all
#     def save_item(self, data): -> save
#     def delete_item(self, data, owner): -> delete

# 5.9 Этот метод был помечен коллегой как пахнущий ^-^ как минимум нужно его переименовать
#     # it smells
#     def find(self, username): -> find_by_name
#         return self.session.query(models.User).filter(models.User.username == username).first()

# 5.10 ClientAddress имеет метод получения объекта клиентского адреса по IP, нужно отразить это в названии
#      get_item(self, ip) -> get_by_ip

# 5.11 ReportHistoryController имеет метод destroy удаления истории отчета и
#      в рамках проекта destroy лучше переименовать в remove и отразить,
#      что метод после удаления истории отчета перенаправляет на url с обновленной
#      страницей отчетов
#      destroy -> remove_and_redirect

# 5.12 class Report Runner имеет метод _document_name нужно отразить что имя отчета генерится
#      исходя из текущей даты и времени (временной метки )
#        _document_name() -> generate_document_name_with_current_timestamp()
