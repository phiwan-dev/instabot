
import requests
import json
import creds

# general config
BASE_URL: str = "https://graph.instagram.com"
VERSION: str = "v22.0"


# get long lived access token
ACCESS_TOKEN_DIR: str = "/access_token"
GRANT_TYPE: str = "ig_exchange_token"
access_token_url = f"{BASE_URL}/access_token?grant_type=ig_exchange_token&client_secret={creds.APP_SECRET}&access_token={creds.SHORT_LIVED_TOKEN}"
#print(access_token_url)
params = {
    "grant_type": GRANT_TYPE,
    "client_secret": creds.APP_SECRET,
    "access_token": creds.SHORT_LIVED_TOKEN
}
#response = requests.get(f"{BASE_URL}{ACCESS_TOKEN_DIR}", params=params)
#print(response)
#print(response.content)
#print(json.loads(response.content))



# /me
# query instagram api for "me"-node. can represent various things, here it represents "IG User"
# all fields for the "IG USER" node (for some reason I cant query some of them): biography,followers_count,follows_count,has_profile_pic,id,is_published,legacy_instagram_user_id,media_count,name,profile_picture_url,shopping_product_tag_eligibility,username,website
# also works with edges like media
FIELDS = "biography,followers_count,follows_count,id,media_count,name,profile_picture_url,username"
MEDIA = "media{caption,comments_count,id,like_count,media_url,permalink,children}"  # technically "children" is an edge of an edge
params = {
    "fields": f"{FIELDS},{MEDIA}",
    "access_token": creds.LONG_LIVED_TOKEN
}
#response_raw = requests.get(f"{BASE_URL}/{VERSION}/me", params=params)
#response_json = json.loads(response_raw.content)
#print(json.dumps(response_json, indent = 4))



# /debug_token
# Doesn't work, gives me a permission error. I can't find it in the docs either.
# Use the online web-tool instead: https://developers.facebook.com/tools/debug/accesstoken/
# Used to query information about the input token. 
# Could be used to e.g. see for how long the token is still valid.
#params = {
    #"input_token": creds.LONG_LIVED_TOKEN,
    #"access_token": creds.LONG_LIVED_TOKEN,
#}
#response_raw = requests.get(f"{BASE_URL}/{VERSION}/debug_token", params=params)
#response_json = json.loads(response_raw.content)
#print(json.dumps(response_json, indent = 4))







