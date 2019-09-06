# app.py
import flask, random, os, requests, json, random, requests_oauthlib  

app = flask.Flask(__name__)



@app.route('/')  
def index(): 
    #Genius API search
    url = "https://api.genius.com/search?q=Kehlani"
    
    #Genius API Authorization 
    my_headers = {
    "Authorization": "Bearer gMMP35gIwZgzN7zTtmwcgpE24HRHIMvzNOj7hhqIjxbYFbq89genbmdvo-4DZc5d"
    }
    
    #Chooses a random song
    random_song = random.randint(0,8)
    response = requests.get(url, headers=my_headers)
    json_body = response.json()
    
    pic = json_body["response"]["hits"][random_song]["result"]['header_image_url']
    song = json_body["response"]["hits"][random_song]["result"]["full_title"]
    artist = json_body["response"]["hits"][random_song]["result"]['primary_artist']['name']
    
    
    #Twitter API to search for tweets
    twitt_url = "https://api.twitter.com/1.1/search/tweets.json?q=kehlani"
    
    #Retrieves a random tweet
    twitter_tweet = random.randint(0,14)
    
    #Authorization for the Twitter API
    oauth = requests_oauthlib.OAuth1(
    "qBkUI9Od70x3S08iyliKXt2o0", 
    "kjPdoRemvjUFwM5GmnRvpqgZSrmsRl0NnkRJGE7OGotzUhWj9d ",
    "1167117656073412608-vFF34UgaXtFhNDxuXhMceeTadWEL6H",
    "Qw61OwavaJ3UTSeE20xqhkZ0qqP4r1CsGVoXFa0idtBfV"
    )

    response = requests.get(twitt_url, auth=oauth)
    json_body = response.json()
    

    kehlani_tweets = json_body['statuses'][twitter_tweet]['text']
  
    

    return flask.render_template("index.html", 
                                pic = pic, 
                                song = song, 
                                artist = artist, 
                                kehlani_tweets = kehlani_tweets)


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True
)