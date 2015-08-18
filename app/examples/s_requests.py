import requests
from retrying import retry
from requests import ConnectionError, HTTPError

def decroate_retry(func):
  @retry(wait_exponential_multiplier=1000, wait_exponential_max=10000, stop_max_attempt_number=5)
  def retry_metrics(*args, **kwargs):
    try:
      response = func(*args, **kwargs)
      response.raise_for_status()
    except ConnectionError as e:
      print("ConnectionError:", e.message)
      #log metrics
      raise
    except HTTPError as e:
      print("HTTPError:", e.message)
      #log metrics
      raise

  return retry_metrics

# @retry(wait_exponential_multiplier=1000, wait_exponential_max=10000, stop_max_attempt_number=5)
@decroate_retry
def test_500_retry():
  url = "https://httpbin.org/status/500"
  response = requests.get(url)
  return response

if __name__ == '__main__':
  print("hello")
  test_500_retry()