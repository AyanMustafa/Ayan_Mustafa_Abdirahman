import schedule 
import time
from datetime import datetime
import requests  

messages = [
    "Monday Motivation: Start your week with a positive mindset! #MondayMotivation",
    "Tuesday Tips: Did you know that consistency is key to success? #TuesdayTips",
    "Wednesday Wisdom: Keep pushing forward, you're halfway through the week! #WednesdayWisdom",
    "Thursday Thoughts: Reflect on your progress and set new goals! #ThursdayThoughts",
    "Friday Fun: It's almost the weekend! What are your plans? #FridayFun",
    "Saturday Vibes: Take a break and enjoy some leisure time! #SaturdayVibes",
    "Sunday Reflections: Prepare for the week ahead and set your intentions! #SundayReflections"
]

# Telegram Bot credentials
TELEGRAM_BOT_TOKEN = '7622029833:AAFNR2EKYgxhvEaBlY-XrQEinklAJ7b36WQ'
TELEGRAM_CHAT_ID = '6237919251'  #this is sending messages to my personal telegram account

# Function to post a message to Telegram
def post_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print(f"Telegram: Message sent successfully: {message}")
        else:
            print(f"Telegram: Failed to send message: {response.text}")
    except Exception as e:
        print(f"Telegram: Error sending message: {e}")

# Example: Post today's message to Telegram
def post_daily_message():
    day_index = datetime.now().weekday()  # Monday=0, Sunday=6
    message = messages[day_index]
    post_to_telegram(message)

# Schedule daily posting at 9:00 AM when you initiate the script
def schedule_daily_posts():
    schedule.every().day.at("09:00").do(post_daily_message)
    print("These are scheduled daily posts at 09:00 AM.")
    while True:
        schedule.run_pending()
        time.sleep(60)

# Uncomment to run the scheduler
def main():
    #post_daily_message() #you can add this line to post immediately 
    schedule_daily_posts()

if __name__ == "__main__":
     main()

# Requirements:
# pip install schedule requests











