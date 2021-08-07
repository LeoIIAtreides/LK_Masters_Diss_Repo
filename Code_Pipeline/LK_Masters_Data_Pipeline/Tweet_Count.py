#Tweet Count
#Count results - Keyword Relevant tweets between 2020/12/03-2020/12/30 = 6620
from Secrets import TOKEN
from twarc import Twarc2
import datetime
import json

# Replace your bearer token below
client = Twarc2(bearer_token=TOKEN)

def main(query:str):
    # Specify the start time in UTC for the time period you want Tweets from
    start_time = datetime.datetime(2020, 12, 3, 0, 0, 0, 0, datetime.timezone.utc)

    # Specify the end time in UTC for the time period you want Tweets from
    end_time = datetime.datetime(2020, 12, 30, 0, 0, 0, 0, datetime.timezone.utc)

    # The counts_all method call the full-archive Tweet counts endpoint to get Tweet volume based on the query, start and end times
    count_results = client.counts_all(query=query, start_time=start_time, end_time=end_time)

    # Twarc returns all Tweet counts for the criteria set above, so we page through the results
    for page in count_results:
        print(json.dumps(page))


if __name__ == "__main__":
    main(query = "(vaccine OR vaccinate OR vaccinated OR vaccination OR vaccinations OR immunisation OR immunization OR immunize OR immunise OR vax OR vaxd OR covax OR covidvaccine) -is:nullcast -is:retweet -is:reply -is:quote lang:en place_country:gb")