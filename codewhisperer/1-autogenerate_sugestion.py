# TODO: place your cursor at the end of line 5 and press Enter to generate a suggestion.
# Tip: press tab to accept the suggestion.

fake_users = [
    { "name": "User 1", "id": "user1", "city": "San Francisco", "state": "CA" },
    { "name": "User 2", "id": "user2", "city": "New York", "state": "NY" },
    { "name": "User 3", "id": "user3", "city": "Chicago", "state": "IL" },
    { "name": "User 4", "id": "user4", "city": "Los Angeles", "state": "CA" },
    { "name": "User 5", "id": "user5", "city": "Miami", "state": "FL" },
]
for user in fake_users:
    print(user["name"], user["id"], user["city"], user["state"])
    print("----------------------")
    