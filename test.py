
import requests
import json
import creds

# general config
BASE_URL: str = "https://graph.instagram.com"
VERSION: str = "v22.0"


# /me
# query instagram api for "me"-node. can represent various things, here it represents "IG User"
# all fields for the "IG USER" node (for some reason I cant query some of them): biography,followers_count,follows_count,has_profile_pic,id,is_published,legacy_instagram_user_id,media_count,name,profile_picture_url,shopping_product_tag_eligibility,username,website
# also works with edges like media
FIELDS = "biography,followers_count,follows_count,id,media_count,name,profile_picture_url,username"
MEDIA = "media{caption,comments_count,id,like_count,media_url,permalink,children}"  # technically "children" is an edge of an edge
url = f"{BASE_URL}/{VERSION}/me?fields={FIELDS},{MEDIA}&access_token={creds.LONG_LIVED_TOKEN}"
print(url)



