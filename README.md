# Укротитель ссылок BITLY

Утилита позволяет автоматизировать процесс создания битлинков и их мониторинг.

### Как установить

Проект создавался и проверялся на версии Python 3.9

Для работы утилиты требуется GENERAL TOKEN, который вы сможете получить после регистрации на сервисе BITLY. Создайте в папке проекта файл .env и поместите туда строку 

`BITLY_ACCESS_TOKEN = <полученный токен>`

Также понадобится установить дополнительные библиотеки (для удобства воспользуйтесь витруальным окружением)

`pip install -r requirements.txt`

### Как пользоваться

Откройте текущий проект в окне терминала

Для создания битлинка введите

`python main.py <ваш URL>`

Если у вас уже есть битлинк и вы хотете проверить количество переходов укажите битлинк вместо ссылки