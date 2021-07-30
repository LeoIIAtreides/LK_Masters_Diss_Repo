from Secrets import TOKEN
from twarc import Twarc2, expansions
import datetime
import json

client = Twarc2(bearer_token=TOKEN)


def main():
    # Start date and time 03/12/2020 - 6pm (time to account for news disseminating)
    start_time = datetime.datetime(2020, 12, 3, 18, 0, 0, 0, datetime.timezone.utc)

    # End date and time 30/12/2020 - 6pm
    end_time = datetime.datetime(2020, 12, 30, 18, 0, 0, 0, datetime.timezone.utc)

    # Keyword relevant, UK geo OR bio location, eng lang, non retweets, non ads
    query = "Vaccine -is:nullcast -is:retweet lang:en place_country:gb OR place:england OR place:scotland OR place:wales OR place:U.K."

    # File to write tweets to
    file_name = 'Twarc_Test_Bed_Data.json'

    search_results = client.search_all(query=query, start_time=start_time, end_time=end_time, max_results=10)

    for page in search_results:
        result = expansions.flatten(page)
        # One JSON object per new line
        with open(file_name, 'a+') as filehandle:
            for tweet in result:
                filehandle.write('%s\n' % json.dumps(tweet))
