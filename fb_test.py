import os
import facebook
import json
import requests
import codecs

if __name__ == '__main__':
    #token = os.environ.get('FACEBOOK_TEMP_TOKEN')

    token = "Should be your token"

    graph = facebook.GraphAPI(token)
    posts = graph.get_connections('me', 'posts')
    #user = graph.get_object('me')
    #friends = graph.get_connections(user['id'], "friends")
    #profile = graph.get_object('me', fields='name,location{location}')

    while True :
        try:
            with open('my_posts.txt', 'a') as f:
                for post in posts['data']:
                    f.write(json.dumps(post)+"\n")
                posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            break

    #print(json.dumps(friends, indent=4))