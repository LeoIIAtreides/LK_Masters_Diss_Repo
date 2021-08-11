from Secrets import TOKEN
from twarc import Twarc2, expansions
import json

# Replace your bearer token below
client = Twarc2(bearer_token=TOKEN)


def main():
    # List of user IDs to lookup, add the ones you would like to lookup
    users = ['ID HERE']
    # The user_lookup function gets the hydrated user information for specified users
    lookup = client.user_lookup(users=users)
    for page in lookup:
        result = expansions.flatten(page)
        for user in result:
            # Here we are printing the full Tweet object JSON to the console
            print(json.dumps(user))


if __name__ == "__main__":
    main()