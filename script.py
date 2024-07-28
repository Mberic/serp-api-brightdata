import pprint
import requests

host = 'brd.superproxy.io'
port = 22225


# please replace with your `username` and `password`
# You can get these details from the Access Parameters tab of the proxy product. See below:
#
# https://brightdata.com/cp/zones/serp_api1/access_params
#

username = 'brd-customer-hl_be7c1b49-zone-serp_api1'
password = 'a84ql433nvd4'

proxy_url = f'http://{username}:{password}@{host}:{port}'

proxies = {
  'http': proxy_url,
  'https': proxy_url
}

# In the link below, `pizza` is our search query. You can change it to something
# else like `elections`
#
# We have added `Trends` query parameters by using the ampersand (&) on the link
# Here is the API for query parameters
# https://docs.brightdata.com/scraping-automation/serp-api/query-parameters/google
#

url = "https://www.google.com/search?q=pizza&geo=us&timenow+7-d&brd_json=1"

# Please fill in the absolute path to the `ca.crt` file you downloaded
# Don't use "~" to refer to home
# e.g  /home/josh/Documents/google-trends/ca.crt is correct


cert_path = "/home/eric/Documents/code/python/google-trends/ca.crt"

response = requests.get(url, proxies=proxies, verify=cert_path)


# Check the status code
if response.status_code == 200:
  try:
      # Try to parse the response as JSON
      data = response.json()
   
      # Save the response text to a file
      with open("response.json", "w") as file:
          file.write(response.text)
      print("Response has been saved to response.json")
  except ValueError as e:
      # Handle the case where the response is not JSON
      print("Response is not in JSON format.")
      # Save the response text to a file
      with open("response.html", "w") as file:
          file.write(response.text)
      print("Response has been saved to response.html")
else:
  print(f"Request failed with status code {response.status_code}")
