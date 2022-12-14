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


    def create_user(self, display_name, mail_nickname, upn):
        self.display_name = display_name
        self.mail_nickname = mail_nickname
        self.account_enabled = True
        self.upn = upn
        self.password = "O365user!"
        self.usage_location = "BG"


        access_token = token_creation()
        url = 'https://graph.microsoft.com/beta/users'
        headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json'
        }

        req_body = json.dumps(
            {
            "accountEnabled": self.account_enabled,
            "displayName": self.display_name,
            "mailNickname": self.mail_nickname,
            "userPrincipalName": upn,
            "usageLocation": self.usage_location,
            "passwordProfile" : {
                "forceChangePasswordNextSignIn": False,
                "password": self.password
            }
            }
            )
        
        requests.post(url=url, headers=headers, data=req_body)
