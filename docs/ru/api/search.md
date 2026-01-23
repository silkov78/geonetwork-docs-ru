# Служба поиска

GeoNetwork предоставляет доступ к конечным точкам ***Elasticsearch*** `/srv/api/search/records/_search` и `/srv/api/search/records/_msearch`. Эти конечные точки принимают `POST`-запросы, тело которых содержит JSON-запрос Elasticsearch.

**Справочные материалы:**

-   [Search API](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html) (Руководство Elasticsearch)
-   [Multi search API](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-multi-search.html) (Руководство Elasticsearch)

## Примеры поисковых API-запросов

Этот раздел содержит несколько примеров `POST`-запросов к конечной точке `/srv/api/search/records/_search`:

1.  Для тестирования примеров перейдите к документации Swagger API по адресу `/srv/api/index.html`.

2.  Найдите заголовок *search* и конечную точку `POST` `/search/records/_search`.

3.  Используйте кнопку *Try it out* со следующими параметрами:
     
     * **bucket**: `metadata`
     * **relatedType**: (оставьте пустым)
     * **Request body**: выберите один из примеров ниже.

4.  Нажмите **Execute**, чтобы выполнить пример.

     ![](img/swagger-search-endpoint.png)

### Запрос текстового поиска

Запрос по любому полю для метаданных, содержащих строку `infrastructure`, с использованием синтаксиса Lucene и с исключением шаблонов метаданных:

```json
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "query": "+anytext:infrastructure "
          }
        }
      ],
      "filter": [
        {
          "term": {
            "isTemplate": {
              "value": "n"
            }
          }
        }
      ]
    }
  }
}
```

### Выборка результатов

Запрос по любому полю для метаданных, содержащих строку `infrastructure`, с использованием синтаксиса Lucene и с исключением шаблонов метаданных, возвращающий только часть информации:

```json
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "query": "+anytext:infrastructure "
          }
        }
      ],
      "filter": [
        {
          "term": {
            "isTemplate": {
              "value": "n"
            }
          }
        }
      ]
    }
  },
  "_source": {
    "includes": [
      "uuid",
      "id",
      "resourceType",
      "resourceTitle*",
      "resourceAbstract*"
    ]
  }
}
```

### Запрос по наборам данных

Запрос по наборам данных, заголовок которых содержит строку `infrastructure`, с использованием синтаксиса Lucene и с исключением шаблонов метаданных:

```json
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "query": "+anytext:infrastructure +resourceType:dataset"
          }
        }
      ],
      "filter": [
        {
          "term": {
            "isTemplate": {
              "value": "n"
            }
          }
        }
      ]
    }
  }
}
```

### Запрос по дате ревизии

Запрос по наборам данных с датой ревизии в июне 2019 года и с исключением шаблонов метаданных:

```json
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "resourceType": {
              "value": "dataset"
            }
          }
        },
        {
          "range": {
            "resourceTemporalDateRange": {
              "gte": "2019-06-01",
              "lte": "2019-06-30",
              "relation": "intersects"
            }
          }
        }
      ],
      "filter": [
        {
          "term": {
            "isTemplate": {
              "value": "n"
            }
          }
        }
      ]
    }
  }
}
```