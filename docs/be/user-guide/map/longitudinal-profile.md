# Падоўжны профіль

*******************

Маючы ў якасці крыніцы ЛМР або батыметрычны слой і зададзены на ім шлях, гэты інструмент дазваляе разлічыць **Падоўжны профіль** і адлюстраваць яго ў выглядзе інтэрактыўнага графіка.

!!! заўвага
    Плагін працуе толькі ў тым выпадку, калі ў [GeoServer](http://geoserver.org/) правільна ўсталяваны **працэс WPS "Падоўжны профіль"**. Для атрымання дадатковай інфармацыі пра гэты працэс і яго ўстаноўку звярніцеся да афіцыйнай [анлайн-дакументацыі](https://docs.geoserver.org/latest/en/user/community/wps-longitudinal-profile/index.html). Модуль падоўжнага профілю для GeoServer даступны пачынаючы з версіі Geoserver v2.20.x ад жніўня 2023 года.

Пры націску на кнопку **Падоўжны профіль** <img src="../img/button/long-profile-button.jpg" class="ms-docbutton"/>, даступную на [Бакавой панэлі інструментаў](mapstore-toolbars.md#side-toolbar), адкрываецца выпадальнае меню, у якім карыстальнік можа кіраваць даступнымі опцыямі, уключаючы розныя спосабы разліку профілю:

<img src="../img/longitudinal-profile/dropdown-menu-long-profile.jpg" class="ms-docimage"/>

* Можна намаляваць лінію прама на карце з дапамогай кнопкі <img src="../img/button/drawing-line.jpg" class="ms-docbutton"/>

<video class="ms-docimage" controls><source src="../img/longitudinal-profile/drawing-line.mp4"/></video>

* У якасці альтэрнатывы можна таксама імпартаваць лінейны профіль у выглядзе вектарнага файла (даступныя фарматы: `GeoJSON`, `ShapeFile` або `DXF`) з дапамогай кнопкі <img src="../img/button/import-file.jpg" class="ms-docbutton"/>

<video class="ms-docimage" controls><source src="../img/longitudinal-profile/import-file.mp4"/></video>

* Нарэшце, з дапамогай кнопкі <img src="../img/button/selection-layer.jpg" class="ms-docbutton"/> карыстальнік таксама можа выбраць вектарны лінейны слой у [Панэлі зместу](toc.md), а затым выбраць на карце лінейны аб'ект, які прадстаўляе жаданы шлях профілю.

<video class="ms-docimage" controls><source src="../img/longitudinal-profile/selection-layer.mp4"/></video>

## Графік

Калі геаметрыя шляху профілю намаляваная на карце, адкрываецца панэль **Падоўжны профіль**, і на ўкладцы **Графік** з'яўляецца сам графік.

<img src="../img/longitudinal-profile/chart-tab.jpg" class="ms-docimage"/>

У той час як вось *X* паказвае адлегласць ад пачатковай кропкі зададзенага шляху, вось *Y* паказвае вышыню кропак уздоўж профілю, разлічаную па зададзеным шляху. Карыстальнік можа наводзіць курсор на графік для ўзаемадзеяння паміж графікам і лініяй на карце наступным чынам:

<video class="ms-docimage" controls><source src="../img/longitudinal-profile/interact-with-chart.mp4"/></video>

**Панэль інструментаў графіка**, якая адлюстроўваецца ў правым куце графіка, дазваляе карыстальніку:

<img src="../img/longitudinal-profile/bar_charts.jpg" class="ms-docimage"/>

* **Спампаваць** графік у фармаце `png` з дапамогай кнопкі <img src="../img/button/download_png.jpg" class="ms-docbutton"/>.

* **Маштабаваць** графік з дапамогай кнопкі <img src="../img/button/zoom_chart.jpg" class="ms-docbutton"/>.

* **Перамяшчаць** графік з дапамогай кнопкі <img src="../img/button/pan_chart.jpg" class="ms-docbutton"/>.

* **Наблізіць** графік з дапамогай кнопкі <img src="../img/button/zoom_in_chart.jpg" class="ms-docbutton"/>.

* **Аддаліць** графік з дапамогай кнопкі <img src="../img/button/zoom_out_chart.jpg" class="ms-docbutton"/>.

* **Аўтамаштаб** для аўтаматычнага маштабавання восей па адлюстраваных даных з дапамогай кнопкі <img src="../img/button/autoscale_chart.jpg" class="ms-docbutton"/>.

* **Скінуць восі** для вяртання графіка ў зыходны стан з дапамогай кнопкі <img src="../img/button/reset_axes_chart.jpg" class="ms-docbutton"/>.

Таксама можна экспартаваць *Падоўжны профіль* у выглядзе файла `CSV`, `PNG` або `PDF`.

<img src="../img/longitudinal-profile/export-profile.jpg" class="ms-docimage"/>

## Інфармацыя

На ўкладцы **Інфармацыя** прадстаўлены ўсе адпаведныя паказчыкі, звязаныя з разлікам падоўжнага профілю. У прыватнасці, тут пазначаны:

<img src="../img/longitudinal-profile/profile-info.jpg" class="ms-docimage"/>

* Слой, выкарыстаны для разліку профілю

* Агульная лінейная даўжыня профілю

* Сумарны набор вышыні

* Сумарная страта вышыні

* Колькасць апрацаваных кропак (колькасць кропак залежыць ад абранага кроку).

## Наладка параметраў

З дапамогай кнопкі <img src="../img/button/parameters-button.jpg" class="ms-docbutton"/> можна наладзіць уласцівасці профілю. Даступныя параметры, якія выкарыстоўваюцца для разліку падоўжнага профілю:

<img src="../img/longitudinal-profile/setting-parameters.jpg" class="ms-docimage"/>

* **Слой профілю**, які выбіраецца з даступных слаёў у выпадальным меню

* **Адлегласць**, выбар максімальнай адлегласці паміж дзвюма кропкамі ўздоўж профілю (у `м`)

* **Загаловак графіка**, які будзе выкарыстоўвацца ў інтэрфейсе над графікам.

<img src="../img/longitudinal-profile/chart-title.jpg" class="ms-docimage"/>