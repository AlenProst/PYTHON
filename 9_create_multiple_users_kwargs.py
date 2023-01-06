def create_multiple_users_kwargs(**kwargs):
    for key,value in kwargs.items():
        display_name = value
        mail_nickname = value
        account_enabled = True
        upn = "{}@b.dns-cloud.net".format(value)
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

#user keys:
users_keys_list=[]
my_user_args = "U"
for my_var in range(1,11):
    my_user_args = my_user_args + str(my_var)
    users_keys_list.append(my_user_args)
    print(my_user_args)
    my_user_args = "U"

my_users_keys= users_keys_list

#user values
#user keys:
users_value_list=[]
my_user_args = "kwarg"
for my_var in range(1,11):
    my_user_args = my_user_args + str(my_var)
    users_value_list.append(my_user_args)
    print(my_user_args)
    my_user_args = "kwarg"

my_users_value= users_value_list




#METHOD 1
# to convert lists to dictionary
# res = {}
# for key in my_users_keys:
#     for value in my_users_value:
#         res[key] = value
#         my_users_value.remove(value)
#         break
 
# # Printing resultant dictionary
# print("Resultant dictionary is : " + str(res))



#METHOD 2 

# res = {my_users_keys[i]: my_users_value[i] for i in range(len(my_users_keys))}
 
# # Printing resultant dictionary
# print("Resultant dictionary is : " + str(res))

#METHOD 3
res = dict(zip(my_users_keys, my_users_value))


 
# Printing resultant dictionary
print("Resultant dictionary is : " + str(res))

create_multiple_users_kwargs(**res)
