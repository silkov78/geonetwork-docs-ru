# Устаноўка пошукавай платформы

Пошукавы рухавік GeoNetwork пабудаваны на базе Elasticsearch. Платформа выкарыстоўваецца для індэксавання запісаў, а таксама для індэксавання даных WFS (гл. [Аналіз і візуалізацыя даных](../user-guide/analyzing/data.md)).

Для працы GeoNetwork патрабуецца ўстаноўка экземпляра [Elasticsearch](https://www.elastic.co/products/elasticsearch) побач з каталогам.

## Сумяшчальнасць з Elasticsearch

Версія Java-кліента Elasticsearch: 8.19.13

| Версія Elasticsearch | Сумяшчальнасць |
|-----------------------| ------------- |
| Elasticsearch 8.19.13 | рэкамендуецца |
| Elasticsearch 8.14.x  | мінімальная   |

Больш старыя версіі могуць падтрымлівацца, але не тэсціраваліся.

## Устаноўка

=== "Ручная ўстаноўка"
        
    1. **Загрузка:** Elasticsearch `8.19.13` з сайта <https://www.elastic.co/downloads/elasticsearch> і распакуйце файл.

        ``` shell
        wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.19.13.tar.gz
        tar xvfz elasticsearch-8.19.13.tar.gz
        ```

    2. **Запуск**: Уручную запусціце Elasticsearch з дапамогай:

        ``` shell
        elasticsearch-8.19.13/bin/elasticsearch
        ```

    3. **Спыненне**: Уручную спыніце Elasticsearch з дапамогай:

        ``` shell
        elasticsearch-8.19.13/bin/elasticsearch stop
        ```
        
=== "Устаноўка з дапамогай Maven"

    1. Распрацоўшчыкам рэкамендуецца запускаць Elasticsearch з выкарыстаннем Maven, каб выконваць тэсціраванне на той версіі Elasticsearch, якая прызначана для наступнага рэлізу.
    
        !!! note
            
            Пры запуску з зыходнага кода версія Elasticsearch бярэцца з уласцівасці `es.version` у файле [pom.xml](https://github.com/geonetwork/core-geonetwork/blob/main/pom.xml).
    
    2. **Загрузка**: Запусціце maven з дырэкторыі **`es`**.

          ``` shell
          cd es
          mvn install -Pes-download
          ```
    
    3. **Запуск**: Выкарыстоўвайце плагін maven ``exec`` для запуску Elasticsearch:
    
        ``` shell
        mvn exec:exec -Des-start
        ```
        
        Elasticsearch будзе працаваць у рэжыме foreground, выводзячы паведамленні ў кансоль.

    4. **Спыненне**: Для спынення Elasticsearch выкарыстоўвайце камбінацыю ++ctrl+c++, каб спыніць працэс maven.

## Стварэнне індэкса

1. GeoNetwork падключыцца да Elasticsearch пры запуску, і індэксы будуць створаны, калі яны не існуюць.
   
    * GeoNetwork запусціцца, нават калі індэкс Elasticsearch недаступны (або яшчэ не запушчаны).
    
    * Калі GeoNetwork не можа звязацца з Elasticsearch, будзе адлюстравана папярэджанне.
    
    * Калі індэкс Elasticsearch стане даступны, індэксы будуць створаны, калі іх яшчэ няма.

2. Апцыянальна: Каб стварыць індэксы ўручную, выкарыстоўвайце **Кансоль адміністратара** для стварэння індэкса па змаўчанні.
   
    Прыкладанне створыць індэксы аўтаматычна, як толькі Elasticsearch будзе запушчаны, пры ўмове, што індэксы не знойдзены.

## Настройка індэкса

1. Карыстальніку можа спатрэбіцца наладзіць параметры індэкса, напрыклад, для змены канфігурацыі мовы (гл. [es/README.md](https://github.com/geonetwork/core-geonetwork/tree/main/es#readme)).

2. Праверце канфігурацыйны файл у **`$GN_DATA_DIRECTORY/config/index`**.

3. Каб уручную выдаліць і перастварыць індэкс, выкарыстоўвайце наступнае:
    
    ``` shell
    cd $GN_DATA_DIRECTORY/config/index
    curl -X DELETE http://localhost:9200/features
    curl -X DELETE http://localhost:9200/records
    curl -X DELETE http://localhost:9200/searchlogs
    
    curl -X PUT http://localhost:9200/features -H 'Content-Type: application/json' -d @features.json
    curl -X PUT http://localhost:9200/records -H 'Content-Type: application/json' -d @records.json
    curl -X PUT http://localhost:9200/searchlogs -H 'Content-Type: application/json' -d @searchlogs.json
    ```

## Праверка ўстаноўкі Elasticsearch

1. Перайдзіце на старонку адміністравання Elasticsearch па адрасе <http://localhost:9200/>.

    !!! note
    
        Адкрываць порт `9200` вонкі не трэба і не рэкамендуецца. GeoNetwork абараняе экземпляр Elasticsearch, прадастаўляючы доступ толькі да API пошуку і кіруючы правамі карыстальніка.

## Настройка падключэння GeoNetwork да Elasticsearch

Па змаўчанні GeoNetwork чакае, што Elasticsearch запушчаны па адрасе <http://localhost:9200> без аўтэнтыфікацыі. Калі ваш сервер Elasticsearch знаходзіцца на іншым хосце, порце або патрабуе аўтэнтыфікацыі, вам трэба будзе наладзіць параметры падключэння, выкарыстоўваючы адзін з наступных метадаў:

* Вызначце параметры падключэння ва ўласцівасцях Java.

  ```shell
  export JAVA_OPTS="$JAVA_OPTS -Des.protocol=http -Des.port=9200 -Des.host=localhost  -Des.protocol=http -Des.username= -Des.password="
  ```

* Вызначце параметры падключэння ў пераменных асяроддзя.

  ```shell
  export GEONETWORK_ES_HOST=localhost
  export GEONETWORK_ES_PROTOCOL=http
  export GEONETWORK_ES_PORT=9200
  export GEONETWORK_ES_USERNAME=
  export GEONETWORK_ES_PASSWORD=
  ```

* Адрэдагуйце значэнні ў ```WEB-INF/config.properties``` (не рэкамендуецца):

  ```properties
  es.protocol=#{systemEnvironment['GEONETWORK_ES_PROTOCOL']?:'http'}
  es.port=#{systemEnvironment['GEONETWORK_ES_PORT']?:9200}
  es.host=#{systemEnvironment['GEONETWORK_ES_HOST']?:'localhost'}
  es.username=#{systemEnvironment['GEONETWORK_ES_USERNAME']?:''}
  es.password=#{systemEnvironment['GEONETWORK_ES_PASSWORD']?:''}
  ```

Пасля завяршэння настройкі неабходна перазапусціць прыкладанне.