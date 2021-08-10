from Secrets import TOKEN
from twarc import Twarc2, expansions
import datetime
import json

client = Twarc2(bearer_token=TOKEN)


def main(query:str):
    # Specify the start time in UTC for the time period you want Tweets from
    start_time = datetime.datetime(2020, 12, 3, 0, 0, 0, 0, datetime.timezone.utc)

    # Specify the end time in UTC for the time period you want Tweets from
    end_time = datetime.datetime(2021, 2, 3, 0, 0, 0, 0, datetime.timezone.utc)

    # File to write tweets to
    file_name = 'Keyword_Query_RAW_Data_2.json'

    # the following calls the full archive search endpoint
    search_results = client.search_all(query=query, start_time=start_time, end_time=end_time)

    # Twarc returns all Tweets for the criteria set above, so we page through the results
    for page in search_results:
        # The API returns the Tweet info, user, media, etc. separately
        # so we use expansions.flatten to get all the information in a single JSON
        result = expansions.flatten(page)
        # We will open the file and append one JSON object per new line
        with open(file_name, 'a+') as filehandle:
            for tweet in result:
                filehandle.write('%s\n' % json.dumps(tweet))

if __name__ == "__main__":
    main(query = "(vaccine OR vaccinate OR vaccinated OR vaccination OR vaccinations OR immunisation OR immunization OR immunize OR immunise OR vax OR vaxd OR covax OR covidvaccine) -is:nullcast -is:retweet -is:reply -is:quote lang:en place_country:gb")