# Налада базы даных {#configuring-database}

## Уводзіны

GeoNetwork выкарыстоўвае базу даных для захоўвання такіх аспектаў, як запісы метаданых, прывілеі і канфігурацыі. Структура базы даных па змаўчанні ствараецца дадаткам пры першым запуску. Наступныя выпускі GeoNetwork будуць аўтаматычна абнаўляць структуру базы даных. Па гэтай прычыне карыстальніку базы даных першапачаткова неабходны правы на стварэнне аб'ектаў у базе даных. Падтрымліваецца шэраг дыялектаў баз даных: ***H2***, ***PostgreSQL***, ***PostGIS***, ***Oracle***, ***SQL Server***. У гэтым раздзеле апісаны розныя варыянты налады падключэння да базы даных.

## База даных H2

Па змаўчанні пры першым запуску прыкладання наладжваецца і ствараецца база даных [H2](https://www.h2database.com/html/main.html). База даных H2 з імем `gn.h2.db` ствараецца:

-   У тэчцы **`jetty`** ўнутры тэчкі прыкладання GeoNetwork пры выкарыстанні [ZIP-дыстрыбутыва](installing-from-zip.md).
-   У тэчцы **`bin`** сервера Tomcat пры разгортванні [WAR-файла](installing-from-war-file.md) у Tomcat (запуск праз `startup.sh`).

!!! note

    Вам **не трэба** наладжваць базу даных, калі вас задавальняе лакальная база даных H2. Змяняйце канфігурацыю толькі ў тым выпадку, калі вы хочаце захоўваць даныя ў аддаленай базе даных.


## Налада базы даных праз файлы канфігурацыі

Дыялект базы даных наладжваецца ў файле **`/WEB-INF/config-node/srv.xml`**. Раскаментаванайце выкарыстоўваны дыялект.

Драйвер JDBC уключаны для PostgreSQL, Oracle і H2. Для іншых дыялектаў патрабуецца ўстаноўка драйвера JDBC. Загрузіце бібліятэку JDBC для патрэбнага дыялекту і змесціце яе ў `/WEB-INF/lib` ці ў тэчку бібліятэк Tomcat або GeoNetwork.

Каб абнавіць параметры падключэння, змяніце файл **`WEB-INF/config-db/jdbc.properties`**, пазначыўшы адпаведную інфармацыю аб падключэнні.

GeoNetwork мяркуе, што даныя захоўваюцца ў схеме па змаўчанні для карыстальніка. Калі гэта не так, вам неабходна актываваць наладу `hibernate.default_schema` у файле **`/WEB-INF/config-spring-geonetwork.xml`**. Існуюць скрыпты, якія выконваюцца непасрэдна ў базе даных пры ініцыялізацыі і не могуць выкарыстоўваць параметр `hibernate.default-schema`. Для гэтых скрыптоў неабходна задаць схему па змаўчанні ўручную. У PostgreSQL гэта магчыма шляхам дадання `?currentSchema=example` да радка падключэння да базы даных.

## Налада базы даных праз JNDI

Java Naming and Directory Interface (JNDI) — гэта тэхналогія, якая дазваляе наладзіць базу даных у Tomcat і спасылацца на JNDI-злучэнне па імені.

1.  Каб актываваць JNDI, неабходна актываваць тып базы даных JNDI у **`/WEB-INF/config-node/srv.xml`**.

2.  Наладзьце JNDI-злучэнне ў Tomcat, дадаўшы новы рэсурс у **`TOMCAT/conf/context.xml`**. Для Jetty — у **`WEB-INF/jetty-env.xml`**.

    ``` xml
    <Resource name="geonetwork"
        type="javax.sql.DataSource"
        driverClassName="org.postgresql.Driver"
        url="jdbc:postgresql://localhost:5432/geonetwork"
        username="xxxxx" password="xxxxxx"
        maxActive="20"
        />
    ```

## Налада базы даных праз пераменныя асяроддзя

Устаноўка параметраў канфігурацыі праз пераменныя асяроддзя з'яўляецца распаўсюджанай практыкай у кантэйнерных асяроддзях, такіх як Docker. Існуе два варыянты:

1.  Дадайце параметры непасрэдна ў асяроддзе Java, замяніўшы JAVA_OPTS.

    ``` text
    docker run --rm --name gn -p 8080:8080 -e JAVA_OPTS=" 
        -Dgeonetwork.db.type=postgres 
        -Djdbc.database=example 
        -Djdbc.username=example
        -Djdbc.password=xxx
        -Djdbc.host=localhost
        -Djdbc.port=5432" geonetwork:latest
    ```

2.  Усталюйце дакладную пераменную асяроддзя, уключаючы сімвал «.». Многія параметры канфігурацыі GeoNetwork утрымліваюць кропку, што з'яўляецца праблемай пры падстаноўцы праз пераменныя асяроддзя. Docker з'яўляецца выключэннем, ён дае механізм, які дазваляе выкарыстоўваць кропкі ў пераменных асяроддзя.

    ``` text
    docker run --rm --name gn -p 8080:8080
        -e geonetwork.db.type=postgres 
        -e jdbc.database=example 
        -e jdbc.username=example
        -e jdbc.password=xxx
        -e jdbc.host=localhost
        -e jdbc.port=5432 geonetwork:latest
    ```

Для PostgreSQL можна наладзіць тры значэнні `geonetwork.db.type`:

- `postgres`: (і для іншых дыялектаў баз даных) для захоўвання прасторавага ахопу метаданых ствараецца Shape-файл.
- `postgres-postgis`: GeoNetwork будзе выкарыстоўваць прасторавыя магчымасці PostGIS для фільтрацыі метаданых.
- `postgres-postgis-hikari`: Усе магчымасці PostGIS з выкарыстаннем Hikari «паверх» для забеспячэння кіравання злучэннямі, больш адаптаванага для Postgres.

Пры выбары паміж postgres-postgis і postgres-postgis-hikari рэкамендуецца postgres-postgis-hikari: ён заснаваны на пуле злучэнняў Hikari, які забяспечвае лепшае кіраванне злучэннямі пры выкарыстанні 'connectionTestQuery' замест 'validationQuery' па змаўчанні ў defaultJdbcDataSource.

## Журналяванне (Logging)

Каб убачыць больш дэталяў аб падключэнні да базы даных і запытах, узровень журнала можна пераключыць на DEBUG у `web/src/main/webapp/WEB-INF/classes/log4j.xml` (або гл. [Сервер каталога](../administrator-guide/configuring-the-catalog/system-configuration.md#system-config-server) --> Узровень журнала).

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

## Рэзюмэ

Існуе некалькі спосабаў налады базы даных у GeoNetwork. JNDI і пераменныя асяроддзя з'яўляюцца пераважнымі, паколькі пры абнаўленні да новай версіі або змене базы даных вам не трэба змяняць файлы прыкладання.

Тыпы, якія падтрымліваюцца:

* db2
* h2 (па змаўчанні)
* jndi
* mysql
* oracle
* postgres
* postgres-postgis
* postgres-postgis-hikari
* sqlserver