#!C:\Program Files\Python39\python.exe
print("Content-type: text/html")
print()


import cgi
form = cgi.FieldStorage()

name = form["id"].value

#This file directory is not available in Pythonanywhere repository (available in local network)
#I should google it

opened_file = open('C:\SERVER\\apache2\htdocs\BD Data Storage\Data\\'+name,'r',encoding="UTF-8")
lists = opened_file.readlines()
opened_file.close

month = int(lists[2])
date = lists[3]

if month == 1:
    Cmonth = 'Jan '
elif month == 2:
    Cmonth = 'Feb '
elif month == 3:
    Cmonth = 'Mar '
elif month == 4:
    Cmonth = 'Apr '
elif month == 5:
    Cmonth = 'May '
elif month == 6:
    Cmonth = 'Jun '
elif month == 7:
    Cmonth = 'Jul '
elif month == 8:
    Cmonth = 'Aug '
elif month == 9:
    Cmonth = 'Sep '
elif month == 10:
    Cmonth = 'Oct '
elif month == 11:
    Cmonth = 'Nov '
elif month == 12:
    Cmonth = 'Dec '

timestring = Cmonth + date + ", 2022 00:00:00"


# HTML Code
print('''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>BD Data Storage</title>
        <meta http-equiv = "refresh" content = "0; url = http://localhost/BD%20Data%20Storage/countdown_page.py" />
    </head>
    <body>

        <form name="myForm" action="countdown_page.py" method="post">
            <input type="hidden" name="Pname" value="{name}">
            <input type="hidden" name="timestring" value="{timestring}">
        </form>
        <script>
            document.myForm.submit();
        </script>
    </body>
</html>'''.format(timestring = timestring, name = name))