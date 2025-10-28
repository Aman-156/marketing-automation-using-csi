# discovery_engine.py
import os
from serpapi import SerpApiClient

def find_leads(service: str, location: str = "Austin, Texas, United States") -> list[dict]:
    """
    Finds leads for a given service using SerpAPI.

    Args:
        service: The service to search for (e.g., "Web Development").
        location: The location for the search.

    Returns:
        A list of dictionaries, where each dictionary contains the 'name' and 'url' of a lead.
    """
    # It's best practice to set your API key as an environment variable.
    # For now, you can paste it directly, but be careful sharing your code!
    api_key = os.getenv("SERPAPI_KEY", "112e338a5fa3e635466c027001003d249c4bb7c4e1f75bbdb8e50a09330c2c00")
    
    if api_key == "112e338a5fa3e635466c027001003d249c4bb7c4e1f75bbdb8e50a09330c2c00":
        print("⚠️ WARNING: Please replace '112e338a5fa3e635466c027001003d249c4bb7c4e1f75bbdb8e50a09330c2c00' with your actual SerpAPI key.")
        return []

    params = {
        "engine": "google",
        "q": service,
        "location": location,
        "api_key": api_key
    }

    try:
        client = SerpApiClient(params)
        results = client.get_dict()
        organic_results = results.get("organic_results", [])
        
        leads = []
        for result in organic_results:
            leads.append({
                "name": result.get("title"),
                "url": result.get("link")
            })
        
        print(f"✅ Found {len(leads)} leads for '{service}'.")
        return leads
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return []

# Example of how to run this function directly for testing
if __name__ == '__main__':
    find_leads("Plumbers in Mangaluru")