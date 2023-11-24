from pymongo.collation import Collation
from datetime import datetime

def search_tweets(tweetscollection):
   
    words = input("Enter keyword(s): ").lower().split()
    query = {'$and': [{'content': {'$regex': word, '$options': 'i'}} for word in words]}
    
    search = tweetscollection.find(query, collation=Collation(locale='en', strength=4))
                    
    for tweet in search:
        print("\n")
        print("tweet_id: ", tweet["id"],"\ndate: ", tweet["date"], "\ncontent: ", tweet["content"], "\nusername: ", tweet["user"]["username"], "\n")
        
    running = True
    while running:
        tweet_selected = int(input("\nEnter tweet_id: "))
        if check_tweet_select(search, tweet_selected):
            tweet_info = tweetscollection.find_one({"id":tweet_selected})
            print("\ntweet_info:" , tweet_info, "\n")
            running = False
        else:
            print("\ntweet id doesn't exist in the current search\n")
        
def search_users(tweetscollection):
    words = input("Enter one keyword: ").lower().split()
    word = words[0]
    
    query = { '$or': [{'user.displayname': {'$regex': word, '$options': 'i'}}, {'user.location': {'$regex': word, '$options': 'i'}}]}
    search = tweetscollection.find(query, collation=Collation(locale='en', strength=4))
    
    seen = []
    for user in search:
        if user["user"]["username"] not in seen:
            seen.append(user["user"]["username"])
            print("\n")
            print("username:  ", user["user"]["username"], "\ndisplayname: ", user["user"]["displayname"], "\nlocation: ", user["user"]["location"], "\n")
            
    running = True
    while running:
        user_input = input("\nEnter username: ")
        if check_user_select(seen,user_input):
            user_info = tweetscollection.find_one({"user.username":user_input},{"user":1})
            print("\nuser_info:" , user_info, "\n")
            running = False
        else:
            print("\nusername doesn't exist in the current search\n")
    
def list_tweets(tweetscollection):
    pass

def list_users(tweetscollection):
    # This function displays the top n users based on followersCount (n is inputted by the user)

    length = tweetscollection.count_documents({"_id": {"$exists":True}})
    # prompt user for number of accounts they would like to see
    n = input("Enter the number of accounts you would like to see: ")
    # check if the input is valid
    while True:
        # check if an integer is inputted
        try:
            n = int(n)
        except Exception:
            print("Invalid input.")
            n = input("Enter the number of accounts you would like to see: ")
            continue
        # check if the integers is within range of 0 to the number of documents
        if n > length or n < 0:
            print("Invalid input.")
            n = input("Enter the number of accounts you would like to see: ")
        else:
            break
    # sort the documents by followersCount
    results = tweetscollection.find().sort("user.followersCount", -1)
    shown = []  # keep track of possible duplicates
    i = 0
    limit = 0
    # display top n accounts
    while limit < n and i < length:
        if results[i]["user"]["username"].lower() not in shown:
            shown.append(results[i]["user"]["username"].lower())
            print("Username: %s" % results[i]["user"]["username"])
            if results[i]["user"]["displayname"]:
                print("Display name: %s" % results[i]["user"]["displayname"])
            print("Followers count: %d" % results[i]["user"]["followersCount"])
            print("")
            limit += 1
        i += 1
    # prompt user for the username of an account they would like to see more information about
    select_user = input("Enter a username to see more information: ").lower()
    validUser = False
    while not validUser:
        for username in shown:
            if select_user == username:
                validUser = True
                break
        if validUser:
            break
        else:
            print("Invalid username.")
            select_user = input("Enter a username to see more information: ").lower()
    # display all user information
    for acc in results:
        if acc["user"]["username"].lower() == select_user:
            print("Username: %s" % acc["user"]["username"])
            if acc["user"]["displayname"]:
                print("Display name: %s" % acc["user"]["displayname"])
            if acc["user"]["id"]:
                print("ID: %d" % acc["user"]["id"])
            if acc["user"]["description"]:
                print("Description: %s" % acc["user"]["description"])
            if acc["user"]["verified"]:
                print("Verified")
            else:
                print("Not verified")
            if acc["user"]["created"]:
                print("Date created: %s" % acc["user"]["created"])
            if acc["user"]["followersCount"]:
                print("Followers count: %d" % acc["user"]["followersCount"])
            if acc["user"]["friendsCount"]:
                print("Friends count: %d" % acc["user"]["friendsCount"])
            if acc["user"]["statusesCount"]:
                print("Statuses count: %d" % acc["user"]["statusesCount"])
            if acc["user"]["favouritesCount"]:
                print("Favourites count: %d" % acc["user"]["favouritesCount"])
            if acc["user"]["listedCount"]:
                print("Listed count: %d" % acc["user"]["listedCount"])
            if acc["user"]["mediaCount"]:
                print("Media count: %d" % acc["user"]["mediaCount"])
            if acc["user"]["location"] != "":
                print("Location: %s" % acc["user"]["location"])
            if acc["user"]["protected"]:
                print("Protected")
            if acc["user"]["linkUrl"]:
                print("Link URL: %s" % acc["user"]["linkUrl"])
            if acc["user"]["linkTcourl"]:
                print("Link t.co URL: %s" % acc["user"]["linkTcourl"])
            if acc["user"]["profileImageUrl"]:
                print("Profile Image URL: %s" % acc["user"]["profileImageUrl"])
            if acc["user"]["profileBannerUrl"]:
                print("Profile Banner URL: %s" % acc["user"]["profileBannerUrl"])
            if acc["user"]["url"]:
                print("URL: %s" % acc["user"]["url"])
    return

def compose_tweet(tweetscollection):
    # This function allows the user to create a tweet and inserts the tweet into the database

    # prompt the user to input content
    content = input("Enter your tweet: ")
    # get system date and time
    date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
    # create the new tweet document
    new_tweet = {
    "url": None,
    "date": date,
    "content": content,
    "renderedContent": content,
    "id": None,
    "user": {
        "username": "291user",
        "displayname": None,
        "id": None,
        "description": None,
        "rawDescription": None,
        "descriptionUrls": [],
        "verified": False,
        "created": None,
        "followersCount": 0,
        "friendsCount": 0,
        "statusesCount": 0,
        "favouritesCount": 0,
        "listedCount": 0,
        "mediaCount": 0,
        "location": "",
        "protected": False,
        "linkUrl": None,
        "linkTcourl": None,
        "profileImageUrl": None,
        "profileBannerUrl": None,
        "url": None
    },
    "outlinks": [],
    "tcooutlinks": [],
    "replyCount": 0,
    "retweetCount": 0,
    "likeCount": 0,
    "quoteCount": 0,
    "conversationId": None,
    "lang": None,
    "source": None,
    "sourceUrl": None,
    "sourceLabel": None,
    "media": [
        {
        "previewUrl": None,
        "fullUrl": None,
        "type": None
        }
    ],
    "retweetedTweet": None,
    "quotedTweet": None,
    "mentionedUsers": None
    }
    # insert into database
    tweetscollection.insert_one(new_tweet)
    return


def check_tweet_select(list_items, user_input):
    exist = False
    
    for i in list_items:
        if i["id"] == int(user_input):
            exist = True
            return exist
    return exist

def check_user_select(list_items, user_input):
    exist = False
    
    for i in list_items:
        if i == user_input:
            exist = True
            return exist
    return exist
    
    

