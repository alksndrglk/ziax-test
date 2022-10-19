.. role:: shell(code)
   :language: shell

Как использовать?
=================
Как запустить REST API сервис локально на порту 8081:

.. code-block:: shell

    docker run -p 8081:8081 -e ANALYZER_API_KEY=ziax alksglk/text_analyzer

Все доступные опции запуска любой команды можно получить с помощью
аргумента :shell:`--help`:

.. code-block:: shell

    docker run alksglk/text_analyzer text_analyzer-api --help

Опции для запуска можно указывать как аргументами командной строки, так и
переменными окружения с префиксом :shell:`ANALYZER` 

.. code-block:: shell

    docker run -p 8081:8081 alksglk/text_analyzer text_analyzer-api --api-key ziax
    docker run -p 8081:8081 -e ANALYZER_API_KEY=ziax alksglk/text_analyzer

Разработка
==========

Быстрые команды
---------------
* :shell:`make` Отобразить список доступных команд
* :shell:`make devenv` Создать и настроить виртуальное окружение для разработки
* :shell:`make lint` Проверить синтаксис и стиль кода с помощью `pylint`
* :shell:`make mypy` Проверить стиль кода с помощью `mypy`
* :shell:`make clean` Удалить кеш и, файлы созданные модулем `distutils`
* :shell:`make test` Запустить тесты
* :shell:`make sdist` Создать `source distribution`
* :shell:`make docker` Собрать Docker-образ
* :shell:`make upload` Загрузить Docker-образ на hub.docker.com

Подготовить окружение для разработки и запустить локально
------------------
.. code-block:: shell

    make devenv
    . env/bin/activate
    text_analyzer-api --api-key ziax

Запустить тесты локально
------------------
.. code-block:: shell
    
    make devenv
    . env/bin/activate
    make test
