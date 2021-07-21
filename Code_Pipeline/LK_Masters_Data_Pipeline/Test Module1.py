from Secrets import TOKEN
from twarc import Twarc2, expansions
import json
import ssl
import os
client = Twarc2(bearer_token=TOKEN)

randTweets = []

def main():
    for count, result in enumerate(client.sample()):
        tweet = expansions.flatten(result)
        randTweets.append(tweet)
       # print(json.dumps(tweet))
        if count > 3:
            break

    with open('data.json', 'w') as f:
        json.dump(randTweets,f)



if __name__ == "__main__":
    main()

print(os.environ['BEARER_TOKEN'])
