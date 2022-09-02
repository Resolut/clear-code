# Ясный код. Урок 8

# 3.1.1
from abc import ABC, abstractmethod
import json
from xml.etree import ElementTree


class ReportChart:
    @abstractmethod
    def make_header(self, header):
        pass

    @abstractmethod
    def make_labels(self, labels):
        pass

    @abstractmethod
    def build_report(self):
        pass


class BarChart(ReportChart):
    def __init__(self, header, labels):
        self.header = header
        self.labels = labels

    def make_header(self, header):
        pass

    def make_labels(self, labels):
        pass

    def build_report(self):
        return "bar report"


class PieChart(ReportChart):
    def __init__(self, header, labels):
        self.header = header
        self.labels = labels

    def make_header(self, header):
        pass

    def make_labels(self, labels):
        pass

    def build_report(self):
        return "pie report"


class FactoryReportChart:
    @staticmethod
    def _build_report(report_type, header, labels):
        if report_type == 'BarChart':
            return BarChart(header, labels).build_report()
        elif report_type == 'PieChart':
            return PieChart(header, labels).build_report()
        else:
            raise ValueError("Unknown ReportChart type")

    def build_report(self, report_type, header=None, labels=None):
        report = self._build_report(report_type, header, labels)
        return report


# пример использования
report_factory = FactoryReportChart()
pie_report = report_factory.build_report("pie", "quarter_header", ("week", "salary"))
bar_report = report_factory.build_report("bar", "year_header", ("months", "profit"))

# 3.1.2


class JsonSerializer:
    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'name': object_name,
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer:
    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = ElementTree.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = ElementTree.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return ElementTree.tostring(self._element, encoding='unicode')


class SerializerFactory:

    def __init__(self):
        self._creators = {}

    def register_format(self, format_type, creator):
        self._creators[format_type] = creator

    def get_serializer(self, format_type):
        creator = self._creators.get(format_type)
        if not creator:
            raise ValueError(format_type)
        return creator()


# пример использования объекта-фабрики
factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('XML', XmlSerializer)

# 3.1.3


class Body(ABC):
    @abstractmethod
    def assembly_engine(self):
        pass

    @abstractmethod
    def get_body_type(self):
        pass


class RegularBody(Body):
    def assembly_engine(self):
        return "regular_engine"

    def get_body_type(self):
        return "regular body"


class SportBody(Body):
    def assembly_engine(self):
        return "power_engine"

    def get_body_type(self):
        return "sport body"


class Hardware(ABC):
    @abstractmethod
    def put_console(self):
        pass

    @abstractmethod
    def assembly_seats(self):
        pass


class StandardHardware(Hardware):
    def put_console(self):
        return "Audio Panel, No Screen"

    def assembly_seats(self):
        return "Small Size, Artificial leather "


class CarFactory(ABC):

    def get_body(self) -> Body:
        return Body()

    def get_hardware(self) -> Hardware:
        return Hardware()


class FamilyCar(CarFactory):
    def get_body(self) -> Body:
        return RegularBody()

    def get_hardware(self) -> Hardware:
        return StandardHardware()


class OutdoorCar(CarFactory):
    def get_body(self) -> Body:
        return SportBody()

    def get_hardware(self) -> Hardware:
        return StandardHardware()


def choose_car():
    return {
        "Family": FamilyCar(),
        "Outdoor": OutdoorCar(),
    }


# пример использования
car = choose_car().get("Family")

body_car = car.get_body()
hardware_car = car.get_hardware()

body_car.assembly_engine()
body_car.get_body_type()
hardware_car.put_console()
hardware_car.assembly_seats()

# 3.2.1 Filterable, Sortable - интерфейсы реализации фильтров и их модификации для получения запросов из базы данных

# 3.2.2 Pageable - интерфейс для получения порциями (страницами) результатов запроса (для реализации пагинации)

# 3.2.3 BaseStream - абстрактный класс описывающий методы взаимодействия с потоком данных ввода-вывода.
#       SocketStream, наследующий BaseStream, реализует интерфейсы для работы с потоком ввода-вывода

# 3.2.4  Descriptor абстрактный класс, описывающий методы создания объекта,
#        поддерживающего базовый протокол дескриптора.
#        TypedDescriptor - класс наследующий абстрактный класс Descriptor,
#        реализующий методы проверки типов атрибутов объекта
