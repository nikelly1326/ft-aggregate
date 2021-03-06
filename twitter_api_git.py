#clean version of code

#Required packages
import tweepy
import argparse
import json
import ijson
import os
import re
import pandas as pd
#does not truncate columns when displaying
pd.set_option('display.max_colwidth', -1)
import time
import numpy
#set up working directory
os.getcwd()
os.chdir("/Users/nicolekelly/Documents/ft_aggregate/")



#Setting up Twitter API
#twitterkeys.py is a file that contains my consumer_key, consumer_secret, access_token and access_token_secret
import twitterkeys

auth = tweepy.OAuthHandler(twitterkeys.consumer_key, twitterkeys.consumer_secret)
auth.set_access_token(twitterkeys.access_token, twitterkeys.access_token_secret)

api = tweepy.API(auth)



#second method from David
#Pull in most recent 20 tweets
#need to figure out how to pull in nested dictionaries 
    #like retweeted_status (which gives more information than just an indicator for retweets), hashtags, etc
ArepaZone_timeline=api.user_timeline("ArepaZone")
arepa_tweets=[]
for tweet in ArepaZone_timeline:
    tweet_parts = {
        "id":tweet.id,
        "created_at":tweet.created_at,
        "text":tweet.text,
        #"retweeted_status":tweet.retweeted_status,
        "in_reply_to_status_id":tweet.in_reply_to_status_id,
        "in_reply_to_user_id":tweet.in_reply_to_user_id,
        "lang":tweet.lang,
        "source":tweet.source,
        "favorited":tweet.favorited,
        "coordinates":tweet.coordinates,
        "place":tweet.place,
        "geo":tweet.geo,
        "is_quote_status":tweet.is_quote_status,
        "contributors":tweet.contributors,
        "retweeted":tweet.retweeted,
        "truncated":tweet.truncated,
        "favorite_count":tweet.favorite_count,
        "retweet_count":tweet.retweet_count
    }
    arepa_tweets.append(tweet_parts)

ArepaZone_df = pd.DataFrame(arepa_tweets)
#ArepaZone_df.text



#doesn't work yet, something with the pd.DataFrame line syntax
trucks=['captaincookiedc']
for food_truck_twitter_handle in trucks:
    food_truck_twitter_handle_timeline=api.user_timeline('{}'.format(food_truck_twitter_handle))
    food_truck_twitter_handle_tweets=[]
    for tweet in food_truck_twitter_handle_timeline:
        tweet_parts = {
            "id":tweet.id,
            "created_at":tweet.created_at,
            "text":tweet.text
        }
        food_truck_twitter_handle_tweets.append(tweet_parts)
    food_truck_twitter_handle_df = pd.DataFrame(food_truck_twitter_handle_tweets)
    return food_truck_twitter_handle_df



#Function does the same thing as above, make sure to have a df=tweets_to_datafram(values) for it to save the values
def tweets_to_dataframe(food_truck_twitter_handle, food_truck_twitter_handle_string):
    food_truck_twitter_handle_timeline=api.user_timeline('{}'.format(food_truck_twitter_handle_string))
    food_truck_twitter_handle_tweets=[]
    for tweet in food_truck_twitter_handle_timeline:
        tweet_parts = {
            "id":tweet.id,
            "created_at":tweet.created_at,
            "text":tweet.text,
            "in_reply_to_status_id":tweet.in_reply_to_status_id,
            "in_reply_to_user_id":tweet.in_reply_to_user_id,
            "lang":tweet.lang,
            "source":tweet.source,
            "favorited":tweet.favorited,
            "coordinates":tweet.coordinates,
            "place":tweet.place,
            "geo":tweet.geo,
            "is_quote_status":tweet.is_quote_status,
            "contributors":tweet.contributors,
            "retweeted":tweet.retweeted,
            "truncated":tweet.truncated,
            "favorite_count":tweet.favorite_count,
            "retweet_count":tweet.retweet_count
            }
        food_truck_twitter_handle_tweets.append(tweet_parts)
    food_truck_twitter_handle_df = pd.DataFrame(food_truck_twitter_handle_tweets)
    #When I append multiple food trucks together into a larger dataframe, I want to be able to identify them 
    food_truck_twitter_handle_df['username']='{}'.format(food_truck_twitter_handle_string)
    return food_truck_twitter_handle_df


