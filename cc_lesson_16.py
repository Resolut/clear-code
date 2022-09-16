# Ясный код. Урок 16

# 1 Информативный комментарий, проясняющий смысл префикса
# prefix = "dc"  # url prefix for distributed config protocol


# 2
# Информативный комментарий, поясняющий фильтрацию записей событий в сессии
# sess_df = pd.DataFrame({"log": info})
# # exclude not sufficient events
# sess_df = sess_df[~sess_df["type"].isin(EVENTS_TO_EXCLUDE)]
# if sess_df.empty:
#     return None


# 3
# Предупреждающий комментарий о пересмотре возвращаемых значений
# def produce(
#     objs: Iterable,
#     strict: bool = False,
#     encoder: Optional[Callable[..., str]] = StreamV1Encoder.default,
# ) -> Generator[str, None, None]:
#
#     for obj in objs:
#         try:
#             serialized = json.dumps(obj, default=encoder, separators=(",", ":"), sort_keys=True)
#         except TypeError as ex:
#             log.error("Cannot serialize object: %r", obj)
#             if strict:
#                 raise ex
#             else:
#                 continue
#         yield serialized, obj  # return only serialized without obj???


# 4
# Поясняющий комментарий о возвращаемом адресе
# def get_server_ip():
#     ip = config.web_app["hostip"]
#
#     if ip:
#         return ip
#
#     return socket.gethostbyname(socket.gethostname())  # get ip received current request


# 5
# Комментарий с усилением и пояснением нюансов в методе получения стектрейса исключения
# def full_stack():
#     try:
#         exc = sys.exc_info()[0]
#         stack = traceback.extract_stack()[:-1]  # last one would be full_stack()
#
#         # i.e. an exception is present
#         if exc is not None:
#             # remove call of full_stack, the printed exception
#             # will contain the caught exception caller instead
#             del stack[-1]
#
#         trc = 'Traceback (most recent call last):\n'
#         stackstr = trc + ''.join(traceback.format_list(stack))
#
#         if exc is not None:
#             stackstr += '  ' + traceback.format_exc().lstrip(trc)
#     except Exception:
#         stackstr = "Stack trace couldn't be received"
#
#     return stackstr


# 6
# Комментарий с описанием намерений при выполнении нестабильного кода
# def save_result():
#     sname = "/tmp/screenshot-{}.png".format(request.node.name)
#     page.driver.save_screenshot(sname)
#     allure.attach.file(sname, attachment_type=allure.attachment_type.PNG)
#     with connection.sudo():
#         r = connection.run("cat /opt/program_special_path/log/main.log")
#         allure.attach(r.stdout, name="main.log", attachment_type=allure.attachment_type.TEXT)
#     # here we're trying to get the whole page screenshot, but it should be investigated
#     html = page.driver.find_element_by_tag_name("html")
#     sname = "screenshot-{}.png".format(request.node.name)
#     html.screenshot(sname)


# 7
# Описание намерений при выполнении потенциально проблемного блока кода

# try:
#     # пытаемся найти кнопку логаута, если нашли, значит мы уже авторизованы
#     page.find_element((By.XPATH, '//a[@href="/auth/logout"]'), time=1)
#     return page
# except TimeoutException:
#     # если не нашли, то мы на стр авторизации
#     user = page.find_element((By.ID, 'username'))
#     user.send_keys("admin")
#     password = page.find_element((By.ID, 'password'))
#     password.send_keys("admin")
#     sign_in = page.find_element((By.TAG_NAME, 'button'))
#     sign_in.click()
#     return page


# 8
# Поясняющие комментарии использования команд библиотеки cv2
# import cv2
# # read image to be resized by imread() function of openCV library
# img = cv2.imread('input.jpg')
# # set the ratio of resized image
# k = 5
# width = int((img.shape[1])/k)
# height = int((img.shape[0])/k)
#
# # resize the image by resize() function of openCV library
# scaled = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)


# 9
# Поясняющие комментарии для списка и словаря, а также усиление на том факте,
# что файл будет удален при наличии ключа в словаре
# # Dictionary to store the hash and filename
# hashMap = {}
#
# # List to store deleted files
# deletedFiles = []
# filelist = [f for f in os.listdir() if os.path.isfile(f)]
# for f in filelist:
#     key = hashFile(f)
#     # If key already exists, it deletes the file
#     if key in hashMap.keys():
#         deletedFiles.append(f)
#         os.remove(f)
#     else:
#         hashMap[key] = f


# 10
# комментарий с заметкой сделать в будущем
# class PersonProxySchema(BaseSchema):
#     class Meta(BaseSchema.Meta):
#         model = models.PersonProxy
#
#     # TODO schema validation method should be added in the class


# 11
# комментарий с заметкой сделать в будущем
# def storage_iterator(path: str) -> t.Iterator[t.Tuple[str, str]]:
#     rx = re.compile("^[0-9a-f]{2,28}$")
#
#     for dirname, dirs, files in os.walk(path):
#         dirs[:] = filter(lambda d: rx.search(d), dirs)
#         if dirs:
#             continue
#         # TODO: refactor to remove empty hash entries
#         basename = os.path.basename(dirname)
#         if len(basename) < 28:
#             continue
#
#         yield dirname, basename


# 12
# комментарий с заметкой сделать в будущем
# @pytest.fixture(scope="session")
# def driver_path(request):
#     # TODO make chrome support also
#     return os.environ.get("GECKODRIVER_BIN", "/usr/local/bin/geckodriver")
