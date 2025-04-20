import json
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

TOKEN_FILE = 'token.json'
TOKEN_KEY = 'bot_token'

def get_token():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    token_file_path = os.path.join(script_dir, TOKEN_FILE)

    try:
        with open(token_file_path, 'r') as f:
            config = json.load(f)
            token = config.get(TOKEN_KEY)
            return token
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print(f"Ошибка: Некорректный формат JSON в файле {token_file_path}.")
        return None
    except KeyError:
        print(f"Ошибка: Ключ '{TOKEN_KEY}' не найден в файле {token_file_path}.")
        return None

def save_token(token):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    token_file_path = os.path.join(script_dir, TOKEN_FILE)
    config = {TOKEN_KEY: token}
    try:
        with open(token_file_path, 'w') as f:
            json.dump(config, f, indent=4)
        print("Токен бота сохранен в файле token.json.")
    except IOError:
        print(f"Ошибка: Не удалось записать токен в файл {token_file_path}.")

def start(update, context):
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Привет, {user.mention_markdown_v2()}! 👋'
    )

def echo(update, context):
    update.message.reply_text(update.message.text)

def caps(update, context):
    text = ' '.join(context.args).upper()
    update.message.reply_text(text)

def main():
    token = get_token()

    if not token:
        token = input("Пожалуйста, введите токен вашего бота: ")
        save_token(token)
    elif token:
        print("Токен найден в файле token.json.")

    if token:
        updater = Updater(token, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
        dp.add_handler(CommandHandler("caps", caps, pass_args=True))

        updater.start_polling()
        updater.idle()
    else:
        print("Бот не может быть запущен без токена.")

if __name__ == '__main__':
    main()
