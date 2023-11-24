from pymongo.collation import Collation

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
    pass

def compose_tweet(tweetscollection):
    pass


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
    
    

