#!/usr/bin/python3

import cgi
import datetime
import mysql.connector
SQL = "sql"

def write_html_header():
  '''Writes the HTML header'''
  htmlpart = '''Content-type: text/html\n
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <title>Todo</title>'''
  print(htmlpart)


def write_html_footer():
  '''Writes the HTML footer'''
  htmlpart = '''  <br/>
    <footer><p>PC</p></footer>
  </body>
</html>'''
  print(htmlpart)


def write_html_stylesheet():
  '''Writes the CSS stulesheet'''
  htmlpart = '''  <style>
  header {
    background-color:#b0cfff;
    color:black;
    text-align:center;
    padding:5px;
  }
  article {
    padding:5px;
    float:left;
  }
  a {
    color: black;
    text-decoration: none;
  }
  footer {
    background-color:#b0cfff;
    color:black;
    clear:both;
    text-align:center;
    padding:1px;	 	 
  }

  table { border-collapse: collapse; table-layout: fixed; }
  td { border: 1px solid #dddddd; text-align: center; padding: 6px; }
  th { border: 1px solid #dddddd; text-align: center; padding: 2px; }
  tr { align: left; }
  tr:nth-child(even) { background-color: #b0cfff; }
  tr:hover {background-color:#d0efff;}
  a.menubutton { font-size:150%; padding-left: 12px; padding-right: 12px;}

  #formfield {
    font-size: 1em;
  }
  </style>'''
  print(htmlpart)


def write_html_body_init():
  '''Writes the transition from <head></head> to <body></body'''
  htmlpart = '''</head>
<body>'''
  print(htmlpart)


def write_html_top_of_the_page():
  '''Writes the HTML title section and top banner'''
  htmlpart = '''  <header>
  <h2><a href="http://raspberrypi/index.py">Todo in Python</a></h2>
  </header>'''
  print(htmlpart)


def GetListItem(listname, index):
  '''To capture non existing items in list'''
  try:
    data = listname[index]
  except:
    data = ' '
  return data


def write_html_body():
  '''Writes the actual body of the web page'''
  htmlpart = '''  <br/>
  <table width="100%">
    <tr><th colspan="5">TODO</th></tr>
    <tr><th>*</th><th>**</th><th>***</th><th>****</th><th>*****</th></tr>'''
  print(htmlpart)

  mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="hunter2",
    database="todo"
  )
  mycursor = mydb.cursor()
  mycursor.execute("select item, priority, done, date from todo")
  myresult = mycursor.fetchall()
  Priority1List=list()
  Priority2List=list()
  Priority3List=list()
  Priority4List=list()
  Priority5List=list()
  DoneList=dict()
  for record in myresult:
    item, priority, done, date = record
    if not done:
      if priority == '1':
        Priority1List.append(item)
      if priority == '2':
        Priority2List.append(item)
      if priority == '3':
        Priority3List.append(item)
      if priority == '4':
        Priority4List.append(item)
      if priority == '5':
        Priority5List.append(item)
    else:
      DoneList[item] = date
  for i in range( max( len(Priority1List), len(Priority2List), len(Priority3List), len(Priority4List), len(Priority5List) ) ): 
    htmlpart = '    <tr>'

    htmlpart = htmlpart + '<td>'
    if i <= len(Priority1List):
      htmlpart = htmlpart + GetListItem(Priority1List,i)
    if i < len(Priority1List):
      htmlpart = htmlpart + '<a href="http://raspberrypi/index.py?prio=2&item=' + GetListItem(Priority1List,i) + '">&#62;</a>'
      htmlpart = htmlpart + '<a href="http://raspberrypi/index.py?delete=' + GetListItem(Priority1List,i) + '">&nbsp;&#8730</a>'
    htmlpart = htmlpart + '</td>'

    htmlpart = htmlpart + '<td>'
    if i < len(Priority2List):
      htmlpart = htmlpart + '<a href="http://raspberrypi/index.py?prio=1&item=' + GetListItem(Priority2List,i) + '">&#60;</a>'
    if i <= len(Priority2List):
      htmlpart = htmlpart + GetListItem(Priority2List,i)
    if i < len(Priority2List):
      htmlpart = htmlpart + '<a href="http://raspberrypi/index.py?prio=3&item=' + GetListItem(Priority2List,i) + '">&#62;</a>'
      htmlpart = htmlpart + '<a href="http://raspberrypi/index.py?delete=' + GetListItem(Priority2List,i) + '">&nbsp;&#8730;</a>'
    htmlpart = htmlpart + '</td>'

    htmlpart = htmlpart + '<td>'
    if i < len(Priority3List):
      htmlpart = htmlpart + '<a href="http://raspberrypi/index.py?prio=2&item=' + GetListItem(Priority3List,i) + '">&#060;</a>'
    if i <= len(Priority3List):
      htmlpart = htmlpart + GetListItem(Priority3List,i)
    if i < len(Priority3List):
      htmlpart = htmlpart + '<a href="http://raspberrypi/index.py?prio=4&item=' + GetListItem(Priority3List,i) + '">&#062;</a>'
      htmlpart = htmlpart + '<a href="http://raspberrypi/index.py?delete=' + GetListItem(Priority3List,i) + '">&nbsp;&#8730;</a>'
    htmlpart = htmlpart + '</td>'

    htmlpart = htmlpart + '<td>'
    if i < len(Priority4List):
      htmlpart = htmlpart + '<a href="http://raspberrypi/index.py?prio=3&item=' + GetListItem(Priority4List,i) + '">&#060;</a>'
    if i <= len(Priority4List):
      htmlpart = htmlpart + GetListItem(Priority4List,i)
    if i < len(Priority4List):
      htmlpart = htmlpart + '<a href="http://raspberrypi/index.py?prio=5&item=' + GetListItem(Priority4List,i) + '">&#062;</a>'
      htmlpart = htmlpart + '<a href="http://raspberrypi/index.py?delete=' + GetListItem(Priority4List,i) + '">&nbsp;&#8730;</a>'
    htmlpart = htmlpart + '</td>'

    htmlpart = htmlpart + '<td>'
    if i < len(Priority5List):
      htmlpart = htmlpart + '<a href="http://raspberrypi/index.py?prio=4&item=' + GetListItem(Priority5List,i) + '">&#060;</a>'
    if i <= len(Priority5List):
      htmlpart = htmlpart + GetListItem(Priority5List,i)
    if i < len(Priority5List):
      htmlpart = htmlpart + '<a href="http://raspberrypi/index.py?delete=' + GetListItem(Priority5List,i) + '">&nbsp;&#8730;</a>'
    htmlpart = htmlpart + '</td>'

    htmlaprt = htmlpart + '</tr>'
    print(htmlpart)

  mydb.close()

  htmlpart = '    <tr>'
  htmlpart = htmlpart + '<td>'
  htmlpart = htmlpart + '<form action="/index.py">'
  htmlpart = htmlpart + '<input id="formfield" type="text" id="newitem1" name="newitem1">'
  htmlpart = htmlpart + '</form>'
  htmlpart = htmlpart + '</td>'
  htmlpart = htmlpart + '<td>'
  htmlpart = htmlpart + '<form action="/index.py">'
  htmlpart = htmlpart + '<input id="formfield" type="text" id="newitem2" name="newitem2">'
  htmlpart = htmlpart + '</form>'
  htmlpart = htmlpart + '</td>'
  htmlpart = htmlpart + '<td>'
  htmlpart = htmlpart + '<form action="/index.py">'
  htmlpart = htmlpart + '<input id="formfield" type="text" id="newitem3" name="newitem3">'
  htmlpart = htmlpart + '</form>'
  htmlpart = htmlpart + '</td>'
  htmlpart = htmlpart + '<td>'
  htmlpart = htmlpart + '<form action="/index.py">'
  htmlpart = htmlpart + '<input id="formfield" type="text" id="newitem4" name="newitem4">'
  htmlpart = htmlpart + '</form>'
  htmlpart = htmlpart + '</td>'
  htmlpart = htmlpart + '<td>'
  htmlpart = htmlpart + '<form action="/index.py">'
  htmlpart = htmlpart + '<input id="formfield" type="text" id="newitem5" name="newitem5">'
  htmlpart = htmlpart + '</form>'
  htmlpart = htmlpart + '</td>'
  htmlpart = htmlpart + '</tr>'
  print(htmlpart)

  htmlpart = '  </table>'
  print(htmlpart)


  htmlpart = '''  <br/><br/><br/>
  <table width="100%">
    <tr><th colspan="5">DONE</th></tr>'''
  for x, y in DoneList.items(): 
    htmlpart = htmlpart + '<tr><td>'
    htmlpart = htmlpart + '<a href="http://raspberrypi/index.py?purge=' + str(x) + '">&nbsp;&#8855;</a>'
    htmlpart = htmlpart + '&nbsp;' + x + '&nbsp;' + str(y) 
    htmlpart = htmlpart + '</td></tr>'
  htmlpart = htmlpart + '</table>'
  print(htmlpart)


