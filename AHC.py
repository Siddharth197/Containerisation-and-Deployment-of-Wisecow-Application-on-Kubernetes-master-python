import requests
import time

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "The application is UP and running smoothly!"
        else:
            return f"The application is DOWN with status code: {response.status_code}"
    except requests.ConnectionError:
        return "Connection Error: Unable to connect to the application."
    except requests.Timeout:
        return "Timeout Error: Connection to the application timed out."
    except requests.RequestException:
        return "Request Exception: Unable to access the application."


if __name__ == "__main__":
    url = input("Please enter the URL of the application you want to check: ")
    interval = int(input("Enter the interval (in seconds) between checks: "))
    
    # Continuously checking the application health
    while True:
        print("\nChecking application health...")
        # Calling the function to check the application health and printing the result
        status = check_application_health(url)
        print(status)
        
        # Waiting for the specified interval before checking again
        time.sleep(interval)
