def get_all_users():

    users = "users?$select=id"
    #endpoint = "https://graph.microsoft.com/v1.0/users{}".format(my_user)
    endpoint = "https://graph.microsoft.com/v1.0/{}".format(users)
    counter = 1

    headers = {
        'Authorization': access_token
    }

    graph_result = requests.get(url=endpoint, headers=headers)
    data = graph_result.json()

    more_available = True

    while more_available:
        graph_result = requests.get(url=endpoint, headers=headers)
        data = graph_result.json()


        for mailid in data['value']:
            counter +=1
            print(counter)
            print(mailid['id'])

        # If @odata.nextLink is present
        more_available = '@odata.nextLink' in data
        if more_available == False:
            print("No more users in tenant")
            break
        print('\nMore users available?', more_available, '\n')
        
        print(data['@odata.nextLink'])
        endpoint = data['@odata.nextLink']
        

    



