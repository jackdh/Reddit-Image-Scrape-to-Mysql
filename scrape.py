import requests
import mysql.connector
import time
import re
from pprint import  pprint

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'port': '8889',
    'database': 'sytykr',
}




list_of_subreddits_swf = ["AdviceAnimals", "aww", "woahdude", "foodporn",
                          "EarthPorn", "AbandonedPorn", "soccer", "Minecraft", "GlobalOffensive", "hearthstone", "MURICA",
                          "tf2", "cringe", "thatHappened", "spaceporn"
]




def tableCreate():
    cnx = mysql.connector.connect(**config)
    c = cnx.cursor()
    c.execute("CREATE TABLE gameitem( ID INTEGER PRIMARY KEY AUTO_INCREMENT, subreddit TEXT, title TEXT, image_url TEXT, post_url TEXT)")


    #done


def dataEntry(_subreddit, _title, _imageURL, _post_url):
    cnx = mysql.connector.connect(**config)

    c = cnx.cursor()
    insert = ("""INSERT INTO gameitem
                    (subreddit, title, image_url, post_url )
                    VALUES (%s, %s, %s, %s)""")

    data_value = (_subreddit, _title, _imageURL, _post_url)

    c.execute(insert, data_value)
    cnx.commit()
    c.close()
    cnx.close()

def dataScrape(itemAmount, subreddit_json, sr):
    count = 0
    items = 0
    itemAmount_var = itemAmount
    subreddit_json_var = subreddit_json
    try:
        for i in subreddit_json_var['data']['children']:
            base_url = subreddit_json_var['data']['children'][count]['data']

            image_link = base_url['is_self']
            domain_check = base_url['domain']

            if image_link == False and  domain_check == "i.imgur.com":
                items += 1
                subreddit = base_url['subreddit']
                title = base_url['title']
                image_url = base_url['url']
                post_url = base_url['permalink']

                #image check
                image_url = makeFriendlyUrls(image_url)

                print ( "subreddit : " + subreddit )
                print ( "title : " + title )
                print ( "url : " + image_url)
                print ( str(items) + "\n")
                dataEntry(subreddit, title, image_url, post_url)

            count += 1
            if items >= itemAmount_var:
                break
    except KeyError as e:
        # Ugly as hell but should there be a error when getting the JSON this will call remake which will then
        # attempt to recreate the JSON and try again!
        print("Key error now waiting 5 seconds.")
        time.sleep(5)
        print("Running now")
        time.sleep(1)
        dataScrape(itemAmount_var, makeSubredditJson(sr), sr)

def makeFriendlyUrls(image_url):
    try:
        x = image_url[:-len(str(re.match('.*?([0-9]+)$', image_url).group(1)))]
        if x[-4:] == "gifv":
            x = x[:-1]
        elif x[-1:] == "?":
            x = x[:-1]
        #This is new here may break it ^
        return x
    except AttributeError:
        return image_url


def makeSubredditJson(i):
    makeURL = "http://www.reddit.com/r/"+i+".json"+"?limit=30"
    print("Waiting to make request")
    time.sleep(2.5)
    r = requests.get(makeURL)
    return r.json()

def main(subreddit_list):
    for subreddit in subreddit_list:
        subreddit_json = makeSubredditJson(subreddit)
        dataScrape(4, subreddit_json, subreddit)


choice = input("Would you like to (S)crape images or make a (T)able?")

if choice == "s":
    main(list_of_subreddits_swf)
elif choice == "t":
    tableCreate()
else:
    exit()

