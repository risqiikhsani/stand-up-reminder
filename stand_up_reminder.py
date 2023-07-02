import time
from plyer import notification

def remind():
    # Display the notification three times
    for _ in range(3):
        message = "Take a break\nand stand up !!\nand streching !\nfor every one hour !\njust do it !"
        notification.notify(
            title="Stand Up Reminder",
            message=message,
            timeout=10
        )
        time.sleep(10)

# Run the reminder loop
while True:
    remind()
    # Wait for one hour
    time.sleep(60 * 60)