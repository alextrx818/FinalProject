"""
Main entry point for the sports data aggregation service.
"""

from aggregator import SportsAggregator

def main():
    aggregator = SportsAggregator()
    aggregator.run()

if __name__ == "__main__":
    main()
