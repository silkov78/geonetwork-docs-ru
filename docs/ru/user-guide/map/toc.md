# Панель содержания

**************************

Панель содержания (далее сокращенно TOC - Table of Contents) — это пространство, где перечислены все слои и группы слоев. С помощью этой панели также можно выполнять следующие операции:

* Добавлять и удалять слои и группы

* Выполнять поиск среди слоев

* Изменять положение (и, следовательно, порядок отображения на карте) слоев и групп

* Устанавливать некоторые опции отображения непосредственно с панели

* Управлять слоями и группами, а также запрашивать слои с помощью действий на панели инструментов

## Настройки и панель инструментов TOC

Пользователь может получить доступ к TOC с помощью кнопки <img src="../img/button/show-layers.jpg" class="ms-docbutton"/> в левом верхнем углу окна просмотра карты. После этого появится следующая панель:

<img src="../img/toc/toc.jpg" class="ms-docimage"  style="max-width:400px;" />

С помощью *панели инструментов TOC* пользователь может:

* **Добавить новый слой** с помощью кнопки <img src="../img/button/add_layer_button.jpg" class="ms-docbutton"/>: откроется панель [Каталога](catalog.md#catalog-services), и пользователь сможет выбрать желаемый слой для добавления его на карту с помощью кнопки <img src="../img/button/add_to_map_button.jpg" class="ms-docbutton"/>.

<video class="ms-docimage" controls><source src="../img/toc/add-layer.mp4"/></video>

* **Добавить новую группу** с помощью кнопки <img src="../img/button/add_group_button.jpg" class="ms-docbutton"/>: откроется следующее окно, где пользователь может ввести название группы и добавить ее в TOC с помощью кнопки <img src="../img/button/add_group_confirm_button.jpg" class="ms-docbutton"/>.

<video class="ms-docimage" controls><source src="../img/toc/add-group.mp4"/></video>

* **Добавить новые Аннотации** с помощью кнопки <img src="../img/button/annotations2.jpg" class="ms-docbutton" style="max-height:30px;"/>, как описано в разделе [Аннотации](annotations.md).

Приложение позволяет пользователю настраивать отображение групп и слоев в *TOC*, включая/отключая некоторые опции с помощью кнопки <img src="../img/button/toc-settings-button.jpg" class="ms-docbutton"/>:

<img src="../img/toc/toc-settings-panel.jpg" class="ms-docimage"  style="max-width:350px;"/>

Здесь пользователь может:

* Включить/отключить открытие TOC при инициализации карты с помощью кнопки <img src="../img/button/arrow-button.jpg" class="ms-docbutton"/>.

* Изменить тему TOC, выбрав между **Темой по умолчанию** или **Темой легенды** с помощью кнопки <img src="../img/button/theme-button.jpg" class="ms-docbutton"/>. С **Темой легенды** у пользователя нет возможности перетаскивать положение групп/слоев. Этот режим предоставляет упрощенный и более легкий TOC при необходимости.

* Включить/отключить возможность отображения полного названия групп/слоев с помощью кнопки <img src="../img/button/text-button.jpg" class="ms-docbutton"/>.

* **Показать/скрыть ползунок прозрачности** для слоев с помощью кнопки <img src="../img/button/opacity-slider-button.jpg" class="ms-docbutton"/>.

* Если *Ползунок прозрачности* включен, **Показать/скрыть подсказку о прозрачности** для слоев с помощью кнопки <img src="../img/button/opacity-tooltip-button.jpg" class="ms-docbutton"/>.

При щелчке правой кнопкой мыши по телу TOC, в дополнение к опциям, доступным в меню *Настройки TOC*, описанном выше, пользователь может получить доступ к некоторым дополнительным настройкам, таким как:

<video class="ms-docimage" controls><source src="../img/toc/toc-settings-panel2.mp4"/></video>

* Показать все группы и слои, присутствующие в TOC, включив **Показать все дочерние узлы** с помощью кнопки <img src="../img/button/show-all-child-nodes.jpg" class="ms-docbutton"/>.

* Скрыть все группы и слои, присутствующие в TOC, включив **Скрыть все дочерние узлы** с помощью кнопки <img src="../img/button/hide-all-child-nodes.jpg" class="ms-docbutton"/>.

* Свернуть все группы, присутствующие в TOC, включив **Свернуть все дочерние узлы** с помощью кнопки <img src="../img/button/collapse-all-child-nodes.jpg" class="ms-docbutton"/>.

* Развернуть все группы, присутствующие в TOC, включив **Развернуть все дочерние узлы** с помощью кнопки <img src="../img/button/expand-all-child-nodes.jpg" class="ms-docbutton"/>. Легенда каждого слоя также разворачивается.

* Добавить новую группу в TOC с помощью кнопки <img src="../img/button/add-group.jpg" class="ms-docbutton"/>.

* Приблизить карту к экстенту, охватывающему все слои TOC, с помощью кнопки <img src="../img/button/zoom-extent.jpg" class="ms-docbutton"/>.

### Поиск слоев

С помощью TOC также можно выполнять поиск среди добавленных слоев. Эту операцию можно выполнить, просто введя имя (или его часть) слоя в строку поиска:

<img src="../img/toc/search.jpg" class="ms-docimage"  style="max-width:300px;"/>

### Выбор положения слоев и групп

Пользователь может изменить положение *Слоя* в TOC, щелкнув по значку перетаскивания слоя <img src="../img/button/drag-drop-button.jpg" class="ms-docbutton"/>.
Можно изменить положение слоя внутри его группы или переместить его в другую группу. После этого порядок слоя на карте также изменится соответствующим образом.
Ниже приведен пример изменения положения слоя с помощью функции перетаскивания.

<video class="ms-docimage" controls><source src="../img/toc/ded-layers.mp4"/></video>

Ту же операцию можно выполнить и с любой *Группой* слоев.

<video class="ms-docimage" controls><source src="../img/toc/ded-groups.mp4"/></video>

Положение слоев также можно изменить, нажав на кнопку **Настройки слоя** <img src="../img/button/properties.jpg" class="ms-docbutton"/>, доступную на панели инструментов. Она появляется после выбора слоя в TOC. Эта кнопка открывает панель, где пользователь может выбрать группу назначения:

<img src="../img/toc/settings-group.jpg" class="ms-docimage"  style="max-width:350px;"/>

### Опции отображения на панели

Непосредственно из интерфейса TOC пользователь может получить доступ к различным опциям отображения. В частности, для слоев можно:

<img src="../img/toc/layer-legend.jpg" class="ms-docimage"/>

* Включить/отключить видимость слоя с помощью флажка слева от элемента слоя <img src="../img/button/check-box.jpg" class="ms-docbutton"/>

* Развернуть <img src="../img/button/expand-all-child-nodes.jpg" class="ms-docbutton"/> или свернуть <img src="../img/button/collapse-all-child-nodes.jpg" class="ms-docbutton"/> легенду слоя.

* Настроить прозрачность слоя на карте, перемещая ползунок прозрачности.

Для групп пользователь может:

<img src="../img/toc/group.jpg" class="ms-docimage" style="max-width:500px;"/>

* Развернуть <img src="../img/button/expand-all-child-nodes.jpg" class="ms-docbutton"/> или свернуть <img src="../img/button/collapse-all-child-nodes.jpg" class="ms-docbutton"/> слои или группы внутри.

* Включить/отключить видимость группы с помощью флажка слева от элемента группы <img src="../img/button/check-box.jpg" class="ms-docbutton"/>

!!! примечание
   Когда пользователь отключает видимость группы, видимость на карте всех слоев и групп внутри нее изменяется соответствующим образом, но их исходное состояние видимости в TOC остается неизменным; просто все вложенные элементы становятся серыми, чтобы указать, что они не видны на карте, а другие функции (например, через контекстное меню) остаются доступными.

## Настройки и панель инструментов группы

После выбора группы появляется следующая панель инструментов, и пользователь может:

<img src="../img/toc/group-toolbar.jpg" class="ms-docimage"/>

* **Добавить слой в выбранную группу** с помощью кнопки <img src="../img/button/add_layer_button.jpg" class="ms-docbutton"/> (можно добавить один или несколько слоев в группу)

* **Добавить подгруппу в выбранную группу** с помощью кнопки <img src="../img/button/add_group_button.jpg" class="ms-docbutton"/> (можно добавить одну или несколько подгрупп в выбранную группу)

* **Приблизить к экстенту выбранных слоев**, чтобы приблизить карту к экстенту, охватывающему все слои, принадлежащие данной группе, с помощью кнопки <img src="../img/button/zoom-layer.jpg" class="ms-docbutton"/>

* Открыть **Настройки группы** с помощью кнопки <img src="../img/button/properties.jpg" class="ms-docbutton"/>: откроется панель *Настройки*, и пользователь может:
  **-** Изменить **Заголовок**
  **-** Установить перевод заголовка группы, открыв всплывающее окно **Локализовать текст** с помощью кнопки <img src="../img/button/localize_button.jpg" class="ms-docbutton"/>. Таким образом, язык заголовка будет меняться в соответствии с текущим языком приложения 
  **-** Редактировать **Описание** группы
  **-** Настроить **Подсказку**, которая появляется при наведении курсора на элемент группы в TOC. В этом случае пользователь может решить, будет ли отображаться *Заголовок*, *Описание*, оба или ничего. Кроме того, можно установить *Расположение* подсказки, выбрав *Сверху*, *Справа* или *Снизу*. В любом случае, если заголовок полностью виден в TOC, подсказка не появляется.

<img src="../img/toc/group-settings-panel.jpg" class="ms-docimage"/>

* **Удалить выбранную группу** и ее содержимое с помощью кнопки <img src="../img/button/delete.jpg" class="ms-docbutton"/>

Щелкнув правой кнопкой мыши по группе, пользователь может изменить некоторые свойства группы, такие как:

<video class="ms-docimage" controls><source src="../img/toc/group-settings-panel.mp4"/></video>

* Показать все группы и слои, присутствующие в выбранной группе, включив **Показать все дочерние узлы** с помощью кнопки <img src="../img/button/show-all-child-nodes.jpg" class="ms-docbutton"/>.

* Скрыть все группы и слои, присутствующие в выбранной группе, включив **Скрыть все дочерние узлы** с помощью кнопки <img src="../img/button/hide-all-child-nodes.jpg" class="ms-docbutton"/>.

* Активировать взаимоисключающую видимость групп и слоев внутри выбранной группы, включив **Активировать взаимоисключающую видимость дочерних узлов** с помощью кнопки <img src="../img/button/mutually-exclusive-visibility.jpg" class="ms-docbutton"/>. Таким образом, на карте одновременно может быть виден только один слой или подгруппа.

* Свернуть все группы, присутствующие в выбранной группе, включив **Свернуть все дочерние узлы** с помощью кнопки <img src="../img/button/collapse-all-child-nodes.jpg" class="ms-docbutton"/>.

* Развернуть все группы, присутствующие в выбранной группе, включив **Развернуть все дочерние узлы** с помощью кнопки <img src="../img/button/expand-all-child-nodes.jpg" class="ms-docbutton"/>. Легенда каждого слоя также разворачивается.

* Добавить подгруппу под выбранной группой с помощью кнопки <img src="../img/button/add-group.jpg" class="ms-docbutton"/>.

* Приблизить карту к экстенту слоев выбранной группы с помощью кнопки <img src="../img/button/zoom-extent.jpg" class="ms-docbutton"/>.

* Удалить выбранную группу с помощью кнопки <img src="../img/button/remove-button.jpg" class="ms-docbutton"/>.

## Настройки и панель инструментов слоя

При выборе слоя панель инструментов выглядит следующим образом:

<img src="../img/toc/layer-toolbar.jpg" class="ms-docimage"/>

В этом случае пользователю разрешено:

* **Приблизить к экстенту выбранного слоя** <img src="../img/button/zoom-layer.jpg" class="ms-docbutton"/>: чтобы приблизить карту к экстенту слоя

* Получить доступ к [Настройкам выбранного слоя](layer-settings.md#layer-settings) <img src="../img/button/properties.jpg" class="ms-docbutton"/>

* [Установить фильтр](filtering-layers.md#filtering-layers) для этого слоя <img src="../img/button/filter-layer.jpg" class="ms-docbutton"/>

* Получить доступ к [Таблице атрибутов](attributes-table.md) <img src="../img/button/attributes-table.jpg" class="ms-docbutton"/>

* **Удалить** выбранный слой <img src="../img/button/delete.jpg" class="ms-docbutton"/>

* [Создать виджеты](widgets.md#widgets) для выбранного слоя <img src="../img/button/widgets.jpg" class="ms-docbutton"/>

* [Экспортировать](export-data.md#export-layer-data) данные выбранного слоя <img src="../img/button/export_data.jpg" class="ms-docbutton"/>

* Открыть **Метаданные слоя** <img src="../img/button/info_button.jpg" class="ms-docbutton"/> (если настроено), чтобы получить метаданные слоя из удаленного источника каталога.

<img src="../img/toc/layer_metadata_panel.jpg" class="ms-docimage" style="max-width:600px;"/>

!!! примечание
    **Инструмент "Метаданные"** по умолчанию не настроен. Полная документация по его настройке доступна в рамках [документации по плагинам TOC](https://mapstore.geosolutionsgroup.com/mapstore/docs/api/plugins#plugins.TOC) (см. *metadataOptions*). После настройки **Инструмента "Метаданные"** приложение сможет загружать метаданные слоя из удаленной службы CSW и анализировать их для представления пользователю в соответствии с предоставленной конфигурацией плагина. Эта функция автоматически работает в случае слоев WMS, поступающих из источника каталога CSW, в то время как для слоев, поступающих непосредственно из источника каталога WMS, в GetCapabilities слоя WMS должна присутствовать [Ссылка на метаданные](https://docs.geoserver.org/latest/en/user/data/webadmin/layers.html#basic-info).

Щелкнув правой кнопкой мыши по слою, пользователь может управлять некоторыми свойствами слоя, такими как:

<video class="ms-docimage" controls><source src="../img/toc/layer-settings-panel.mp4"/></video>

* Приблизить карту к экстенту выбранного слоя с помощью кнопки <img src="../img/button/zoom-extent.jpg" class="ms-docbutton"/>.

* Удалить выбранный слой с помощью кнопки <img src="../img/button/remove-button.jpg" class="ms-docbutton"/>.

* Включить инструмент **Шторка** на карте для выбранного слоя с помощью кнопки <img src="../img/button/swipe-button.jpg" class="ms-docbutton"/>.

<img src="../img/toc/swipe_on_map.jpg" class="ms-docimage" style="max-width:600px;"/>

Пользователь может изменить ориентацию шторки с *Вертикальной* на *Горизонтальную*, нажав на кнопку <img src="../img/button/swipe-icon.jpg" class="ms-docbutton"/>, которая появилась справа от названия слоя.

* Включить инструмент **Лупа** на карте для выбранного слоя с помощью кнопки <img src="../img/button/syp-glass-button.jpg" class="ms-docbutton"/>.

<img src="../img/toc/spy_on_map.jpg" class="ms-docimage" style="max-width:600px;"/>

Пользователь может изменить размер лупы (`радиус`), нажав на кнопку <img src="../img/button/syp-glass-icon.jpg" class="ms-docbutton"/>, которая появилась справа от названия слоя.