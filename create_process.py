#!C:\Program Files\Python39\python.exe

import cgi
form = cgi.FieldStorage()

#form data
name = form["name"].value
pw = form["password"].value
month = form["month"].value
date = form["date"].value


#Creating File
opened_file = open('Data/'+name, 'w')
#Article Design
article = name + '\n' + pw + '\n' + month + '\n' + date
opened_file.write(article)
opened_file.close()


#Redirection
#countdown page 만들면 거기로 리다이렉트 하면됨
#print("Location: countdown.py?id=" + name)
print("Location: index.py")
print()