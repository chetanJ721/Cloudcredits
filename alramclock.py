import time
import datetime
import winsound  # Windows only. Use 'playsound' for cross-platform support.

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("⏰ Alarm Ringing!")
            winsound.Beep(1000, 2000)  # Beeps at 1000Hz for 2 seconds
            break
        time.sleep(1)

alarm_time = input("Enter alarm time (HH:MM:SS): ")
print(f"⏳ Alarm set for {alarm_time}...")

set_alarm(alarm_time)
