import shutil
import logging
import sys 
import itertools
from tqdm import tqdm

sys.path.append("..")
from lib import LCD_1inch28

from PIL import Image

spinner = itertools.cycle(['-', '/', '|', '\\'])
RST = 27
DC = 25
BL = 23
bus = 0 
device = 0
colours = ["green","lime","orange","yellow","red",]

# load images into Pi memory
for num, colour in iter(colours):
    source_prefix = "/home/hopkira/spi_animate/images/" + colour
    target_prefix = "/var/tmp/"
    for x in tqdm(range(90)):
        source = source_prefix + "frame_{0:02d}_delay-0.06s.jpg".format(x)
        target = target_prefix + str(num) + "_{0:02d}.jpg".format(x)
        shutil.copyfile(source, target)

try:
    #disp = LCD_1inch28.LCD_1inch28(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl>
    disp = LCD_1inch28.LCD_1inch28(rst=RST,bl=BL,dc=DC)
    disp.Init()
    disp.clear()
    while True:
        for x in range(90):
            image_file = target_prefix + "4_{0:02d}.jpg".format(x)
            image = Image.open(image_file)
            disp.ShowImage(image)
            sys.stdout.write(next(spinner))   # write the next character
            sys.stdout.flush()                # flush stdout buffer (actual character display)
            sys.stdout.write('\b')            # erase the last written char
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()
