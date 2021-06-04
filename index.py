#!/usr/bin/python
import cgi
import cgitb
import mysql.connector
import os
import sys
import time

cgitb.enable()


# Print necessary headers.
print("Content-Type: text/html")
print()
print("hello")

# Prepare DB connection
try:
  db = mysql.connector.connect(user='marquee', password='eeuqram', database='marquee')
  # prepare a cursor object using cursor() method
  cursor = db.cursor()
  form = cgi.FieldStorage()
  if "text" not in form:
    print("<h1>Error</h1>")
    print("please send text")
    clear()
    sys.exit(0)
  text_items=form.getlist("text")
  for text in text_items:
    print(text)
    timestamp = time.time() 
    host = cgi.escape(os.environ["REMOTE_ADDR"])
    sql = "INSERT INTO received_messages (timestamp, host, text) values (%s, %s, %s)"
    data=(timestamp, host, text)
    cursor.execute(sql, data)
    db.commit()
    print("message received, loud and clear :)")
  print("All done. Thank you, and have a nice day!")
except mysql.connector.Error as e:
  print("Sorry, didn't copy that! :(")
  print(e)
  sys.exit(1)
finally:
  cursor.close()

sys.exit(0)

