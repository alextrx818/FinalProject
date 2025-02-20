# JSON Tools Directory

This directory contains tools for viewing, formatting, and converting JSON data.

## Available Tools

1. `json_to_table.py` - Convert JSON data to Excel/CSV tables
   - Supports both .xlsx and .csv output formats
   - Auto-formats columns for readability
   - Creates files in `~/output` directory

2. `paste_json_here.txt` - Empty file for pasting JSON data
   - Use this file to paste your JSON data
   - Works with json_to_table.py for conversion

## Usage

1. To convert JSON to table:
   ```bash
   # Option 1: Paste JSON directly
   python json_to_table.py
   
   # Option 2: Use the paste file
   cat paste_json_here.txt | python json_to_table.py
   ```

2. Output location:
   - All generated files are saved in `~/output/`
   - Files can be downloaded via VS Code Explorer

## Output Formats

1. Excel (.xlsx):
   - Full formatting
   - Auto-sized columns
   - Sheet name: "Tennis Odds"

2. CSV (.csv):
   - Simple text format
   - Compatible with all spreadsheet software
   - No formatting
