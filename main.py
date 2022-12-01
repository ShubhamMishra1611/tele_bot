import game
import requests
import json

offset = None

with open('static.json', 'r') as f:
    base_url = json.load(f)["0"]

with open('updated_id.json', 'r') as f:
    offset = json.load(f)


def send_Msg(text):
    parameters = {
        "chat_id": "5544591417",
        "text": text
    }
    resp = requests.get(base_url+"/sendMessage", data=parameters)
    print(resp.text)


def get_Msg():
    global offset
    parameters = {
        "offset": offset[0],
        "limit": "1"
    }

    resp = requests.get(base_url+"/getUpdates", data=parameters)
    print(resp.json())
    try:
        text = resp.json()["result"][0]["message"]["text"]
        print(text)
        offset[0] += 1
        return text
    except:
        print("No message received")
        return 0


while True:
    text = get_Msg()
    game_on = False
    if text == "/start":
        game_on = True
        send_Msg("Starting Game...")
        send_Msg("Guess the word!!!")
        g = game.Wordle()
        counter = 1
        while True:
            word = get_Msg()
            if word == 0:
                continue
            elif game_on and (word == "/start" or word == "/help"):
                send_Msg("Let's first finish this game 🤔")
            else:
                reply = g.check_word(word=word)
                if len(reply) == 3:
                    if reply[2] == 1:
                        send_Msg(reply[0])
                        send_Msg(reply[1])
                    break
                elif reply[1] == 0:
                    send_Msg(reply[0])
                    continue
                else:
                    send_Msg(reply[0])
                    send_Msg(reply[1])
                if counter == 6:
                    send_Msg("Ohh you lost🔴😔\nBetter Luck Next Time")
                    break
                counter += 1
    elif text == "/help":
        send_Msg("This is a wordle game...\n You have to guess the 5 letter word using the hints given... \n🟩 implies the letter is in the word and is at correct position\n🟨 implies the letter is in the word but at wrong place\n🟫 implies the letter is not in the word ")

    print(offset[0])
    json.dump(offset, open("updated_id.json", "w"))
