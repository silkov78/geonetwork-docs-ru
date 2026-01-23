# Пакетнае рэдагаванне з дапамогай XSLT {#batchupdate_xsl}

## Прымяненне змяненняў {#batch-process-apply}

Карыстальнік-адміністратар можа выкарыстоўваць API каталога для абнаўлення набору запісаў з дапамогай [XSLT-пераўтварэнні](https://ru.wikipedia.org/wiki/XSLT). 
Для гэтага неабходна выканаць наступныя дзеянні:

- Увайсці ў сістэму ў якасці адміністратара
- Знайсці запісы для абнаўлення з дапамогай [Q-пошуку](../../api/search.md). Напрыклад, выбар усіх шаблонаў у пэўным стандарце: <http://localhost:8080/geonetwork/srv/eng/q?_schema=iso19115-3&_isTemplate=y>.
- Выбраць усе запісы, якія адпавядаюць пошуку, з дапамогай <http://localhost:8080/geonetwork/srv/eng/metadata.select?selected=add-all>.
- Запусціць працэс з дапамогай <http://localhost:8080/geonetwork/srv/eng/md.processing.batch?process=my-custom-process>.
- Праверыць справаздачу аб ходзе выканання з дапамогай <http://localhost:8080/geonetwork/srv/eng/md.processing.batch.report>.

Па заканчэнні працэсу выдаецца зводка:

- Колькасць запісаў для апрацоўкі
- Колькасць запісаў, якія былі апрацаваны
- Колькасць не знойдзеных запісаў (у выпадку, калі адзін запіс быў выдалены пасля выбару)
- Колькасць запісаў з памылкамі
- Колькасць запісаў, для якіх працэс не вызначаны ў стандарце
- Колькасць запісаў, якія бягучы карыстальнік не можа рэдагаваць.

Працэс таксама можа быць ужыты да аднаго запісу метададзеных з дапамогай сэрвісу `md.processing`. 
Напрыклад, <http://localhost:8080/geonetwork/srv/eng/md.processing?uuid=46eac9e4-33cb-45b7-a104-7bcc8e654c98&process=keywords-mapper&search=water&replace=Water>.

Параметрамі з'яўляюцца:

- uuid або id: UUID метададзеных або ўнутраны ідэнтыфікатар метададзеных
- працэс: Ідэнтыфікатар працэсу
- дадаць іншыя дадатковыя параметры ў залежнасці ад працэсу (гл. ніжэй).

## Даданне пакетнага працэсу

### Стварэнне файла апрацоўкі

Пакетныя працэсы вызначаюцца на аснове кожнага стандарту метададзеных. 
Каб праверыць спіс даступных працэсаў для стандарту, праверце папку `<datadirectory>/config/schemaPlugins/<schemaId>/process`.

Папка `process` змяшчае набор XSLT-пераўтварэнняў. Імя XSLT-файла без пашырэння выкарыстоўваецца для запуску працэсу. 
Напрыклад, калі выкарыстоўваецца `md.processing.batch?process=my-custom-process`, XSLT працэсу ПАВІНЕН мець імя `my-custom-process.xsl`.

### Апрацоўка XML запісу

Працэс XSLT будзе ужыты да кожнага запісу метададзеных у падборцы. 
Кожны дакумент будзе мець у якасці каранёвага элемента XML-дакумент метададзеных з элементам `geonet:info`. 
Элемент `geonet:info` змяшчае метададзеныя аб метададзеных. Гэты элемент ПАВІНЕН быць выдалены працэсам, каб не змяняць запіс пры захаванні ў базе дадзеных.

``` xml
<gmd:MD_Metadata>
    ...
    <geonet:info xmlns:geonet="http://www.fao.org/geonetwork">
        <id>73481</id>
        <uuid>bb151890-2da5-4cfb-8659-7839e7138be7</uuid>
        <schema>iso19139</schema>
        <createDate>2015-12-23T17:05:36</createDate>
        <changeDate>2015-12-23T18:07:40</changeDate>
        <source>2cc603e1-981c-41a2-a183-39429c7dcc49</source>
        <ownerId>1</ownerId>
        <edit>true</edit>
        <owner>true</owner>
        <isPublishedToAll>false</isPublishedToAll>
        <view>true</view>
        <notify>true</notify>
        <download>true</download>
        <dynamic>true</dynamic>
        <featured>true</featured>
        <selected>true</selected>
    </geonet:info>
</gmd:MD_Metadata>
```

### Даданне параметраў

XSLT-працэс можа атрымаць параметры, якія могуць быць указаны ў URL з дапамогай `xsl:param`. 
Напрыклад, пры выкарыстанні `md.processing.batch?process=my-custom-process&myParameter=test`.

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0"
                exclude-result-prefixes="#all">

    <xsl:param name="myParameter" select="''"/>
```

У гэтым прыкладзе `xsl:param` будзе даступны як пераменная з дапамогай `$myParameter` і будзе мець пустое значэнне, калі не зададзены параметр URL. 
Каб праверыць, ці правільна зададзены параметр, выкарыстоўвайце `xsl:message` для вываду інфармацыі ў файл часопіса.

``` xml
<xsl:param name="myParameter" select="''"/>
<xsl:message>myParameter: <xsl:value-of select="$myParameter"/></xsl:message>
```

Працэс XSLT таксама мае доступ да параметраў каталога:

- guiLang: Бягучая мова карыстальніцкага інтэрфейсу
- baseUrl: Базавы URL-адрас сэрвісу (напрыклад, `http://localhost:8080/geonetwork`)
- catalogUrl: URL-адрас каталога (напрыклад, `http://localhost:8080/geonetwork/srv/eng`)
- nodeId: Ідэнтыфікатар вузла (па змаўчанні `srv`).

Каб выкарыстоўваць адзін з гэтых параметраў у працэсе, выкарыстоўвайце `xsl:param`:

``` xml
<xsl:param name="guiLang" select="''"/>
```


### XLST-працэс павінен

Як мінімум працэс ПАВІНЕН рабіць:

- копію ўсяго запісу
- выдаліць элемент geonet:info

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
                xmlns:geonet="http://www.fao.org/geonetwork" version="2.0"
                exclude-result-prefixes="#all">

    <!-- Do a copy of every nodes and attributes recursively -->
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <!-- Remove geonet:* elements. -->
    <xsl:template match="geonet:*" priority="2"/>
</xsl:stylesheet>
```

Затым можна рэдагаваць сам запіс метададзеных.

### Прыклады апрацоўкі

Прыклады глядзіце ў `schemas/iso19139/src/main/plugin/iso19139/process`.

У дадатак да мінімуму, які працэс ПАВІНЕН выконваць, працэс можа вызначаць дадатковыя дзеянні, выкарыстоўваючы новыя шаблоны:

- Выдаленне элемента. Напрыклад, выдаленне ўсіх справаздач аб DQ_TopologicalConsistency:

``` xml
<xsl:template match="gmd:report[gmd:DQ_TopologicalConsistency]"
              priority="2"/>
```

Усталюйце прыярытэт на 2, каб шаблон меў прыярытэт над асноўным шаблонам, які стварае копіі ўсяго.

## Рэгістрацыя працэсу ў якасці падказкі

Гл. [Прапанова па паляпшэнні зместу метададзеных](suggestion.md).

## Рэгістрацыя працэсу ў якасці дзеяння рэдактара {#xslt-in-editor}

XSLT-працэс можа выкарыстоўвацца ў рэдактары для запуску пэўных дзеянняў. 
Напрыклад, у прадстаўленні INSPIRE адлюстроўваецца кнопка для дадання ідэнтыфікатара рэсурсу, калі ён не вызначаны, заканчваючыся ідэнтыфікатарам метададзеных.
``` xml
<action type="batch"
        process="add-resource-id"
        if="count(gmd:MD_Metadata/gmd:identificationInfo/*/
                      gmd:citation/gmd:CI_Citation/
                          gmd:identifier[
                          ends-with(
                              gmd:MD_Identifier/gmd:code/gco:CharacterString,
                              //gmd:MD_Metadata/gmd:fileIdentifier/gco:CharacterString
                          )]) = 0"/>
```

Гл. спасылку:``creating-custom-editor``.

## Даданне XSLT-пераўтварэння для імпарту {#customizing-xslt-conversion}

Даданне XSLT-пераўтварэння ў папку `web/geonetwork/xsl/conversion/import` прадастаўляе карыстальніку новыя магчымасці імпарту. 
Файлы могуць быць дададзены ў гэтую папку без перазапуску дадатка.