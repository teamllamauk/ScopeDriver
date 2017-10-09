#!/usr/bin/env python

import sys
import time

import dothat.backlight as backlight
import dothat.lcd as lcd
import dothat.touch as nav
from dot3k.menu import Menu, MenuOption

# Add the root examples dir so Python can find the plugins
sys.path.append('../')

#from plugins.clock import Clock
#from plugins.graph import IPAddress, GraphTemp, GraphCPU, GraphNetSpeed
from plugins.text import Text
#from plugins.utils import Backlight, Contrast
#from plugins.wlan import Wlan


print("""
This advanced example uses the menu framework.
It gives you a basic menu setup with plugins. You should be able to view system info and adjust settings!
Press CTRL+C to exit.
""")


"""
Using a set of nested lists you can describe
the menu you want to display on dot3k.
Instances of classes derived from MenuOption can
be used as menu items to show information or change settings.
See GraphTemp, GraphCPU, Contrast and Backlight for examples.
"""

menu = Menu(
    structure={
        'WiFi': '1',        
        'Clock': '2',
        'Status': {
            'IP': '1.2.3.4',
            'CPU': 'graph',
            'Temp': 'temp'
        },
        'Settings': {
            'Display': {
                'Contrast': 'lcd',
                'Backlight': 'back'
            }
        }
    },
    lcd=lcd,    
    input_handler=Text())

"""
You can use anything to control dot3k.menu,
but you'll probably want to use dot3k.touch
"""
#nav.bind_defaults(menu)

while 1:
    menu.down()
    menu.redraw()
    time.sleep(3)
