import shutil
import logging
import sys 
import itertools

sys.path.append("..")
from lib import LCD_1inch28

from PIL import Image

spinner = itertools.cycle(['-', '/', '|', '\\'])

# load images into Pi memory
source_prefix = "/home/hopkira/spi_animate/images/"
target_prefix = "/var/tmp/"
for x in range(90):
    source = source_prefix + "frame_{0:02d}_delay-0.06s.gif".format(x)
    target = target_prefix + "01_{0:02d}.gif".format(x)
    shutil.copyfile(source, target)
    print(source,"->",target)

try:
    disp = LCD_1inch28.LCD_1inch28()
    disp.Init()
    disp.clear()
    while True:
        sys.stdout.write(next(spinner))   # write the next character
        sys.stdout.flush()                # flush stdout buffer (actual character display)
        sys.stdout.write('\b')            # erase the last written char
        for x in range(90):
            image_file = target_prefix + "01_{0:02d}.gif".format(x)
            image = Image.open(image_file)      
            disp.ShowImage(image)
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()
