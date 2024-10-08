# Сбор данных из ARCSDE-узла {#sde_harvester}

Это протокол сбора метаданных, хранящихся на сервере, где запущен [ArcSDE](https://en.wikipedia.org/wiki/ArcSDE).

## Добавление сборщика ArcSDE

Сборщик определяет формат метаданных ESRI: ESRI ISO, ESRI FGDC и затем применяет необходимые XSLT-преобразования метаданных в ISO19139. 


Комбайн определяет формат метаданных ESRI: ESRI ISO, ESRI FGDC, чтобы применить необходимые xslts для преобразования метаданных в ISO19139. Параметры конфигурации:

- **Идентификация**
    - *Имя* - Это краткое описание узла. Оно будет отображаться на главной странице сбора урожая.
    - *Группа* - Администратор этой группы и администратор каталога могут управлять этим узлом.
    - *Пользователь* - Пользователь, которому принадлежат собранные метаданные.
- **Расписание** - Конфигурация расписания для выполнения харвестера.
- **Конфигурация для протокола ArcSDE**
    - *Сервер* - IP-адрес или имя сервера ArcSde.
    - *Порт* - Порт службы ArcSde (обычно 5151) или порт базы данных ArcSde, в зависимости от выбранного типа соединения, см. ниже раздел *Тип соединения*.
    - *Имя базы данных* - имя экземпляра ArcSDE (обычно esri_sde).
    - *Версия ArcSde* - версия ArcSde для сбора данных. Модель данных, используемая ArcSde, отличается в зависимости от версии ArcSde.
    - *Тип соединения*
        - *ArcSde service* - Используется служба ArcSde для получения метаданных.

            !!! Примечание

                Для использования сборщика ArcSDE требуются дополнительные шаги по установке, так как он требует установки проприетарных библиотек ESRI Java api.
    
                Библиотеки ArcSDE Java API должны быть установлены пользователем в GeoNetwork (папка INSTALL_DIR_GEONETWORK/WEB-INF/lib), так как это проприетарные библиотеки, не распространяемые с GeoNetwork.
    
                Требуются следующие конфигурационные java-файлы:
    
                - jpe_sdk.jar
                - jsde_sdk.jar
    
                dummy-api-XXX.jar должен быть удален из INSTALL_DIR/web/geonetwork/WEB-INF/lib


        - *Прямое подключение к базе данных* - Использует подключение к базе данных (JDBC) для получения метаданных.

            !!! обратите внимание

                Прямое подключение к базе данных требует копирования драйверов JDBC в INSTALL_DIR_GEONETWORK/WEB-INF/lib.


            !!! примечание

                Драйверы JDBC для Postgres распространяются вместе с GeoNetwork, но не для Oracle или SqlServer.

    - *Тип базы данных* - Тип базы данных ArcSde: Oracle, Postgres, SqlServer. Доступно только в том случае, если тип соединения настроен на *Прямое соединение с базой данных*.
    - *Имя пользователя* - Имя пользователя для подключения к серверу ArcSDE.
    - *Пароль* - Пароль пользователя ArcSDE.

- **Дополнительные опции для протокола arcsde**
    - *Проверять записи перед импортом* - Определяет критерии для отклонения метаданных, которые являются недействительными в соответствии с правилами XSD и schematron.
        - Принимать все метаданные без проверки.
        - Принимать метаданные, которые являются XSD-действительными.
        - Принимать метаданные, которые являются XSD и schematron валидными.
- **Привилегии** - Назначение привилегий для собранных метаданных.