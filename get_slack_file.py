# Usage: python3 download_files_from_slack.py <URL>

import sys
import re
import requests


def get_file_from_url(url):
    token = os.environ["SLACK_TOKEN"]
    resp = requests.get(url, headers={'Authorization': 'Bearer %s' % token})
    headers = resp.headers['content-disposition']
    fname = re.findall("filename=(.*?);", headers)[0].strip("'").strip('"')
    assert not os.path.exists(fname), print("File already exists. Please remove/rename and re-run")
    out_file = open(fname, mode="wb+")
    out_file.write(resp.content)
    out_file.close()

