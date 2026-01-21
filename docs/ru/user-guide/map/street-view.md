# Просмотр улиц

*******************

Инструмент **Просмотр улиц** позволяет пользователю просматривать панорамные изображения от различных поддерживаемых провайдеров, таких как [Google Street View](https://www.google.com/streetview/) или [Cyclomedia Street Smart](https://www.cyclomedia.com/en/street-smart).

## Google Street View

С помощью кнопки <img src="../img/button/street-view-button.jpg" class="ms-docbutton"/>, доступной на [Боковой панели инструментов](mapstore-toolbars.md#боковая-панель-инструментов), можно активировать инструмент для навигации по карте с помощью [Google Street View](https://www.google.com/streetview/).

<img src="../img/street-view/streetview-popup.jpg" class="ms-docimage" width="500px"/>

Когда инструмент активирован, открывается окно, и на карте подсвечиваются улицы, чтобы пользователь мог выбрать одну из них простым щелчком мыши.

<video class="ms-docimage" controls><source src="../img/street-view/add-street.mp4"/></video>

При нажатии на улицу на карте в окне инструмента отображается Просмотр улиц, и пользователь может по нему перемещаться.

* **Приближать/отдалять** улицу

<video class="ms-docimage" controls><source src="../img/street-view/zoom-street.mp4"/></video>

* Использовать **панорамирование** для перемещения по улице во всех направлениях

<video class="ms-docimage" controls><source src="../img/street-view/pan-street.mp4"/></video>

* Включать/отключать **полноэкранный режим** <img src="../img/button/full-screen-street.jpg">

## Cyclomedia Street Smart

Если в качестве провайдера для инструмента "Просмотр улиц" настроен [Cyclomedia Street Smart](https://www.cyclomedia.com/en/street-smart), пользовательский опыт остается прежним: инструмент можно активировать с помощью той же кнопки <img src="../img/button/street-view-button.jpg" class="ms-docbutton"/> на [Боковой панели инструментов](mapstore-toolbars.md#боковая-панель-инструментов).

<img src="../img/street-view/cyclomedia-popup.jpg" class="ms-docimage" width="500px"/>

!!! примечание
    Провайдер **[Cyclomedia Street Smart](https://www.cyclomedia.com/en/street-smart)** можно настроить в плагине *Просмотр улиц*, как описано [здесь](https://mapstore.geosolutionsgroup.com/mapstore/docs/api/plugins#plugins.StreetView)

Когда инструмент активирован, пользователь должен ввести *Имя пользователя* и *Пароль* и нажать <img src="../img/button/submit-button.jpg" class="ms-docbutton"/>.

<img src="../img/street-view/credentials_api.jpg" class="ms-docimage" width="500px"/>

!!! внимание
    Учетные данные необходимы для визуализации слоя улиц, в то время как обычный ключ аутентификации (authkey) требуется в конфигурации плагина для взаимодействия с API Street Smart (см. страницу конфигурации плагина [здесь](https://mapstore.geosolutionsgroup.com/mapstore/docs/api/plugins#plugins.StreetView))

После этого открывается окно, и слой улиц визуализируется в виде точек, чтобы подсветить улицы на карте, чтобы пользователь мог выбрать одну из них простым щелчком мыши.

<video class="ms-docimage" controls><source src="../img/street-view/add-point.mp4"/></video>

При нажатии на подсвеченную точку на карте в окне инструмента отображается Просмотр улиц, и пользователь может по нему перемещаться как обычно или взаимодействовать с *панелью навигации*.

<img src="../img/street-view/cyclomedia_navigation_bar.jpg" class="ms-docimage" width="500px"/>

С помощью панели навигации можно:

* Открыть всплывающее окно **Наложения** с помощью кнопки <img src="../img/button/overlays-button.jpg" class="ms-docbutton"/>, чтобы:
  **-** Просматривать и включать/отключать слои, присутствующие в виде, на вкладке **Слои**
  **-** Включать/отключать *Показывать положение мыши* и *Показывать компас* на вкладке **Просмотрщик**

* Открыть всплывающее окно **Отображение** с помощью кнопки <img src="../img/button/display-button.jpg" class="ms-docbutton"/>, чтобы:
    **-** Установить *Яркость* вида
    **-** Установить *Контрастность* вида

* Просмотреть **Информацию об объекте** с помощью кнопки <img src="../img/button/object-nformation-button.jpg" class="ms-docbutton"/>.

* Открыть всплывающее окно **Поперечное сечение** с помощью кнопки <img src="../img/button/cross-section-button.jpg" class="ms-docbutton"/>.

* Просмотреть **Высоту** с помощью кнопки <img src="../img/button/elevation-button.jpg" class="ms-docbutton"/>.

* Открыть всплывающее окно **Сообщить о проблеме** с помощью кнопки <img src="../img/button/report-issue-button.jpg" class="ms-docbutton"/>.

* Открыть всплывающее окно **Облако точек** с помощью кнопки <img src="../img/button/point-cloud-button.jpg" class="ms-docbutton"/>.

* Открыть всплывающее окно **Просмотрщик наклонных снимков** с помощью кнопки <img src="../img/button/oblique-viewer-button.jpg" class="ms-docbutton"/>.

* Открыть всплывающее окно **Измерения** с помощью кнопки <img src="../img/button/cyclomedia-measurements-button.jpg" class="ms-docbutton"/>.

* **Скачать** изображение циклорамы в формате `png` с помощью кнопки <img src="../img/button/cyclomedia-download-button.jpg" class="ms-docbutton"/>.

* Открыть всплывающее окно **Информация об изображении** с помощью кнопки <img src="../img/button/image-info-button.jpg" class="ms-docbutton"/> для доступа к метаданным изображения, таким как общая информация об изображении, а также геопространственные привязки самого изображения.