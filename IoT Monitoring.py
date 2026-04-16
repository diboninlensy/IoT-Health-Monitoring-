import random
import requests
import time


api_key = "R91O9D4SNHTUERSW"

while True:
    # 📊 Random health data generate
    heart_rate = random.randint(60, 120)
    temperature = round(random.uniform(36, 40), 2)

    # 🖥️ Print values
    print("Heart Rate:", heart_rate)
    print("Temperature:", temperature)

    # ⚠️ Alert conditions
    if heart_rate > 100:
        print("⚠️ High Heart Rate Alert!")

    if temperature > 38:
        print("⚠️ Fever Alert!")

    # 🌐 Send data to ThingSpeak
    url = f"https://api.thingspeak.com/update?api_key={api_key}&field1={heart_rate}&field2={temperature}"
    response = requests.get(url)

    print("Data Sent to ThingSpeak\n")

    # ⏱️ 15 seconds delay (ThingSpeak limit)
    time.sleep(10)
