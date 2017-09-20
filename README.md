Запуск
======

    pip3 install -rrequirements.txt
    CHECKER_KEY_FILENAME=<filename> FLASK_APP=flag_decoder flask run --host=0.0.0.0 --port=<port>

API
======

* **/flag**. Раскодирует переданную ему капсулу и возвращает флаг.

  При GET-запросе текст капсулы берётся из GET-параметра capsule, при POST-запросе — из тела запроса.

  Результат — код 200 и текст флага или код 400 и сообщение об ошибке.