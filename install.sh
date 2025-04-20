#!/bin/bash

echo -e "\033[2J\033[3;1f"

cat <<EOF

\033[1;34m╭━━━┳╮╱╱╱╱╱╱╭╮\033[0m
\033[1;34m┃╭━╮┃┃╱╱╱╱╱╱┃┃\033[0m
\033[1;34m┃╰━━┫╰━┳━━┳━╯┣━━┳╮╭╮╭╮\033[0m
\033[1;34m╰━━╮┃╭╮┃╭╮┃╭╮┃╭╮┃╰╯╰╯┃\033[0m
\033[1;34m┃╰━╯┃┃┃┃╭╮┃╰╯┃╰╯┣╮╭╮╭╯\033[0m
\033[1;34m╰━━━┻╯╰┻╯╰┻━━┻━━╯╰╯╰╯\033[0m
\033[1;35mShadow is starting... ✨\033[0m

EOF

echo -e "\n\n\033[0;96mChecking dependencies...\033[0m"

if ! command -v python3 &> /dev/null; then
    echo -e "\033[0;31mError: Python 3 не найден. Пожалуйста, установите его.\033[0m"
    exit 1
fi

if ! command -v pip3 &> /dev/null; then
    echo -e "\033[0;31mError: pip не найден. Пожалуйста, установите его.\033[0m"
    exit 1
fi

printf "\r\033[K\033[0;32mDependencies ready!\e[0m\n"
echo -e "\033[0;96mInstalling requirements...\033[0m"

pip3 install -r requirements.txt --no-cache-dir --no-warn-script-location --disable-pip-version-check --upgrade

printf "\r\033[K\033[0;32mRequirements installed!\e[0m\n"

echo -e "\033[0;96mStarting Shadow bot...\033[0m"
echo -e "\033[2J\033[3;1f"

printf "\033[1;32mShadow bot is starting...\033[0m\n"

cd shadow
python3 shadow.py
