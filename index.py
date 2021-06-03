#!/usr/bin/python
import time
import board
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
import cgi
import cgitb
import os
import random
import socket
import sys

cgitb.enable()

random.seed()

# Print necessary headers.
print("Content-Type: text/html\n\n")
print()
print("hello")

# Modify this if you have a different sized Character LCD
lcd_columns = 16
lcd_rows = 2

# Initialise I2C bus.
i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialise the LCD class
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

lcd.clear()
# Set LCD color

def clear():
  # Clear the lcd
  lcd.color = [0, 0, 0]
  lcd.clear()

form = cgi.FieldStorage()
if "text" not in form:
  print("<h1>Error</h1>")
  print("please send text")
  clear()
  sys.exit(0)

text_items=form.getlist("text")
for text in text_items:
  red=random.randint(0,100)
  green=random.randint(0,100)
  blue=random.randint(0,100)
  lcd.color = [red, green, blue]
  lcd.message=cgi.escape(os.environ["REMOTE_ADDR"])+"\n"+text
  time.sleep(2)
  lcd.clear()
lcd.message="goodbye!"
time.sleep(2)
clear()
