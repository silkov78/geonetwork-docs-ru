# Сборщики данных

Работа с данными становится интереснее, когда несколько каталогов и служб совместно используют свои ресурсы.

Сбор данных (харвестинг) — это процесс получения метаданных из удаленных источников и их последующего сохранения в локальном каталоге для быстрого поиска.

!!! warning "Важно"
    Локальная копия метаданных синхронизируется с удаленными метаданными. При изменении метаданных на удалённом источники будут изменяться метаданные и в локальном.

Cбор данных возможен со следующих источников:

- [Сборщик данных GeoNetwork 2.0](harvesting-geonetwork.md)
- [Сбор данных из CSW-сервисов](harvesting-csw.md)
- [Сбор данных из OGC-сервисов](harvesting-ogcwxs.md)
- [Простой сбор по URL (opendata)](harvesting-simpleurl.md)
- [Сбор данных из локальной файловой системы](harvesting-filesystem.md)
- [Сбор данных по протоколу WEBDAV](harvesting-webdav.md)
- [Сбор данных по протоколу OAI-PMH](harvesting-oaipmh.md)
- [Сбор данных с узла ARCSDE](harvesting-sde.md)
- [Сбор данных по GeoPortal REST](harvesting-geoportal.md)
- [Сбор данных с THREDDS](harvesting-thredds.md)
- [Сбор данных по WFS GetFeature](harvesting-wfs-features.md)

## Обзор механизма сбора данных

Важная часть механизма сбора данных - идентификатор `UUID (universally unique identifier)`. 
Этот идентификатор уникален не только для локального каталога, который его сгенерировал, но и глобально. Он представляет собой комбинацию:

- MAC-адреса сетевого интерфейса,
- текущей даты/времени
- и случайного числа.

Для каждой новой записи генерируется и назначается свой UUID.

Вторая важная часть сбора данных — «дата последнего изменения». Каждый раз, в запись метаданных вносятся изменения, дата последнего изменения обновляется. 
Простое сохранение этого параметра и сравнение его с новым позволяет любой системе узнать, была ли изменена запись метаданных с момента последнего обновления.

Эти две концепции позволяют каталогам извлекать удаленные метаданные, проверять, были ли они обновлены, и удалять их локально, если они были удалены удаленно. 
UUID также позволяет осуществлять сбор данных между каталогами в случае, если каталог B собирает данные из каталога C, а каталог A собирает данные из каталога B.

## Жизненный цикл сбора данных

Метаданные, полученные с помощью сборщик, извлекаются и сохраняются локально во время первого запуска сборщика. 
Для некоторых сборщиков данных после первого запуска будут извлечены только измененные метаданные.

Собранные метаданные (по умолчанию) не подлежат редактированию по следующим причинам:

1. Сбор данных является периодическим, поэтому любые локальные изменения собранных метаданных будут потеряны во время следующего запуска.
2. Дата изменения используется для отслеживания изменений, поэтому если метаданные будут изменены, механизм сбора данных может быть сломан.

Поэтому при попытке обновить свойства метаданных (такие как категории, права доступа и т. д.), 
при следующем запуске сборщика свойства метаданных будут снова скопированы с удалённого сервера.

