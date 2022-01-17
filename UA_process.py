#!C:\Program Files\Python39\python.exe


import cgi
form = cgi.FieldStorage()

import os

name = form["name"].value
link = form["link"].value
input_password = form["input_pw"].value




#This file directory is not available in Pythonanywhere repository (available in local network)
#I should google it
opened_file = open('C:\SERVER\\apache2\htdocs\BD Data Storage\Data\\'+name,'r',encoding="UTF-8")
lists = opened_file.readlines()
opened_file.close()
#password = "{}".format(lists[1])   
password = lists[1]
#Deleting escape string(\n)
password = password[0:(len(password) - 1)]


month = lists[2]
date = lists[3]


if link == "update":
    if input_password == password:
        # Deleting Process
        #This file directory is not available in Pythonanywhere too
        fileToDelete = open('C:\SERVER\\apache2\htdocs\BD Data Storage\Data\\'+name,'w',encoding="UTF-8")
        fileToDelete.close()
        os.remove("Data/"+name)
        #HTML Code
        print("Content-type: text/html")
        print()
        print('''<!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <title>Update Page</title>
                <link rel="stylesheet" href="UA_style.css">
                <script src="nightMODE.js"></script>
            </head>
            <body>
                <h1 class="main_title"><a href="index.py">BD Data Storage</a> - Update</h1>
                <div class="Tools">
                    <a href="index.py">
                        <p class="homeLink">Home</p>
                    </a>
                    <a href="countdown_pipeline.py?id={name}">
                        <p class="cntdn_button">Countdown</p>
                    </a>
                    <input class="nightmode" type="button" value="NightMode" onclick="
                        nightDay(this);
                    ">
                </div>

                <form action="update_process.py" method="post">
                    <div class="update">
                        <div class="update_index">Name</div>
                        <input id="input_text" class="update_input" type="text" value="{name}" name="name">
                        <br>
                        <div class="update_index">Password</div>
                        <input id="input_text" class="update_input" type="text" value="{password}" name="password">
                        <br>
                        <div class="update_index">Month and Date of the Birthday</div>
                        <input id="input_text" class="update_input" type="text" value="{month}" name="month"><br>
                        <input id="input_text" class="update_input" type="text" value="{date}" name="date"><br>
                        <input class="update_submit" type="submit" value="Update">
                    </div>
                </form>
            </body>
        </html>'''.format(name=name, password=password, month=month, date=date))
    else:
        # Redirecting
        # HTML Code
        print("Content-type: text/html")
        print()
        print('''
        <title>Wrong Password!</title>
        <form name="myForm" action="UA_page.py" method="post">
            <input type="hidden" name="name" value="{name}">
            <input type="hidden" name="link" value="{link}">
        </form>
        <script>
            alert('WRONG Password! Try Again');
            document.myForm.submit();
        </script>'''.format(name=name, link=link))


elif link == "delete":
    if input_password == password:
        # Deleting Process
        #This file directory is not available in Pythonanywhere too
        fileToDelete = open('C:\SERVER\\apache2\htdocs\BD Data Storage\Data\\'+name,'w',encoding="UTF-8")
        fileToDelete.close()
        os.remove("Data/"+name)
        #Redirection
        print("Location: index.py")
        print()
    else:
        # Redirecting
        # HTML Code
        print("Content-type: text/html")
        print()
        print('''
        <title>Wrong Password!</title>
        <form name="myForm" action="UA_page.py" method="post">
            <input type="hidden" name="name" value="{name}">
            <input type="hidden" name="link" value="{link}">
        </form>
        <script>
            alert('WRONG Password! Try Again');
            document.myForm.submit();
        </script>'''.format(name=name, link=link))

else:
    # ERROR MESSAGE
    # HTML Code
    print("Content-type: text/html")
    print()
    print('''
    <title>Error Occured</title>
    <form name="myForm" action="UA_page.py" method="post">
        <input type="hidden" name="name" value="{name}">
        <input type="hidden" name="link" value="{link}">
    </form>
    <script>
        alert('Error Occured. Please report bug: mathuho1109@gmail.com');
        document.myForm.submit();
    </script>'''.format(name=name, link=link))
