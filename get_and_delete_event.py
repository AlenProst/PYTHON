def get_calendars_graph(): 

    upn = "ivansto@b.dns-cloud.net"

    endpoint = "https://graph.microsoft.com/v1.0/users/{}/calendars?$select=name,id".format(upn)

    headers = {
        'Authorization': access_token
    }

    graph_result = requests.get(url=endpoint, headers=headers)
    data = graph_result.json()

    print("For which calendar do you want to see the events:\n")
    list_of_calendar_IDs = []
    counter = 0
    for calendar in data['value']:
        #print("NAME: {} \n{}".format(calendar['name'], calendar['id']))
        print("{} NAME: {} ".format(counter, calendar['name']))
        list_of_calendar_IDs.append(calendar['id'])
        counter = counter + 1

    
    calender_name_from_input = int(input('Please enter a number\n'))
    calendar_id = list_of_calendar_IDs[calender_name_from_input]
    #print(list_of_calendar_IDs[calender_name_from_input])

    endpoint_for_events = "https://graph.microsoft.com/v1.0/users/{}/calendars/{}/events?$select=subject,id".format(upn,calendar_id)
    print(endpoint_for_events)

    graph_result = requests.get(url=endpoint_for_events, headers=headers)
    data = graph_result.json()

    number_events = 0
    list_of_event_IDs = []
    print("All the events in the calendar you have chosen:\n")
    for event in data['value']:
        print("{} NAME: {} ".format(number_events, event['subject']))
        list_of_event_IDs.append(event['id'])
        number_events = number_events + 1


    print("\nWhich event would you like to delete? Please enter a number:")

    event_name_from_input = int(input('Please enter a number\n'))

    event_to_delete = list_of_event_IDs[event_name_from_input]


    endpoint_for_events_to_delete = "https://graph.microsoft.com/v1.0/users/{}/calendars/{}/events/{}".format(upn,calendar_id,event_to_delete)

    print(endpoint_for_events_to_delete)

    graph_result = requests.get(url=endpoint_for_events_to_delete, headers=headers)
    data = graph_result.json()

    print("\n\nIs this the EVENT you want to delete?\n\n")

    print(data['subject'])
    print("\n")

    choice_for_deletion = int(input('1 Yes\n2 No\n\n'))
    if choice_for_deletion == 1:
        graph_result = requests.delete(url=endpoint_for_events_to_delete, headers=headers)
    else:
        print("Program end")
