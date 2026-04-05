# RewindRec

An open source project that helps you discover and revisit older entries in a franchise before a new release drops. Results are rendered as an HTML page, grouped by genre, with posters and rewatch suggestions inline.

## What It Does

When a new installment of a franchise (game, movie, TV show, book series, etc.) is announced or about to release, RewindRec recommends which older titles in that franchise you should watch first — so you're fully caught up and ready.

Results are rendered as an HTML page, grouped by genre, with posters and rewatch suggestions inline.

## Features

- Fetches upcoming movies from TMDB within a configurable time window
- Detects if a movie belongs to a collection and surfaces prior entries to rewatch
- Groups results by genre
- Renders a dark-themed HTML page with posters and rewatch thumbnails
- Supports mock date for historical simulation (uses `/discover/movie`) vs live mode (uses `/movie/upcoming`)

## Project Structure

```
RewindRec/
├── main.py           # Entry point
├── config.py         # API key, base URL, mock date config
├── requirements.txt
└── src/
    ├── tmdb.py       # TMDB API calls
    ├── recommender.py # Collection + rewatch logic
    ├── renderer.py   # HTML generation
    └── utils.py      # Helpers
```

## Getting Started

### Prerequisites

- Python 3.8+
- A free TMDB API key from [themoviedb.org](https://www.themoviedb.org/settings/api)

### Installation

```bash
git clone https://github.com/your-username/RewindRec.git
cd RewindRec
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```
TMDB_API_KEY=your_api_key_here
```

To simulate a past date (e.g. for testing), set `MOCK_TODAY` in `config.py`:

```python
MOCK_TODAY = "2025-08-01"  # uses /discover/movie with that date range
MOCK_TODAY = None           # uses /movie/upcoming (live mode)
```

You can also adjust the lookahead window:

```python
UPCOMING_MONTHS_AHEAD = 3  # in src/tmdb.py
```

### Run

```bash
python3 main.py
open output.html
```

## Contributing

This is an open source project and contributions are welcome. If you know of a franchise or have recommendation logic to add, feel free to open a pull request or file an issue.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a pull request

## License

[MIT](LICENSE)
