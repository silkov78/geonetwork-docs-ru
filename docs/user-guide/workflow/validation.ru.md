# Проверка записей метаданных {#validation}

1.  В редакторе записи метаданных пользователю надо нажать кнопку `Проверка`, чтобы запустить проверку. На правой панели отображаются все результаты проверки по уровням:

    ![](img/validation.png)

2.  Для отображения ошибок нажмите на значки больших пальцев вверх или вниз. Ошибки, выделенные синим цветом, предназначены только для информации и не влияют на глобальную проверку записи:

    ![](img/validation-details.png)

    Редактор также сообщает о сообщениях об ошибках прямо в форме около проблемных элементов, где это применимо (поскольку все сообщения об ошибках не могут быть показаны в редакторе):

    ![](img/validation-inline.png)

3.  После проверки записи статус проверки сохраняется и отображается на странице доски редактора:

    ![](img/validation-status.png)

Пользователь может отфильтровать записи метаданных согласно их статусу проверки с помощью множественного выбора в панели редактора.

## Настройка проверки

Администраторы каталога могут настроить процесс проверки записи метаданных, чтобы она автоматически проводилась каждый раз, когда пользователь-редактор выходит или закрывает интерфейс редактирования метаданных (см. раздел [Конфигурация системы](../../administrator-guide/configuring-the-catalog/system-configuration.md)). Настроить уровни проверки (см. [Настройка уровней проверки](../../administrator-guide/managing-metadata-standards/configure-validation.md)). В случае записей INSPIRE можно использовать удаленный валидатор (см. [Валидация INSPIRE](../../administrator-guide/configuring-the-catalog/inspire-configuration.md#inspire-validation)).