def CheckForUpdates():
  args = cgi.FieldStorage()
  if "prio" in args:
    mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="hunter2",
      database="todo"
    )
    mycursor = mydb.cursor()
    SQL = "UPDATE todo SET priority = " + args["prio"].value + " WHERE item = '" + args["item"].value + "'"
    mycursor.execute(SQL)
    mydb.commit()
    mydb.close()

def CheckForNewItems():
  args = cgi.FieldStorage()
  prio = 0
  if "newitem1" in args:
    prio = 1
    item = args["newitem1"].value
  if "newitem2" in args:
    prio = 2
    item = args["newitem2"].value
  if "newitem3" in args:
    prio = 3
    item = args["newitem3"].value
  if "newitem4" in args:
    prio = 4
    item = args["newitem4"].value
  if "newitem5" in args:
    prio = 5
    item = args["newitem5"].value

  if (prio == 1) or (prio == 2) or (prio == 3) or (prio == 4) or (prio == 5):
    mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="hunter2",
      database="todo"
    )
    mycursor = mydb.cursor()
    today = datetime.datetime.now()
    SQL = "INSERT INTO todo values('" + item + "','" + str(prio) + "','0','" + today.strftime('%Y-%m-%d') + "')" 
    mycursor.execute(SQL)
    mydb.commit()
    mydb.close()
  

def CheckForDelete():
  args = cgi.FieldStorage()
  if "delete" in args:
    item = args["delete"].value
    mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="hunter2",
      database="todo"
    )
    mycursor = mydb.cursor()
    SQL = "UPDATE todo SET done = TRUE WHERE item = '" + item + "'"
    mycursor.execute(SQL)
    mydb.commit()
    mydb.close()


def CheckForPurge():
  args = cgi.FieldStorage()
  if "purge" in args:
    item = args["purge"].value
    mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="hunter2",
      database="todo"
    )
    mycursor = mydb.cursor()
    SQL = "DELETE FROM todo WHERE item='" + item + "'"
    mycursor.execute(SQL)
    mydb.commit()
    mydb.close()



CheckForUpdates()
CheckForNewItems()
CheckForDelete()
CheckForPurge()
write_html_header()
write_html_stylesheet()
write_html_body_init()
write_html_top_of_the_page()
write_html_body()
write_html_footer()



