class Licensed_User(User):
    def __init__(self, display_name, mail_nickname, upn):
        super().__init__(display_name, mail_nickname, upn)
 

    def __str__(self):
        text = super(Licensed_User, self).__str__()
        return text
        


    def create_user_license(self, display_name, mail_nickname, upn):
        self.display_name = display_name
        self.mail_nickname = mail_nickname
        self.account_enabled = True
        self.upn = upn
        self.password = "O365user!"
        self.location = "BG"

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
            "userPrincipalName": self.upn,
            "usageLocation": self.location,
            "passwordProfile" : {
                "forceChangePasswordNextSignIn": False,
                "password": self.password
            }
            }
            )
        
        requests.post(url=url, headers=headers, data=req_body)
        def license_user(upn,SKU):

            licenseURL = "https://graph.microsoft.com/v1.0/users/{}/assignLicense".format(upn)
            print(licenseURL)
            print(SKU)


            req_body_license = json.dumps(
                {
                    "addLicenses": [
                        {
                            "skuId": SKU
                        }
                    ],
                    "removeLicenses": []
                }
            )

            headers = {
            'Authorization': access_token,
            'Content-Type': 'application/json'
            }

            requests.post(url=licenseURL, headers=headers, data=req_body_license)
        license_user(self.upn, "b05e124f-c7cc-45a0-a6aa-8cf78c946968")
