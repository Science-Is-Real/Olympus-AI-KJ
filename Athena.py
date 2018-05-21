from GUI_ath import *
from conversation_ath import *
import GlobalFile
import os
from os.path import join
import datetime

#   TKinter interfaces:
#   Buttons: button(Text, Command): allows you to make a button on the screen with a command to what it does
#   Printing to the GUI: Talk(Text): allows you to print directly to the GUI

def command():
    button('GPS Location', locationGPS)
    button('Rename', familiarName)
    button('Time', time)
    button('Import new modules', athImport)
    button('Talk to me!', interests)
    button('File Search', fileSearch)
    button('World Clock', worldClock)

def familiarName(x=1):
    GlobalFile.User = str(input('What would you like me to call you?\n>>> '))
    if x == 1:
        Talk('Ok, ' + GlobalFile.User + ', What would you like me to do now?')
        
def locationGPS():
    from temboo.Library.Google.Geocoding import GeocodeByAddress
    from temboo.core.session import TembooSession
    locale = str(input('What is the address? '))
    session = TembooSession('jack727', 'myFirstApp', 'ZjdczC9s7nPiHX80gyXx7YxkoYVDQRBK')
    geocodeByAddressChoreo = GeocodeByAddress(session)
    geocodeByAddressInputs = geocodeByAddressChoreo.new_input_set()
    geocodeByAddressInputs.set_Address(str(locale))
    geocodeByAddressResults = geocodeByAddressChoreo.execute_with_results(geocodeByAddressInputs)
    Talk("Longitude: " + geocodeByAddressResults.get_Longitude,1())
    Talk("Latitude: " + geocodeByAddressResults.get_Latitude())

def time():
    final = ''
    dates = datetime.datetime.now()
    dates2 = str(dates).split(' ')
    time = dates2[1].split(':')
    month1 = dates2[0].split('-')
    month="JanFebMarAprMayJunJulAugSepOctNovDec"
    number = int(month1[1])
    n=number*3
    final += str(month[n-3:n]) + ' ' + str(month1[2]) + ', ' + str(month1[0]) + ' '
    if int(time[0]) > 12:
        final += str(int(time[0]) - 12) + ':' + str(time[1]) + str(' PM')
    else:
        final += str(time[0]) + ':' + str(time[1]) + str(' AM')
    Talk(final)

def fileSearch():
    lookfor = str(input('What file would you like to search for today?: '))
    for root, dirs, files in os.walk('C:\\'):
        #print("searching", root)
        if lookfor in files:
            print("Found: %s" % join(root, lookfor))
            break

