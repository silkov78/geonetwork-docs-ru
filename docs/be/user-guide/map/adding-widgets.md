# Даданне віджэтаў

****************

Пры націску на кнопку <img src="../../../ru/user-guide/map/img/button/++++.jpg" class="ms-docbutton"/> на [бакавой панэлі інструментаў](exploring-dashboards.md#side-toolbar) адкрываецца панэль *Віджэт*, якая паказвае спіс даступных тыпаў віджэтаў, якія можна дадаць на інфармацыйную панэль:

<img src="../../../ru/user-guide/map/img/adding-widgets/widgets-panel.jpg" class="ms-docimage"  style="max-width:400px;"/>

У прыватнасці, можна выбраць:

* **Дыяграма**

* **Тэкст**

* **Табліца**

* **Лічыльнік**

* **Карта**

Працэдура стварэння віджэтаў *Дыяграма*, *Тэкст*, *Табліца* і *Лічыльнік* амаль такая ж, як апісана для [стварэння віджэтаў на картах](widgets.md#widgets). Адзіныя нязначныя адрозненні наступныя:

* У інфармацыйных панэлях, як толькі карыстальнік выбірае тып віджэта, з'яўляецца панэль для выбару слоя, з якога будзе створаны віджэт. Можна выбраць паміж службамі CSW, WMS і WMTS ад GeoSolutions, якія прысутнічаюць па змаўчанні, або атрымаць доступ да аддаленых службаў WMS, WFS, CSW, WMTS і TMS, як тлумачыцца ў раздзеле [Кіраванне аддаленымі службамі](catalog.md#managing-remote-services).

<img src="../../../ru/user-guide/map/img/adding-widgets/default-services.jpg" class="ms-docimage"  style="max-width:400px;"/>

* У інфармацыйных панэлях магчымасць падключэння/адключэння віджэтаў ад карты заменена магчымасцю падключаць/адключаць віджэты "Карта" паміж сабой або з іншымі тыпамі віджэтаў (гэты момант будзе больш падрабязна растлумачаны ў раздзеле [Злучэнне віджэтаў](connecting-widgets.md#connecting-widgets)).

Стварэнне віджэтаў тыпу "Карта", у сваю чаргу, з'яўляецца функцыянальнасцю, якая прысутнічае толькі ў інфармацыйных панэлях.

## Віджэт "Карта"

У інфармацыйных панэлях, пры выбары віджэта тыпу "Карта", з'яўляецца наступная панэль:

<img src="../../../ru/user-guide/map/img/adding-widgets/wid-select-map.jpg" class="ms-docimage"  style="max-width:400px;"/>

Тут карыстальнік можа:

* Вярнуцца да выбару тыпу віджэта з дапамогай кнопкі <img src="../../../ru/user-guide/map/img/button/back.jpg" class="ms-docbutton"/>

* Шукаць карту па яе назве

* Выбраць адну або некалькі карт са спіса (абавязкова для пераходу да наступнага кроку)

* Перайсці да наступнага кроку з дапамогай кнопкі <img src="../../../ru/user-guide/map/img/button/next.jpg" class="ms-docbutton"/>

Пасля выбару карты панэль адлюстроўвае слаі, якія прысутнічаюць на карце ў папярэднім праглядзе, і пералічвае слаі, звязаныя з картай.

!!!заўвага
    Калі карыстальнік выбраў больш за адну карту, майстар карт адлюстроўвае выпадальны спіс *пераключальніка карт*, які дазваляе карыстальніку выбіраць і наладжваць карту.

<img src="../../../ru/user-guide/map/img/adding-widgets/wid-layers-list.jpg" class="ms-docimage"  style="max-width:400px;"/>

!!!заўвага
    Калі абрана **Пустая карта**, карыстальнік можа:

    * Стварыць віджэт карты, выкарыстоўваючы пустую карту.

    * Калі ў выбары карты ёсць пустая карта, карыстальніку прапануецца ўвесці назву карты.

    * Пасля дадання назвы, майстар карт адлюстроўвае пераключальнік карт, які дазваляе карыстальніку выбіраць і наладжваць карту.

    * Дадаваць слаі на карту з дапамогай кнопкі <img src="../../../ru/user-guide/map/img/button/+++.jpg" class="ms-docbutton"/>, як паказана ніжэй: <video controls class="ms-docimage"  style="max-width:400px;"><source src="../../../ru/user-guide/map/img/adding-widgets/wid-add-layer.mp4"> /></video>

На панэлі **Наладзіць параметры карты** карыстальнік можа пераключаць бачнасць слоя і ўсталёўваць празрыстасць слаёў, як тлумачыцца ў раздзеле [Опцыі адлюстравання](toc.md#display-options-in-panel). Акрамя таго, карыстальнік можа кіраваць слоем з дапамогай новых кнопак на панэлі інструментаў слоя, выбраўшы слой у спісе слаёў.

<img src="../../../ru/user-guide/map/img/adding-widgets/wid-layers-new-buttons.jpg" class="ms-docimage"  style="max-width:400px;"/>

Тут карыстальніку дазволена:

* **Наблізіць** да слаёў з дапамогай кнопкі <img src="../../../ru/user-guide/map/img/button/zoom-layer.jpg" class="ms-docbutton"/>

* Атрымаць доступ да [наладак слоя](layer-settings.md#layer-settings) з дапамогай кнопкі <img src="../../../ru/user-guide/map/img/button/properties.jpg" class="ms-docbutton"/>

* **Выдаліць** слаі з дапамогай кнопкі <img src="../../../ru/user-guide/map/img/button/delete.jpg" class="ms-docbutton"/>

* Адключыць/уключыць [плаваючы інструмент "Ідэнтыфікацыя"](navigation-toolbar.md#floating-identify-tool) для атрымання інфармацыі пра аб'екты слаёў, даступных на карце, з дапамогай кнопкі <img src="../../../ru/user-guide/map/img/button/identify_green_burron.jpg" class="ms-docbutton"/>

!!!увага
    Інструмент *Плаваючая ідэнтыфікацыя* актыўны па змаўчанні (кнопка зялёная).

Пасля націску кнопкі <img src="../../../ru/user-guide/map/img/button/next.jpg" class="ms-docbutton"/>, апошні крок працэсу адлюстроўваецца наступным чынам:

<img src="../../../ru/user-guide/map/img/adding-widgets/map-wid-info.jpg" class="ms-docimage" style="max-width:400px;"/>

Тут у карыстальніка ёсць магчымасць увесці **Загаловак** і **Апісанне** для віджэта (неабавязковыя палі) і завяршыць яго стварэнне, націснуўшы на кнопку <img src="../../../ru/user-guide/map/img/button/save-icon.jpg" class="ms-docbutton"/>. Пасля гэтага віджэт дадаецца ў прастору прагляду:

<img src="../../../ru/user-guide/map/img/adding-widgets/viewer-map.jpg" class="ms-docimage" style="max-width:600px;"/>

## Віджэт "Легенда"

Калі створаны і дададзены на інфармацыйную панэль хаця б адзін віджэт "Карта", з'яўляецца магчымасць дадаць таксама віджэт **Легенда**, даступны ў спісе тыпаў віджэтаў:

<img src="../../../ru/user-guide/map/img/adding-widgets/list-legend.jpg" class="ms-docimage" style="max-width:400px;"/>

Выбіраючы віджэт "Легенда", карыстальнік можа выбраць віджэт "Карта", з якім будзе звязана легенда (калі на інфармацыйнай панэлі прысутнічае толькі адзін віджэт "Карта", гэты крок прапускаецца):

<img src="../../../ru/user-guide/map/img/adding-widgets/select-map-connection.jpg" class="ms-docimage" style="max-width:600px;"/>

Пасля падключэння віджэта "Карта" панэль папярэдняга прагляду выглядае наступным чынам:

<img src="../../../ru/user-guide/map/img/adding-widgets/legend-preview.jpg" class="ms-docimage" style="max-width:400px;"/>

Тут карыстальнік можа вярнуцца <img src="../../../ru/user-guide/map/img/button/back.jpg" class="ms-docbutton"/> да раздзела тыпаў віджэтаў, падключыць <img src="../../../ru/user-guide/map/img/button/connect-widget.jpg" class="ms-docbutton"/> або адключыць <img src="../../../ru/user-guide/map/img/button/connection-icon.jpg" class="ms-docbutton"/> легенду ад карты і перайсці <img src="../../../ru/user-guide/map/img/button/next.jpg" class="ms-docbutton"/> да параметраў віджэта. 
Калі абрана апошняя опцыя, панэль канфігурацыі, аналагічная панэлі [віджэтаў "Карта"](#map-widget), дае магчымасць перад захаваннем усталяваць *Загаловак* і *Апісанне* для віджэта "Легенда". 

Прыкладам віджэта "Карта" і віджэта "Легенда" з'яўляецца наступны:

<img src="../../../ru/user-guide/map/img/adding-widgets/legend-ex.jpg" class="ms-docimage"/>