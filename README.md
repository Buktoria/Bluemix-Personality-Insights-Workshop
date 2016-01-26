# Bluemix Personality Insights Workshop
---

This workshop is here to give you an introduction to IBM Bluemix and their personality insights api. I have written a simple wrapper for making http requests to their api.

## References

Feel free to use  the code that is provided in this workshop. In addition IBM offers docs for HTTP, node, and Java for this api. There is also a sample python application you can look at. You can play around and build off of it if you choose.

[Bluemix Personality Insights Api Docs](http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/personality-insights/api/v2/?node#introduction)

[Sample Python Application](https://github.com/watson-developer-cloud/personality-insights-python)

[Other samples using Bluemix Api's](https://github.com/watson-developer-cloud)

### Step One: Create a service

1. Log in to your Bluemix account
2. Go to API's or Catalog
3. Under Watson services click on Personality Insights
4. Click create "Create"

### Step Two: Setup

1. Make a new python virtual environment for the tutorial in python3. You can do this by doing the following, `virtualenv -p python3 personality_venv` Then to activate, `source personality_venv/bin/activate` Then do a pip install for requests by doing the following `pip install requests`

2. Get your service credentials. To do this go to "Service Credentials"

3. Copy and paste your credentials into the `personaliy_insights_interface.py` file.

### Step Three: Find Text to Analyze

1. Create three different .txt files of content coming from different places. These can be a collection of blog posts, articles, or even Facebook. Try to make sure each file has at least 3,500 words in it.

2. Add the file names to the `files` list in the `personaliy_insights_interface.py` file.

3. Run `python personality_insights_interface.py` and be amazed!
