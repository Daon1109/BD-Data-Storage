#!C:\Program Files\Python39\python.exe
print("Content-type: text/html")
print()


#HTML Code
print('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Create Page</title>
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
        <h1 class="main_title"><a href="index.py">BD Data Storage</a> - Create</h1>
        <div class="Tools">
            <a href="index.py">
                <p class="homeLink">Home</p>
            </a>
            <input class="nightmode" type="button" value="NightMode" onclick="
                nightDay(this);
            ">
        </div>

        <form action="create_process.py" method="post">
            <div class="create">
                <div class="create_index">Name</div>
                <input id="input_text" class="create_input" type="text" placeholder="Enter your name" name="name">
                <br>
                <div class="create_index">PassWord</div>
                <input id="input_text" class="create_input" type="text" placeholder="Enter your password" name="password">
                <br>
                <div class="create_index">Month and Date of the Birthday</div>
                <input id="input_text" class="create_input" type="text" placeholder="Month" name="month"><br>
                <input id="input_text" class="create_input" type="text" placeholder="Date" name="date"><br>
                <input class="create_submit" type="submit" value="Create">
            </div>
        </form>
    </body>
</html>''')
