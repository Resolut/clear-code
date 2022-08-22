# Ясный код. Урок 2

# 6.1

# 6.2 Примеры использования специальных терминов в качестве имен переменных


# 6.3 Примеры имен переменных заданных с учетом контекста (функции, метода, класса)

# 6.3.1
def get_license_from_xml(root: Element) -> Optional[Dict]:
    licence_signs = []  # переменная с учетом контекста, номера лицензий с учетом переданного элемента

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

# f_count -> filesProcessedWithSuccess
# счетчик успешно обработанных файлов

# success -> login_successful
# флаг статуса успешной операции логина

# payment -> month_bill_payment

