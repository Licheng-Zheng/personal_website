import os
import json
import requests

def fetch_and_save_telemetry():
    # Retrieve environment variables injected by GitHub Actions
    api_url = os.environ.get("TASK_TRACKER_URL")
    secret_key = os.environ.get("TELEMETRY_SECRET_KEY")

    if not api_url or not secret_key:
        print("CRITICAL ERROR: Missing environment variables for API URL or Secret Key.")
        print("Failure Meaning: The GitHub Actions runner cannot find your credentials. Verify that TELEMETRY_SECRET_KEY is saved in the repository Secrets and TASK_TRACKER_URL is defined in the workflow YAML.")
        return

    headers = {
        "Authorization": f"Bearer {secret_key}",
        "Content-Type": "application/json"
    }

    try:
        print(f"Fetching telemetry data from {api_url}...")
        response = requests.get(api_url, headers=headers)
        
        # This will immediately trigger an exception for 401 Unauthorized, 404 Not Found, or 500 Server Error responses.
        response.raise_for_status()
        
        data = response.json()
        
        # Ensure the output directory exists before attempting to write
        output_path = os.path.join("assets", "data", "telemetry.json")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
            
        print(f"Successfully saved telemetry data to {output_path}")

    except requests.exceptions.RequestException as e:
        print(f"NETWORK ERROR: Failed to fetch telemetry data: {e}")
        print("Failure Meaning: The script successfully read the token, but the HTTP GET request to your backend failed. This means your backend server is offline, the endpoint URL is incorrect, or the provided token was rejected by your server.")

if __name__ == "__main__":
    fetch_and_save_telemetry()