1. ~~Создать БД, написать к ней тесты~~
2. ~~Настроить автоматический запуск тестов при коммите на репозиторий~~
3. ~~Сделать копию Job из лабораторной работы номер 1 в виде Pipeline скрипта~~
4. ~~Запуск Job из Gerrit change (при загрузке нового или измененного patch-set)~~
   * check-out / fetch
   * выполнить тест
   * сохранить результаты
   * +1 / -1 в gerrit
5. ~~Запуск Job из Gerrit change (при загрузке нового или измененного patch-set)~~
   * check-out / fetch
   * check-out master
   * определить какой тест запустить
   * выполнить тест
   * сохранить результаты
   *  +1 / -1 в gerrit
6. ~~Sentry~~ файл job_sentry.py
   * показать ошибки exception
   * показать отправку ошибок без exception
   * дабавить tag в отправку