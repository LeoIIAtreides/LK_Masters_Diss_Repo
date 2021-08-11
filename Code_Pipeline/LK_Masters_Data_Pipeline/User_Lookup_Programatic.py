from Secrets import TOKEN
from twarc import Twarc2, expansions
import datetime
import json
import tweeterid

# Replace your bearer token below
client = Twarc2(bearer_token=TOKEN)

def main():

    def Twitter_Handle():
        T_Handel = (tweeterid.id_to_handle('<USER_ID_HERE>'))
        X_Handel = T_Handel.lstrip("@")
        return (X_Handel)
    Twitter_Handle()

    def User_Request():
        # Specify the start time in UTC for the time period you want Tweets from
        start_time = datetime.datetime(2020, 11, 5, 0, 0, 0, 0, datetime.timezone.utc)

        # Specify the end time in UTC for the time period you want Tweets from
        end_time = datetime.datetime(2020, 12, 2, 0, 0, 0, 0, datetime.timezone.utc)

        # File to write tweets to
        file_name = 'User_Lookup_Data.json'

        # This timeline functions gets the Tweet timeline for a specified user
        user_timeline = client.timeline(user=Twitter_Handle(), start_time=start_time, end_time=end_time)

        # Twarc returns all Tweets for the criteria set above, so we page through the results
        for page in user_timeline:
            result = expansions.flatten(page)
            # We will open the file and append one JSON object per new line
            with open(file_name, 'a+') as filehandle:
                for tweet in result:
                    filehandle.write('%s\n' % json.dumps(tweet))
    User_Request()


if __name__ == "__main__":
    main()