!!! Примечание

    Если пользователь по каким-то причинам намерен редактировать собранные записи метаданных и его не беспокоят возможные проблемы, описанные выше, 
    существует настройка, которая позволит это сделать. См. [Импорт метаданных](../../administrator-guide/configuring-the-catalog/system-configuration.md#editing_harvested_records) для получения более подробной информации.

    Альтернативный вариант — добавить собранные записи в локальный каталог, а затем их изменить. 
    На данный момент ни один интерфейс не позволяет изменять исходный каталог записи.


Процесс сбора продолжается до тех пор, пока не возникнет одна из следующих ситуаций:

1. Администратор останавливает (деактивирует) сборщик.
2. Возникает исключение. В этом случае сборщик автоматически останавливается.

!!! Примечание
    При удалении сборщика удаляются все записи метаданных, связанные с этим сборщиком.

## Множественный сбор и иерархии

Информация из каталогов, использующие UUID для идентификации записей метаданных (например GeoNetwork), 
может собираться несколько раз без необходимости заботиться о конфликтах при синхронизации метаданных.

В качестве примера можно рассмотреть следующий сценарий сбора метаданных:

1. Узел (A) создал метаданные (a)
2. Узел (B) собирает (a) из (A)
3. Узел (C) собирает (a) из (B)
4. Узел (D) собирает из (A), (B) и (C)

В этом сценарии узел (D) получит одни и те же метаданные (a) из всех 3 узлов (A), (B), (C). 
Метаданные будут передаваться в (D) по 3 разным путям, но благодаря его UUID будет сохранена только одна копия. 
Когда (a) изменяется в (A), новая версия перейдет в (D), но благодаря дате изменения копия в (D) будет обновлена до самой последней версией.

## Сбор фрагментов метаданных для повторного использования {#harvesting_fragments}

Все сборщики, за исключением THREDDS и OGC WFS GetFeature, создают полную запись метаданных, которая вставляется в существующую запись в каталоге или заменяет ее. 
Однако часто бывает так, что:

-    метаданные, собранные из внешнего источника, на самом деле представляют собой только один или несколько фрагментов метаданных, необходимых для описания ресурса
-    возможна необходимость объединения собранных фрагментов метаданных в одну запись
-    фрагмент метаданных, собранный из внешнего источника, может потребоваться в более чем одной записи метаданных

Например, пользователя может интересовать только сбор информации о контактной информации из внешнего источника. 
В таком случаем пользователя может захотеть повторное использование контактной информации для человека или организации в более чем одной записи метаданных.

Для поддержки этой возможности *сборщик данных WFS GetFeature* и *сборщик данных THREDDS* позволяют собирать фрагменты метаданных 
и связывать их в запись шаблона для создания записей метаданных. Фрагменты, которые сохраняются в базе данных GeoNetwork, 
называются **подшаблонами** и могут использоваться в более чем одной записи метаданных.

Как показано выше, примером фрагмента метаданных является элемент gmd:contactInfo документа iso19139. 
Этот элемент содержит контактные данные для лица или организации. Если фрагмент хранится в базе данных GeoNetwork как подшаблон для данного лица или организации, 
то на этот фрагмент можно ссылаться в записях метаданных, где эта организация или лицо указаны с помощью механизма связывания XML, называемого XLink.

## Поддержка HTTPS

Сбор данных между узлами GeoNetwork может потребовать протокол HTTPS. 
При сборе данных по https GeoNetwork-серверу потребуется доверенный сертификат в хранилище ключей JVM, доступный узлу GeoNetwork, выполняющему сбор данных.

Если доверенный сертификат в хранилище ключей JVM отсутствует, сборщик данных может выдать исключение, подобное этому, при попытке сбора данных с https-GeoNetwork:

``` text
javax.net.ssl.SSLHandshakeException:
   sun.security.validator.ValidatorException: PKIX path building failed:
   sun.security.provider.certpath.SunCertPathBuilderException:
   unable to find valid certification path to requested target

Caused by: sun.security.validator.ValidatorException:
   PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException:
   unable to find valid certification path to requested target

Caused by: sun.security.provider.certpath.SunCertPathBuilderException:
   unable to find valid certification path to requested target
```

Сертификат сервера для GeoNetwork, который собирается, 
необходимо добавить в хранилище ключей JVM с помощью [keytool](https://docs.oracle.com/en/java/javase/11/tools/keytool.html), чтобы он был доверенным.

Альтернативный способ добавить сертификат — использовать скрипт вроде:

``` bash
## JAVA SSL Certificate import script
## Based on original MacOs script by LouiSe@louise.hu : http://louise.hu
##
## Usage: ./ssl_key_import.sh <sitename> <port>
##
## Example: ./ssl_key_import.sh mail.google.com 443 (to read certificate from https://mail.google.com)

## Compile and start
javac InstallCert.java
java InstallCert $1:$2

## Copy new cert into local JAVA keystore
echo "Please, enter administrator password:"
sudo cp jssecacerts $JAVA_HOME/jre/lib/security/jssecacerts
# Comment previous line and uncomment next one for MacOs
#sudo cp jssecacerts /Library/Java/Home/lib/security/
```

Для использования скрипта необходимо установить компилятор Java и загрузить файл [InstallCert.java](https://github.com/escline/InstallCert) и поместить его в тот же каталог, что и скрипт.

Скрипт добавит сертификат в хранилище ключей JVM, если запустить его следующим образом::

    $ ./ssl_key_import.sh https_server_name 443

## Главная страница

Чтобы получить доступ к главной странице сбора данных (харвестинга), необходимо войти в систему как администратор. 
Чтобы открыть окно по управлению сборщиков данных, нужно выбрать `Администрирование` - `Сборщики данных`.

На странице отображается список текущих сборщиков и набор кнопок для управления. Значение каждого столбца в списке харвестеров следующее:

1. *Выбрать* Флажок для выбора одного или нескольких сборщиков. Выбранные сборщики будут затронуты первым рядом кнопок (активировать, деактивировать, запустить, удалить). Например, если выберать три сборщика и нажить кнопку Удалить, они все будут удалены.
2. *Имя* Это имя сборщика, заданное администратором.
3. *Тип* Тип сборщика (например, GeoNetwork, WebDAV и т. д.\...).
4. *Статус* Значок, показывающий текущий статус. См. [Значки статуса и ошибок сбора данных](index.md#admin_harvesting_status) для различных значков и описаний состояний.
5. *Ошибки* Значок, показывающий результат последнего запуска сбора данных, который мог быть успешным или нет. См. [Значки статуса и ошибок сбоар данных](index.md#admin_harvesting_status) для различных значков и описаний ошибок. Наведение курсора на значок покажет подробную информацию о последнем запуске сбора данных.
6. *Запуск в* и *Каждый*: Планирование запусков сбора данных. По сути, время дня + количество часов между повторениями и в какие дни будет работать сборщик.
7. *Последний запуск* Дата в формате ISO 8601 самого последнего запуска сбора данных.
8. *Операция* Список кнопок/ссылок на операции для сборщика.
   - Выбор *Редактировать* позволит вам изменить параметры для харвестера.
   - Выбор *Клонировать* позволит вам создать клон этого сборщика и начать редактировать данные клона.
   - Выбор *История* позволит вам просмотреть/изменить историю сбора данных для сборщика - см. [История сбора данных](index.md#harvest_history).

Внизу списка сборщиков находятся два ряда кнопок. Первый ряд содержит кнопки, которые могут работать с выбранным набором сборщиков. 
С помощью флажка в столбце «Выбрать» можно выбрать сборщики для какого-то действия.
А затем нажать одну из этих кнопок. Когда кнопка закончит свое действие, флажки будут сняты. Вот значение каждой кнопки:

1. *Активировать* Когда создается новый харвестер, его статус *неактивен*. Используйте эту кнопку, чтобы сделать его *активным* и запустить харвестер(ы) в соответствии с расписанием, которое он/они настроили для использования.
2. *Деактивировать* Останавливает харвестер(ы). Примечание: это не означает, что текущий запущенный харвестер(ы) будет остановлен. Вместо этого это означает, что харвестер(ы) не будет запланирован для повторного запуска.
3. *Запустить* Немедленно запустить выбранные харвестеры. Это полезно для тестирования настроек харвестера.
4. *Удалить* Удалить все выбранные в данный момент харвестеры. Диалоговое окно попросит пользователя подтвердить действие.

Вторая строка содержит кнопки общего назначения. Вот значение каждой кнопки:

1. *Назад* Просто возвращает на главную страницу администрирования.
2. *Добавить* Эта кнопка создает новый харвестер.
3. *Обновить* Обновляет текущий список харвестеров с сервера. Это может быть полезно, чтобы увидеть, был ли список харвестеров изменен кем-то другим, или получить статус запущенных харвестеров.
4. *История* Показывает историю харвестеров всех харвестеров. Подробнее см. [История харвестеров](index.md#harvest_history).

## Значки статуса и ошибок сбора данных {#admin_harvesting_status}

## Результаты сбора данных

Когда сбор данных запускается и завершается, в столбце **Ошибки** для сбора данных отображаются подсказки с подробной информацией о процессе сбора данных. 
Если сбор данных прошел успешно, то при наведении курсора на подсказку будет показана таблица, в которой некоторые строки будут помечены следующим образом:

- **Всего** — это общее количество метаданных найденных, найденных на удалённом источнике. Метаданные с одинаковым идентификатором считаются одним.
- **Добавлено** — количество метаданных, добавленных в систему, поскольку они отсутствовали локально.
- **Удалено** — количество удаленных локально метаданных, поскольку их больше нет на сервере, с которого собираются данные.
- **Обновлено** — количество локально присутствующих метаданных, которые необходимо обновить, поскольку дата их последнего изменения отличалась от удаленной.
- **Не изменено** — локальные метаданные остались без изменений. Их дата последнего изменения на удаленном сервере не изменилась.
- **Неизвестная схема** - Количество пропущенных метаданных, поскольку их формат не был распознан GeoNetwork.
- **Неизвлекаемые** - Количество метаданных, которые были готовы к извлечению с удаленного сервера, но по какой-то причине возникло исключение во время процесса передачи данных.
- **Неправильный формат** - Количество пропущенных метаданных, поскольку у них не было допустимого представления XML.
- **Не проверяется** - Количество метаданных, которые не прошли проверку по своей схеме. Эти метаданные были успешно собраны, но пропущены из-за процесса проверки. Обычно есть возможность принудительной проверки: если вы все равно хотите собрать эти метаданные, просто отключите/не трогайте ее.
- **Миниатюры/Миниатюры ошибка** - Количество добавленных/не добавленных из-за какой-то ошибки миниатюр метаданных.
- **Использованный атрибут URL метаданных** - Количество слоев/типов объектов/покрытий, которые имели URL метаданных, который можно было использовать для ссылки на запись метаданных (только OGC Service Harvester).
- **Добавленные службы** - Количество записей служб ISO19119, созданных и добавленных в каталог (только для сбора каталога THREDDS).
- **Добавленные коллекции** - Количество записей наборов данных коллекций, добавленных в каталог (только для сбора каталога THREDDS).
- **Atomics добавлено** – количество записей набора данных АТОМ, добавленных в каталог (только для сбора каталога THREDDS).
- **Добавленные подшаблоны** - Количество подшаблонов (= фрагмент, видимый в каталоге), добавленных в каталог метаданных.
- **Удаленные подшаблоны** - Количество подшаблонов (= фрагмент, видимый в каталоге), удаленных из каталога метаданных.
- **Фрагменты с неизвестной схемой** - Количество фрагментов с неизвестной схемой метаданных.
- **Возвращено фрагментов** - Количество фрагментов, возвращенных сборщиком.
- **Совпавших фрагментов** - Количество фрагментов, имеющих идентификаторы, которые в шаблоне использовались сборщиком.
- **Существующие наборы данных** - Количество записей метаданных для наборов данных, которые существовали при запуске сборщика THREDDS.
- **Создано записей** - Количество записей, созданных сборщиком из шаблона и фрагментов.
- **Не удалось вставить** - Количество записей, которые сборщик не смог вставить в каталог (обычно потому, что запись уже присутствовала, например, в сборщике Z3950 это может произойти, если одна и та же запись собирается с разных серверов).

## Добавление новых сборщиков

Кнопка `Собрать из` на главной странице позволяет добавлять новые сборщики. Затем отображается раскрывающийся список со всеми доступными протоколами и типами сборщиков.

Пользователь может выбрать тип сбора, который он собирается выполнить. Поддерживаемые харвестеры и их особенности приведены в последующих разделах.

## История сбора данных {#harvest_history}

Каждый раз, когда запускается харвестер, он генерирует отчет о состоянии того, что было собрано и что пошло не так. 
Эти отчеты хранятся в таблице в базе данных, используемой GeoNetwork.
История для отдельного харвестера также можно вызвать с помощью вкладки `История сборщика`, открыв информацию о конкретном сборщике.

После отображения истории сбора данных можно:

- развернуть детали любых исключений и ошибок
- отсортировать историю по дате сбора (или в случае истории всех харвестеров по имени харвестера)
- удалить любую запись истории или всю историю
