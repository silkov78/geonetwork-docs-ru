# Пакетное редактирование с помощью XSLT {#batchupdate_xsl}

## Применение изменений {#batch-process-apply}

Пользователь-администратор может использовать API каталога для обновления набора записей с помощью [XSLT-преобразования](https://ru.wikipedia.org/wiki/XSLT). 
Для этого необходимо выполнить следующие действия:

- Войти в систему в качестве администратора
- Найти записи для обновления с помощью [Q-поиска](../../api/search.md). Например, выбор всех шаблонов в определенном стандарте: <http://localhost:8080/geonetwork/srv/eng/q?_schema=iso19115-3&_isTemplate=y>.
- Выбрать все записи, соответствующие поиску, с помощью <http://localhost:8080/geonetwork/srv/eng/metadata.select?selected=add-all>.
- Запустить процесс с помощью <http://localhost:8080/geonetwork/srv/eng/md.processing.batch?process=my-custom-process>.
- Проверить отчет о ходе выполнения с помощью <http://localhost:8080/geonetwork/srv/eng/md.processing.batch.report>.

По окончании процесса выдается сводка:

- Количество записей для обработки
- Количество записей, которые были обработаны
- Количество не найденных записей (в случае, если одна запись была удалена после выбора)
- Количество записей с ошибками
- Количество записей, для которых процесс не определен в стандарте
- Количество записей, которые текущий пользователь не может редактировать.

Процесс также может быть применен к одной записи метаданных с помощью сервиса `md.processing`. 
Например, <http://localhost:8080/geonetwork/srv/eng/md.processing?uuid=46eac9e4-33cb-45b7-a104-7bcc8e654c98&process=keywords-mapper&search=water&replace=Water>.

Параметрами являются:

- uuid или id: UUID метаданных или внутренний идентификатор метаданных
- процесс: Идентификатор процесса
- добавить другие дополнительные параметры в зависимости от процесса (см. ниже).

## Добавление пакетного процесса {#batch-process-add}

### Создание файла обработки

Пакетные процессы определяются на основе каждого стандарта метаданных. 
Чтобы проверить список доступных процессов для стандарта, проверьте папку `<datadirectory>/config/schemaPlugins/<schemaId>/process`.

Папка `process` содержит набор XSLT-преобразований. Имя XSLT-файла без расширения используется для запуска процесса. 
Например, если используется `md.processing.batch?process=my-custom-process`, XSLT процесса ДОЛЖЕН иметь имя `my-custom-process.xsl`.

### Обработка XML записи

Процесс XSLT будет применен к каждой записи метаданных в подборке. 
Каждый документ будет иметь в качестве корневого элемента XML-документ метаданных с элементом `geonet:info`. 
Элемент `geonet:info` содержит метаданные о метаданных. Этот элемент ДОЛЖЕН быть удален процессом, чтобы не изменять запись при сохранении в базе данных.

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

### Добавление параметров

XSLT-процесс может получить параметры, которые могут быть указаны в URL с помощью `xsl:param`. 
Например, при использовании `md.processing.batch?process=my-custom-process&myParameter=test`.

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0"
                exclude-result-prefixes="#all">

    <xsl:param name="myParameter" select="''"/>
```

В этом примере `xsl:param` будет доступен как переменная с помощью `$myParameter` и будет иметь пустое значение, если не задан параметр URL. 
Чтобы проверить, правильно ли задан параметр, используйте `xsl:message` для вывода информации в файл журнала.

``` xml
<xsl:param name="myParameter" select="''"/>
<xsl:message>myParameter: <xsl:value-of select="$myParameter"/></xsl:message>
```

Процесс XSLT также имеет доступ к параметрам каталога:

- guiLang: Текущий язык пользовательского интерфейса
- baseUrl: Базовый URL-адрес сервиса (например, `http://localhost:8080/geonetwork`)
- catalogUrl: URL-адрес каталога (например, `http://localhost:8080/geonetwork/srv/eng`)
- nodeId: Идентификатор узла (по умолчанию `srv`).

Чтобы использовать один из этих параметров в процессе, используйте `xsl:param`:

``` xml
<xsl:param name="guiLang" select="''"/>
```


### XLST-процесс должен

Как минимум процесс ДОЛЖЕН делать:

- копию всей записи
- удалить элемент geonet:info

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

Затем можно редактировать саму запись метаданных.

### Примеры обработки

Примеры смотрите в `schemas/iso19139/src/main/plugin/iso19139/process`.

В дополнение к минимуму, который процесс ДОЛЖЕН выполнять, процесс может определять дополнительные действия, используя новые шаблоны:

- Удаление элемента. Например, удаление всех отчетов о DQ_TopologicalConsistency:

``` xml
<xsl:template match="gmd:report[gmd:DQ_TopologicalConsistency]"
              priority="2"/>
```

Установите приоритет на 2, чтобы шаблон имел приоритет над основным шаблоном, создающим копии всего.

## Регистрация процесса в качестве подказки {#customizing-xslt-suggestion}

См. [Предложение по улучшению содержания метаданных](suggestion.md).

## Регистрация процесса в качестве действия редактора {#xslt-in-editor}

XSLT-процесс может использоваться в редакторе для запуска определенных действий. 
Например, в представлении INSPIRE отображается кнопка для добавления идентификатора ресурса, если он не определен, заканчиваясь идентификатором метаданных.
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

См. ссылку:``creating-custom-editor``.

## Добавление XSLT-преобразования для импорта {#customizing-xslt-conversion}

Добавление XSLT-преобразования в папку `web/geonetwork/xsl/conversion/import` предоставляет пользователю новые возможности импорта. 
Файлы могут быть добавлены в эту папку без перезапуска приложения.
