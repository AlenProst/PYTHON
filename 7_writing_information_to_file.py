def get_mail_for_user_with_filter():

    #endpoint = "https://graph.microsoft.com/v1.0/users/ivansto@b.dns-cloud.net/messages?$top=2&select=id"
    endpoint = "https://graph.microsoft.com/v1.0/users/ivansto@b.dns-cloud.net/messages?$top=2"

    headers = {
        'Authorization': access_token
    }

    graph_result = requests.get(url=endpoint, headers=headers)
    data = graph_result.json()

    save_folder=r"C:\Users\Ivan\Desktop\save"

    for mailid in data['value']:
        print(mailid['id'])
        with open(os.path.join(save_folder,'readme.txt'), 'a') as f:
            f.write(mailid['id'])
            f.write("\n")
