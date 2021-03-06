

# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials, cache_discovery=False)

    request = youtube.videos().list(
        part="id",
        id="EJX18Ft3-lw"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()


# reponse
"""
{
 "kind": "youtube#videoListResponse",
 "etag": "\"p4VTdlkQv3HQeTEaXgvLePAydmU/BEPTEAogWiiLXL576wca1nFY5UE\"",
 "pageInfo": {
  "totalResults": 1,
  "resultsPerPage": 1
 },
 "items": [
  {
   "kind": "youtube#video",
   "etag": "\"p4VTdlkQv3HQeTEaXgvLePAydmU/-tNbt5quSqln65UaPF0nAuWJHWI\"",
   "id": "EJX18Ft3-lw"
  }
 ]
}
"""