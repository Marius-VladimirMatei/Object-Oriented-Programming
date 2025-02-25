def seconds_to_minutes_seconds(seconds: int) -> str:
    """Convert seconds to MM:SS format"""
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes}:{remaining_seconds:02d}"


def minutes_seconds_to_seconds(time_str: str) -> int:
    """Convert MM:SS format to seconds"""
    try:
        if ":" not in time_str:
            raise ValueError("Invalid time format. Use MM:SS (e.g. 3:45)")

        parts = time_str.strip().split(":")
        if len(parts) != 2:
            raise ValueError("Invalid time format. Use MM:SS (e.g. 3:45)")

        minutes, seconds = map(int, parts)
        if minutes < 0 or seconds < 0 or seconds >= 60:
            raise ValueError(
                "Invalid time values. Minutes should be positive, seconds between 0-59"
            )

        return (minutes * 60) + seconds

    except (ValueError, TypeError) as e:
        if str(e).startswith("Invalid time"):
            raise
        raise ValueError("Invalid time format. Use MM:SS (e.g. 3:45)")
