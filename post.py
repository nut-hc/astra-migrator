import json
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

strapi_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNzE4MzUwMjIwLCJleHAiOjE3MjA5NDIyMjB9.1gtjFiOXs_GJn7ma-LOWqgbv6PGTmtIgGI1c5Phkhec"


def postWithRetry(url, errors, body=None, retry_count=3):
    isDuplicated = False
    request_headers = {"Authorization": f"Bearer {strapi_token}"}

    retry_strategy = Retry(
        total=retry_count,
        status_forcelist=[429, 500, 502, 503, 504],  # Status codes to retry on
        allowed_methods=["HEAD", "GET", "POST", "OPTIONS"],  # Methods to retry
        backoff_factor=1,  # A backoff factor to apply between attempts
    )

    session = requests.Session()
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    try:
        response = session.post(
            url,
            json=body,
            headers=request_headers,
        )
        if not response.status_code == 200:
            errors = response.json()["error"]["details"]["errors"]
            for e in errors:
                if not "must be unique" in e["message"]:
                    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
                else:
                    isDuplicated = True
        if isDuplicated:
            return None
        return json.loads(response.content.decode())
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        errors.append(body)
        return None
