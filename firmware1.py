# Here is a script to test out micro:bit programming
from microbit import display, Image, sleep

# This is a list, one of the basic storage types in programming
all_Images = [Image.HAPPY, Image.HEART, Image.FABULOUS, Image.SILLY, Image.ASLEEP, Image.SURPRISED]

# This is a while loop, as long as it's "True" it will repeat forever
while True:

    # This makes the text scroll across the micro:bit screen
    display.scroll('Hello, world!')

    # This is will display the "HAPPY" image
    display.show(Image.HAPPY)

    # this will make the program sleep for 2 seconds
    sleep(2000)

    # Can you guess what this does?
    display.show(Image.HEART)

    # What about this one?
    sleep(2000)
    
    # This will show each of the images in the list with a short delay between them
    display.show(all_Images, delay=400)