#!/usr/bin/python
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
import board
import mysql.connector
import os
import random
import sys
import time

random.seed()

def clear():
  # Clear the lcd
  lcd.color = [0, 0, 0]
  lcd.clear()

# Prepare DB connection
try:
  db = mysql.connector.connect(user='marquee', password='eeuqram', database='marquee')
  # prepare a cursor object using cursor() method
  cursor = db.cursor()

  sql = "select timestamp, host, text from received_messages"
#  if cursor.execute(sql):
  cursor.execute(sql)
  messages = cursor.fetchall()
# Modify this if you have a different sized Character LCD
  lcd_columns = 16
  lcd_rows = 2

# Initialise I2C bus.
  i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialise the LCD class
  lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

  lcd.clear()
  for (timestamp,host,text) in messages:
    red=random.randint(0,100)
    green=random.randint(0,100)
    blue=random.randint(0,100)
    lcd.color = [red, green, blue]
    lcd.message = str(timestamp) + "|" + str(host) + "\n" + str(text)
    time.sleep(2)
    lcd.color = [0, 0, 0]
    lcd.clear()
  lcd.message="goodbye!"
  time.sleep(2)
except mysql.connector.Error as e:
  print(e)
  sys.exit(1)
finally:
  cursor.close()

clear()
sys.exit(0)







