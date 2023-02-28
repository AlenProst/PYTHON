class User:

    def __init__(self, display_name, mail_nickname, upn):
        self.display_name = display_name
        self.mail_nickname = mail_nickname
        self.account_enabled = True
        self.upn = upn
        self.password = "O365user!"

    #what happens when we print the object
    def __str__(self):
        return "display_name: {}, mail_nickname: {}, account_enabled: {}, upn: {}, password: {}".format(self.display_name, self.mail_nickname, self.account_enabled, self.upn, self.password )


    def create_user(self):
        display_name = self.display_name
        mail_nickname = self.mail_nickname
        account_enabled = True
        upn = self.upn
        password = "O365user!"
        usage_location = "BG"


        access_token = token_creation()
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

#We create the new user: 

new_user = User("PYclass1", "PYclass1", "PYclass1@b.dns-cloud.net")

#we invoke the method that creates the user 
new_user.create_user()



## WITH A GLOBAL VARIABLE 

class User:

    random_number_user = random.randint(0,100000)

    def __init__(self, display_name, mail_nickname, upn):
        self.display_name = display_name
        self.mail_nickname = mail_nickname
        self.account_enabled = True
        self.upn = upn
        self.password = "O365user!"

    #what happens when we print the object
    def __str__(self):
        return "display_name: {}, mail_nickname: {}, account_enabled: {}, upn: {}, password: {}".format(self.display_name, self.mail_nickname, self.account_enabled, self.upn, self.password )


    def create_user_random(self):
        display_name = self.display_name + str(User.random_number_user)
        mail_nickname = self.mail_nickname + str(User.random_number_user)
        account_enabled = True
        upn = display_name + "@b.dns-cloud.net"
        password = "O365user!"
        usage_location = "BG"


        access_token = token_creation()
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
        return upn


new_user = User("GlobalVariablee", "Globalvariablee", "GlobalVariablee@b.dns-cloud.net")

upn = new_user.create_user_random()
print(upn)
