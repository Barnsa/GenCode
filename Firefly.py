import radio
import random
from microbit import display, Image, button_a, button_b, sleep

# This is one of the basic data types in python known as a dictionary
image_dict = {
    'happy': Image.HAPPY,
    'heart': Image.HEART,
    'smile': Image.SMILE,
    'sad': Image.SAD,
    'confused': Image.CONFUSED,
    'angry': Image.ANGRY,
    'asleep': Image.ASLEEP,
    'surprised': Image.SURPRISED,
    'silly': Image.SILLY,
    'fabulous': Image.FABULOUS,
    'meh': Image.MEH,
    'yes': Image.YES,
    'no': Image.NO, 
    'flash': Image().invert() 
}

# We have to turn the radio on for it to work
radio.on()

# We also need to set the configuration
radio.config(channel=8, address=4)

while True:

    # This is how we interact with button A
    if button_a.was_pressed():
        radio.send('silly')

    # ...and how we also interact with button B
    if button_b.was_pressed():
        radio.send('meh')

    # we store the incoming radio signals so that we can use them
    incoming = radio.receive()

    # if the message isn't blank or we're not receiving a signal
    if incoming is not None:
        
        # Then we look in the dictionary to see what image we should display,
        # the last bit creates the additional animation frames to make it fade
        flash = [image_dict[incoming]*(i/9) for i in range(9, -1, -1)]

        # We wait a small amount of time for dramatic effect, 
        # but we make it random
        sleep(random.randint(50, 350))

        # then we display the full animation on the display
        display.show(flash, delay=100, wait=False)

        # Randomly re-broadcast the flash message after a
        # slight delay. 1 in 10 chance
        if random.randint(0, 9) == 0:
        
            # this bit creates a random message to send back
            message = random.choice(list(image_dict))
            
            # We wait a little while 
            sleep(500)
            
            radio.send(message) # then send the message
