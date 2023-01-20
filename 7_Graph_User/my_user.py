import msal
import os
import base64
import requests
import json

def token_creation():
    

    # Enter the details of your AAD app registration
    client_id = "9eea4655-3e62-4c77-800c-abdcb5c488d8"
    client_secret = ""
    authority = 'https://login.microsoftonline.com/ba906cf0-0514-4c13-ba89-21d3f49dd2c7'
    scope = ['https://graph.microsoft.com/.default']


    # Create an MSAL instance providing the client_id, authority and client_credential parameters
    client = msal.ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)

    # First, try to lookup an access token in cache
    token_result = client.acquire_token_silent(scope, account=None)

    # If the token is available in cache, save it to a variable
    # if token_result:
    #   access_token = 'Bearer ' + token_result['access_token']
    #   print('Access token was loaded from cache')

    # If the token is not available in cache, acquire a new one from Azure AD and save it to a variable

    token_result = client.acquire_token_for_client(scopes=scope)
    access_token = 'Bearer ' + token_result['access_token']
    print('New access token was acquired from Azure AD')
    return access_token


def create_user_in_office(user_dispayName,user_domain,access_token):
    display_name = user_dispayName
    mail_nickname = user_dispayName
    account_enabled = True
    upn = user_dispayName + "@" + user_domain
    password = "O365user!"
    location = "BG"
    
    url = 'https://graph.microsoft.com/beta/users'
    headers = {
    'Authorization': access_token,
    'Content-Type': 'application/json'
    }

    req_body = json.dumps(
        {
        "accountEnabled": account_enabled,
        "displayName": display_name,
        "mailNickname": mail_nickname,
        "userPrincipalName": upn,
        "usageLocation": location,
        "passwordProfile" : {
            "forceChangePasswordNextSignIn": False,
            "password": password
        }
        }
        )        
    
    requests.post(url=url, headers=headers, data=req_body)



def delete_user_graph(upn,access_token):

    
    endpoint = "https://graph.microsoft.com/v1.0/users/{}".format(upn)

    headers = {
        'Authorization': access_token
    }

    graph_result = requests.delete(url=endpoint, headers=headers)
