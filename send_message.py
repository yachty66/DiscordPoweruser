import requests
import config
import json
import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 2:
    print("Usage: python script.py <members.json>")
    sys.exit(1)

# Load the message from the hardcoded message.json file
with open("message.json", "r") as message_file:
    message_data = json.load(message_file)
    MESSAGE = message_data["message"]


# Load the member list from the JSON file passed as the argument
members_file_path = sys.argv[1]
with open(members_file_path, "r") as members_file:
    members_data = json.load(members_file)

#token taken from network tab of discord
TOKEN = config.token_wobbert
headers = {
    'Authorization': TOKEN,
    'Content-Type': 'application/json',
    'X-Audit-Log-Reason': 'Sending automated message to user'
}

for RECIPIENT_ID, recipient_name in members_data.items():
    if RECIPIENT_ID == "null":
        continue

    create_dm_data = {
        'recipient_id': RECIPIENT_ID,
    }

    create_dm_response = requests.post(
        'https://discord.com/api/v9/users/@me/channels',
        headers=headers,
        json=create_dm_data,
    )

    if create_dm_response.status_code == 200:
        dm_channel_id = create_dm_response.json()['id']

        send_message_data = {
            'content': MESSAGE,
        }

        send_message_response = requests.post(
            f'https://discord.com/api/v9/channels/{dm_channel_id}/messages',
            headers=headers,
            json=send_message_data,
        )

        if send_message_response.status_code == 200:
            print(f"Message sent successfully to {recipient_name}.")
        else:
            print(f"Error sending message to {recipient_name}: {send_message_response.status_code} - {send_message_response.text}")

    else:
        print(f"Error creating DM channel for {recipient_name}: {create_dm_response.status_code} - {create_dm_response.text}")