import asyncio
import aiohttp
import json

API_TOKEN = "213380-3ngqZ80Cx59eaU"
BASE_URL = "https://api.b365api.com/v3"
SPORT_ID = "13"  # Tennis

async def fetch_data():
    # Get tennis events first
    events_url = f"{BASE_URL}/events/upcoming?sport_id={SPORT_ID}&token={API_TOKEN}"
    async with aiohttp.ClientSession() as session:
        async with session.get(events_url) as response:
            if response.status == 200:
                events_data = await response.json()
                if events_data.get("success") == 1 and events_data.get("results"):
                    # Get first event's bet365_id
                    event = events_data["results"][0]
                    bet365_id = event.get("bet365_id")
                    
                    if bet365_id:
                        # Now get prematch odds for this event
                        prematch_url = f"{BASE_URL}/bet365/prematch?sport_id={SPORT_ID}&token={API_TOKEN}&FI={bet365_id}"
                        print(f"\nFetching prematch odds for event:")
                        print(f"Event: {event['home']['name']} vs {event['away']['name']}")
                        print(f"League: {event['league']['name']}")
                        
                        async with session.get(prematch_url) as prematch_response:
                            if prematch_response.status == 200:
                                prematch_data = await prematch_response.json()
                                if prematch_data.get("success") == 1 and prematch_data.get("results"):
                                    print("\nPrematch odds data:")
                                    print(json.dumps(prematch_data["results"], indent=2))
                                else:
                                    print("No prematch data or API error:", prematch_data)
                            else:
                                print(f"Prematch request error: {prematch_response.status}")
                    else:
                        print("No bet365_id found for event")
                else:
                    print("No events data or API error:", events_data)
            else:
                print(f"Events request error: {response.status}")

if __name__ == "__main__":
    asyncio.run(fetch_data())
