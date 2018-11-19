# from slackclient import SlackClient
# import json
#
# SLACK_TOKEN = "THIS IS A WRONG SLACK TOKEN"
# SLACK_CHANNEL = "#random"
#
#
# def send_slack_message(result):
#     sc = SlackClient(SLACK_TOKEN)
#     desc = "{0} | {1} | {2} | <{3}>".format(result["area"], result["price"], result["name"], result["url"])
#     sc.api_call(
#         "chat.postMessage", channel=SLACK_CHANNEL, text=desc,
#         username='pybot', icon_emoji=':robot_face:'
#     )
#
#
# if __name__ == "__main__":
#     # Read data from test_data.json, parse it into results we want, and post it
#     with open('test_data.json', 'r') as f:
#         data = json.load(f)
#         # Only really want first result
#         # Transform to result dict
#         result = {
#             "area": data[0]["where"],
#             "price": data[0]["price"],
#             "url": data[0]["url"],
#             "name": data[0]["name"]
#         }
#         # TODO: Need to think of a way to test this, and not just manually.
#         send_slack_message(result)
