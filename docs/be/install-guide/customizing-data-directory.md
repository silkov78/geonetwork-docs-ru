# Настройка дырэкторыі даных {#customizing-data-directory}

Дырэкторыя даных — гэта месца ў файлавай сістэме, дзе каталог захоўвае большую частку сваіх карыстальніцкіх налад і файлаў, якія загружаюцца. Гэтая канфігурацыя вызначае такія параметры, як:

-   Які тэзаўрус выкарыстоўвае GeoNetwork?
-   Якая схема падключана ў GeoNetwork?

Дырэкторыя даных таксама змяшчае шэраг дапаможных файлаў, якія выкарыстоўваюцца каталогам для розных мэт:

-   канфігурацыя індэкса
-   лагатыпы
-   загружаныя дакументы, прымацаваныя да запісаў метаданых
-   мініяцюры

Рэкамендуецца вызначаць знешнюю дырэкторыю даных пры пераходзе да эксплуатацыі (production), каб спрасціць будучыя абнаўленні. Дырэкторыя даных дазваляе WAR-файлу працаваць у рэжыме «толькі для чытання» у выпадку неабходнасці.

## Стварэнне новай дырэкторыі даных

Дырэкторыю даных неабходна стварыць перад запускам каталога. Яна павінна быць даступнай для чытання і запісу карыстальніку, які запускае каталог.

Калі дырэкторыя даных з'яўляецца пустой папкай, каталог ініцыялізуе структуру дырэкторыі па змаўчанні, выкарыстоўваючы `INSTALL_DIR/web/geonetwork/WEB-INF/data`.

Калі дырэкторыя даных не зададзена, пры запуску праграмы ў логу адлюстроўваецца наступнае паведамленне:

``` shell
2015-12-16 07:59:17,108 WARN  [geonetwork.data.directory] -     - Data directory properties is not set. Use geonetwork.dir or geonetwork.dir properties.
2015-12-16 07:59:17,108 WARN  [geonetwork.data.directory] -     - Data directory provided could not be used. Using default location: /data/dev/gn/3.0.x/web/src/main/webapp/WEB-INF/data
```

Калі дырэкторыя даных недаступная для карыстальніка, у логу адлюстроўваецца:

``` shell
2015-12-16 08:09:17,723 WARN  [geonetwork.data.directory] -     - Data directory '/tmp/gndatadir' is not writable. Set read/write privileges to user starting the catalogue (i.e. francois).
2015-12-16 08:09:17,723 WARN  [geonetwork.data.directory] -     - Data directory provided could not be used. Using default location: /data/dev/gn/3.0.x/web/src/main/webapp/WEB-INF/data
```

## Устаноўка дырэкторыі даных

Пераменная дырэкторыі даных можа быць устаноўлена з дапамогай:

-   Пераменнай асяроддзя Java
-   Параметра кантэксту сервлета
-   Сістэмнай пераменнай асяроддзя
-   Канфігурацыі кампанентаў (Bean) (дададзена ў версіі 3.0.4)

Для пераменнай асяроддзя Java і параметра кантэксту сервлета выкарыстоўвайце:

-   <webappName>.dir і, калі не зададзена, выкарыстоўвайце geonetwork.dir

Для сістэмнай пераменнай асяроддзя выкарыстоўвайце:

-   <webappName>_dir і, калі не зададзена, выкарыстоўвайце geonetwork_dir

Парадак вырашэння (прыярытэтнасці):

1.  <webappname>.dir
    1.  Пераменная асяроддзя Java (напрыклад, -D<webappname>.dir=/a/data/dir)
    2.  Параметр кантэксту сервлета (напрыклад, web.xml)
    3.  Параметр appHandler у config.xml (напрыклад, config.xml)
    4.  Сістэмная пераменная асяроддзя (напрыклад, <webappname>_dir=/a/data/dir). Сімвал "." не падтрымліваецца ў пераменных асяроддзя
2.  geonetwork.dir
    1.  Пераменная асяроддзя Java (напрыклад, -Dgeonetwork.dir=/a/data/dir)
    2.  Параметр кантэксту сервлета (напрыклад, web.xml)
    3.  Параметр appHandler у config.xml (напрыклад, config.xml)
    4.  Сістэмная пераменная асяроддзя (напрыклад, geonetwork_dir=/a/data/dir). Сімвал "." не падтрымліваецца ў пераменных асяроддзя

## Сістэмная ўласцівасць Java

У залежнасці ад кантэйнера сервлетаў, які выкарыстоўваецца, таксама можна ўказаць размяшчэнне дырэкторыі даных з дапамогай сістэмнай уласцівасці Java.

Для Tomcat канфігурацыя выглядае так:

