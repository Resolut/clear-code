# Ясный код. Урок 6

# 3.1
# 3.1.1
# IncidentProccessor -> IncidentController
# Класс управляющий процессами возникающих инцидентов в системе

# 3.1.2
# Adapter -> CasbinPloicyAdapter
# Вспомогательный класс прослойка для интерфейсов библиотеки Casbin для управления политикой разрешений

# 3.1.3
# JobRunner -> BaseJobRunner
# Базовый класс, создающий и запускающий задачу отдельными процессом

# 3.1.4
# Parser - IncomeEventLogParser
# Класс парсера логов событий входа в систему

# 3.1.5
# WhitelistEditRule -> WhiteListRuleEditor
# Класс, управляющий правилами для управления "белыми" списками ресурсов

# 3.2
# 3.2.1
# purge -> remove
# для очистки любых неактуальных объектов и файлов в системе по смыслу больше подходит 'remove'

# 3.2.2
# def _integrity_violations(self): # следует переназвать в get_integrity_checker_path
#     return self._get_file(config.system["integrity_checker"])
# integrity_checker - утилита для проверки целостности пакетов в системе

# 3.2.3
# class Session():
#     <...>
#     метод 'info' следует переназвать в 'get_all_sessions_per_limit'
#     def info(self, limit: datetime) -> str:
#         <...>

# 3.2.4 'rotate' -> rotate_data_in_cluster
# название метода уточняет, что ротация данных происходит только в переданном контейнере хранилища
# def rotate(self, cluster: storageCluster, limit: datetime, extra: dict):
#     <...>

# 3.2.5 Anomaly -> AnomalyDetector
# объект класса аномалий, фиксирующий в отдельном лог-журнале любое неописанное в системе поведение.

# 3.2.6  get_list стоит переназвать в 'get_all_paged_proxies'
# class Proxy(object):
#     get_list() -> dict:
#         return {"items": query.all(), "pager": paged.pager}

# 3.2.7 Group -> PersonGroup
# объект класса - группы на которые подразделяются пользователи в системе

