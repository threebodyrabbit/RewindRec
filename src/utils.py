from datetime import date


def sort_by_release_date(parts: list) -> list:
    """Sort franchise parts by release date ascending."""
    return sorted(parts, key=lambda x: x.get("release_date") or "")


def filter_older_entries(parts: list) -> list:
    """Return all entries except the latest (newest) one."""
    today = str(date.today())
    released = [p for p in parts if p.get("release_date") and p["release_date"] <= today]
    return released[:-1] if len(released) > 1 else released
