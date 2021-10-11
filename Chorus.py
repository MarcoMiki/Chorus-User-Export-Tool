import requests
import pandas


class Chorus:
    def __init__(self, key, url):
        '''Authenticates to a Chorus site. Requires URL and a site API key generated from the "admin - site" menu'''
        self.url = url
        self.login_response = requests.post(url=url + "/rest/v1/auth/loginWithKey", json={"apiKey": key})
        self.sessionID = self.login_response.json()["sessionId"]
        self.chorus_headers = {"X-Chorus-Session": self.sessionID}

    # GET USER DATA AND EXPORT IT

    def get_user_ids(self):
        """returns the IDs of all site users"""
        response = requests.get(url=self.url + "/rest/v1/site/users", headers=self.chorus_headers)
        return response.json()["response"]

    def get_multiple_user_details(self):
        """given a list of ids, returns details for them"""
        ids_list = self.get_user_ids()
        body = {
            "userIds": ids_list
        }
        response = requests.post(url=self.url + "/rest/v1/users/multi", json=body, headers=self.chorus_headers)
        return response.json()

    def export_user_data(self):
        """given a path to export to, downloads a .csv file with details for all site's users"""
        user_details = self.get_multiple_user_details()
        data = user_details["response"]
        df = pandas.DataFrame(data)
        csv = df.to_csv(index=False, encoding="utf-8")
        return csv