#df_ needs to go first because some trucknames start with numbers
#I should probably get the loop working because this is a ton of lines for 200+ trucks
df_abunaifood=tweets_to_dataframe('abunaifood','abunaifood')
df_AmoriniPanini=tweets_to_dataframe('AmoriniPanini','AmoriniPanini')
df_AngryBurgerNOW=tweets_to_dataframe('AngryBurgerNOW','AngryBurgerNOW')
df_arepacrew=tweets_to_dataframe('arepacrew','arepacrew')
df_ArepaZone=tweets_to_dataframe('ArepaZone','ArepaZone')
df_AstroDoughnuts=tweets_to_dataframe('AstroDoughnuts','AstroDoughnuts')
df_Partytrucks=tweets_to_dataframe('Partytrucks','Partytrucks')
df_AZNeats=tweets_to_dataframe('AZNeats','AZNeats')
df_alocubanotruck=tweets_to_dataframe('alocubanotruck','alocubanotruck')
df_BabasBigBite=tweets_to_dataframe('BabasBigBite','BabasBigBite')
df_badabingdc=tweets_to_dataframe('badabingdc','badabingdc')
df_balkaniktaste=tweets_to_dataframe('balkaniktaste','balkaniktaste')
df_theballtruck=tweets_to_dataframe('theballtruck','theballtruck')
df_BanhMiAnnie=tweets_to_dataframe('BanhMiAnnie','BanhMiAnnie')
df_BasilThymeDC=tweets_to_dataframe('BasilThymeDC','BasilThymeDC')
df_bbqbusdc=tweets_to_dataframe('bbqbusdc','bbqbusdc')
df_gotbeachfries=tweets_to_dataframe('gotbeachfries','gotbeachfries')
df_BeirutDelights=tweets_to_dataframe('BeirutDelights','BeirutDelights')
df_bellavitawheels=tweets_to_dataframe('bellavitawheels','bellavitawheels')
df_bestburritos1=tweets_to_dataframe('bestburritos1','bestburritos1')
df_okbibija=tweets_to_dataframe('okbibija','okbibija')
df_bigcheesetruck=tweets_to_dataframe('bigcheesetruck','bigcheesetruck')
df_BITE2GO=tweets_to_dataframe('BITE2GO','BITE2GO')
df_eatBONMi=tweets_to_dataframe('eatBONMi','eatBONMi')
df_Borinquenlunchb=tweets_to_dataframe('Borinquenlunchb','Borinquenlunchb')
df_BLTfoodtruck=tweets_to_dataframe('BLTfoodtruck','BLTfoodtruck')
df_bratwurstking=tweets_to_dataframe('bratwurstking','bratwurstking')
df_bklynsandwichco=tweets_to_dataframe('bklynsandwichco','bklynsandwichco')
df_eatbrownbag=tweets_to_dataframe('eatbrownbag','eatbrownbag')
df_bubbleteaparty=tweets_to_dataframe('bubbleteaparty','bubbleteaparty')
df_burgorilla=tweets_to_dataframe('burgorilla','burgorilla')
df_CAslidercompany=tweets_to_dataframe('CAslidercompany','CAslidercompany')
df_cajunators=tweets_to_dataframe('cajunators','cajunators')
df_CapitalCW=tweets_to_dataframe('CapitalCW','CapitalCW')
df_capmacdc=tweets_to_dataframe('capmacdc','capmacdc')
df_CaptainCookieDC=tweets_to_dataframe('CaptainCookieDC','CaptainCookieDC')
df_Caribbean2Go=tweets_to_dataframe('Caribbean2Go','Caribbean2Go')
df_CarmensCarts=tweets_to_dataframe('CarmensCarts','CarmensCarts')
df_carnbbq=tweets_to_dataframe('carnbbq','carnbbq')
df_EatCarolinaQ=tweets_to_dataframe('EatCarolinaQ','EatCarolinaQ')
df_1styellowvendor=tweets_to_dataframe('1styellowvendor','1styellowvendor')
df_ChatpatTruck=tweets_to_dataframe('ChatpatTruck','ChatpatTruck')
df_cheesequakedc=tweets_to_dataframe('cheesequakedc','cheesequakedc')
df_chefalex2013=tweets_to_dataframe('chefalex2013','chefalex2013')
df_ChefonWheels11=tweets_to_dataframe('ChefonWheels11','ChefonWheels11')
#chefsebonwheels is deactivated currently
#df_chefsebonwheels=tweets_to_dataframe('chefsebonwheels','chefsebonwheels')
df_ChezAdilmos=tweets_to_dataframe('ChezAdilmos','ChezAdilmos')
df_chickfilamobile=tweets_to_dataframe('chickfilamobile','chickfilamobile')
df_ChittiGrill=tweets_to_dataframe('ChittiGrill','ChittiGrill')
df_ChixNStixDC=tweets_to_dataframe('ChixNStixDC','ChixNStixDC')
df_coles_palette=tweets_to_dataframe('coles_palette','coles_palette')
df_cornedbeefking=tweets_to_dataframe('cornedbeefking','cornedbeefking')
df_CrabCab=tweets_to_dataframe('CrabCab','CrabCab')
df_CRAVEIT2=tweets_to_dataframe('CRAVEIT2','CRAVEIT2')
df_cremedelacakedc=tweets_to_dataframe('cremedelacakedc','cremedelacakedc')
df_crepelovetruck=tweets_to_dataframe('crepelovetruck','crepelovetruck')
df_CrepesParfait=tweets_to_dataframe('CrepesParfait','CrepesParfait')
df_JoyCupcakes=tweets_to_dataframe('JoyCupcakes','JoyCupcakes')
df_CurbSideCrab=tweets_to_dataframe('CurbSideCrab','CurbSideCrab')
df_curbsidecupcake=tweets_to_dataframe('curbsidecupcake','curbsidecupcake')
df_CurleysQ=tweets_to_dataframe('CurleysQ','CurleysQ')
df_ThePieTruckDC=tweets_to_dataframe('ThePieTruckDC','ThePieTruckDC')
df_DcBallers=tweets_to_dataframe('DcBallers','DcBallers')
df_dc_doner=tweets_to_dataframe('dc_doner','dc_doner')
df_DCEmpanadas=tweets_to_dataframe('DCEmpanadas','DCEmpanadas')
df_dc_greekfood=tweets_to_dataframe('dc_greekfood','dc_greekfood')
df_dcpollos=tweets_to_dataframe('dcpollos','dcpollos')
df_DCQuesadilla=tweets_to_dataframe('DCQuesadilla','DCQuesadilla')
df_dcslices=tweets_to_dataframe('dcslices','dcslices')
df_DCSLIDERSTRUCK=tweets_to_dataframe('DCSLIDERSTRUCK','DCSLIDERSTRUCK')
df_DCTacoTruck=tweets_to_dataframe('DCTacoTruck','DCTacoTruck')
df_dirtysouthdeli=tweets_to_dataframe('dirtysouthdeli','dirtysouthdeli')
df_DolciGelatiTruk=tweets_to_dataframe('DolciGelatiTruk','DolciGelatiTruk')
df_donburidc=tweets_to_dataframe('donburidc','donburidc')
df_DorothyMoon1=tweets_to_dataframe('DorothyMoon1','DorothyMoon1')
df_dougthefooddude=tweets_to_dataframe('dougthefooddude','dougthefooddude')
df_DuckysGrub=tweets_to_dataframe('DuckysGrub','DuckysGrub')
df_elFuegoDc=tweets_to_dataframe('elFuegoDc','elFuegoDc')
df_EndlessPLLC=tweets_to_dataframe('EndlessPLLC','EndlessPLLC')
df_FarEastTG=tweets_to_dataframe('FarEastTG','FarEastTG')
df_Fasikacuisin=tweets_to_dataframe('Fasikacuisin','Fasikacuisin')
df_FavaPot=tweets_to_dataframe('FavaPot','FavaPot')
df_FedCityBros=tweets_to_dataframe('FedCityBros','FedCityBros')
df_feelincrabby=tweets_to_dataframe('feelincrabby','feelincrabby')
df_eatFireNRice=tweets_to_dataframe('eatFireNRice','eatFireNRice')
df_firemanscafe=tweets_to_dataframe('firemanscafe','firemanscafe')
df_FoodLady2011=tweets_to_dataframe('FoodLady2011','FoodLady2011')
df_foodforceone1=tweets_to_dataframe('foodforceone1','foodforceone1')
df_freshgreenfood=tweets_to_dataframe('freshgreenfood','freshgreenfood')
df_FroZenYoToGo=tweets_to_dataframe('FroZenYoToGo','FroZenYoToGo')
df_FCFoodTruck=tweets_to_dataframe('FCFoodTruck','FCFoodTruck')
df_GeorgesWingTruk=tweets_to_dataframe('GeorgesWingTruk','GeorgesWingTruk')
df_gofishtruckdc=tweets_to_dataframe('gofishtruckdc','gofishtruckdc')
df_mobilekitchen=tweets_to_dataframe('mobilekitchen','mobilekitchen')
df_GAHDTruck=tweets_to_dataframe('GAHDTruck','GAHDTruck')
df_GREENEGGBURGERS=tweets_to_dataframe('GREENEGGBURGERS','GREENEGGBURGERS')
df_GridsWaffles=tweets_to_dataframe('GridsWaffles','GridsWaffles')
df_GuaposFoodTruck=tweets_to_dataframe('GuaposFoodTruck','GuaposFoodTruck')
df_habebe19=tweets_to_dataframe('habebe19','habebe19')
df_wherehalal=tweets_to_dataframe('wherehalal','wherehalal')
df_hardysbbqdivine=tweets_to_dataframe('hardysbbqdivine','hardysbbqdivine')
df_healthyfool=tweets_to_dataframe('healthyfool','healthyfool')
df_henhousedc=tweets_to_dataframe('henhousedc','henhousedc')
df_HolyCrepesTruck=tweets_to_dataframe('HolyCrepesTruck','HolyCrepesTruck')
df_HotPeopleFood=tweets_to_dataframe('HotPeopleFood','HotPeopleFood')
df_DCHotWheels=tweets_to_dataframe('DCHotWheels','DCHotWheels')
df_HouseofFalafel=tweets_to_dataframe('HouseofFalafel','HouseofFalafel')
df_hulagirltruck=tweets_to_dataframe('hulagirltruck','hulagirltruck')
df_hungryheartllc=tweets_to_dataframe('hungryheartllc','hungryheartllc')
df_italiansubs1=tweets_to_dataframe('italiansubs1','italiansubs1')
df_JMCCurbside=tweets_to_dataframe('JMCCurbside','JMCCurbside')
df_jerkchickenfest=tweets_to_dataframe('jerkchickenfest','jerkchickenfest')
df_KababjiTruck=tweets_to_dataframe('KababjiTruck','KababjiTruck')
df_KabobBites=tweets_to_dataframe('KabobBites','KabobBites')
df_kabob_king=tweets_to_dataframe('kabob_king','kabob_king')
df_kabobpalace1=tweets_to_dataframe('kabobpalace1','kabobpalace1')
df_KaftaMania=tweets_to_dataframe('KaftaMania','KaftaMania')
df_kalaverasdc=tweets_to_dataframe('kalaverasdc','kalaverasdc')
df_KimchiBBQ=tweets_to_dataframe('KimchiBBQ','KimchiBBQ')
df_dckbbqbox=tweets_to_dataframe('dckbbqbox','dckbbqbox')
df_korengy=tweets_to_dataframe('korengy','korengy')
df_kravingkabob=tweets_to_dataframe('kravingkabob','kravingkabob')
df_kushimototruck=tweets_to_dataframe('kushimototruck','kushimototruck')
df_LATacoTruck=tweets_to_dataframe('LATacoTruck','LATacoTruck')
df_LaTingeriaTruck=tweets_to_dataframe('LaTingeriaTruck','LaTingeriaTruck')
df_latinamericanf1=tweets_to_dataframe('latinamericanf1','latinamericanf1')
df_lemongrasstruck=tweets_to_dataframe('lemongrasstruck','lemongrasstruck')
df_LilypadontheRun=tweets_to_dataframe('LilypadontheRun','LilypadontheRun')
df_Limetreetruck=tweets_to_dataframe('Limetreetruck','Limetreetruck')
df_LLuncheonette=tweets_to_dataframe('LLuncheonette','LLuncheonette')
df_LittleItalyDC=tweets_to_dataframe('LittleItalyDC','LittleItalyDC')
df_chefty99=tweets_to_dataframe('chefty99','chefty99')
df_loslobosburrito=tweets_to_dataframe('loslobosburrito','loslobosburrito')
df_macattackdc=tweets_to_dataframe('macattackdc','macattackdc')
df_macsdonuts=tweets_to_dataframe('macsdonuts','macsdonuts')
df_MakiShopTruck=tweets_to_dataframe('MakiShopTruck','MakiShopTruck')
df_MamasDonutBites=tweets_to_dataframe('MamasDonutBites','MamasDonutBites')
df_MayurKababHouse=tweets_to_dataframe('MayurKababHouse','MayurKababHouse')
df_Med_Delight=tweets_to_dataframe('Med_Delight','Med_Delight')
df_Meggrollmania=tweets_to_dataframe('Meggrollmania','Meggrollmania')
df_meskihealthy2go=tweets_to_dataframe('meskihealthy2go','meskihealthy2go')
df_mesobonwheels=tweets_to_dataframe('mesobonwheels','mesobonwheels')
df_Miamiviceburger=tweets_to_dataframe('Miamiviceburger','Miamiviceburger')
df_MidniteCC=tweets_to_dataframe('MidniteCC','MidniteCC')
df_MightyDogAcai=tweets_to_dataframe('MightyDogAcai','MightyDogAcai')
df_MisoHoneyTruck=tweets_to_dataframe('MisoHoneyTruck','MisoHoneyTruck')
df_mohmohdumpling=tweets_to_dataframe('mohmohdumpling','mohmohdumpling')
df_mojaitalatinfla=tweets_to_dataframe('mojaitalatinfla','mojaitalatinfla')
df_Mojotruck=tweets_to_dataframe('Mojotruck','Mojotruck')
df_Miyagifoodtruck=tweets_to_dataframe('Miyagifoodtruck','Miyagifoodtruck')
df_MuncheezDC=tweets_to_dataframe('MuncheezDC','MuncheezDC')
#NaanStopDC is currently deactivated
#df_NaanStopDC=tweets_to_dataframe('NaanStopDC','NaanStopDC')
df_NeatMeatDC=tweets_to_dataframe('NeatMeatDC','NeatMeatDC')
df_NYDeliTruck=tweets_to_dataframe('NYDeliTruck','NYDeliTruck')
df_OliviasCupcakes=tweets_to_dataframe('OliviasCupcakes','OliviasCupcakes')
df_OohDaTChickeN=tweets_to_dataframe('OohDaTChickeN','OohDaTChickeN')
df_orangecowdc=tweets_to_dataframe('orangecowdc','orangecowdc')
df_overtherice=tweets_to_dataframe('overtherice','overtherice')
df_parskabob=tweets_to_dataframe('parskabob','parskabob')
df_passl0nfrult=tweets_to_dataframe('passl0nfrult','passl0nfrult')
df_pepefoodtruck=tweets_to_dataframe('pepefoodtruck','pepefoodtruck')
df_perubrothers=tweets_to_dataframe('perubrothers','perubrothers')
df_buritosontherun=tweets_to_dataframe('buritosontherun','buritosontherun')
df_philliesphamous=tweets_to_dataframe('philliesphamous','philliesphamous')
df_phojunkies=tweets_to_dataframe('phojunkies','phojunkies')
#PhoBachi changed its handle to @PhoBachi
#df_PhoBachiInc=tweets_to_dataframe('PhoBachiInc','PhoBachiInc')
df_PhoBachi=tweets_to_dataframe('PhoBachi','PhoBachi')
df_dcphonation=tweets_to_dataframe('dcphonation','dcphonation')
df_PhoWheels=tweets_to_dataframe('PhoWheels','PhoWheels')
df_pleasantpops=tweets_to_dataframe('pleasantpops','pleasantpops')
df_PoppedRepublic=tweets_to_dataframe('PoppedRepublic','PoppedRepublic')
df_dcpuddin=tweets_to_dataframe('dcpuddin','dcpuddin')
df_quickwraps=tweets_to_dataframe('quickwraps','quickwraps')
df_therandyradish=tweets_to_dataframe('therandyradish','therandyradish')
df_RebasFunnelCake=tweets_to_dataframe('RebasFunnelCake','RebasFunnelCake')
df_LobstertruckDC=tweets_to_dataframe('LobstertruckDC','LobstertruckDC')
df_redbonefc=tweets_to_dataframe('redbonefc','redbonefc')
df_ReggaeVibesTruk=tweets_to_dataframe('ReggaeVibesTruk','ReggaeVibesTruk')
df_riochurrascoDC=tweets_to_dataframe('riochurrascoDC','riochurrascoDC')
df_RitoLoco=tweets_to_dataframe('RitoLoco','RitoLoco')
df_RoamingRoti=tweets_to_dataframe('RoamingRoti','RoamingRoti')
df_RocklandsTruck=tweets_to_dataframe('RocklandsTruck','RocklandsTruck')
df_RockSalt_=tweets_to_dataframe('RockSalt_','RockSalt_')
df_Rollinpizzadc=tweets_to_dataframe('Rollinpizzadc','Rollinpizzadc')
df_rollinkabob=tweets_to_dataframe('rollinkabob','rollinkabob')
df_RollsOnRolls=tweets_to_dataframe('RollsOnRolls','RollsOnRolls')
df_RovingItalian=tweets_to_dataframe('RovingItalian','RovingItalian')
df_asgharboa=tweets_to_dataframe('asgharboa','asgharboa')
df_saffrontruckdc=tweets_to_dataframe('saffrontruckdc','saffrontruckdc')
df_SangOnWheels=tweets_to_dataframe('SangOnWheels','SangOnWheels')
df_SaransVegiTruck=tweets_to_dataframe('SaransVegiTruck','SaransVegiTruck')
df_SateTruck=tweets_to_dataframe('SateTruck','SateTruck')
df_Scoops2u=tweets_to_dataframe('Scoops2u','Scoops2u')
#Senortaco7 appears deactivated
#df_senortaco7=tweets_to_dataframe('senortaco7','senortaco7')
df_SeoulFoodDC=tweets_to_dataframe('SeoulFoodDC','SeoulFoodDC')
#Sidewalkssweets tweets are protected, I could follow them but for now I will ignore
#df_sidewalksweets=tweets_to_dataframe('sidewalksweets','sidewalksweets')
df_simple_wheels=tweets_to_dataframe('simple_wheels','simple_wheels')
df_simplysoulfood=tweets_to_dataframe('simplysoulfood','simplysoulfood')
df_Sinplicity1=tweets_to_dataframe('Sinplicity1','Sinplicity1')
df_SloppyMamas=tweets_to_dataframe('SloppyMamas','SloppyMamas')
df_BayouGators=tweets_to_dataframe('BayouGators','BayouGators')
df_smokingkowbbq=tweets_to_dataframe('smokingkowbbq','smokingkowbbq')
df_solmexicangrill=tweets_to_dataframe('solmexicangrill','solmexicangrill')
df_SouthMeetsEast=tweets_to_dataframe('SouthMeetsEast','SouthMeetsEast')
df_SouvlakiStop=tweets_to_dataframe('SouvlakiStop','SouvlakiStop')
df_SpitfireTruck=tweets_to_dataframe('SpitfireTruck','SpitfireTruck')
df_steakbites=tweets_to_dataframe('steakbites','steakbites')
df_stellaspopkern=tweets_to_dataframe('stellaspopkern','stellaspopkern')
#StreetCream34 seems deactivated
#df_StreetCream34=tweets_to_dataframe('StreetCream34','StreetCream34')
#Sundevich made it to the big time (aka multiple storefronts), no longer a truck
#df_SUNdeVICHtruck=tweets_to_dataframe('SUNdeVICHtruck','SUNdeVICHtruck')
df_surfsidetruckdc=tweets_to_dataframe('surfsidetruckdc','surfsidetruckdc')
df_SUSHIPAO=tweets_to_dataframe('SUSHIPAO','SUSHIPAO')
df_sweetbitestruck=tweets_to_dataframe('sweetbitestruck','sweetbitestruck')
df_swizzlerfoods=tweets_to_dataframe('swizzlerfoods','swizzlerfoods')
df_takorean=tweets_to_dataframe('takorean','takorean')
df_tapastruckdc=tweets_to_dataframe('tapastruckdc','tapastruckdc')
df_tashascookies=tweets_to_dataframe('tashascookies','tashascookies')
df_TasteOfEasternE=tweets_to_dataframe('TasteOfEasternE','TasteOfEasternE')
df_TastyFriedDC=tweets_to_dataframe('TastyFriedDC','TastyFriedDC')
df_tastykabob=tweets_to_dataframe('tastykabob','tastykabob')
df_TastyToranj=tweets_to_dataframe('TastyToranj','TastyToranj')
df_TempoDiPasta=tweets_to_dataframe('TempoDiPasta','TempoDiPasta')
df_thaimachine=tweets_to_dataframe('thaimachine','thaimachine')
df_cheesecaketruc=tweets_to_dataframe('cheesecaketruc','cheesecaketruc')
df_thecornfactory=tweets_to_dataframe('thecornfactory','thecornfactory')
df_tfmcupcakery=tweets_to_dataframe('tfmcupcakery','tfmcupcakery')
df_tiscreamery=tweets_to_dataframe('tiscreamery','tiscreamery')
df_thewagonmeal=tweets_to_dataframe('thewagonmeal','thewagonmeal')
df_TinHeavenDC=tweets_to_dataframe('TinHeavenDC','TinHeavenDC')
df_tokyointhecity=tweets_to_dataframe('tokyointhecity','tokyointhecity')
df_topdogtruck=tweets_to_dataframe('topdogtruck','topdogtruck')
df_topstrucks=tweets_to_dataframe('topstrucks','topstrucks')
df_tortugatruck=tweets_to_dataframe('tortugatruck','tortugatruck')
df_BakedTSR=tweets_to_dataframe('BakedTSR','BakedTSR')
df_TURKISHKABOBDC=tweets_to_dataframe('TURKISHKABOBDC','TURKISHKABOBDC')
df_urbanbumpkinbbq=tweets_to_dataframe('urbanbumpkinbbq','urbanbumpkinbbq')
df_urbanpoutine=tweets_to_dataframe('urbanpoutine','urbanpoutine')
df_VillageCafeINC=tweets_to_dataframe('VillageCafeINC','VillageCafeINC')
df_wassubdc=tweets_to_dataframe('wassubdc','wassubdc')
df_WestraysFinest=tweets_to_dataframe('WestraysFinest','WestraysFinest')
df_whatthephodc=tweets_to_dataframe('whatthephodc','whatthephodc')
df_wijammincaters=tweets_to_dataframe('wijammincaters','wijammincaters')
#rebranded as @NuVeganCafe, as of 2/1/16 the tweeted that they plan to bring back the truck this month
#df_WoodlandsVB=tweets_to_dataframe('WoodlandsVB','WoodlandsVB')
df_YellaFoodTruck=tweets_to_dataframe('YellaFoodTruck','YellaFoodTruck')
df_yellowvendor=tweets_to_dataframe('yellowvendor','yellowvendor')
df_YummyYum_Food=tweets_to_dataframe('YummyYum_Food','YummyYum_Food')
df_yumplingdc=tweets_to_dataframe('yumplingdc','yumplingdc')
#ZBurgerMobile seems to be deactivated
#df_ZBurgerMobile=tweets_to_dataframe('ZBurgerMobile','ZBurgerMobile')
df_ZestyKabob=tweets_to_dataframe('ZestyKabob','ZestyKabob')

