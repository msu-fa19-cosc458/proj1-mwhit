# app.py
import flask, random, os, requests, json, random, requests_oauthlib  

app = flask.Flask(__name__)



@app.route('/')  
def index(): 
    #Genius API search
    url = "https://api.genius.com/search?q=Kehlani"
    
    #Genius API Authorization 
    my_headers = {
    "Authorization": "Bearer IQdtZyfMUnXQ53F8b9e3y-jWqaNNNRXoVK-aUdbF1crCTkG7S_VCvMrMOD_Nm2FR"
    }
    
    #Chooses a random song
    random_song = random.randint(0,8)
    response = requests.get(url, headers=my_headers)
    json_body = response.json()
    
    coverart = json_body["response"]["hits"][random_song]["result"]['header_image_url']
    song = json_body["response"]["hits"][random_song]["result"]["full_title"]
    artist = json_body["response"]["hits"][random_song]["result"]['primary_artist']['name']
    
    
    #Twitter API to search for tweets
    twitter_url = "https://api.twitter.com/1.1/search/tweets.json?q=kehlani"
    
    #Retrieves a random tweet
    twitter_tweet = random.randint(0,10)
    
    #Authorization for the Twitter API
    oauth = requests_oauthlib.OAuth1(
    "P9G9BJPDMdNWmitx3sn68UXm3", 
    "EVTYPFAOVa4jgk9fkYMgTP6dpqwPhniUlht7dLtbORM7Yq9LPr",
    "1167117656073412608-vFF34UgaXtFhNDxuXhMceeTadWEL6H",
    "90rgA5HLFb4SvWSHEr3q3oRKOnWzPpg4NfSVleWzctQcV"
    )

    response = requests.get(twitter_url, auth=oauth)
    json_body = response.json()
    

    tweets = json_body['statuses'][twitter_tweet]['text']
  
    

    return flask.render_template("index.html", 
                                coverart = coverart, 
                                song = song, 
                                artist = artist, 
                                tweets = tweets)


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True
)