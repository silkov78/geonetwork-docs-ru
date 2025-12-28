# Выполнение измерений

Инструмент "Измерение" позволяет пользователю выполнять различные виды измерений (такие как расстояние, площадь, азимут и т. д.) на карте. Он также предоставляет некоторые дополнительные функции, которые описаны в этом разделе документации. Инструмент доступен с [Боковой панели инструментов](mapstore-toolbars.md#side-toolbar) при выборе кнопки <img src="../img/button/measurament.jpg" class="ms-docbutton" style="max-height:20px;"/>, которая открывает следующую панель инструментов:

<img src="../img/measure/measure.jpg" class="ms-docimage" style="max-width:600px;"/>

С помощью этого окна можно:

* Измерить расстояние <img src="../img/button/measure-distance.jpg" class="ms-docbutton"/>

* Измерить площадь <img src="../img/button/measure-area.jpg" class="ms-docbutton"/>

* Измерить азимут <img src="../img/button/measure-bearing.jpg" class="ms-docbutton"/>

* Очистить измерения <img src="../img/button/delete_button.jpg" class="ms-docbutton"/>

* Экспортировать измерения в *GeoJSON* <img src="../img/button/json_export_button.jpg" class="ms-docbutton"/>

* Добавить измерение в качестве слоя в [Панели содержания](toc.md#table-of-contents) <img src="../img/button/layers_button.jpg" class="ms-docbutton"/>

* Добавить измерение в качестве [Аннотации](annotations.md) <img src="../img/button/add-as-annotation.jpg" class="ms-docbutton"/>

!!! примечание
    Пользователь может выполнять несколько измерений одновременно на карте, а затем отменить их с помощью кнопки **Очистить измерения** <img src="../img/button/delete_button.jpg" class="ms-docbutton"/>

## Измерение расстояния

Как только открывается окно измерения, по умолчанию выбрана опция измерения расстояния <img src="../img/button/measure-distance-green.jpg" class="ms-docbutton"/>. Для выполнения измерения расстояния каждый щелчок на карте соответствует сегменту линии (требуется как минимум один сегмент), а двойной щелчок вставляет последний сегмент линии и завершает сеанс рисования.

<video class="ms-docimage" style="max-width:600px;" controls><source src="../img/measure/measure-distance-ex.mp4"/></video>

Доступные единицы измерения:

<img src="../img/measure/distance-uom.jpg" class="ms-docimage" style="max-width:300px;"/>

!!! примечание
    Длина сегмента линии отображается на карте вместе с измерением общей длины всех сегментов.

## Измерение площади

После выбора кнопки **Измерить площадь** <img src="../img/button/measure-area-green.jpg" class="ms-docbutton"/> можно начать сеанс рисования (в этом случае необходимо указать как минимум 3 вершины). Как и при измерении расстояния, каждый щелчок соответствует вершине, а двойной щелчок указывает последнюю.

<video class="ms-docimage" style="max-width:600px;" controls><source src="../img/measure/measure-area-ex.mp4"/></video>

В этом случае доступны следующие единицы измерения:

<img src="../img/measure/area-uom.jpg" class="ms-docimage" style="max-width:300px;"/>

!!! примечание
    Длина каждой стороны полигона отображается на карте вместе с его периметром и площадью.

## Измерение азимута

Измерение азимута позволяет измерять направления и углы. В системе четвертных румбов азимут линии измеряется как угол от опорного меридиана, либо северного, либо южного, в сторону востока или запада. Азимуты в системе четвертных румбов записываются как меридиан, угол и направление. Например, азимут N 30 W определяет угол 30 градусов к западу от севера. Азимут S 15 E определяет угол 15 градусов к востоку от юга.
После выбора кнопки **Измерить азимут** <img src="../img/button/measure-bearing-green.jpg" class="ms-docbutton"/> пользователь может нарисовать линию только с двумя вершинами, которые указывают соответственно начальную и конечную точки.

<video class="ms-docimage" style="max-width:600px;" controls><source src="../img/measure/measure-bearing-ex.mp4"/></video>

## Экспорт измерения

Измерения, нарисованные на карте, можно экспортировать в формат `GeoJson` с помощью кнопки <img src="../img/button/json_export_button.jpg" class="ms-docbutton"/>.

## Добавление измерения в качестве слоя

После того как измерение нарисовано, его можно добавить в качестве слоя с помощью кнопки <img src="../img/button/layers_button.jpg" class="ms-docbutton"/>. Созданный слой добавляется в [Панели содержания](toc.md#table-of-contents) следующим образом:

<img src="../img/measure/as_layer.jpg" class="ms-docimage"/>

## Добавление измерения в качестве аннотации

После того как измерение нарисовано, его можно добавить в качестве [Аннотации](annotations.md) с помощью кнопки <img src="../img/button/add-as-annotation.jpg" class="ms-docbutton"/>. Откроется следующая панель:

<img src="../img/measure/add-as-annotation-ex.jpg" class="ms-docimage"/>

Начиная с этого шага, процесс создания такой же, как описано в разделе [Аннотации](annotations.md).

## Измерения в 3D-навигации

Когда включена [3D-навигация](navigation-toolbar.md#3d-navigation), у пользователя есть возможность выполнять измерения расстояния, площади, координат точек, высоты от рельефа, углов и уклонов на 3D-карте.

!!! примечание
    3D-режим приложения работает на базе библиотеки картографирования CesiumJS, где для представления картографических объектов используется эллипсоидальная система координат. По этой причине все измерения, выполненные с помощью инструмента измерения, следует интерпретировать как имеющие высоту, рассчитанную над эллипсоидом.

### Измерение расстояния в 3D-навигации

Как только открывается окно измерения, по умолчанию выбрана опция **Измерить расстояние в 3D-пространстве** <img src="../img/button/measure-distance-on-3d.jpg" class="ms-docbutton"/>. Для выполнения измерения расстояния каждый щелчок на карте соответствует сегменту линии (требуется как минимум один сегмент), а двойной щелчок вставляет последний сегмент линии и завершает сеанс рисования.

<video class="ms-docimage" style="max-width:600px;" controls><source src="../img/measure/measure-distance-3d-ex.mp4"/></video>

### Измерение геодезического расстояния

После выбора кнопки **Измерить геодезическое расстояние** <img src="../img/button/measure-distance-green.jpg" class="ms-docbutton"/> можно начать сеанс рисования. Как и при измерении расстояния, каждый щелчок соответствует вершине (требуется как минимум две вершины), а двойной щелчок указывает последнюю. С этим типом измерения также возможно в 3D-режиме получить геодезическое расстояние, рассчитанное на абсолютном нуле эллипсоида WGS84.

<video class="ms-docimage" style="max-width:600px;" controls><source src="../img/measure/measure-geodesic-ex.mp4"/></video>

### Измерение площади в 3D-навигации

После выбора кнопки **Измерить площадь в 3D-пространстве** <img src="../img/button/measure-area-on-3d.jpg" class="ms-docbutton"/> можно начать сеанс рисования (в этом случае необходимо указать как минимум 3 вершины). Как и при измерении расстояния, каждый щелчок соответствует вершине, а двойной щелчок указывает последнюю.

<video class="ms-docimage" style="max-width:600px;" controls><source src="../img/measure/measure-area-3d-ex.mp4"/></video>

### Измерение координат точки

После выбора кнопки **Измерить координаты точки** <img src="../img/button/measure-point-coordinate-on-3d.jpg" class="ms-docbutton"/> редактор может щелкнуть по точке на карте и узнать широту, долготу и высоту этой точки.

<video class="ms-docimage" style="max-width:600px;" controls><source src="../img/measure/measure-point-3d-ex.mp4"/></video>

### Измерение высоты от рельефа

После выбора кнопки **Измерить высоту от рельефа** <img src="../img/button/measure-height-from-terrain-on-3d.jpg" class="ms-docbutton"/> можно щелкнуть по точке на карте и узнать расстояние от этой точки до рельефа.

<video class="ms-docimage" style="max-width:600px;" controls><source src="../img/measure/measure-height-from-terrain-3d-ex.mp4"/></video>

### Измерение угла

После выбора кнопки **Измерить угол в 3D-пространстве** <img src="../img/button/measure-angle-on-3d.jpg" class="ms-docbutton"/> редактор может нарисовать три точки на карте и получить значение угла.

<video class="ms-docimage" style="max-width:600px;" controls><source src="../img/measure/measure-angle-3d-ex.mp4"/></video>

### Измерение уклона

После выбора кнопки **Измерить уклон** <img src="../img/button/measure-slope-on-3d.jpg" class="ms-docbutton"/> редактор может нарисовать три точки на карте, чтобы создать треугольную поверхность и получить значение уклона.

<video class="ms-docimage" style="max-width:600px;" controls><source src="../img/measure/measure-slope-3d-ex.mp4"/></video>