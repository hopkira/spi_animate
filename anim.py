import shutil
import logging
import sys 
import itertools
import time

sys.path.append("..")
from lib import LCD_1inch28

from PIL import Image
from PIL import GifImagePlugin

spinner = itertools.cycle(['-', '/', '|', '\\'])
RST = 27
DC = 25
BL = 23
bus = 0 
device = 0

# load images into Pi memory
source_prefix = "/home/hopkira/spi_animate/images/"
target_prefix = "/var/tmp/"
for x in range(90):
    source = source_prefix + "frame_{0:02d}_delay-0.06s.jpg".format(x)
    target = target_prefix + "01_{0:02d}.jpg".format(x)
    shutil.copyfile(source, target)
    print(source,"->",target)

try:
    #disp = LCD_1inch28.LCD_1inch28(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl>
    disp = LCD_1inch28.LCD_1inch28(rst=RST,bl=BL,dc=DC)
    disp.Init()
    disp.clear()
    while True:
        for x in range(90):
            image_file = target_prefix + "01_{0:02d}.gif".format(x)
            image = Image.open(image_file)
            disp.ShowImage(image)
            print(image_file)
            time.sleep(1)
            sys.stdout.write(next(spinner))   # write the next character
            sys.stdout.flush()                # flush stdout buffer (actual character display)
            sys.stdout.write('\b')            # erase the last written char
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()
