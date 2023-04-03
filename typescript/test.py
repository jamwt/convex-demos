from convex import ConvexClient
from pprint import pprint
client = ConvexClient('https://dapper-quail-967.convex.cloud')
messages = client.query("listMessages")
pprint(messages)
client.mutation("sendMessage", {'author': 'Jamie', 'body': 'This is good'})
messages = client.query("listMessages")
pprint(messages)