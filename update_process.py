#!C:\Program Files\Python39\python.exe


import cgi
form = cgi.FieldStorage()

#Receiving form data
name = form["name"].value
password = form["password"].value
month = form["month"].value
date = form["date"].value

#Creating File
opened_file = open('Data/'+name, 'w', encoding="UTF-8")
#Article Design
article = name + '\n' + password + '\n' + month + '\n' + date
opened_file.write(article)
opened_file.close()


#Redirection
print("Location: countdown_pipeline.py?id=" + name)
print()