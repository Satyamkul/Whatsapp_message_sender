# Importing the required modules
import pyautogui as pg
import time

# Giving delay to run program
print("Program will run after 5 seconds")
time.sleep(5)
print("Running")

# Note: After running the program, immediately open WhatsApp Web and then open the chat of the person you want to send messages to

# For loop
for i in range(100):
    # Writing the message
    pg.write("Enter your message")
    time.sleep(0.5)
    # Sending the message by pressing enter
    pg.press("enter")
    # Adding a delay after sending each message
    time.sleep(1)