#Combine all food trucks into one dataset
combined_truck_df=df_abunaifood
combined_truck_df=combined_truck_df.append(df_AmoriniPanini)
combined_truck_df=combined_truck_df.append(df_AngryBurgerNOW)
combined_truck_df=combined_truck_df.append(df_arepacrew)
combined_truck_df=combined_truck_df.append(df_ArepaZone)
combined_truck_df=combined_truck_df.append(df_AstroDoughnuts)
combined_truck_df=combined_truck_df.append(df_Partytrucks)
combined_truck_df=combined_truck_df.append(df_AZNeats)
combined_truck_df=combined_truck_df.append(df_alocubanotruck)
combined_truck_df=combined_truck_df.append(df_BabasBigBite)
combined_truck_df=combined_truck_df.append(df_badabingdc)
combined_truck_df=combined_truck_df.append(df_balkaniktaste)
combined_truck_df=combined_truck_df.append(df_theballtruck)
combined_truck_df=combined_truck_df.append(df_BanhMiAnnie)
combined_truck_df=combined_truck_df.append(df_BasilThymeDC)
combined_truck_df=combined_truck_df.append(df_bbqbusdc)
combined_truck_df=combined_truck_df.append(df_gotbeachfries)
combined_truck_df=combined_truck_df.append(df_BeirutDelights)
combined_truck_df=combined_truck_df.append(df_bellavitawheels)
combined_truck_df=combined_truck_df.append(df_bestburritos1)
combined_truck_df=combined_truck_df.append(df_okbibija)
combined_truck_df=combined_truck_df.append(df_bigcheesetruck)
combined_truck_df=combined_truck_df.append(df_BITE2GO)
combined_truck_df=combined_truck_df.append(df_eatBONMi)
combined_truck_df=combined_truck_df.append(df_Borinquenlunchb)
combined_truck_df=combined_truck_df.append(df_BLTfoodtruck)
combined_truck_df=combined_truck_df.append(df_bratwurstking)
combined_truck_df=combined_truck_df.append(df_bklynsandwichco)
combined_truck_df=combined_truck_df.append(df_eatbrownbag)
combined_truck_df=combined_truck_df.append(df_bubbleteaparty)
combined_truck_df=combined_truck_df.append(df_burgorilla)
combined_truck_df=combined_truck_df.append(df_CAslidercompany)
combined_truck_df=combined_truck_df.append(df_cajunators)
combined_truck_df=combined_truck_df.append(df_CapitalCW)
combined_truck_df=combined_truck_df.append(df_capmacdc)
combined_truck_df=combined_truck_df.append(df_CaptainCookieDC)
combined_truck_df=combined_truck_df.append(df_Caribbean2Go)
combined_truck_df=combined_truck_df.append(df_CarmensCarts)
combined_truck_df=combined_truck_df.append(df_carnbbq)
combined_truck_df=combined_truck_df.append(df_EatCarolinaQ)
combined_truck_df=combined_truck_df.append(df_1styellowvendor)
combined_truck_df=combined_truck_df.append(df_ChatpatTruck)
combined_truck_df=combined_truck_df.append(df_cheesequakedc)
combined_truck_df=combined_truck_df.append(df_chefalex2013)
combined_truck_df=combined_truck_df.append(df_ChefonWheels11)
combined_truck_df=combined_truck_df.append(df_ChezAdilmos)
combined_truck_df=combined_truck_df.append(df_chickfilamobile)
combined_truck_df=combined_truck_df.append(df_ChittiGrill)
combined_truck_df=combined_truck_df.append(df_ChixNStixDC)
combined_truck_df=combined_truck_df.append(df_coles_palette)
combined_truck_df=combined_truck_df.append(df_cornedbeefking)
combined_truck_df=combined_truck_df.append(df_CrabCab)
combined_truck_df=combined_truck_df.append(df_CRAVEIT2)
combined_truck_df=combined_truck_df.append(df_cremedelacakedc)
combined_truck_df=combined_truck_df.append(df_crepelovetruck)
combined_truck_df=combined_truck_df.append(df_CrepesParfait)
combined_truck_df=combined_truck_df.append(df_JoyCupcakes)
combined_truck_df=combined_truck_df.append(df_CurbSideCrab)
combined_truck_df=combined_truck_df.append(df_curbsidecupcake)
combined_truck_df=combined_truck_df.append(df_CurleysQ)
combined_truck_df=combined_truck_df.append(df_ThePieTruckDC)
combined_truck_df=combined_truck_df.append(df_DcBallers)
combined_truck_df=combined_truck_df.append(df_dc_doner)
combined_truck_df=combined_truck_df.append(df_DCEmpanadas)
combined_truck_df=combined_truck_df.append(df_dc_greekfood)
combined_truck_df=combined_truck_df.append(df_dcpollos)
combined_truck_df=combined_truck_df.append(df_DCQuesadilla)
combined_truck_df=combined_truck_df.append(df_dcslices)
combined_truck_df=combined_truck_df.append(df_DCSLIDERSTRUCK)
combined_truck_df=combined_truck_df.append(df_DCTacoTruck)
combined_truck_df=combined_truck_df.append(df_dirtysouthdeli)
combined_truck_df=combined_truck_df.append(df_DolciGelatiTruk)
combined_truck_df=combined_truck_df.append(df_donburidc)
combined_truck_df=combined_truck_df.append(df_DorothyMoon1)
combined_truck_df=combined_truck_df.append(df_dougthefooddude)
combined_truck_df=combined_truck_df.append(df_DuckysGrub)
combined_truck_df=combined_truck_df.append(df_elFuegoDc)
combined_truck_df=combined_truck_df.append(df_EndlessPLLC)
combined_truck_df=combined_truck_df.append(df_FarEastTG)
combined_truck_df=combined_truck_df.append(df_Fasikacuisin)
combined_truck_df=combined_truck_df.append(df_FavaPot)
combined_truck_df=combined_truck_df.append(df_FedCityBros)
combined_truck_df=combined_truck_df.append(df_feelincrabby)
combined_truck_df=combined_truck_df.append(df_eatFireNRice)
combined_truck_df=combined_truck_df.append(df_firemanscafe)
combined_truck_df=combined_truck_df.append(df_FoodLady2011)
combined_truck_df=combined_truck_df.append(df_foodforceone1)
combined_truck_df=combined_truck_df.append(df_freshgreenfood)
combined_truck_df=combined_truck_df.append(df_FroZenYoToGo)
combined_truck_df=combined_truck_df.append(df_FCFoodTruck)
combined_truck_df=combined_truck_df.append(df_GeorgesWingTruk)
combined_truck_df=combined_truck_df.append(df_gofishtruckdc)
combined_truck_df=combined_truck_df.append(df_mobilekitchen)
combined_truck_df=combined_truck_df.append(df_GAHDTruck)
combined_truck_df=combined_truck_df.append(df_GREENEGGBURGERS)
combined_truck_df=combined_truck_df.append(df_GridsWaffles)
combined_truck_df=combined_truck_df.append(df_GuaposFoodTruck)
combined_truck_df=combined_truck_df.append(df_habebe19)
combined_truck_df=combined_truck_df.append(df_wherehalal)
combined_truck_df=combined_truck_df.append(df_hardysbbqdivine)
combined_truck_df=combined_truck_df.append(df_healthyfool)
combined_truck_df=combined_truck_df.append(df_henhousedc)
combined_truck_df=combined_truck_df.append(df_HolyCrepesTruck)
combined_truck_df=combined_truck_df.append(df_HotPeopleFood)
combined_truck_df=combined_truck_df.append(df_DCHotWheels)
combined_truck_df=combined_truck_df.append(df_HouseofFalafel)
combined_truck_df=combined_truck_df.append(df_hulagirltruck)
combined_truck_df=combined_truck_df.append(df_hungryheartllc)
combined_truck_df=combined_truck_df.append(df_italiansubs1)
combined_truck_df=combined_truck_df.append(df_JMCCurbside)
combined_truck_df=combined_truck_df.append(df_jerkchickenfest)
combined_truck_df=combined_truck_df.append(df_KababjiTruck)
combined_truck_df=combined_truck_df.append(df_KabobBites)
combined_truck_df=combined_truck_df.append(df_kabob_king)
combined_truck_df=combined_truck_df.append(df_kabobpalace1)
combined_truck_df=combined_truck_df.append(df_KaftaMania)
combined_truck_df=combined_truck_df.append(df_kalaverasdc)
combined_truck_df=combined_truck_df.append(df_KimchiBBQ)
combined_truck_df=combined_truck_df.append(df_dckbbqbox)
combined_truck_df=combined_truck_df.append(df_korengy)
combined_truck_df=combined_truck_df.append(df_kravingkabob)
combined_truck_df=combined_truck_df.append(df_kushimototruck)
combined_truck_df=combined_truck_df.append(df_LATacoTruck)
combined_truck_df=combined_truck_df.append(df_LaTingeriaTruck)
combined_truck_df=combined_truck_df.append(df_latinamericanf1)
combined_truck_df=combined_truck_df.append(df_lemongrasstruck)
combined_truck_df=combined_truck_df.append(df_LilypadontheRun)
combined_truck_df=combined_truck_df.append(df_Limetreetruck)
combined_truck_df=combined_truck_df.append(df_LLuncheonette)
combined_truck_df=combined_truck_df.append(df_LittleItalyDC)
combined_truck_df=combined_truck_df.append(df_chefty99)
combined_truck_df=combined_truck_df.append(df_loslobosburrito)
combined_truck_df=combined_truck_df.append(df_macattackdc)
combined_truck_df=combined_truck_df.append(df_macsdonuts)
combined_truck_df=combined_truck_df.append(df_MakiShopTruck)
combined_truck_df=combined_truck_df.append(df_MamasDonutBites)
combined_truck_df=combined_truck_df.append(df_MayurKababHouse)
combined_truck_df=combined_truck_df.append(df_Med_Delight)
combined_truck_df=combined_truck_df.append(df_Meggrollmania)
combined_truck_df=combined_truck_df.append(df_meskihealthy2go)
combined_truck_df=combined_truck_df.append(df_mesobonwheels)
combined_truck_df=combined_truck_df.append(df_Miamiviceburger)
combined_truck_df=combined_truck_df.append(df_MidniteCC)
combined_truck_df=combined_truck_df.append(df_MightyDogAcai)
combined_truck_df=combined_truck_df.append(df_MisoHoneyTruck)
combined_truck_df=combined_truck_df.append(df_mohmohdumpling)
combined_truck_df=combined_truck_df.append(df_mojaitalatinfla)
combined_truck_df=combined_truck_df.append(df_Mojotruck)
combined_truck_df=combined_truck_df.append(df_Miyagifoodtruck)
combined_truck_df=combined_truck_df.append(df_MuncheezDC)
combined_truck_df=combined_truck_df.append(df_NeatMeatDC)
combined_truck_df=combined_truck_df.append(df_NYDeliTruck)
combined_truck_df=combined_truck_df.append(df_OliviasCupcakes)
combined_truck_df=combined_truck_df.append(df_OohDaTChickeN)
combined_truck_df=combined_truck_df.append(df_orangecowdc)
combined_truck_df=combined_truck_df.append(df_overtherice)
combined_truck_df=combined_truck_df.append(df_parskabob)
combined_truck_df=combined_truck_df.append(df_passl0nfrult)
combined_truck_df=combined_truck_df.append(df_pepefoodtruck)
combined_truck_df=combined_truck_df.append(df_perubrothers)
combined_truck_df=combined_truck_df.append(df_buritosontherun)
combined_truck_df=combined_truck_df.append(df_philliesphamous)
combined_truck_df=combined_truck_df.append(df_phojunkies)
combined_truck_df=combined_truck_df.append(df_PhoBachi)
combined_truck_df=combined_truck_df.append(df_dcphonation)
combined_truck_df=combined_truck_df.append(df_PhoWheels)
combined_truck_df=combined_truck_df.append(df_pleasantpops)
combined_truck_df=combined_truck_df.append(df_PoppedRepublic)
combined_truck_df=combined_truck_df.append(df_dcpuddin)
combined_truck_df=combined_truck_df.append(df_quickwraps)
combined_truck_df=combined_truck_df.append(df_therandyradish)
combined_truck_df=combined_truck_df.append(df_RebasFunnelCake)
combined_truck_df=combined_truck_df.append(df_LobstertruckDC)
combined_truck_df=combined_truck_df.append(df_redbonefc)
combined_truck_df=combined_truck_df.append(df_ReggaeVibesTruk)
combined_truck_df=combined_truck_df.append(df_riochurrascoDC)
combined_truck_df=combined_truck_df.append(df_RitoLoco)
combined_truck_df=combined_truck_df.append(df_RoamingRoti)
combined_truck_df=combined_truck_df.append(df_RocklandsTruck)
combined_truck_df=combined_truck_df.append(df_RockSalt_)
combined_truck_df=combined_truck_df.append(df_Rollinpizzadc)
combined_truck_df=combined_truck_df.append(df_rollinkabob)
combined_truck_df=combined_truck_df.append(df_RollsOnRolls)
combined_truck_df=combined_truck_df.append(df_RovingItalian)
combined_truck_df=combined_truck_df.append(df_asgharboa)
combined_truck_df=combined_truck_df.append(df_saffrontruckdc)
combined_truck_df=combined_truck_df.append(df_SangOnWheels)
combined_truck_df=combined_truck_df.append(df_SaransVegiTruck)
combined_truck_df=combined_truck_df.append(df_SateTruck)
combined_truck_df=combined_truck_df.append(df_Scoops2u)
combined_truck_df=combined_truck_df.append(df_SeoulFoodDC)
combined_truck_df=combined_truck_df.append(df_simple_wheels)
combined_truck_df=combined_truck_df.append(df_simplysoulfood)
combined_truck_df=combined_truck_df.append(df_Sinplicity1)
combined_truck_df=combined_truck_df.append(df_SloppyMamas)
combined_truck_df=combined_truck_df.append(df_BayouGators)
combined_truck_df=combined_truck_df.append(df_smokingkowbbq)
combined_truck_df=combined_truck_df.append(df_solmexicangrill)
combined_truck_df=combined_truck_df.append(df_SouthMeetsEast)
combined_truck_df=combined_truck_df.append(df_SouvlakiStop)
combined_truck_df=combined_truck_df.append(df_SpitfireTruck)
combined_truck_df=combined_truck_df.append(df_steakbites)
combined_truck_df=combined_truck_df.append(df_stellaspopkern)
combined_truck_df=combined_truck_df.append(df_surfsidetruckdc)
combined_truck_df=combined_truck_df.append(df_SUSHIPAO)
combined_truck_df=combined_truck_df.append(df_sweetbitestruck)
combined_truck_df=combined_truck_df.append(df_swizzlerfoods)
combined_truck_df=combined_truck_df.append(df_takorean)
combined_truck_df=combined_truck_df.append(df_tapastruckdc)
combined_truck_df=combined_truck_df.append(df_tashascookies)
combined_truck_df=combined_truck_df.append(df_TasteOfEasternE)
combined_truck_df=combined_truck_df.append(df_TastyFriedDC)
combined_truck_df=combined_truck_df.append(df_tastykabob)
combined_truck_df=combined_truck_df.append(df_TastyToranj)
combined_truck_df=combined_truck_df.append(df_TempoDiPasta)
combined_truck_df=combined_truck_df.append(df_thaimachine)
combined_truck_df=combined_truck_df.append(df_cheesecaketruc)
combined_truck_df=combined_truck_df.append(df_thecornfactory)
combined_truck_df=combined_truck_df.append(df_tfmcupcakery)
combined_truck_df=combined_truck_df.append(df_tiscreamery)
combined_truck_df=combined_truck_df.append(df_thewagonmeal)
combined_truck_df=combined_truck_df.append(df_TinHeavenDC)
combined_truck_df=combined_truck_df.append(df_tokyointhecity)
combined_truck_df=combined_truck_df.append(df_topdogtruck)
combined_truck_df=combined_truck_df.append(df_topstrucks)
combined_truck_df=combined_truck_df.append(df_tortugatruck)
combined_truck_df=combined_truck_df.append(df_BakedTSR)
combined_truck_df=combined_truck_df.append(df_TURKISHKABOBDC)
combined_truck_df=combined_truck_df.append(df_urbanbumpkinbbq)
combined_truck_df=combined_truck_df.append(df_urbanpoutine)
combined_truck_df=combined_truck_df.append(df_VillageCafeINC)
combined_truck_df=combined_truck_df.append(df_wassubdc)
combined_truck_df=combined_truck_df.append(df_WestraysFinest)
combined_truck_df=combined_truck_df.append(df_whatthephodc)
combined_truck_df=combined_truck_df.append(df_wijammincaters)
combined_truck_df=combined_truck_df.append(df_YellaFoodTruck)
combined_truck_df=combined_truck_df.append(df_yellowvendor)
combined_truck_df=combined_truck_df.append(df_YummyYum_Food)
combined_truck_df=combined_truck_df.append(df_yumplingdc)
combined_truck_df=combined_truck_df.append(df_ZestyKabob)
combined_truck_df

