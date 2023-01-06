def create_multiple_users_args(*args):
    for arg in args:
        display_name = arg
        mail_nickname = arg
        account_enabled = True
        upn = "{}@b.dns-cloud.net".format(arg)
        password = "O365user!"
        usage_location = "BG"

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
            "usageLocation": usage_location,
            "passwordProfile" : {
                "forceChangePasswordNextSignIn": False,
                "password": password
            }
            }
            )
        
        requests.post(url=url, headers=headers, data=req_body)

users_args=[]
my_user_args = "args_user"
for my_var in range(1,11):
    my_user_args = my_user_args + str(my_var)
    users_args.append(my_user_args)
    print(my_user_args)
    my_user_args = "args_user"

my_users= users_args

#unpac a variable
create_multiple_users_args(*my_users)


