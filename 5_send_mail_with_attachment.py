def send_mail_with_attachment():

    def draft_attachment(file_path):
        if not os.path.exists(file_path):
            print('file is not found')
            return
        
        with open(file_path, 'rb') as upload:
            media_content = base64.b64encode(upload.read())
            
        data_body = {
            '@odata.type': '#microsoft.graph.fileAttachment',
            'contentBytes': media_content.decode('utf-8'),
            'name': os.path.basename(file_path)
        }
        return data_body

    headers = {
        'Authorization': access_token
    }

    request_body = {
        'message': {
            # recipient list
            'toRecipients': [
                {
                    'emailAddress': {
                        'address': 'ivansto@b.dns-cloud.net'
                    }
                }
            ],
            # email subject
            'subject': 'You got an email',
            'importance': 'normal',
            'body': {
                'contentType': 'HTML',
                'content': '<b>Be Awesome</b>'
            },
            # include attachments
            'attachments': [
                draft_attachment(r'C:\Users\Ivan\Desktop\ivanst.txt'),
                draft_attachment(r'C:\Users\Ivan\Desktop\ivanst.txt')
            ]
        }
    }

    GRAPH_ENDPOINT = 'https://graph.microsoft.com/v1.0'
    endpoint = GRAPH_ENDPOINT + '/users/ivansto@b.dns-cloud.net/sendMail'

    response = requests.post(endpoint, headers=headers, json=request_body)
    if response.status_code == 202:
        print('Email sent')
    else:
        print(response.reason)

