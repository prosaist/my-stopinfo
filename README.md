#### Моя остановка
Стоит ли ждать трамвай? В моём телефоне отключён мобильный интернет (дома, на работе и в транспорте мне достаточно Wi-Fi). Каждый рабочий день утром и вечером в определённое время я подхожу к трамвайной остановке и жду прибытия определённых трамваев. Если на путях ДТП или другая причина существенных задержек, я поеду на метро. Я хочу получать СМС с прогнозом времени прибытия трамваев на остановку. Эта задача решена на Python 3. Последовательность действий:
1. Зарегистрировался на сайте [sms.ru](https://sms.ru), указав ФИО, e-mail и номер телефона. После регистрации был создан api_id **(ключ для внешних программ)** вида 00000000-ABCD-ABCD-0000-000000000000. Номер своего телефона и полученный api_id нужно записать в файл params.json.
2. Установил [Yandex Transport Webdriver API](https://github.com/OwlSoul/YandexTransportWebdriverAPI-Python) `pip3 install yandex-transport-webdriver-api`
3. Скачал и установил [Docker Desktop](https://download.docker.com/win/stable/Docker%20Desktop%20Installer.exe).
 Установил [Yandex Transport Proxy](https://github.com/OwlSoul/YandexTransportProxy)
 `docker pull owlsoul/ytproxy:latest`
 Запустил докер-контейнер:
 `docker run -it -p 25555:25555 owlsoul/ytproxy:latest`
4. Открыл [Яндекс Карты](https://yandex.ru/maps/) в браузере, выбрал интересующую остановку и кликнул на неё. URL поменялся на https://yandex.ru/maps/213/moscow/stops/stop__9649649/?ll=37.656740%2C55.775324&z=19. Преобразовал URL к виду https://yandex.ru/maps/213/moscow/?masstransit[stopId]=stop__9649649&ll=37.656740%2C55.775324&z=19 и сохранил его в файле params.json. Интересующие меня номера трамваев записал в массив "tramways".
5. Отредактировал пути к python.exe и к mystopinfo.py в файле get.cmd.
6. Мой компьютер включён круглосуточно. В планировщике заданий создал два назначенных задания, указав триггер еженедельно с понедельника по пятницу в нужное время (утром и вечером) и действие C:\Users\user\Projects\my-stopinfo\get.cmd.

sms.ru может присылать до 5 сообщений в сутки бесплатно на зарегистрированный телефон. Если текущее время до 13:00, то информация присылается по первой остановке, иначе, по второй.

![Результат](https://drive.google.com/open?id=1EQlq008fF4E-lx73IT0e2IH7McmPRI91)




