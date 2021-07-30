from Secrets import TOKEN
from twarc import Twarc2, expansions
import datetime
import json

client = Twarc2(bearer_token=TOKEN)


def main():
    # Specify the start time in UTC for the time period you want Tweets from
    start_time = datetime.datetime(2021, 1, 1, 0, 0, 0, 0, datetime.timezone.utc)

    # Specify the end time in UTC for the time period you want Tweets from
    end_time = datetime.datetime(2021, 5, 30, 0, 0, 0, 0, datetime.timezone.utc)

    # This is where we specify our query as discussed in module 5
    query = "asimov -is:retweet"

    # File to write tweets to
    file_name = 'Twarc_Test_Bed_Data.json'

    # the following calls the full archive search endpoint and defines the max result (current 10 for testing)
    search_results = client.search_all(query=query, start_time=start_time, end_time=end_time, max_results=10)

    # Twarc returns all Tweets for the criteria set above, so we page through the results
    for page in search_results:
        # The API returns the Tweet info, user, media, etc. separately
        # so we use expansions.flatten to get all the information in a single JSON
        result = expansions.flatten(page)
        # We will open the file and append one JSON object per new line
        with open(file_name, 'a+') as filehandle:
            for tweet in result:
                filehandle.write('%s\n' % json.dumps(tweet))
