#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_1inch28
from PIL import Image,ImageDraw,ImageFont

# load images into memory disk
# retrieve the speaking state from global memory
# import memory
# mem.storeState("speaking",0.0)
# if speaking then retrieve one set of pictures and increment
# if not speaking then display the other set.

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 23 # changed default due to clash with LCD screen
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)

try:
    # display with hardware SPI:
    ''' Warning!!!Don't  creation of multiple displayer objects!!! '''
    #disp = LCD_1inch28.LCD_1inch28(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl>
    disp = LCD_1inch28.LCD_1inch28()
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()

    # Create blank image for drawing.
    image1 = Image.new("RGB", (disp.width, disp.height), "BLACK")
    draw = ImageDraw.Draw(image1)

    im_r=image1.rotate(180)
    disp.ShowImage(im_r)
    logging.info("show image")
    image = Image.open('../pic/LCD_1inch28_1.jpg')      
    im_r=image.rotate(180)
    disp.ShowImage(im_r)
    disp.module_exit()
    logging.info("quit:")
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()