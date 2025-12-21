# Секция "Гео-карусель"

**********************

Секция "Гео-карусель" позволяет создать еще один вид иммерсивного опыта, отличный от [иммерсивной секции](immersive-section.md#immersive-section). Редактор истории может определить список карточек карусели, которые будут представлены с сопроводительным описательным контентом и географическим местоположением. В режиме редактирования она состоит из трех элементов: фоновой карты, описательной панели и панели карусели, где редактор может управлять элементами карусели.

<img src="../img/geocarousel-section/geocarousel-section-fd.jpg" class="ms-docimage"/>

## Фон

Панель редактирования фона позволяет добавить карту в качестве фона секции с помощью кнопки **Изменить источник медиа** <img src="../img/button/change-media.jpg" class="ms-docbutton"/>, которая, как обычно, открывает [редактор медиа](media-editor-window.md#media-editor-window).

<img src="../img/immersive-section/bck-toolbar.jpg" class="ms-docimage" width="550px"/>

!!! примечание

    В *секции "Гео-карусель"*, в отличие от [иммерсивной секции](immersive-section.md#immersive-section) и [секции "Заголовок"](title-section.md#title-section), редактор истории может добавить в качестве фона только **карту**.

После выбора *карты* для фона в левом верхнем углу секции появляется панель редактирования, позволяющая редактору истории управлять фоновым контентом.

<img src="../img/geocarousel-section/geocarousel_background_toolbar.jpg" class="ms-docimage"/>

**Панель редактирования фона** позволяет выполнять следующие действия:

<img src="../img/geocarousel-section/geomap-toolbar.jpg" class="ms-docimage" style="width:300px"/>

* **Изменить источник медиа** <img src="../img/button/change-media.jpg" class="ms-docbutton"/> позволяет выбрать медиа-контент для использования в секции; при нажатии этой кнопки открывается [редактор медиа](media-editor-window.md#media-editor-window).

* **Редактировать конфигурацию карты** позволяет [настроить карту](configure-map.md#configure-the-map).

* **Изменить размер** <img src="../img/button/change-size3.jpg" class="ms-docbutton"/> секции между *маленьким*, *средним*, *большим* или *полным*.

* **Выровнять контент** <img src="../img/button/align3.jpg" class="ms-docbutton"/> по *левому краю*, *центру* или *правому краю*.

* **Изменить тему фона** <img src="../img/button/change-field-theme.jpg" class="ms-docbutton"/>, чтобы установить цвет пустого фона: *по умолчанию* (те же настройки темы по умолчанию, что и у истории, см. [Настройки истории](story-setting.md#story-settings)), *светлый*, *темный* или *пользовательский* (позволяет настроить цвет фона).

!!! внимание
    Кнопки *Выровнять контент* и *Изменить тему фона* отключены, если размер карты установлен на полный экран.

## Описательная панель

Описательная панель позволяет размещать описательный контент, такой как *текст*, *изображение*, *видео* или *карта* для различных карточек, составляющих секцию "Гео-карусель". Редактор истории может настраивать ее с помощью **панели инструментов контента**, как объясняется в разделе [Контент](immersive-section.md#content).

<img src="../img/immersive-section/imm-content-toolbar.jpg" class="ms-docimage" style="width:400px"/>

## Карусель

Карусель состоит из списка карточек, которые должны быть связаны с географическим местоположением. Она расположена в нижней части секции "Гео-карусель", и как только секция добавляется в историю, по умолчанию в ней есть следующая пустая карточка, готовая к настройке:

<img src="../img/geocarousel-section/carousel.jpg" class="ms-docimage" style="width:500px"/>

После выбора карточки в режиме редактирования редактор истории может выполнять следующие операции с помощью **панели редактирования карточек**:

<img src="../img/geocarousel-section/items_toolbar.jpg" class="ms-docimage" style="width:180px"/>

* **Редактировать** <img src="../img/button/edit-card-button.jpg" class="ms-docbutton"/> карточку: при нажатии этой кнопки открывается панель **Редактировать карточку**, позволяющая добавить *эскиз* и *заголовок*. Примером может быть следующий:

<img src="../img/geocarousel-section/edit_card_panel.jpg" class="ms-docimage" style="width:500px"/>

* **Удалить** <img src="../img/button/delete_white_button.jpg" class="ms-docbutton"/> карточку.

* **Добавить маркер** <img src="../img/button/add_marker_button.jpg" class="ms-docbutton"/> на карту или изменить текущее положение маркера: при нажатии этой кнопки открывается **встроенный редактор карты**, и редактор истории может щелкнуть по точке на карте, чтобы добавить новый маркер или изменить его положение, как показано ниже:

<video class="ms-docimage" controls><source src="../img/geocarousel-section/add_marker.mp4"/></video>

В левом верхнем углу панели карусели **панель инструментов карусели** позволяет:

<img src="../img/geocarousel-section/carousel_toolbar.jpg" class="ms-docimage" style="width:500px"/>

* **Добавить карточку** <img src="../img/button/++.jpg" class="ms-docbutton"/> в карусель.

* **Удалить** <img src="../img/button/delete_white_button.jpg" class="ms-docbutton"/> *секцию "Гео-карусель"*.

!!! примечание
    Каждый элемент карусели, а также его маркер на карте, пронумерованы для лучшей идентификации.

## Секция "Гео-карусель" в режиме просмотра

В секции "Гео-карусель", в [режиме просмотра](exploring-stories.md#view-mode), пользователь может выполнять следующие операции:

* Выбрать *карточку карусели* для просмотра связанного с ней описательного контента.

<video class="ms-docimage" style="width:700px" controls><source src="../img/geocarousel-section/items.mp4"/></video>

* Выбрать *маркер* на карте, чтобы отобразить всплывающее окно с названием его карточки карусели и просмотреть его описательный контент.

<video class="ms-docimage" style="width:700px" controls><source src="../img/geocarousel-section/marker.mp4"/></video>

* Использовать левую и правую стрелки <img src="../img/button/left_right_arrow.jpg" class="ms-docbutton"/> для просмотра различного контента гео-карусели.

<video class="ms-docimage" style="width:700px" controls><source src="../img/geocarousel-section/arrows.mp4"/></video>