``` shell
CATALINA_OPTS="-Dgeonetwork.dir=/var/lib/geonetwork_data"
```

## Канфігурацыя кампанентаў (Bean)

!!! info "Версія дадання"

    3.0.4


Каб наладзіць дырэкторыю даных з дапамогай карыстальніцкай канфігурацыі кампанентаў, абнавіце кампанент GeonetworkDataDirectory ў `core/src/main/resources/config-spring-geonetwork.xml`:

``` xml
<bean id="GeonetworkDataDirectory" class="org.fao.geonet.kernel.GeonetworkDataDirectory" lazy-init="true">
  <property name="systemDataDir" ref="GNSystemDataDir"/>
  <property name="schemaPluginsDir" ref="GNSchemaPluginsDir"/>
</bean>
<bean id="GNSystemDataDir" class="java.nio.file.Paths" factory-method="get">
   <constructor-arg index="0" value="/path/to/gn/dir"/>
   <constructor-arg index="1"><array /></constructor-arg>
</bean>
<bean id="GNSchemaPluginsDir" class="java.nio.file.Paths" factory-method="get">
    <constructor-arg index="0" value="/path/to/schema/dir"/>
    <constructor-arg index="1"><array /></constructor-arg>
</bean>
```

## Выкарыстанне аб'ектнага сховішча S3

Калі ваша інфраструктура не мае даступнага пастаяннага сховішча, вы можаце наладзіць GeoNetwork на выкарыстанне аб'ектнага сховішча Amazon S3 (або сумяшчальнага) для захоўвання малюнкаў і даных.

Для гэтага неабходна выкарыстоўваць карыстальніцкую канфігурацыю кампанентаў. Замяніце кампаненты `filesystemStore`, `resourceStore` і `resources` у `core/src/main/resources/config-spring-geonetwork.xml` на нешта падобнае:

``` xml
<bean id="s3credentials" class="org.fao.geonet.resources.S3Credentials">
  <property name="region" value="eu-west-1"/>
  <property name="bucket" value="geonetwork-test"/>
  <property name="keyPrefix" value="geonetwork"/>
  <!-- Трэба толькі калі ў вас няма ~/.aws/credentials -->
  <property name="accessKey" value="MyAccessKey"/>
  <property name="secretKey" value="MySecretKey"/>
  <!-- Трэба толькі пры выкарыстанні не Amazon S3-->
  <property name="endpoint" value="sos-ch-dk-2.exo.io"/>
</bean>
<bean id="filesystemStore" class="org.fao.geonet.api.records.attachments.S3Store" />
<bean id="resourceStore"
      class="org.fao.geonet.api.records.attachments.ResourceLoggerStore">
  <constructor-arg index="0" ref="filesystemStore"/>
</bean>
<bean id="resources" class="org.fao.geonet.resources.S3Resources"/>
```

Кампанент `s3credentials` можна пакінуць пустым і выкарыстоўваць наступныя сістэмныя пераменныя асяроддзя для яго наладкі (зручна ў кантэйнерным асяроддзі):

-   AWS_S3_PREFIX
-   AWS_S3_BUCKET
-   AWS_DEFAULT_REGION
-   AWS_S3_ENDPOINT
-   AWS_ACCESS_KEY_ID
-   AWS_SECRET_ACCESS_KEY

## Выкарыстанне ўніверсальнага воблачнага аб'ектнага сховішча (JCLoud)

