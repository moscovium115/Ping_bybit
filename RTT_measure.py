import requests
import time

def measure_rtt(url, num_requests=10):
    total_rtt = 0
    successful_requests = 0

    for _ in range(num_requests):
        try:
            start_time = time.time()
            response = requests.get(url)
            end_time = time.time()

            if response.status_code == 200:
                rtt = (end_time - start_time) * 1000  # Convert to milliseconds
                total_rtt += rtt
                successful_requests += 1
                print(f"RTT: {rtt:.2f} ms")
            else:
                print(f"HTTP request failed with status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    if successful_requests > 0:
        average_rtt = total_rtt / successful_requests
        print(f"\nAverage RTT over {successful_requests} requests: {average_rtt:.2f} ms")
    else:
        print("No successful requests were made.")

if __name__ == "__main__":
    api_url = "https://api.bybit.com/v5/market/time"
    num_requests = 10
    measure_rtt(api_url, num_requests)
