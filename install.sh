#!/bin/bash

# Проверка прав администратора
if [ "$(id -u)" -ne 0 ]; then
    echo "Для установки необходимо иметь права администратора (root)."
    exit 1
fi

# Убедитесь, что файл kyn существует
if [ ! -f "bin/kyn" ]; then
    echo "Ошибка: скрипт 'bin/kyn' не найден!"
    exit 1
fi

# Делаем скрипт kyn исполнимым
chmod +x bin/kyn

# Путь к каталогу проекта (можно использовать $PWD для текущего каталога)
PROJECT_PATH=$(pwd)

# Добавление пути к bin в переменную окружения PATH
echo "export PATH=\$PATH:$PROJECT_PATH/bin" >> ~/.bashrc
echo "export PATH=\$PATH:$PROJECT_PATH/bin" >> ~/.zshrc

# Создание символической ссылки в /usr/local/bin (чтобы kyn был доступен глобально)
ln -sf $PROJECT_PATH/bin/kyn /usr/local/bin/kyn

# Применяем изменения в окружении
source ~/.bashrc
source ~/.zshrc

echo "Kynium успешно установлен! Вы можете запускать команду 'kyn'."
