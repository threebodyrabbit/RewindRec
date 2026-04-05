import requests
from datetime import date, timedelta
from config import API_KEY, BASE_URL, MOCK_TODAY

UPCOMING_MONTHS_AHEAD = 3


def _today():
    return MOCK_TODAY if MOCK_TODAY else date.today().isoformat()


def get_upcoming_movies(limit=20):
    today_str = _today()
    cutoff = (date.fromisoformat(today_str) + timedelta(days=30 * UPCOMING_MONTHS_AHEAD)).isoformat()
    is_mock_past = MOCK_TODAY and MOCK_TODAY < date.today().isoformat()

    results = []
    page = 1

    if is_mock_past:
        # use discover for historical simulation
        url = f"{BASE_URL}/discover/movie"
        while len(results) < limit:
            params = {
                "api_key": API_KEY,
                "language": "en-US",
                "region": "US",
                "sort_by": "popularity.desc",
                "primary_release_date.gte": today_str,
                "primary_release_date.lte": cutoff,
                "page": page
            }
            res = requests.get(url, params=params).json()
            batch = res.get("results", [])
            total_pages = res.get("total_pages", 1)
            results.extend(batch)
            if page >= total_pages:
                break
            page += 1
    else:
        # use upcoming endpoint for real-time data
        url = f"{BASE_URL}/movie/upcoming"
        while len(results) < limit:
            params = {"api_key": API_KEY, "language": "en-US", "region": "US", "page": page}
            res = requests.get(url, params=params).json()
            batch = res.get("results", [])
            total_pages = res.get("total_pages", 1)
            filtered = [m for m in batch if today_str <= m.get("release_date", "") <= cutoff]
            results.extend(filtered)
            if page >= total_pages:
                break
            page += 1

    print(f"{'[MOCK]' if is_mock_past else '[LIVE]'} date: {today_str} → cutoff: {cutoff}")
    print(f"Got {len(results)} upcoming movies within {UPCOMING_MONTHS_AHEAD} months.")
    return results[:limit]


def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": API_KEY}
    return requests.get(url, params=params).json()


def get_collection_movies(collection_id):
    url = f"{BASE_URL}/collection/{collection_id}"
    params = {"api_key": API_KEY}
    res = requests.get(url, params=params).json()
    return res.get("parts", [])