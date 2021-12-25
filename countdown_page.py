#!C:\Program Files\Python39\python.exe
print("Content-type: text/html")
print()


#
#5-2. 카운트다운 알고리즘 찾고 응용 (계획: 무한 while문에 HTML 코드 넣기 & 즉각적 치환)
#6. 카운트다운 페이지 UI 제작
#


from countdown import LeftTime
import cgi
form = cgi.FieldStorage()


#Receiving Form Data
#name = form["name"].value
name = 'Suho'


while True:
    countdown_List = LeftTime(name)

    month = countdown_List[0]
    day = countdown_List[1]
    hour = countdown_List[2]
    minute = countdown_List[3]
    second = countdown_List[4]

    #HTML Code
    print('''<!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>BD Data Storage</title>
            <link rel="stylesheet" href="countdownstyles.css">
            <script src="nightMODE.js"></script>

            <script>
                function fetchArticle(fileName) {{
                    fetch(fileName).then(function(response) {{
                        response.text().then(function(text) {{
                            document.querySelector('article').innerHTML=text;
                        }})
                    }})
                }}
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
                    <article class="cntText1">{Leftmonth} Month</article>
                    <article class="cntText2">{Leftday} Day</article>
                    <article class="cntText3">{Lefthour} Hour</article>
                    <article class="cntText4">{Leftmin} Minute</article>
                    <article class="cntText5">{Leftsec} Second</article>
            </div>

        </body>
    </html>'''.format(name = name, Leftmonth = month, Leftday = day, Lefthour = hour, Leftmin = minute, Leftsec = second))