import requests

BASE_URL = "http://127.0.0.1:5000"  # Flask backend

def get_predictions():
    """
    Fetch predictions from the Flask API.
    Returns:
        dict: {"real": [...], "predicted": [...]}
    """
    try:
        response = requests.get(f"{BASE_URL}/predictions")
        response.raise_for_status()  # raise error if status != 200
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching predictions: {e}")
        return {"real": [], "predicted": []}