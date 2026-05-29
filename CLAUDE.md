# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment Setup

Requires a `.env` file in the project root (never commit this):
```
ANTHROPIC_API_KEY=sk-ant-...      # console.anthropic.com → API Keys
WEATHER_APP_KEY=your_key_here     # openweathermap.org/api (free tier)
```

Install dependencies:
```bash
pip install anthropic openai pandas matplotlib requests beautifulsoup4 rich python-dotenv
```

## Running Scripts

All scripts live in `python-scripts/` and are run from that directory:

```bash
cd python-scripts

python python_learning_withAI.py   # Python fundamentals demo (all sections)
python Python_Problems.py          # Classic algorithm problems
python Interactive_WordSearch.py   # Terminal word search game
python data_analysis.py            # Honda dataset summary + pie chart
python weather_api.py              # Current "feels like" temp (NJ default)
python web_scraper.py <url>        # Scrape h1 headlines from a URL
python ai_tutor.py                 # Interactive Python tutor via Claude
python ai_data_analyst.py          # Ask questions about Honda dataset via Claude
python ai_data_analyst.py path/to/file.csv  # Use your own CSV
```

## Architecture

### Shared Claude client (`claude_client.py`)
`ai_tutor.py` and `ai_data_analyst.py` both import from `claude_client.py`, which centralizes:
- `get_client()` — builds `anthropic.Anthropic` from `ANTHROPIC_API_KEY`, raises clearly if missing
- `extract_text()` — pulls the text string out of a `Message` response
- `MODEL` constant — `claude-sonnet-4-6` (change here to update all AI scripts at once)

### AI scripts pattern
Both AI scripts follow the same structure: a `SYSTEM_PROMPT` constant at module level, stateless helper functions that call `client.messages.create(...)`, and a `run()` loop that manages conversation history manually as a `list[MessageParam]`.

`ai_data_analyst.py` injects the full DataFrame (as JSON) into the first user message only; follow-up turns send only the new question — Claude's conversation history carries the data context forward.

### Data layer (`data_analysis.py`)
Contains the Honda used car dataset as an in-memory dict and exposes `load_data() -> pd.DataFrame`. `ai_data_analyst.py` imports `load_data` directly rather than duplicating the data.

### Output
`python_learning_withAI.py` writes to `python-scripts/output/demo.txt` (relative to `__file__`, so it works from any working directory). This folder is untracked.
