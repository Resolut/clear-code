# Ясный код. Урок 3

# 6.1 Примеры использования имен, отражающих уровень абстракции

# 6.1.1
# db.SessionScope() объект получения всех открытых сессий с искомой базой данных

# 6.1.2
# csv_reader = csv.DictReader(file) - объект для чтения данных из таблицы в csv формате

# 6.1.3
# пример демона - класса SysLogListener слушателя системного журнала событий
class BaseJob:
    pass


class SyslogListener(BaseJob):
    def run(self, action):
        pass

# 6.1.4
# класс индексатора для хранения и поиска по записям сессий
class Indexer(object):
    def __init__(self):
        pass

    def close(self):
        pass

    def create_manifest(self, sid):
        pass

    def session_indexing(self, record):
        pass

    def presession_indexing(self, recorc):
        pass

    def add_session(self, record):
        pass

    def add_proxy(self):
        pass

# 6.1.5 класс для параллельного(конкурентного) запуска задач на многоядерных машинах
class JobRunner(object):
    EXCHANGE = "jobrunner"
    EXCHANGE_TYPE = "topic"
    QUEUE = "jobs"
    ROUTING_KEY = "job.#"
    RECONNECT_DELAY = 5
    CPU = os.cpu_count()

    def __init__(self):
        pass

    def setup_connection(self):
        pass

    def on_message(self, message_body):
        pass

    def shutdown(self, signum, _frame):
        pass

    def cleanup_state_locks(self):
        pass

    def run(self):
        pass


# 6.2 Примеры использования специальных терминов в качестве имен переменных

# 6.2.1
# producer - объект для записи (производства) сообщений в очередь
# с последующим их разбором потребителями (consumers)

# 6.2.2
# adapter - объект класса-прослойки для переопределения несовместимых методов
# других классов, от которых он наследуется

# 6.2.3
# garbage_collector (gc) "сборщик мусора" специальный объект удаляющий временные
# или более неиспользуемые программой объекты

# 6.2.4
# observer - объект, оповещающий другие объекты об изменениях своего состояния

# 6.2.5
# parser - объект с функциональностью синтаксического разбора, разделения переданных ему данных.


# 6.3 Примеры имен переменных заданных с учетом контекста (функции, метода, класса)

# 6.3.1
def get_license_from_xml(root: Element) -> Optional[Dict]:
    licence_signs = []  # переменная с учетом контекста, номера лицензий переданного элемента (страницы)

    for element in root:
        if element.tag == "signature":
            for sign in element:
                licence_signs.append(sign.text)
        else:
            ValueError("Incorrect tag of license %s", element.tag)
            return None

# 6.3.2
class SpecialDateFormat:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class Calendar:
    # <.. другие члены и методы класса>
    def format_date(self, year, month, day):
        #  <запись выбранной даты в специальном формате>
        return SpecialDateFormat(year, month, day)

    def get_calendar_for(self, year, month):
        current_date = self.format_date(year, month, 1)  # переменная с учетом контекста метода
        # <.. вычисления и формирование календаря для текущей даты>

# 6.3.3
class Button:
    def __init__(self, width: int, height: int, btn_color: str, text_color: str, message: str):
        """Инициализирует атрибуты кнопки."""
        # Назначение размеров и свойств кнопок.
        self.width, self.height = width, height
        self.button_color = btn_color
        self.text_color = text_color
        self.text = message

# 6.4 имена не попадающие в диапазон 8-20 символов
# было -> стало
# 6.4.1
# f_count -> filesProcessedWithSuccess
# счетчик успешно обработанных файлов

# 6.4.2
# success -> login_successful
# флаг статуса успешной операции логина

# 6.4.3
# payment -> month_bill_payment
# объект формы месячного счета на оплату

# 6.4.4
# file_id -> document_file_id
# идентификатор загруженного пользователем документа

# 6.4.5
# match -> matched_pattern
# шаблон поиска подстроки в формате регулярного выражения
