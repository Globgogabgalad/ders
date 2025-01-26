from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Path to your ChromeDriver
chromedriver_path = "/path/to/chromedriver"  # Make sure to change this to your actual path

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--disable-infobars')  # Disable the "Chrome is being controlled by automated software" bar
options.add_argument('--mute-audio')  # Mute audio, as the game has sound

# Initialize the Chrome driver
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

# Navigate to the Dinosaur game page (this opens the page when you're disconnected)
driver.get('chrome://dino')

# Wait for the page to load
time.sleep(2)

# Get the HTML body element, which we will use to send key presses
body = driver.find_element("tag name", "body")

# Simulate pressing the spacebar to start the game
body.send_keys(Keys.SPACE)

# Play the game by sending the spacebar key at intervals
try:
    while True:
        # Simulate pressing the spacebar to jump over obstacles
        body.send_keys(Keys.SPACE)
        time.sleep(0.5)  # Adjust the delay for jumping frequency
except KeyboardInterrupt:
    print("Game stopped!")

# Close the browser when done
driver.quit()
