#!C:\Program Files\Python39\python.exe
print("Content-type: text/html")
print()

#Making List
import os
filenames = os.listdir('Data')
lists = ''
for eachfile in filenames:
      lists = lists + '<li><a href = "countdown.py?id={name}">{name}</a></li>'.format(name = eachfile)
      lists = "{}".format(lists)

#Writing List file
opened_file = open('List', 'w')
opened_file.write(lists)
opened_file.close()

#HTML Code
print('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>BD Data Storage</title>
        <link rel="stylesheet" href="style.css">
        <script src="nightMODE.js"></script>

        <script>
            function fetchArticle(fileName) {{
                fetch(fileName).then(function(response) {{
                    response.text().then(function(text) {{
                        document.querySelector('#namelist').innerHTML=text;
                    }})
                }})
            }}
        </script>
    </head>
    <body>
        <h1 class="main_title">BD Data Storage</h1>
        <div class="Tools">
            <a href="create.py">
                <p class="createData">Create</p>
            </a>
            <input class="nightmode" type="button" value="NightMode" onclick="
                nightDay(this);
            ">
        </div>

        <form action="countdown.py">
            <div class="search">
                <input class="search_input" type="text" placeholder="Enter your name" name="name">
                <input class="search_submit" type="submit" value="Search">
            </div>
        </form>

        <div>
            <h2 class="list_article" onclick="fetchArticle('List')">See Other People's Birthday</h2>
            <p id="namelist"></p>
        </div>
    </body>
</html>'''.format(lists=lists))