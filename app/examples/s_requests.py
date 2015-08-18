import requests
from retrying import retry


@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000, stop_max_attempt_number=5)
def test_500_retry():
  url = "https://httpbin.org/status/500"

  response = requests.get(url)
  try:
    print("testing")
    response.raise_for_status()
  except requests.exceptions.HTTPError as e:
    print('And you get an HTTPError: %s' % e.message)
    raise

if __name__ == '__main__':
  print("hello")
  test_500_retry()