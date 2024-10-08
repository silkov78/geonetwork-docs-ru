# Сбор данных по протоколу GeoPortal REST {#geoportal_rest_harvester}

Этот сборщик данных подключится к удаленному серверу GeoPortal версии 9.3.x или 10.x и извлечет записи метаданных, которые соответствуют параметрам запроса, указанным с помощью GeoPortal REST API.

## Добавление сборщика данных GeoPortal REST
Нажмите `Собрать из` - `Geoportal REST`, чтобы создать сборщика метаданных по протоколу `Geoportal REST`. Доступные параметры следующие:

-   **Идентификация** - параметры собранных данных в каталоге GeoNetwork.
    -    *Имя* - Это краткое описание удаленного сайта. Оно будет показано на главной странице сбора в качестве имени для этого экземпляра CSW-харвестера.
    -    *Выбор логотипа* - Логотип будет использоваться при отображении собранных записей метаданных в результатах поиска.
    -    *Группа* - Группа, в которой разместятся собираемые метаданные.
    -    *Пользователь* - Пользователь, который будет владельцем собранных метаданных.
-   **Расписание** - Параметры расписания, согласно которым сборщик будет собирать метаданные.
    -    *Частота* - Частота (периодичность) запуска сбора метаданных харвестером.
    -    *Только один запуск* - Сборщик будет запущен только один раз, если выбран пункт.
-   **Настроить подключение** - параметры подключения к CSW-серверу.
    -    *URL сервиса* - URL CSW с параметрами GetCapabilities или без них. Например, <http://geonetwork-site.com/srv/eng/csw?service=CSW&request=GetCabilities&version=2.0.2>.
    -    *Удалённая аутентификация* - Учетные данные для базовой HTTP-аутентификации на сервере CSW (Логин и Пароль).
-   **Фильтр поиска** - Пользователь может запросить любое поле на сервере GeoPortal, используя синтаксис запроса Lucene, описанный на странице <http://webhelp.esri.com/geoportal_extension/9.3.1/index.htm#srch_lucene.htm>.
-   **Параметры поиска** - специфические параметры сбора для этого харвестера.
    -    *Сортировка по* - Определение порядка сортировки для запроса GetRecords. Это может решить проблему для больших наборов, когда некоторые записи могут измениться на удаленном узле во время сбора данных и вернуться на разных страницах. Сортировка A - это UUID в алфавитном порядке.
    -    *Выходная схема* - Идентификатор URI запрошенного с CSW сервера стандарта метаданных. Сервер должен поддерживать этот стандарт. Поддерживаемые стандарты перечислены в документе CSW Capabilities в операции GetRecordById.
    -    *Распределенный поиск* - Распределенный поиск на удаленном сервере (если он это обеспечивает). Когда эта опция включена, удаленный каталог направляет поиск на настроенные удалённые CSW-серверы
-   **Правила слияния UUID** - Действие при дублировании UUID.
-   **Фильтрация и обработка ответа**
    -    *Проверка записей перед импортом* - Проверка записей перед импортом.
    -    *Поиск дубликатов ресурсов по идентификатору ресурса* - Сравнение выполнено по элементу 'gmd:identificationInfo/*/gmd:citation/gmd:CI_Citation/gmd:identifier/*/gmd:code/gco:CharacterString'. Оно применимо только к записям по ISO19139 или профилям ISO.
    -    *XPath фильтр* - Когда запись получена с удаленного сервера, проверьте выражение XPath, чтобы принять или отклонить запись. 
    -    *XSL-преобразование* - XSL-преобразование, которое будет применено к каждой записи перед добавлением в GeoNetwork.
    -    *Пакетное редактирование* - Пакетное обновление собираемых метаданных. Используется для добавления, замены или удаления элементов записей.
    -    *Категория для собранных записей* - Задать категорию собранным записям.
-   **Доступность для собранных записей** - Назначение привилегий определённым группам по собранным метаданным.
    -    *Если запись существует* - Применяется только при обновлении, и если при конфликте UUID предписано задано перезаписывать записи. Если включено, привилегии не удаляются при обновлении.

!!! Примечания

    - этот сборщик использует две службы REST из API GeoPortal:
    - `rest/find/document` с параметром searchText для возврата списка RSS записей метаданных, соответствующих критериям поиска (максимум 100000)
    - `rest/document` с параметром id из каждого результата, возвращенного в списке RSS
    - этот сборщик был протестирован с GeoPortal 9.3.x и 10.x. Его можно использовать вместо сборщика CSW, если есть проблемы с обработкой стандартов OGC и т. д.
    - обычно метаданные ISO19115, созданные программным обеспечением Geoportal, не будут иметь префикса 'gmd' для пространства имен `http://www.isotc211.org/2005/gmd`. GeoNetwork XSLT поймет эти метаданные, но не сможет сопоставить заголовки и списки кодов в средстве просмотра/редакторе. Чтобы устранить эту проблему, выберите `Добавить-gmd-префикс (Add-gmd-prefix)` и   `Применить этот XSLT к собранным записям` в наборе параметров **Собранный контент**, описанном ранее.