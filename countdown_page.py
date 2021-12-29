#!C:\Program Files\Python39\python.exe
print("Content-type: text/html")
print()


import cgi
form = cgi.FieldStorage()

name = form["Pname"].value
timestring = form["timestring"].value


# HTML Code
print('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>BD Data Storage</title>
        <link rel="stylesheet" href="countdownstyles.css">
        <script src="countdown.js"></script>
        <script src="nightMODE.js"></script>
        <script>
            data = "{timestring}"
            sendingdata(data);
        </script>
    </head>

    <body>
        <h1 class="main_title">{name}'s Birthday Countdown</h1>
        <div class="Tools">
            <a href="index.py">
                <p class="homeLink">Home</p>
            </a>
            <input class="nightmode" type="button" value="NightMode" onclick="
                nightDay(this);
            ">
            <a href="update.py">
                <p class="updateLink">Update</p>
            </a>
            <a href="delete.py">
                <p class="deleteLink">Delete</p>
            </a>
        </div>

        <div class="countdownarticle">
                <article class="cntText"><span id="form_date"></span> Days</article>
                <article class="cntText"><span id="form_hour"></span> Hours</article>
                <article class="cntText"><span id="form_min"></span> Minutes</article>
                <article class="cntText"><span id="form_sec"></span> Seconds</article>
        </div>

    </body>
</html>'''.format(timestring = timestring, name = name))