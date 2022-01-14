#!C:\Program Files\Python39\python.exe
print("Content-type: text/html")
print()


import cgi
form = cgi.FieldStorage()

name = form["name"].value
linkAddress = form["link"].value


# HTML Code
print('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>User Authentication Page</title>
        <link rel="stylesheet" href="UA_style.css">
        <script src="nightMODE.js"></script>
    </head>
    <body>
        <h1 class="main_title"><a href="index.py">BD Data Storage</a> - User Authentication</h1>
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

        <form action="UA_process.py" method="post">
            <div class="inputblock">
                <h1 class="input_title">User Authentication - {name}</h1>
                <input id="input_text" class="pswd_input" type="text" placeholder="Enter your password" name="input_pw">
                <input type="hidden" name="link" value="{link_address}">
                <input type="hidden" name="name" value="{name}">
                <input class="pw_submit" type="submit" value="Submit">
            </div>
        </form>
    </body>
</html>'''.format(name=name, link_address=linkAddress))