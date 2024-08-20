# Сбор метаданных из CSW-сервисов

Такой сборщик данных будет подключаться к удаленному серверу CSW и извлекать записи метаданных, которые соответствуют указанным параметрам запроса.

## Добавление CSW-сборщика

Доступные параметры следующие:

-   **Сайт** - Параметры удаленного сайта.
    -    *Имя* - Это краткое описание удаленного сайта. Оно будет показано на главной странице сбора в качестве имени для этого экземпляра CSW-харвестера.
    -    *URL-адрес сервиса* - URL-адрес документа возможностей сервера CSW, который будет собираться. Например, <http://geonetwork-site.com/srv/eng/csw?service=CSW&request=GetCabilities&version=2.0.2>. Этот документ используется для обнаружения местоположения сервисов для вызова для запроса и извлечения метаданных.
    -    *Значок (иконка)* - Значок будет использоваться при отображении собранных записей метаданных в результатах поиска.
    -    *Использовать учетную запись* - Учетные данные для базовой HTTP-аутентификации на сервере CSW.
-   **Критерии поиска** - С помощью кнопки `Добавить` можно добавить несколько критериев поиска. Вы можете запрашивать только поля, распознаваемые протоколом CSW.
-   **Параметры** - Параметры расписания (периодичности), согласно которым сборщик будет собирать метаданные.
-   **Параметры** - специфические параметры сбора для этого харвестера.
    -    *Проверка* - метаданные будут проверены после извлечения. Если проверка не пройдена, метаданные будут пропущены.
-   **Привилегии** - Назначение привилегий собранным метаданным.
-   **Категории**

-   **Site** - Options about the remote site.
    -   *Name* - This is a short description of the remote site. It will be shown in the harvesting main page as the name for this instance of the CSW harvester.
    -   *Service URL* - The URL of the capabilities document of the CSW server to be harvested. eg. <http://geonetwork-site.com/srv/eng/csw?service=CSW&request=GetCabilities&version=2.0.2>. This document is used to discover the location of the services to call to query and retrieve metadata.
    -   *Icon* - An icon to assign to harvested metadata. The icon will be used when showing harvested metadata records in the search results.
    -   *Use account* - Account credentials for basic HTTP authentication on the CSW server.
-   **Search criteria** - Using the Add button, you can add several search criteria. You can query only the fields recognised by the CSW protocol