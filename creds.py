# File for storing the credentials for later use
# so it doesn't need to be hard coded in other code.


APP_SECRET: str = ""
# https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/get-started
# 1. In your app dashboard, click Instagram > API setup with Instagram business login in the left side menu.
# 2. Click Generate token next to the Instagram account you want to access.
# 3. Log into Instagram.
# 4. Copy the access token.
SHORT_LIVED_TOKEN: str = ""
LONG_LIVED_TOKEN: str = ""
# also long lived token?
# LONG_LIVED_TOKEN = "EAAJaMvKqlVoBO4AGm351wYrKjt0OTGrh8qPYSOw8aYczOzavoRLHsJ7kyKfYgUFlZAr6BvJZBq85Q8E7u66DuGx0u0G7BiTxkPTIfGxjIiZCqV4GZCipSrxRz1WDtkF6qVP9f31bYezGEjP0woZBXA2Pqk50uaZAuw0ftEWJXvCt0JIpYrkZBDZCEQBOeMXEbGLC"
REFRESHED_LONG_TOKEN: str = ""


USERNAME: str = ""
# query for instagram page, no access token required.
# fbid_v2 is the instagram account userid
# url = f"https://www.instagram.com/web/search/topsearch/?query={USERNAME}"
USER_ID: str = ""
ID: str = ""



