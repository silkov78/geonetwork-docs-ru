# Продольный профиль

*******************

Имея в качестве источника ЦМР или батиметрический слой и заданный на нем путь, этот инструмент позволяет рассчитать **Продольный профиль** и отобразить его в виде интерактивного графика.

!!! note "Примечание"
    Плагин работает только в том случае, если в [GeoServer](http://geoserver.org/) правильно установлен **процесс WPS "Продольный профиль"**. Для получения дополнительной информации об этом процессе и его установке обратитесь к официальной [онлайн-документации](https://docs.geoserver.org/latest/en/user/community/wps-longitudinal-profile/index.html). Модуль продольного профиля для GeoServer доступен начиная с версии Geoserver v2.20.x от августа 2023 года.

При нажатии на кнопку **Продольный профиль** <img src="../img/button/long-profile-button.jpg" class="ms-docbutton"/>, доступную на [Боковой панели инструментов](mapstore-toolbars.md#боковая-панель-инструментов), открывается выпадающее меню, в котором пользователь может управлять доступными опциями, включая различные способы расчета профиля:

<img src="../img/longitudinal-profile/dropdown-menu-long-profile.jpg" class="ms-docimage"/>

* Можно нарисовать линию прямо на карте с помощью кнопки <img src="../img/button/drawing-line.jpg" class="ms-docbutton"/>

<video class="ms-docimage" controls><source src="../img/longitudinal-profile/drawing-line.mp4"/></video>

* В качестве альтернативы можно также импортировать линейный профиль в виде векторного файла (доступные форматы: `GeoJSON`, `ShapeFile` или `DXF`) с помощью кнопки <img src="../img/button/import-file.jpg" class="ms-docbutton"/>

<video class="ms-docimage" controls><source src="../img/longitudinal-profile/import-file.mp4"/></video>

* Наконец, с помощью кнопки <img src="../img/button/selection-layer.jpg" class="ms-docbutton"/> пользователь также может выбрать векторный линейный слой в [Панели содержания](toc.md), а затем выбрать на карте линейный объект, представляющий желаемый путь профиля.

<video class="ms-docimage" controls><source src="../img/longitudinal-profile/selection-layer.mp4"/></video>

## График

Когда геометрия пути профиля нарисована на карте, открывается панель **Продольный профиль**, и на вкладке **График** появляется сам график.

<img src="../img/longitudinal-profile/chart-tab.jpg" class="ms-docimage"/>

В то время как ось *X* показывает расстояние от начальной точки заданного пути, ось *Y* показывает высоту точек вдоль профиля, рассчитанную по заданному пути. Пользователь может наводить курсор на график для взаимодействия между графиком и линией на карте следующим образом:

<video class="ms-docimage" controls><source src="../img/longitudinal-profile/interact-with-chart.mp4"/></video>

**Панель инструментов графика**, отображаемая в правом углу графика, позволяет пользователю:

<img src="../img/longitudinal-profile/bar_charts.jpg" class="ms-docimage"/>

* **Скачать** график в формате `png` с помощью кнопки <img src="../img/button/download_png.jpg" class="ms-docbutton"/>.

* **Масштабировать** график с помощью кнопки <img src="../img/button/zoom_chart.jpg" class="ms-docbutton"/>.

* **Перемещать** график с помощью кнопки <img src="../img/button/pan_chart.jpg" class="ms-docbutton"/>.

* **Приблизить** график с помощью кнопки <img src="../img/button/zoom_in_chart.jpg" class="ms-docbutton"/>.

* **Отдалить** график с помощью кнопки <img src="../img/button/zoom_out_chart.jpg" class="ms-docbutton"/>.

* **Автомасштаб** для автоматического масштабирования осей по отображаемым данным с помощью кнопки <img src="../img/button/autoscale_chart.jpg" class="ms-docbutton"/>.

* **Сбросить оси** для возврата графика в исходное состояние с помощью кнопки <img src="../img/button/reset_axes_chart.jpg" class="ms-docbutton"/>.

Также можно экспортировать *Продольный профиль* в виде файла `CSV`, `PNG` или `PDF`.

<img src="../img/longitudinal-profile/export-profile.jpg" class="ms-docimage"/>

## Информация

На вкладке **Информация** представлены все соответствующие показатели, связанные с расчетом продольного профиля. В частности, здесь указаны:

<img src="../img/longitudinal-profile/profile-info.jpg" class="ms-docimage"/>

* Слой, использованный для расчета профиля

* Общая линейная длина профиля

* Суммарный набор высоты

* Суммарная потеря высоты

* Количество обработанных точек (число точек зависит от выбранного шага).

## Настройка параметров

С помощью кнопки <img src="../img/button/parameters-button.jpg" class="ms-docbutton"/> можно настроить свойства профиля. Доступные параметры, используемые для расчета продольного профиля:

<img src="../img/longitudinal-profile/setting-parameters.jpg" class="ms-docimage"/>

* **Слой профиля**, выбираемый из доступных слоев в выпадающем меню

* **Расстояние**, выбор максимального расстояния между двумя точками вдоль профиля (в `м`)

* **Заголовок графика**, который будет использоваться в интерфейсе над графиком.

<img src="../img/longitudinal-profile/chart-title.jpg" class="ms-docimage"/>
