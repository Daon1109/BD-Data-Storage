

#This is module file
#It defines function LeftTime

def LeftTime(name):
    
    #Setting Variable

    #This file directory is not available in Pythonanywhere repository (available in local network)
    #I should google it
    opened_file = open('C:\SERVER\\apache2\htdocs\BD Data Storage\Data\\'+name,'r',encoding="UTF-8")
    lists = opened_file.readlines()
    #print(lists)
    opened_file.close

    BD_month = lists[2]
    BD_date = lists[3]


    # Importing required libraries
    from datetime import datetime   #To set date and time

    now = datetime.now()

    current_month = now.strftime("%m")
    current_date = now.strftime("%d")
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")

    monthLeft = int(BD_month) - int(current_month)
    dayLeft = int(BD_date) - int(current_date)
    while True:
        #countdown_month
        if monthLeft < 0:
            monthLeft = monthLeft + 12
        else:
            break
    while True:
        #countdown_date
        if dayLeft < 0:
            current_month = int(current_month) - 1
            monthLeft = monthLeft - 1
            if current_month == 1 or current_month == 3 or current_month == 5 or current_month == 7 or current_month == 8 or current_month == 10 or current_month == 12:
                dayLeft = dayLeft + 31
            elif current_month == 4 or current_month == 6 or current_month == 9 or current_month == 11:
                dayLeft = dayLeft + 30
            elif current_month == 2:
                dayLeft = dayLeft + 28
        else:
            break
    #countdown_hour
    dayLeft = dayLeft - 1
    hourLeft = 24 - int(current_hour)
    #countdown_minute
    hourLeft = hourLeft - 1
    minuteLeft = 60 - int(current_minute)
    #countdown_second
    minuteLeft = minuteLeft - 1
    secLeft = 60 - int(current_second)

    countdown_List = [monthLeft,dayLeft,hourLeft,minuteLeft,secLeft]

    return countdown_List
