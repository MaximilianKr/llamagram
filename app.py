import json
import requests
import time
from urllib.parse import quote_plus
from botdata.llm import LangChainMemoryBot
from botdata.credentials import TOKEN

# Place your Telegram bot API token in botdata/credentials.py
URL = f"https://api.telegram.org/bot{TOKEN}"
POLLING_TIMEOUT = 0.5


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = f"{URL}/getUpdates?timeout=100"
    if offset:
        url += f"&offset={offset}"
    return get_json_from_url(url)


def get_last_update_id(updates):
    return max(int(update["update_id"]) for update in updates["result"])


def get_last_chat_id_and_text(updates):
    last_update = updates["result"][-1]["message"]
    text = last_update["text"]
    chat_id = last_update["chat"]["id"]
    return text, chat_id


def send_message(text, chat_id):
    text = quote_plus(text)
    url = f"{URL}/sendMessage?text={text}&chat_id={chat_id}"
    get_url(url)


def process_update(update):
    try:
        text = update["message"]["text"]
        print("Generating response.")
        response = LLM.predict(text)
        chat_id = update["message"]["chat"]["id"]
        # ToDo: catch here to save chat history persistently
        send_message(response, chat_id)
        print("Listening.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        try:
            if updates["result"]:
                last_update_id = get_last_update_id(updates) + 1
                for update in updates["result"]:
                    process_update(update)
            time.sleep(POLLING_TIMEOUT)
        except KeyError:
            raise KeyError("Could not get updates. Have you placed your "
                           "Telegram bot API token in botdata/credentials.py?")


if __name__ == '__main__':
    LLM = LangChainMemoryBot()
    print("Bot ready.\nListening.")
    main()
