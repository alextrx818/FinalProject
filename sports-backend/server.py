import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import the merger and fetchers from their correct locations
from aggregator.sports.tennis.tennis_merger import TennisMerger
from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite's default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/merged_data")
async def get_merged_data():
    """
    Fetch from BetsAPI + RapidAPI, merge using your Merger,
    and return the raw data (no filtering).
    """
    # Create fetcher instances
    bets_fetcher = BetsapiPrematch()
    rapid_fetcher = RapidInplayOddsFetcher()
    
    try:
        # Fetch data from each source
        bets_data = await bets_fetcher.get_tennis_data()
        rapid_data = await rapid_fetcher.get_tennis_data()
        
        # Merge the data using TennisMerger
        merger = TennisMerger()
        merged_data = merger.merge(bets_data, rapid_data)
        
        # Return the merged data
        return merged_data
    except Exception as e:
        print(f"Error fetching data: {str(e)}")
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