#Write the combined df to csv for further analysis
combined_truck_df_csv_path = "/Users/nicolekelly/Documents/ft_aggregate/" + str(time.time()) + '_' + 'combined_truck_df' +'.csv'
combined_truck_df.to_csv(path_or_buf=combined_truck_df_csv_path, header=['contributors', 'coordinates', 'created_at', 'favorite_count', 'favorited', 'geo', 'id', 'in_reply_to_status_id', 'in_reply_to_user_id', 'is_quote_status', 'lang', 'place', 'retweet_count', 'retweeted', 'source', 'text', 'truncated', 'username'], index=True, sep=',')

#Next steps:
    #1)Use pandas to find food trucks where the most recent tweet occurred before 2016 (as a starting point)
    # to remove from analysis
    #2)Reorder columns in df for more logical order
    #3)Use regex to extract additional info (like RT=retweet, hashtags, etc)
    #4)Figure out how to get information from nested dictionaries, like retweets
    #5)Get more complete dataset for most prolific tweeters (using max and since ids in API call)
    #6)Start storing dataset in SQL/Postgres to add new info to old more easily
    #7)Analyze!

#Use pandas to filter to only food trucks where their oldest of the most recent 20 tweets occurred in 2016
combined_truck_df['year']=combined_truck_df['created_at'].dt.year
combined_truck_df_filter=combined_truck_df.groupby('username').filter(lambda x: min(x['year']) >= 2016)
combined_truck_df_filter_csv_path = "/Users/nicolekelly/Documents/ft_aggregate/" + str(time.time()) + '_' + 'combined_truck_df_filter' +'.csv'
combined_truck_df_filter.to_csv(path_or_buf=combined_truck_df_filter_csv_path, header=['contributors', 'coordinates', 'created_at', 'favorite_count', 'favorited', 'geo', 'id', 'in_reply_to_status_id', 'in_reply_to_user_id', 'is_quote_status', 'lang', 'place', 'retweet_count', 'retweeted', 'source', 'text', 'truncated', 'username', 'year'], index=True, sep=',')

