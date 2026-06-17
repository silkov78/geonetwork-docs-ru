# Dublin Core (dublin-core) {#dublin-core}

Набор элементаў метаданых Dublin Core — гэта слоўнік з пятнаццаці ўласцівасцяў, якія выкарыстоўваюцца для апісання рэсурсаў. Назва "Dublin" абумоўлена месцам яго паходжання — запрашальным семінарам 1995 года ў Дубліне, штат Агая; "core" (ядро) азначае, што яго элементы з'яўляюцца шырокімі і ўніверсальнымі, прыдатнымі для апісання шырокага спектру рэсурсаў.

Больш падрабязная інфармацыя: [Dublin Core Metadata Element Set](http://dublincore.org/documents/dces/)

## Рэдактар метаданых

Дадзены стандарт можа быць закадзіраваны з выкарыстаннем 3 выглядаў.

-   [Выгляд: Просты (па змаўчанні)](dublin-core.md#dublin-core-view-default)
-   [Выгляд: Поўны (пашыраны)](dublin-core.md#dublin-core-view-advanced)
-   [Выгляд: XML (xml)](dublin-core.md#dublin-core-view-xml)

### Выгляд: Просты (па змаўчанні) {#dublin-core-view-default}

Гэты выгляд складаецца з 1 укладкі(ак).

-   [Укладка: Простая (па змаўчанні)](dublin-core.md#dublin-core-tab-default)

Гэты выгляд таксама дазваляе дадаць наступны элемент, нават калі яго няма ў бягучым запісе:

-   Тэма і ключавыя словы (dc:subject)

#### Укладка: Простая (па змаўчанні) {#dublin-core-tab-default}

![](img/dublin-core-tab-default.png)

На гэтай укладцы адлюстроўваюцца элементы з XML-запісу метаданых.

##### Раздзел: Метаданыя

Гл. [Метаданыя](dublin-core.md#dublin-core-elem-simpledc-8506dd4a73872a53513368db419204a3)

### Выгляд: Поўны (пашыраны) {#dublin-core-view-advanced}

Гэты выгляд складаецца з 1 укладкі(ак).

-   [Укладка: Поўная (пашыраная)](dublin-core.md#dublin-core-tab-advanced)

#### Укладка: Поўная (пашыраная) {#dublin-core-tab-advanced}

На гэтай укладцы адлюстроўваюцца элементы з XML-запісу метаданых, а таксама прадастаўляюцца элементы кіравання для дадання ўсіх элементаў, вызначаных у схеме (XSD).

##### Раздзел: Метаданыя

Гл. [Метаданыя](dublin-core.md#dublin-core-elem-simpledc-8506dd4a73872a53513368db419204a3)

### Выгляд: XML (xml) {#dublin-core-view-xml}

Гэты выгляд складаецца з 1 укладкі(ак).

-   [Укладка: XML (xml)](dublin-core.md#dublin-core-tab-xml)

#### Укладка: XML (xml) {#dublin-core-tab-xml}

На гэтай укладцы адлюстроўваюцца элементы з XML-запісу метаданых, а таксама прадастаўляюцца элементы кіравання для дадання ўсіх элементаў, вызначаных у схеме (XSD).

## Тэхнічныя характарыстыкі схемы

Ідэнтыфікатар стандарта

:   

> dublin-core

Версія

:   

> 1.0

Размяшчэнне схемы

:   

Прасторы імёнаў схемы

:   

-   `http://geonetwork-opensource.org/schemas/schema-ident`
-   <http://www.w3.org/2001/XMLSchema-instance>
-   <http://www.w3.org/XML/1998/namespace>

Рэжым вызначэння схемы

:   

> gns:elements (root)

Элементы вызначэння схемы

:   

-   simpledc

## Стандартныя элементы

Спіс усіх элементаў, даступных у стандарце.

### Удзельнік (Contributor) {#dublin-core-elem-dc-contributor-0974cafd6cf5302fe8501874dbe3b3ac}

Назва

:   

> dc:contributor

Апісанне

:   

```{=html}
Сутнасць, адказная за ўнясенне ўкладу ў змест рэсурсу.
```
### Ахоп (Coverage) {#dublin-core-elem-dc-coverage-8a3ad050a5c9949ad92271f646817e10}

Назва

:   

> dc:coverage

Апісанне

:   

```{=html}
Ступень або вобласць зместу рэсурсу. Як правіла, "Ахоп" уключае ў сябе
      прасторавае месцазнаходжанне (назва месца або геаграфічныя каардынаты), часавы перыяд
      (абазначэнне перыяду, дата або дыяпазон дат) або юрысдыкцыю (напрыклад, названая адміністрацыйная адзінка).
```
``` xml
<dc:coverage xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dct="http://purl.org/dc/terms/"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    North 45.668, South 45.635, East 4.805, West 4.768. CHARLY
  </dc:coverage>
```

### Стваральнік (Creator) {#dublin-core-elem-dc-creator-f6d71ca3a0b4e9aeb0e518f195f8256e}

Назва

:   

> dc:creator

Апісанне

:   

```{=html}
Сутнасць, у асноўным адказная за стварэнне зместу рэсурсу.
```
``` xml
<dc:creator xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dct="http://purl.org/dc/terms/"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    Métropole de Lyon / Direction Innovation Numérique et Systèmes d'Information
    (DINSI) (Géomatique et données métropolitaines)
  </dc:creator>
```

### Дата (Date) {#dublin-core-elem-dc-date-23c64254f66925f9eb6e3bd19c442233}

Назва

:   

> dc:date

Апісанне

:   

```{=html}
Дата падзеі ў жыццёвым цыкле рэсурсу. Як правіла, дата асацыюецца
      са стварэннем або даступнасцю рэсурсу.
```
### Апісанне (Description) {#dublin-core-elem-dc-description-8918d5eea5202286bfa9ceaac948b704}

Назва

:   

> dc:description

Апісанне

:   

```{=html}
Справаздача пра змест рэсурсу.
```
``` xml
<dc:description xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dct="http://purl.org/dc/terms/"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    La maquette 3D de la commune (2009 ou 2012) est composée de deux à six
    couches de données. A minima, toutes les maquettes se composent des deux
    couches suivantes : - Le Modèle numérique de terrain (TIN) et ses textures
    associées ; - Les bâtiments 3D texturés (BATIS). Elle est complétée par une
    ou plusieurs des couches ci-dessous : - Les surfaces en eau (WATER) et leurs
    textures associées ; - Les bâtiments « remarquables » (Mairies, Eglises
    etc…) ; - Les ponts « remarquables » ; - Les objets « remarquables »
    (Statues, Fontaines etc…). Ces données sont modélisées suivant la norme
    CityGML et fournies dans ce format. Ces maquettes sont produites avec le
    logiciel RhinoTerrain/RhinoCity.
  </dc:description>
```

### Фармат (Format) {#dublin-core-elem-dc-format-3842730cdb5c8559fe6f2737815429ea}

Назва

:   

> dc:format

Апісанне

:   

```{=html}
Фізічная або лічбавая праява рэсурсу. Як правіла, "Фармат" уключае
      тып медыя або памеры рэсурсу. Фармат можа выкарыстоўвацца для ідэнтыфікацыі праграмнага забеспячэння,
      абсталявання або іншых тэхнічных сродкаў, неабходных для адлюстравання або працы з рэсурсам.
```
### Ідэнтыфікатар рэсурсу (Resource Identifier) {#dublin-core-elem-dc-identifier-7d64a0a5c40868491c49bf7df7574752}

Назва

:   

> dc:identifier

Апісанне

:   

```{=html}
Адназначная спасылка на рэсурс у рамках зададзенага кантэксту.
```
``` xml
<dc:identifier xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dct="http://purl.org/dc/terms/"
               xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">a806d3e1-c240-43a9-bbc3-643e8c93b10d</dc:identifier>
```

### Мова (Language) {#dublin-core-elem-dc-language-74e0ef625be0b45d0e6c64d5f76e1895}

Назва

:   

> dc:language

Апісанне

:   

```{=html}
Мова інтэлектуальнага зместу рэсурсу. Рэкамендаваная практыка
      заключаецца ў выкарыстанні RFC 3066, які ў спалучэнні з ISO 639 вызначае
      двух- і трохлітарныя першасныя моўныя тэгі з неабавязковымі падтэгамі.
```
``` xml
<dc:language xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dct="http://purl.org/dc/terms/"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">fre</dc:language>
```

### Выдавец (Publisher) {#dublin-core-elem-dc-publisher-5534d3efaa13b75c3aa34c379dd91025}

Назва

:   

> dc:publisher

Апісанне

:   

```{=html}
Сутнасць, адказная за забеспячэнне даступнасці рэсурсу.
```
``` xml
<dc:publisher xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dct="http://purl.org/dc/terms/"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    Métropole de Lyon / Direction Innovation Numérique et Systèmes d'Information
    (DINSI) (Géomatique et données métropolitaines)
  </dc:publisher>
```

### Сувязь (Relation) {#dublin-core-elem-dc-relation-3772ef19f1f075e519d2d0a60ec6f05a}

Назва

:   

> dc:relation

Апісанне

:   

```{=html}
Спасылка на звязаны рэсурс.
```
### Кіраванне правамі (Rights Management) {#dublin-core-elem-dc-rights-32dce43ec1342a098287b03b6a5cb72f}

Назва

:   

> dc:rights

Апісанне

:   

```{=html}
Інфармацыя пра правы, якія маюцца на рэсурс і ў адносінах да яго.
```
### Крыніца (Source) {#dublin-core-elem-dc-source-104607b158c41c5855de1ed62ae223dd}

Назва

:   

> dc:source

Апісанне

:   

```{=html}
Спасылка на рэсурс, з якога атрыманы дадзены рэсурс. Сапраўдны
      рэсурс можа быць атрыманы з зыходнага рэсурсу цалкам або часткова.
```
``` xml
<dc:source xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dct="http://purl.org/dc/terms/"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    Le Modèle numérique de terrain est issu d’une saisie photogrammétrique
    réalisée à partir de la prise de vue aérienne (2009 ou 2012). Les fichiers
    des textures associées plaquées sur le MNT correspondent à
    l’orthophotographie aérienne qui possède une résolution de 10 cm pour 2012
    et 16 cm pour 2009. - Les surfaces en eau (WATER) ont été identifiées à
    partir d’une saisie photogrammétrique réalisée à partir de la même prise de
    vue aérienne. - Les bâtiments 3D proviennent de la saisie photogrammétrique
    réalisée à partir de la prise de vue aérienne. Les textures plaquées sur ces
    bâtiments proviennent des clichés issus de la prise de vue aérienne. - Les
    bâtiments « remarquables » (Mairies, Eglises etc…), les ponts « remarquables
    » et les objets « remarquables » (Statues, Fontaines etc…) ont été texturés
    à partir de photographies terrestres.
  </dc:source>
```

### Тэма і ключавыя словы (Subject and Keywords) {#dublin-core-elem-dc-subject-a88bd90b4991695f8c45fe01df3f64d6}

Назва

:   

> dc:subject

Апісанне

:   

```{=html}
Тэма зместу рэсурсу. Як правіла, прадмет выяўляецца ў выглядзе ключавых слоў,
      ключавых фраз або кодаў класіфікацыі, якія апісваюць тэму рэсурсу.
```
``` xml
<dc:subject xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dct="http://purl.org/dc/terms/"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">Localisation</dc:subject>
```

### Назва (Title) {#dublin-core-elem-dc-title-18e3be863c870257c8b70d577038ee5f}

Назва

:   

> dc:title

Апісанне

:   

```{=html}
Імя, дадзенае рэсурсу. Як правіла, назва — гэта імя, пад якім рэсурс
      афіцыйна вядомы.
```
``` xml
<dc:title xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dct="http://purl.org/dc/terms/"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    Maquette 3D texturée de la commune de Charly (la Métropole de Lyon)
  </dc:title>
```

### Тып рэсурсу (Resource Type) {#dublin-core-elem-dc-type-15bbc75f8dbe617d6ed609fcf1202ee1}

Назва

:   

> dc:type

Апісанне

:   

```{=html}
Характар або жанр зместу рэсурсу. Тып уключае тэрміны, якія апісваюць
      агульныя катэгорыі, функцыі, жанры або ўзроўні агрэгавання зместу.
```
Рэкамендаваныя значэнні

| код     | метка   |
|---------|---------|
| dataset | Набор даных |
| service | Сэрвіс  |

``` xml
<dc:type xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dct="http://purl.org/dc/terms/"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">nonGeographicDataset</dc:type>
```

### URI {#dublin-core-elem-dc-URI-8f2cb1e27778e1b1977e670ca7e7a282}

Назва

:   

> dc:URI

Апісанне

:   

### Анатацыя (Abstract) {#dublin-core-elem-dct-abstract-a48c3a17636153c58749c5fc29d1bd28}

Назва

:   

> dct:abstract

Апісанне

:   

```{=html}
Кароткае выкладанне зместу рэсурсу.
```
### Правы доступу (Access Rights) {#dublin-core-elem-dct-accessRights-972cd1c89a0274325b1a3b99e34c95be}

Назва

:   

> dct:accessRights

Апісанне

:   

```{=html}
Інфармацыя пра тое, хто можа атрымаць доступ да рэсурсу, або ўказанне яго
      статусу бяспекі.
```
### Метад паступлення (Accrual Method) {#dublin-core-elem-dct-accrualMethod-6fa8ea67638a1578c231025e31dd40e9}

Назва

:   

> dct:accrualMethod

Апісанне

:   

```{=html}
Метад, з дапамогай якога элементы дадаюцца ў калекцыю.
```
### Перыядычнасць паступлення (Accrual Periodicity) {#dublin-core-elem-dct-accrualPeriodicity-2a4c9a8426dd588e960559174a3df263}

Назва

:   

> dct:accrualPeriodicity

Апісанне

:   

```{=html}
Частата, з якой элементы дадаюцца ў калекцыю.
```
Рэкамендаваныя значэнні

| код         | метка       |
|-------------|-------------|
| continual   | Пастаянна   |
| daily       | Штодзённа   |
| weekly      | Штотыднёва |
| fortnightly | Раз у два тыдні |
| monthly     | Штомесячна  |
| quarterly   | Штоквартальна |
| biannually  | Раз у паўгода |
| annually    | Штогод    |
| asNeeded    | Па неабходнасці |
| irregular   | Нерэгулярна |
| notPlanned  | Не запланавана |
| unknown     | Невядома  |

``` xml
<dct:accrualPeriodicity xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dct="http://purl.org/dc/terms/"
                        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">Irregular</dct:accrualPeriodicity>
```

### Палітыка паступлення (Accrual Policy) {#dublin-core-elem-dct-accrualPolicy-0ae937a1f9081db219a5dd04ed4610d4}

Назва

:   

> dct:accrualPolicy

Апісанне

:   

```{=html}
Палітыка, якая рэгулюе даданне элементаў у калекцыю.
```
### Альтэрнатыўная назва (Alternative Title) {#dublin-core-elem-dct-alternative-2518e8fc9fa67f5a10348016aae8bb0f}

Назва

:   

> dct:alternative

Апісанне

:   

```{=html}
Альтэрнатыўная назва рэсурсу.
```
### Аўдыторыя (Audience) {#dublin-core-elem-dct-audience-a610cbdc155d7cd9c87c8f22ef245521}

Назва

:   

> dct:audience

Апісанне

:   

```{=html}
Клас сутнасцяў, для якіх прызначаны або карысны рэсурс.
```
### Бібліяграфічная спасылка (Bibliographic Citation) {#dublin-core-elem-dct-bibliographicCitation-0d3ba175bdb84be48dec71bdb6b318da}

Назва

:   

> dct:bibliographicCitation

Апісанне

:   

```{=html}
Бібліяграфічная спасылка на рэсурс.
```
### Адпавядае стандарту (Conforms To) {#dublin-core-elem-dct-conformsTo-703d80b57bd6629b2bff3f57efd52dc5}

Назва

:   

> dct:conformsTo

Апісанне

:   

```{=html}
Усталяваны стандарт, якому адпавядае апісаны рэсурс.
```
### Дата стварэння (Date Created) {#dublin-core-elem-dct-created-9aebe20151c1c962d66737fcb9b87c2c}

Назва

:   

> dct:created

Апісанне

:   

```{=html}
Дата стварэння рэсурсу.
```
``` xml
<dct:created xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dct="http://purl.org/dc/terms/"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">2014-12-19</dct:created>
```

### Дата прыняцця (Date Accepted) {#dublin-core-elem-dct-dateAccepted-9f6f7b46bae794b317c939c75170b0f1}

Назва

:   

> dct:dateAccepted

Апісанне

:   

```{=html}
Дата прыняцця рэсурсу.
```
### Дата рэгістрацыі аўтарскіх правоў (Date Copyrighted) {#dublin-core-elem-dct-dateCopyrighted-1a3940c001fd2db761829940957d8bf7}

Назва

:   

> dct:dateCopyrighted

Апісанне

:   

```{=html}
Дата рэгістрацыі аўтарскіх правоў.
```
### Дата падачы (Date Submitted) {#dublin-core-elem-dct-dateSubmitted-0e038c3b8ac6daca57211a938eca6154}

Назва

:   

> dct:dateSubmitted

Апісанне

:   

```{=html}
Дата падачы рэсурсу
```
``` xml
<dct:dateSubmitted xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dct="http://purl.org/dc/terms/"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">2015-01-23</dct:dateSubmitted>
```

### Узровень адукацыі аўдыторыі (Audience Education Level) {#dublin-core-elem-dct-educationLevel-fa33466d34d56fb066753a6d97089631}

Назва

:   

> dct:educationLevel

Апісанне

:   

```{=html}
Клас сутнасцяў, вызначаных з пункту гледжання прагрэсу ў адукацыйным або
      навучальным кантэксце, для якіх прызначаны апісаны рэсурс.
```
### Аб'ём (Extent) {#dublin-core-elem-dct-extent-8a3a9adeaaac054e64dff722ad23c776}

Назва

:   

> dct:extent

Апісанне

:   

```{=html}
Памер або працягласць рэсурсу.
```
### Мае фармат (Has Format) {#dublin-core-elem-dct-hasFormat-d136ed16dc44af39fdf1b98b9fb4bc33}

Назва

:   

> dct:hasFormat

Апісанне

:   

```{=html}
Звязаны рэсурс, які па сутнасці з'яўляецца тым жа, што і раней існуючы апісаны
      рэсурс, але ў іншым фармаце.
```
### Уключае частку (Has Part) {#dublin-core-elem-dct-hasPart-f251f156dd8774a81f44c13c7b4a9e7d}

Назва

:   

> dct:hasPart

Апісанне

:   

```{=html}
Звязаны рэсурс, які ўключаны фізічна або лагічна ў апісаны
      рэсурс.
```
### Мае версію (Has Version) {#dublin-core-elem-dct-hasVersion-b8dc08cd4fc15cf1df605c2905b0c5e3}

Назва

:   

> dct:hasVersion

Апісанне

:   

```{=html}
Звязаны рэсурс, які з'яўляецца версіяй, рэдакцыяй або адаптацыяй апісанага
      рэсурсу.
```
### Метад навучання (Instructional Method) {#dublin-core-elem-dct-instructionalMethod-d220d889250a4a0f7e3efe29fc0f0ada}

Назва

:   

> dct:instructionalMethod

Апісанне

:   

```{=html}
Працэс, які выкарыстоўваецца для атрымання ведаў, поглядаў і навыкаў, які
      рэсурс закліканы падтрымліваць.
```
### З'яўляецца фарматам (Is Format Of) {#dublin-core-elem-dct-isFormatOf-8378903643254b5b83ae2acdc251b6a6}

Назва

:   

> dct:isFormatOf

Апісанне

:   

```{=html}
Звязаны рэсурс, які па сутнасці з'яўляецца тым жа, што і апісаны рэсурс, але ў
      іншым фармаце.
```
### З'яўляецца часткай (Is part of) {#dublin-core-elem-dct-isPartOf-6697c98943756abf56d4c2a50f9dc9a2}

Назва

:   

> dct:isPartOf

Апісанне

:   

```{=html}
Звязаны рэсурс, у які апісаны рэсурс фізічна або лагічна
      ўключаны.
```
``` xml
<dct:isPartOf xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dct="http://purl.org/dc/terms/"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">8017c69a-5b17-404f-acdd-d9c37a0afac4</dct:isPartOf>
```

### Спасылаецца (Is Referenced By) {#dublin-core-elem-dct-isReferencedBy-4cf2c75a368a7773ec781eaa6f4a7c03}

Назва

:   

> dct:isReferencedBy

Апісанне

:   

```{=html}
Звязаны рэсурс, які спасылаецца, цытуе або іншым чынам паказвае на апісаны
      рэсурс.
```
### Замяняецца (Is Replaced By) {#dublin-core-elem-dct-isReplacedBy-1e391e071c75e45dcf0a309285a642a0}

Назва

:   

> dct:isReplacedBy

Апісанне

:   

```{=html}
Звязаны рэсурс, які выцясняе, замяшчае або замяняе апісаны
      рэсурс.
```
### Патрабуецца для (Is Required By) {#dublin-core-elem-dct-isRequiredBy-def534523d854e3440e36701bea47cc4}

Назва

:   

> dct:isRequiredBy

Апісанне

:   

```{=html}
Звязаны рэсурс, які патрабуе апісанага рэсурсу для падтрымкі сваёй функцыі,
      дастаўкі або ўзгодненасці.
```
### Дата выпуску (Date Issued) {#dublin-core-elem-dct-issued-9f6ad8cb4b5e6225c1cb755489adb774}

Назва

:   

> dct:issued

Апісанне

:   

```{=html}
Дата афіцыйнага выпуску (напрыклад, публікацыі) рэсурсу.
```
### З'яўляецца версіяй (Is Version Of) {#dublin-core-elem-dct-isVersionOf-d1658a9e84f777d0a335528e82921417}

Назва

:   

> dct:isVersionOf

Апісанне

:   

```{=html}
Звязаны рэсурс, якога апісаны рэсурс з'яўляецца версіяй, рэдакцыяй або
      адаптацыяй.
```
### Ліцэнзія (License) {#dublin-core-elem-dct-license-865405c25292b886c12f7d056ebaabda}

Назва

:   

> dct:license

Апісанне

:   

```{=html}
Юрыдычны дакумент, які дае афіцыйны дазвол на ўчыненне пэўных дзеянняў з рэсурсам.
```
### Пасрэднік (Mediator) {#dublin-core-elem-dct-mediator-ab02c72730e6dbccbfb74b07e00edf10}

Назва

:   

> dct:mediator

Апісанне

:   

```{=html}
Сутнасць, якая апасродкуе доступ да рэсурсу і для якой рэсурс
      прызначаны або карысны.
```
### Носьбіт (Medium) {#dublin-core-elem-dct-medium-95f834fde8ee306293ebebcfd7a3aba5}

Назва

:   

> dct:medium

Апісанне

:   

```{=html}
Матэрыяльны або фізічны носьбіт рэсурсу.
```
### Дата мадыфікацыі (Date Modified) {#dublin-core-elem-dct-modified-66ecff9b0ec74fad28c5babebc1eec7d}

Назва

:   

> dct:modified

Апісанне

:   

```{=html}
Дата змены метаданых
```
``` xml
<dct:modified xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dct="http://purl.org/dc/terms/"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">2016-02-03T21:33:45</dct:modified>
```
### Паходжанне (Provenance) {#dublin-core-elem-dct-provenance-4ec9c18f260230d4455195d6a6f28c17}

Назва

:   

> dct:provenance

Апісанне

:   

```{=html}
Заява пра любыя змены ў праве ўласнасці і захоўванні рэсурсу з моманту яго
      стварэння, якія маюць значэнне для яго сапраўднасці, цэласнасці і інтэрпрэтацыі.
```
### Звязаны рэсурс (Related resource) {#dublin-core-elem-dct-references-3a44416fcd20eea0684aad2fd3228fdd}

Назва

:   

> dct:references

Апісанне

:   

```{=html}
Звязаны рэсурс, на які спасылаецца, цытуе або іншым чынам паказвае
      апісаны рэсурс.
```
### Замяняе (Replaces) {#dublin-core-elem-dct-replaces-c5b09017642a464af7a04db426f6d74f}

Назва

:   

> dct:replaces

Апісанне

:   

```{=html}
Звязаны рэсурс, які быў выцеснены, замяшчаны або заменены апісаным
      рэсурсам.
```
### Патрабуе (Requires) {#dublin-core-elem-dct-requires-2ad52ab491717dc624f79f92303f4679}

Назва

:   

> dct:requires

Апісанне

:   

```{=html}
Звязаны рэсурс, які патрабуецца апісаным рэсурсам для падтрымкі сваёй
      функцыі, дастаўкі або ўзгодненасці.
```
### Праваўладальнік (Rights Holder) {#dublin-core-elem-dct-rightsHolder-0f4304cc1135f8fc29f7a0ede8daa268}

Назва

:   

> dct:rightsHolder

Апісанне

:   

```{=html}
Асоба або арганізацыя, якая валодае або кіруе правамі на рэсурс.
```
### Прасторавыя характарыстыкі (Spatial) {#dublin-core-elem-dct-spatial-5100d679492a6f79fd3e53db624bcab2}

Назва

:   

> dct:spatial

Апісанне

:   

```{=html}
Прасторавыя характарыстыкі інтэлектуальнага зместу рэсурсу.
```
``` xml
<dct:spatial xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dct="http://purl.org/dc/terms/"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">RGF93 / CC46 (EPSG:3946)</dct:spatial>
```
### Змест (Table Of Contents) {#dublin-core-elem-dct-tableOfContents-c20c496386cad7aa48ad05ca41a6340b}

Назва

:   

> dct:tableOfContents

Апісанне

:   

```{=html}
Спіс падраздзелаў рэсурсу.
```
### Часавы ахоп (Temporal Coverage) {#dublin-core-elem-dct-temporal-0a2abb1d37421418cafeb48bd21e6854}

Назва

:   

> dct:temporal

Апісанне

:   

```{=html}
Часавыя характарыстыкі рэсурсу.
```
### Дата сапраўднасці (Date Valid) {#dublin-core-elem-dct-valid-343768fccc581bc0822c69e6ca19c70c}

Назва

:   

> dct:valid

Апісанне

:   

```{=html}
Дата (часцей дыяпазон) сапраўднасці рэсурсу.
```
### Метаданыя (Metadata) {#dublin-core-elem-simpledc-8506dd4a73872a53513368db419204a3}

Назва

:   

> simpledc

Апісанне

:   

``` xml
<simpledc xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dct="http://purl.org/dc/terms/"
          xsi:noNamespaceSchemaLocation="http://localhost/geonetwork/xml/schemas/dublin-core/schema.xsd">
   <dc:title>
    Maquette 3D texturée de la commune de Charly (la Métropole de Lyon)
  </dc:title>
   <dc:creator>
    Métropole de Lyon / Direction Innovation Numérique et Systèmes d'Information
    (DINSI) (Géomatique et données métropolitaines)
  </dc:creator>
   <dc:subject>Localisation</dc:subject>
   <dc:description>
    La maquette 3D de la commune (2009 ou 2012) est composée de deux à six
    couches de données. A minima, toutes les maquettes se composent des deux
    couches suivantes : - Le Modèle numérique de terrain (TIN) et ses textures
    associées ; - Les bâtiments 3D texturés (BATIS). Elle est complétée par une
    ou plusieurs des couches ci-dessous : - Les surfaces en eau (WATER) et leurs
    textures associées ; - Les bâtiments « remarquables » (Mairies, Eglises
    etc…) ; - Les ponts « remarquables » ; - Les objets « remarquables »
    (Statues, Fontaines etc…). Ces données sont modélisées suivant la norme
    CityGML et fournies dans ce format. Ces maquettes sont produites avec le
    logiciel RhinoTerrain/RhinoCity.
  </dc:description>
   <dc:publisher>
    Métropole de Lyon / Direction Innovation Numérique et Systèmes d'Information
    (DINSI) (Géomatique et données métropolitaines)
  </dc:publisher>
   <dc:type>nonGeographicDataset</dc:type>
   <dc:format>application/zip</dc:format>
   <dc:format>CityGML (taille : 260.0 Mo)</dc:format>
   <dc:format>application/zip</dc:format>
   <dc:format>executable (taille : 829.2 Mo)</dc:format>
   <dc:format>application/zip</dc:format>
   <dc:format>CityGML (taille : 113.5 Mo)</dc:format>
   <dc:format>application/zip</dc:format>
   <dc:format>executable (taille : 339.2 Mo)</dc:format>
   <dc:format>application/pdf</dc:format>
   <dc:format>pdf (taille : 315 Ko)</dc:format>
   <dc:source>
    Le Modèle numérique de terrain est issu d’une saisie photogrammétrique
    réalisée à partir de la prise de vue aérienne (2009 ou 2012). Les fichiers
    des textures associées plaquées sur le MNT correspondent à
    l’orthophotographie aérienne qui possède une résolution de 10 cm pour 2012
    et 16 cm pour 2009. - Les surfaces en eau (WATER) ont été identifiées à
    partir d’une saisie photogrammétrique réalisée à partir de la même prise de
    vue aérienne. - Les bâtiments 3D proviennent de la saisie photogrammétrique
    réalisée à partir de la prise de vue aérienne. Les textures plaquées sur ces
    bâtiments proviennent des clichés issus de la prise de vue aérienne. - Les
    bâtiments « remarquables » (Mairies, Eglises etc…), les ponts « remarquables
    » et les objets « remarquables » (Statues, Fontaines etc…) ont été texturés
    à partir de photographies terrestres.
  </dc:source>
   <dc:language>fre</dc:language>
   <dc:relation>
    https://download.data.grandlyon.com/files/grandlyon/localisation/bati3d/CHARLY_2012.zip
  </dc:relation>
   <dc:relation>
    https://download.data.grandlyon.com/files/grandlyon/localisation/bati3d/_EXE_CHARLY_2012.zip
  </dc:relation>
   <dc:relation>
    https://download.data.grandlyon.com/files/grandlyon/localisation/bati3d/CHARLY_2009.zip
  </dc:relation>
   <dc:relation>
    https://download.data.grandlyon.com/files/grandlyon/localisation/bati3d/_EXE_CHARLY_2009.zip
  </dc:relation>
   <dc:relation>
    https://download.data.grandlyon.com/files/grandlyon/localisation/bati3d/Maquettes_3D_CityGML.pdf
  </dc:relation>
   <dc:relation>
    https://download.data.grandlyon.com/files/grandlyon/LicenceOuverte.pdf
  </dc:relation>
   <dc:coverage>
    North 45.668, South 45.635, East 4.805, West 4.768. CHARLY
  </dc:coverage>
   <dc:rights>Licence Ouverte</dc:rights>
   <dc:rights>Pas de restriction d'accès public selon INSPIRE</dc:rights>
   <dct:created>2014-12-19</dct:created>
   <dct:dateSubmitted>2015-01-23</dct:dateSubmitted>
   <dct:isPartOf>8017c69a-5b17-404f-acdd-d9c37a0afac4</dct:isPartOf>
   <dct:spatial>RGF93 / CC46 (EPSG:3946)</dct:spatial>
   <dct:accrualPeriodicity>Irregular</dct:accrualPeriodicity>
   <dct:modified>2016-02-03T21:33:45</dct:modified>
   <dc:identifier>a806d3e1-c240-43a9-bbc3-643e8c93b10d</dc:identifier>
</simpledc>
```

## Стандартныя спісы кодаў (Codelists)

Спіс усіх спісаў кодаў, даступных у стандарце.

Спісы кодаў не вызначаны.