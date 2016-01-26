import pprint

import requests #http://docs.python-requests.org/en/latest/user/quickstart/

pp = pprint.PrettyPrinter(indent=2)
username = ""
password = ""


class PersonalityInsightsInterface(object):

    def __init__(self, username, password):
        self.url = "https://gateway.watsonplatform.net/personality-insights/api"
        self.auth = requests.auth.HTTPBasicAuth(username, password)

    def authenticate(self):
        response = requests.post(
            self.url,
            auth=self.auth,
        )
        return response.json()

    def profile(self, text):
        response = requests.post(
            self.url + "/v2/profile",
            auth=self.auth,
            headers={"content-type": "text/plain"},
            data=text,
        )
        return response.json()


    def _profile_map(self, profile):
        try:
            tree = profile['tree']['children']
            tree = self.flatten_json(profile)
            keys = set()
            for i in list(tree.keys()):
                keys = keys | set(['_'.join(i.split('_')[:-1])])

            map = {}
            for key in keys:
                try:
                    map[tree[key+'_name']] = tree[key+'_percentage']
                except Exception:
                    pass
            return map
        except Exception:
            return {}

    @staticmethod
    def flatten_json(y):
        out = {}

        def flatten(x, name=''):
            if type(x) is dict:
                for a in x:
                    flatten(x[a], name + a + '_')
            elif type(x) is list:
                i = 0
                for a in x:
                    flatten(a, name + str(i) + '_')
                    i += 1
            else:
                out[str(name[:-1])] = str(x)

        flatten(y)
        return out


if __name__ == '__main__':
    persinal_insights = PersonalityInsightsInterface(
        username,
        password,
    )

    files = [
        'sample1.txt',
        # ...
    ]

    for f in files:
        with open(f, 'r', encoding='latin-1', errors='replace') as file:
            data=file.read()
            profile = persinal_insights.profile(data)
            print('Profile from file {}'.format(f))

            # Indented data
            # pp.pprint(profile)

            # Flattened data
            pp.pp(persinal_insights._profile_map(profile))
