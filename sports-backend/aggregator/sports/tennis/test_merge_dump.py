"""
This script dumps the already merged data from tennis_merger.py to a JSON file for analysis.
"""

import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def dump_merged_data():
    try:
        # Get the merged data from tennis_merger.py
        # TODO: Need to get the merged data from the running bot
        # How do we access the data that's already being merged?
        
        # Write the merged data to a JSON file
        output_file = 'mergedDump.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, indent=2, default=str)

        logger.info(f'Merged data written to {output_file} successfully.')

    except Exception as e:
        logger.error(f'Error dumping merged data: {str(e)}')
        raise

if __name__ == '__main__':
    dump_merged_data()
