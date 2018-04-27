from temboo import *
from GUI_ath import *
import GlobalFile

def command():
    Talk('Right now I can allow you to use these functions:',1)
    Talk('The familiarName() function   -Changes user name',1)
    Talk('The athImport() function  -Imports additional Athena functionality',1)
    Talk('The locationGPS() function  -Gives you the gps coordinates of an address')

def familiarName(x=1):
    GlobalFile.User = str(input('What would you like me to call you?\n>>> '))
    if x == 1:
        Talk('Ok, ' + GlobalFile.User + ', What would you like me to do now?')
        
def locationGPS():
    from temboo.Library.Google.Geocoding import GeocodeByAddress
    from temboo.core.session import TembooSession
    locale = input('What is the address? ')
    session = TembooSession('jack727', 'myFirstApp', 'ZjdczC9s7nPiHX80gyXx7YxkoYVDQRBK')
    geocodeByAddressChoreo = GeocodeByAddress(session)
    geocodeByAddressInputs = geocodeByAddressChoreo.new_input_set()
    geocodeByAddressInputs.set_Address(str(locale))
    geocodeByAddressResults = geocodeByAddressChoreo.execute_with_results(geocodeByAddressInputs)
    Talk("Longitude: " + geocodeByAddressResults.get_Longitude,1())
    Talk("Latitude: " + geocodeByAddressResults.get_Latitude())
    
def athImport():
    print("Ok, for me to import something I need the module's name, and it needs to contain the compatible '_ath' tag for me to utilize it.")
    print('Think of it as giving me notes to study so I can do more cool things for you. ^-^')
    mod = input('What do you want me to import, ' + GlobalFile.User + '?\n>>> ')
    if str(mod[-4:]) != '_ath':
        print('Sorry ' + GlobalFile.User + ", I cant read this, I'm gonna need you to find me a program with the tag '_ath'")
    else:
        print('Ok, let me get this done. it may take a moment for me to finish it')
        exec("import "+mod,globals())
        exec("global "+mod,globals())
        print("There we go, I've imported what you asked for, " + GlobalFile.User + '.')
        
Talk('Welcome to the Athena Network.',1)
familiarName(0)
Talk('Hello ' + GlobalFile.User + ', you can use command() to bring up a list of functions that are compatable with the network')
