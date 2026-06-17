# Настройка базы данных {#configuring-database}

## Введение

GeoNetwork использует базу данных для хранения таких аспектов, как записи метаданных, привилегии и конфигурации. Структура базы данных по умолчанию создается приложением при первом запуске. Последующие выпуски GeoNetwork будут автоматически обновлять структуру базы данных. По этой причине пользователю базы данных изначально необходимы права на создание объектов в базе данных. Поддерживается ряд диалектов баз данных: ***H2***, ***PostgreSQL***, ***PostGIS***, ***Oracle***, ***SQL Server***. В этом разделе описаны различные варианты настройки подключения к базе данных.

## База данных H2

По умолчанию при первом запуске приложения настраивается и создается база данных [H2](https://www.h2database.com/html/main.html). База данных H2 с именем `gn.h2.db` создается:

-   В папке **`jetty`** внутри папки приложения GeoNetwork при использовании [ZIP-дистрибутива](installing-from-zip.md).
-   В папке **`bin`** сервера Tomcat при развертывании [WAR-файла](installing-from-war-file.md) в Tomcat (запуск через `startup.sh`).

!!! note

    Вам **не нужно** настраивать базу данных, если вас устраивает локальная база данных H2. Меняйте конфигурацию только в том случае, если вы хотите хранить данные в удаленной базе данных.


## Настройка базы данных через файлы конфигурации

Диалект базы данных настраивается в файле **`/WEB-INF/config-node/srv.xml`**. Раскомментируйте используемый диалект.

Драйвер JDBC включен для PostgreSQL, Oracle и H2. Для других диалектов требуется установка драйвера JDBC. Загрузите библиотеку JDBC для нужного диалекта и поместите ее в `/WEB-INF/lib` или в папку библиотек Tomcat или GeoNetwork.

Чтобы обновить параметры подключения, измените файл **`WEB-INF/config-db/jdbc.properties`**, указав соответствующую информацию о подключении.

GeoNetwork предполагает, что данные хранятся в схеме по умолчанию для пользователя. Если это не так, вам необходимо активировать настройку `hibernate.default_schema` в файле **`/WEB-INF/config-spring-geonetwork.xml`**. Существуют скрипты, которые выполняются непосредственно в базе данных при инициализации и не могут использовать параметр `hibernate.default-schema`. Для этих скриптов необходимо задать схему по умолчанию вручную. В PostgreSQL это возможно путем добавления `?currentSchema=example` к строке подключения к базе данных.

## Настройка базы данных через JNDI

Java Naming and Directory Interface (JNDI) — это технология, которая позволяет настроить базу данных в Tomcat и ссылаться на JNDI-соединение по имени.

1.  Чтобы активировать JNDI, необходимо активировать тип базы данных JNDI в **`/WEB-INF/config-node/srv.xml`**.

2.  Настройте JNDI-соединение в Tomcat, добавив новый ресурс в **`TOMCAT/conf/context.xml`**. Для Jetty — в **`WEB-INF/jetty-env.xml`**.

    ``` xml
    <Resource name="geonetwork"
        type="javax.sql.DataSource"
        driverClassName="org.postgresql.Driver"
        url="jdbc:postgresql://localhost:5432/geonetwork"
        username="xxxxx" password="xxxxxx"
        maxActive="20"
        />
    ```

## Настройка базы данных через переменные окружения

Установка параметров конфигурации через переменные окружения является распространенной практикой в контейнерных средах, таких как Docker. Существует два варианта:

1.  Добавьте параметры непосредственно в среду Java, заменив JAVA_OPTS.

    ``` text
    docker run --rm --name gn -p 8080:8080 -e JAVA_OPTS=" 
        -Dgeonetwork.db.type=postgres 
        -Djdbc.database=example 
        -Djdbc.username=example
        -Djdbc.password=xxx
        -Djdbc.host=localhost
        -Djdbc.port=5432" geonetwork:latest
    ```

2.  Установите точную переменную окружения, включая символ «.». Многие параметры конфигурации GeoNetwork содержат точку, что является проблемой при подстановке через переменные окружения. Docker является исключением, он предоставляет механизм, позволяющий использовать точки в переменных окружения.

    ``` text
    docker run --rm --name gn -p 8080:8080
        -e geonetwork.db.type=postgres 
        -e jdbc.database=example 
        -e jdbc.username=example
        -e jdbc.password=xxx
        -e jdbc.host=localhost
        -e jdbc.port=5432 geonetwork:latest
    ```

Для PostgreSQL можно настроить три значения `geonetwork.db.type`:

- `postgres`: (и для других диалектов баз данных) для хранения пространственного охвата метаданных создается Shape-файл.
- `postgres-postgis`: GeoNetwork будет использовать пространственные возможности PostGIS для фильтрации метаданных.
- `postgres-postgis-hikari`: Все возможности PostGIS с использованием Hikari «поверх» для обеспечения управления соединениями, более адаптированного для Postgres.

При выборе между postgres-postgis и postgres-postgis-hikari рекомендуется postgres-postgis-hikari: он основан на пуле соединений Hikari, который обеспечивает лучшее управление соединениями при использовании 'connectionTestQuery' вместо 'validationQuery' по умолчанию в defaultJdbcDataSource.

## Журналирование (Logging)

Чтобы увидеть больше деталей о подключении к базе данных и запросах, уровень журнала можно переключить на DEBUG в `web/src/main/webapp/WEB-INF/classes/log4j.xml` (или см. [Сервер каталога](../administrator-guide/configuring-the-catalog/system-configuration.md#system-config-server) --> Уровень журнала).

``` xml
<logger name="org.hibernate.SQL" additivity="false">
    <level value="DEBUG" />
    <appender-ref ref="consoleAppender" />
    <appender-ref ref="fileAppender" />
</logger>
<logger name="org.hibernate.type" additivity="false">
    <level value="DEBUG" />
    <appender-ref ref="consoleAppender" />
    <appender-ref ref="fileAppender" />
</logger>
<logger name="org.hibernate.tool.hbm2ddl" additivity="false">
    <level value="DEBUG" />
    <appender-ref ref="consoleAppender" />
    <appender-ref ref="fileAppender" />
</logger>
```

## Резюме

Существует несколько способов настройки базы данных в GeoNetwork. JNDI и переменные окружения являются предпочтительными, поскольку при обновлении до новой версии или смене базы данных вам не нужно менять файлы приложения.

Поддерживаемые типы:

* db2
* h2 (по умолчанию)
* jndi
* mysql
* oracle
* postgres
* postgres-postgis
* postgres-postgis-hikari
* sqlserver