def worldClock():
    string = ''
    dicti = {'Now': [+0, +0],'London' : [+5, +0],'New York City' : [-4, +0], 'Yeet' : [+0, +0], 'Abu Dhabi' : [+4, +0], 'Abuja' : [+1, +0], 'Accra' : [+0, +0], 'Adak' : [-9,+0], 'Amsterdam' : [+2, +0], 'Anchorage' : [-8, +0], 'Athens' : [+3, +0], 'Nairobi' : [+3, +0], 'Atlanta': [-4, +0], 'Baker Lake' : [-5, +0], 'Barcelona' : [+2, +0], 'Beirut' : [+3, +0], 'Belgrade' : [+2, +0], 'Berlin' : [+2, +0], 'Bern':[+2,+0], 'Boston' : [-4,+0], 'Bratislava':[+2,+0], 'Brussels':[+2, +0], 'Bucharest':[+3, +0], 'Budapest' : [+2, +0], 'Calgary' : [-6, +0], 'Cardiff' : [+1, +0], 'Chicago' : [-5, +0], 'Copenhagen':[+2, +0], 'Dallas' :[-5, +0], 'Damascus':[+3, +0], 'Denver':[-6, +0], 'Detroit':[-4,+0], 'Dubai':[4,0], 'Dublin':[1,0], 'Eureka':[-5,0], 'Frankfurt' : [2, 0], 'Gibraltar':[2, 0], 'Halifax': [-3, 0], 'Hamilton':[-3, 0],'Havana':[-4,0], 'Helsinki':[3, 0], 'Houston':[-5,0], 'Indianapolis' : [-4, 0], 'Jerusalem':[3,0], 'Johannesburg':[2, 0], 'Juneau':[-8,0],'Kansas City':[-5,0], 'Kolkata':[5, 30], 'Kuala Lumpur':[8,0], 'Kyiv':[3,0], 'Las Vegas':[-7, 0], 'Lima':[-5,0], 'Libson': [+1, 0], 'Los Angeles':[-7,0], 'Luxembourg':[+2,+0], 'Madrid':[2, 0],'Mexico City': [-5, 0], 'Miami':[-4, 0], 'Minneapolis':[-5, 0], 'Monaco':[2,0], 'Montreal': [-4,0], 'Nassau':[-4, 0], 'New Orleans':[-5,0],'Nuuk':[-2,0], 'Oslo':[2,0], 'Ottawa':[-4,0], 'Paris':[2,0], 'Philadelphia':[-4,0], 'Port-au-Prince':[-4,0], 'Prague':[2,0], 'Rome':[+2, 0], 'Salt Lake City': [-6,0], 'San Francisco':[-7,0], 'Seattle': [-7,0], 'Sofia':[3,0], 'Stockholm':[2,0],'Tehran':[4,30],'Tokyo':[9,0], 'Toronto':[-4,0],'Vancouver':[-7,0], 'Vatican City' : [+2,0], 'Vienna':[2,0], 'Washington DC':[-4,0], 'Winnipeg':[-5,0], 'Zurich':[2,0]}
    dictikeys = dicti.keys()
    user = input('What MAJOR city would you like to know the time of, if you want all type ALL: ')
    if user not in dicti and user != 'ALL':
        user = 'Yeet'
    if user == 'Yeet':
        print('Not in my database')
    elif user != 'ALL' and user != 'Yeet':
        dates = datetime.datetime.now()
        dates2 = str(dates).split(' ')
        time = dates2[1].split(':')
        month1 = dates2[0].split('-')
        month="JanFebMarAprMayJunJulAugSepOctNovDec"
        number = int(month1[1])
        n=number*3
        day = month1[2]
        hour = int(time[0]) + dicti[user][0] + 4
        minute = int(time[1]) + dicti[user][1]
        if hour > 24:
            hour = hour - 24
            day += 1
        if minute > 59:
            minute = minute - 60
            if minute < 10:
                minute = str(0) + str(minute)
        if user in dicti and user != 'Yeet':
            string += str(user) + ' : ' + str(month[n-3:n]) + ' ' + str(day) + ', ' + str(month1[0]) + ' ' + str(hour) + ':' + str(minute)

        print(string)
    
    elif user == 'ALL':
        for x in dictikeys:
            string = ''
            user = x
            dates = datetime.datetime.now()
            dates2 = str(dates).split(' ')
            time = dates2[1].split(':')
            month1 = dates2[0].split('-')
            month="JanFebMarAprMayJunJulAugSepOctNovDec"
            number = int(month1[1])
            n=number*3
            day = int(month1[2])
            hour = int(time[0]) + dicti[user][0] + 4
            minute = int(time[1]) + dicti[user][1]
            if hour > 24:
                hour = hour - 24
                day += 1
            if minute > 59:
                minute = minute - 60
                if minute < 10:
                    minute = str(0) + str(minute)
            if user in dicti and user != 'Yeet':
                string += str(user) + ' : ' + str(month[n-3:n]) + ' ' + str(day) + ', ' + str(month1[0]) + ' ' + str(hour) + ':' + str(minute)
    
            print(string)
    
def athImport():
    d = 0
    print("Ok, for me to import something I need the module's name, and it needs to contain the compatible '_ath' tag for me to utilize it.")
    print('Think of it as giving me notes to study so I can do more cool things for you. ^-^')
    mod = input('What do you want me to import, ' + GlobalFile.User + '?\n>>> ')
    while d != 1:
        if str(mod[-4:]) != '_ath':
            print('Sorry ' + User + ", I cant read this, I'm gonna need you to find me a program with the tag '_ath'")
            mod = input('What do you want me to import, ' + GlobalFile.User + '?\n>>> ')
            d = 0
        else:
            print('Ok, let me get this done. it may take a moment for me to finish it')
            exec("import "+mod,globals())
            exec("global "+mod,globals())
            print("There we go, I've imported what you asked for, " + GlobalFile.User + '.')
            d = 1
        
Talk('Welcome to the Athena Network.',1)
familiarName(0)
command()
