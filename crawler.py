import sys
import json
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    root = sys.argv[1]
    layer = int(sys.argv[2])

    urls = set() # collect urls
    jobs = [root]

    for l in range(layer):
        print("[{}] jobs: {}".format(l, jobs))
        next_jobs = []

        for url in jobs:
            if url in urls:
                continue

            resp = requests.get(url)
            urls.add(url) # record what we fetched to avoid fetching twice

            soup = BeautifulSoup(resp.text, 'html.parser')

            for a_tag in soup.find_all("a"):
                href = a_tag.get("href")
                next_jobs.append(urljoin(url, href))

        jobs = next_jobs

    else:
        urls.update(jobs)

    sorted_urls = sorted(list(urls))
    print("Root URL:", root)
    print("Layer:", layer)
    print("Total collected:", len(sorted_urls))

    with open("collected.json", "w") as fd:
        json.dump(sorted_urls, fd, indent=4)
