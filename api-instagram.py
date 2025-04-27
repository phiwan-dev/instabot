
import requests
import json
import creds

# general config
BASE_URL: str = "https://graph.instagram.com"
VERSION: str = "v22.0"


def hit_endpoint(method: str, endpoint: str, params: dict[str, str], debug: bool = False):
    if debug:
        print(f"=====[Hitting Endpoint {endpoint}]=====")
        print(f"[Debug]: {method} {BASE_URL}/{VERSION}{endpoint}")
        print(f"[Debug]: {json.dumps(params, indent=4)}")
    if method == "GET":
        response_raw = requests.get(f"{BASE_URL}/{VERSION}{endpoint}", params=params)
    elif method == "POST":
        response_raw = requests.post(endpoint, params=params)
    else:
        raise ValueError("[Error]: Unsupported! Only GET and POST are supported")
    response_obj = json.loads(response_raw.content)
    if debug:
        print("=====[Response]=====")
        response_pretty = json.dumps(response_obj, indent=4)
        print(f"[Debug]: {response_pretty}")
        print("=====[End Response]=====\n")
    return response_obj


def log_stats(username: str="roomrefinery.design") -> None:
    FIELDS = "followers_count,follows_count,media_count"
    params = {
        "fields": f"{FIELDS}",
        "access_token": creds.LONG_LIVED_TOKEN
    }
    hit_endpoint("GET", "/me", params, True)
log_stats()


# /access_token
# get long lived access token
params = {
    "grant_type": "ig_exchange_token",
    "client_secret": creds.APP_SECRET,
    "access_token": creds.SHORT_LIVED_TOKEN
}
#hit_endpoint("GET", "/access_token", params, True)


# /refresh_access_token
# returns a json object which inclueds a new refreshed token which is valid for 60 days = 5184000 seconds
params = {
    "grant_type": "ig_refresh_token",
    "access_token": creds.LONG_LIVED_TOKEN,
}
#hit_endpoint("GET", "/refresh_access_token", params, True)


# /me
# query instagram api for "me"-node. can represent various things, here it represents "IG User"
# all fields for the "IG USER" node (for some reason I cant query some of them): biography,followers_count,follows_count,has_profile_pic,id,is_published,legacy_instagram_user_id,media_count,name,profile_picture_url,shopping_product_tag_eligibility,username,website
# also works with edges like media
FIELDS = "biography,followers_count,follows_count,id,media_count,name,profile_picture_url,username"
MEDIA = "media{caption,comments_count,id,like_count,media_url,permalink,children}"  # technically "children" is an edge of an edge
params = {
    "fields": f"{FIELDS}",
    #"fields": f"{FIELDS},{MEDIA}",
    "access_token": creds.LONG_LIVED_TOKEN
}
#hit_endpoint("GET", "/me", params, True)


# /debug_token
# Doesn't work, gives me a permission error. I can't find it in the docs either.
# Use the online web-tool instead: https://developers.facebook.com/tools/debug/accesstoken/
# Used to query information about the input token. 
# Could be used to e.g. see for how long the token is still valid.
params = {
    "input_token": creds.LONG_LIVED_TOKEN,
    "access_token": creds.LONG_LIVED_TOKEN,
}
#hit_endpoint("GET", "/debug_token", params, True)


# /media
# This can be used to query your own posts/uploaded media.
url = f"{BASE_URL}/{VERSION}/{creds.USER_ID}/media?access_token={creds.LONG_LIVED_TOKEN}"
# story post
# 1 host image publicly
if False:
    from publisher import Publisher
    publisher = Publisher()
    url: str = publisher.publish()
    url = f"{url}/images/0.jpg"
    print(f"Published to {url}")
    input("press enter...")
# 2 create container
    params = {
        "access_token": creds.LONG_LIVED_TOKEN,
        "image_url": url,
        "media_type": "STORIES",
    }
    response_raw = requests.post(f"{BASE_URL}/{VERSION}/{creds.USER_ID}/media", params=params)
    response_json = json.loads(response_raw.content)
    print(json.dumps(response_json, indent = 4))

    publisher.stop()
# 3 publish container
if False:
    params = {
        "access_token": creds.LONG_LIVED_TOKEN,
        "creation_id": "18061878676876286",
    }
    response_raw = requests.post(f"{BASE_URL}/{VERSION}/{creds.USER_ID}/media_publish", params=params)
    response_json = json.loads(response_raw.content)
    print(json.dumps(response_json, indent = 4))






