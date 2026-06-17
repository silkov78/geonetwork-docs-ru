# Установка поисковой платформы

Поисковый движок GeoNetwork построен на базе Elasticsearch. Платформа используется для индексации записей, а также для индексации данных WFS (см. [Анализ и визуализация данных](../user-guide/analyzing/data.md)).

Для работы GeoNetwork требуется установка экземпляра [Elasticsearch](https://www.elastic.co/products/elasticsearch) рядом с каталогом.

## Совместимость с Elasticsearch

Версия Java-клиента Elasticsearch: 8.19.13

| Версия Elasticsearch | Совместимость |
|-----------------------| ------------- |
| Elasticsearch 8.19.13 | рекомендуется |
| Elasticsearch 8.14.x  | минимальная   |

Более старые версии могут поддерживаться, но не тестировались.

## Установка

=== "Ручная установка"
        
    1. **Загрузка:** Elasticsearch `8.19.13` с сайта <https://www.elastic.co/downloads/elasticsearch> и распакуйте файл.

        ``` shell
        wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.19.13.tar.gz
        tar xvfz elasticsearch-8.19.13.tar.gz
        ```

    2. **Запуск**: Вручную запустите Elasticsearch с помощью:

        ``` shell
        elasticsearch-8.19.13/bin/elasticsearch
        ```

    3. **Остановка**: Вручную остановите Elasticsearch с помощью:

        ``` shell
        elasticsearch-8.19.13/bin/elasticsearch stop
        ```
        
=== "Установка с помощью Maven"

    1. Разработчикам рекомендуется запускать Elasticsearch с использованием Maven, чтобы выполнять тестирование на той версии Elasticsearch, которая предназначена для следующего релиза.
    
        !!! note
            
            При запуске из исходного кода версия Elasticsearch берется из свойства `es.version` в файле [pom.xml](https://github.com/geonetwork/core-geonetwork/blob/main/pom.xml).
    
    2. **Загрузка**: Запустите maven из директории **`es`**.

          ``` shell
          cd es
          mvn install -Pes-download
          ```
    
    3. **Запуск**: Используйте плагин maven ``exec`` для запуска Elasticsearch:
    
        ``` shell
        mvn exec:exec -Des-start
        ```
        
        Elasticsearch будет работать в режиме foreground, выводя сообщения в консоль.

    4. **Остановка**: Для остановки Elasticsearch используйте комбинацию ++ctrl+c++, чтобы остановить процесс maven.

## Создание индекса

1. GeoNetwork подключится к Elasticsearch при запуске, и индексы будут созданы, если они не существуют.
   
    * GeoNetwork запустится, даже если индекс Elasticsearch недоступен (или еще не запущен).
    
    * Если GeoNetwork не может связаться с Elasticsearch, будет отображено предупреждение.
    
    * Когда индекс Elasticsearch станет доступен, индексы будут созданы, если их еще нет.

2. Опционально: Чтобы создать индексы вручную, используйте **Консоль администратора** для создания индекса по умолчанию.
   
    Приложение создаст индексы автоматически, как только Elasticsearch будет запущен, при условии, что индексы не найдены.

## Настройка индекса

1. Пользователю может потребоваться настроить параметры индекса, например, для изменения конфигурации языка (см. [es/README.md](https://github.com/geonetwork/core-geonetwork/tree/main/es#readme)).

2. Проверьте конфигурационный файл в **`$GN_DATA_DIRECTORY/config/index`**.

3. Чтобы вручную удалить и пересоздать индекс, используйте следующее:
    
    ``` shell
    cd $GN_DATA_DIRECTORY/config/index
    curl -X DELETE http://localhost:9200/features
    curl -X DELETE http://localhost:9200/records
    curl -X DELETE http://localhost:9200/searchlogs
    
    curl -X PUT http://localhost:9200/features -H 'Content-Type: application/json' -d @features.json
    curl -X PUT http://localhost:9200/records -H 'Content-Type: application/json' -d @records.json
    curl -X PUT http://localhost:9200/searchlogs -H 'Content-Type: application/json' -d @searchlogs.json
    ```

## Проверка установки Elasticsearch

1. Перейдите на страницу администрирования Elasticsearch по адресу <http://localhost:9200/>.

    !!! note
    
        Открывать порт `9200` наружу не нужно и не рекомендуется. GeoNetwork защищает экземпляр Elasticsearch, предоставляя доступ только к API поиска и управляя правами пользователя.

## Настройка подключения GeoNetwork к Elasticsearch

По умолчанию GeoNetwork ожидает, что Elasticsearch запущен по адресу <http://localhost:9200> без аутентификации. Если ваш сервер Elasticsearch находится на другом хосте, порту или требует аутентификации, вам нужно будет настроить параметры подключения, используя один из следующих методов:

* Определите параметры подключения в свойствах Java.

  ```shell
  export JAVA_OPTS="$JAVA_OPTS -Des.protocol=http -Des.port=9200 -Des.host=localhost  -Des.protocol=http -Des.username= -Des.password="
  ```

* Определите параметры подключения в переменных окружения.

  ```shell
  export GEONETWORK_ES_HOST=localhost
  export GEONETWORK_ES_PROTOCOL=http
  export GEONETWORK_ES_PORT=9200
  export GEONETWORK_ES_USERNAME=
  export GEONETWORK_ES_PASSWORD=
  ```

* Отредактируйте значения в ```WEB-INF/config.properties``` (не рекомендуется):

  ```properties
  es.protocol=#{systemEnvironment['GEONETWORK_ES_PROTOCOL']?:'http'}
  es.port=#{systemEnvironment['GEONETWORK_ES_PORT']?:9200}
  es.host=#{systemEnvironment['GEONETWORK_ES_HOST']?:'localhost'}
  es.username=#{systemEnvironment['GEONETWORK_ES_USERNAME']?:''}
  es.password=#{systemEnvironment['GEONETWORK_ES_PASSWORD']?:''}
  ```

После завершения настройки необходимо перезапустить приложение.