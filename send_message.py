import requests

TOKEN = 'MTA5MjE1NzU4NzkxNjU5OTMzNw.G0KzBN.RsnyxwUVK0EuHkO8DdUMeDZAyCRxm2Qhceedm4'
RECIPIENT_ID = '694118037036466187'
MESSAGE = 'Test'

headers = {
    'Authorization': TOKEN,
    'Content-Type': 'application/json',
    'X-Audit-Log-Reason': 'Sending automated message to user'
}

# First, create a Direct Message channel
create_dm_data = {
    'recipient_id': RECIPIENT_ID,
}

create_dm_response = requests.post(
    'https://discord.com/api/v9/users/@me/channels',
    #'https://discord.com/api/v10/users/@me/channels',
    headers=headers,
    json=create_dm_data,
)


if create_dm_response.status_code == 200:
    dm_channel_id = create_dm_response.json()['id']

    # Then, send the message to the created DM channel
    send_message_data = {
        'content': MESSAGE,
    }

    send_message_response = requests.post(
        #todo eventually needs to be v9
        #f'https://discord.com/api/v10/channels/{dm_channel_id}/messages',
        f'https://discord.com/api/v9/channels/{dm_channel_id}/messages',
        headers=headers,
        json=send_message_data,
    )

    if send_message_response.status_code == 200:
        print("Message sent successfully.")
    else:
        print(f"Error sending message: {send_message_response.status_code} - {send_message_response.text}")

else:
    print(f"Error creating DM channel: {create_dm_response.status_code} - {create_dm_response.text}")