Калі ваша інфраструктура не мае даступнага пастаяннага сховішча, вы можаце наладзіць GeoNetwork на выкарыстанне воблачнага аб'ектнага сховішча для захоўвання малюнкаў і даных.
Рэалізацыя JCloud падтрымлівае наступныя [правайдэры](https://jclouds.apache.org/reference/providers/)

Для гэтага неабходна выкарыстоўваць карыстальніцкую канфігурацыю кампанентаў. Замяніце кампаненты `filesystemStore`, `resourceStore` і `resources` у **`core/src/main/resources/config-spring-geonetwork.xml`** на нешта падобнае:

Прыклад для Azure Blob

``` xml
<bean id="jcloudcredentials" class="org.fao.geonet.resources.JCloudCredentials">
  <property name="provider" value="eu-west-1"/>
  <property name="containerName" value="geonetwork-test"/>
  <property name="baseFolder" value="geonetwork"/>
  <property name="storageAccountName" value="MyAccessKey"/>
  <property name="storageAccountKey" value="MySecretKey"/>
</bean>
<bean id="filesystemStore" class="org.fao.geonet.api.records.attachments.JCloudStore" />
<bean id="resourceStore"
      class="org.fao.geonet.api.records.attachments.ResourceLoggerStore">
  <constructor-arg index="0" ref="filesystemStore"/>
</bean>
<bean id="resources" class="org.fao.geonet.resources.JCloudResources"/>
```

Прыклад для AWS S3
```
<bean id="jcloudcredentials" class="org.fao.geonet.resources.JCloudCredentials">
  <property name="provider" value="aws-s3"/>
  <property name="containerName" value="geonetwork-test"/>
  <property name="baseFolder" value="geonetwork"/>
  <property name="storageAccountName" value="MyAccessKey"/>
  <property name="storageAccountKey" value="MySecretKey"/>
</bean>
<bean id="filesystemStore" class="org.fao.geonet.api.records.attachments.JCloudStore" />
<bean id="resourceStore"
      class="org.fao.geonet.api.records.attachments.ResourceLoggerStore">
  <constructor-arg index="0" ref="filesystemStore"/>
</bean>
<bean id="resources" class="org.fao.geonet.resources.JCloudResources"/>
```

Кампанент `jcloudcredentials` можна пакінуць пустым і выкарыстоўваць наступныя сістэмныя пераменныя асяроддзя для яго наладкі (зручна ў кантэйнерным асяроддзі):

 - JCLOUD_PROVIDER
 - JCLOUD_CONTAINERNAME
 - JCLOUD_BASEFOLDER
 - JCLOUD_STORAGEACCOUNTNAME
 - JCLOUD_STORAGEACCOUNTKEY


## Структура дырэкторыі даных

Дырэкторыя даных змяшчае:

``` text
data_directory/
 |--config: Дадатковая канфігурацыя (напрыклад, можа ўтрымліваць перавызначэнні)
 |   |--schemaplugin-uri-catalog.xml
 |   |--codelist: Тэзаўрусы ў фармаце SKOS
 |   |--index: Канфігурацыя індэкса
 |   |--schemaPlugins: Дырэкторыя для захоўвання новых стандартаў метаданых
 |
 |--data
 |   |--metadata_data: Даныя, якія адносяцца да запісаў метаданых
 |   |--resources:
 |   |     |--htmlcache
 |   |     |--images
 |   |     |   |--harvesting
 |   |     |   |--logos
 |   |     |   |--statTmp
 |   |
 |   |--metadata_subversion: Рэпазіторый subversion
 |   |--backup: Папка, якая змяшчае выдаленыя метаданыя
```

## Пашыраная канфігурацыя дырэкторыі даных

Усе паддырэкторыі могуць быць наладжаны асобна з дапамогай сістэмнай уласцівасці Java. Напрыклад, каб размясціць дырэкторыю канфігурацыі індэкса ў карыстальніцкім месцы, выкарыстоўвайце:

-   <webappName>.indexConfig.dir і, калі не зададзена, выкарыстоўвайце:
-   geonetwork.indexConfig.dir

Прыклады:

-   Дадайце наступныя ўласцівасці Java у скрыпт start-geonetwork.sh:

``` shell
java -Xms1g -Xmx1g -Xss2M -XX:MaxPermSize=128m -Dgeonetwork.dir=/app/geonetwork_data_dir
```

-   Дадайце наступныя сістэмныя ўласцівасці ў скрыпт start-geonetwork.sh:

``` shell
export geonetwork_dir=/app/geonetwork_data_dir
```

-   Калі змены ў тэзаўрус або схему не ўносяцца, можа быць мэтазгодна выкарыстоўваць версію з вэб-праграмы. У такім выпадку ўсталюйце:

``` shell
-Dgeonetwork.dir=/data/catalogue
-Dgeonetwork.schema.dir=/app/tomcat/webapps/geonetwork/WEB-INF/data/config/schema_plugins
-Dgeonetwork.indexConfig.dir=/app/tomcat/webapps/geonetwork/WEB-INF/data/config/index
-Dgeonetwork.codeList.dir=/app/tomcat/webapps/geonetwork/WEB-INF/data/config/codelist
```

Спіс уласцівасцей, якія можна задаць:

-   geonetwork.dir
-   geonetwork.indexConfig.dir
-   geonetwork.config.dir
-   geonetwork.codeList.dir
-   geonetwork.schema.dir
-   geonetwork.data.dir
-   geonetwork.resources.dir
-   geonetwork.svn.dir
-   geonetwork.upload.dir
-   geonetwork.backup.dir
-   geonetwork.formatter.dir
-   geonetwork.htmlcache.dir

## Праверка канфігурацыі

Пасля запуску праверце канфігурацыю на старонцы `Кансоль адміністратара` --> `Статыстыка і статус` --> `Інфармацыя`.

![](img/datadirectory.png)