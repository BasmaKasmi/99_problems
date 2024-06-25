def yulaw(s: str) -> str:
    seen = set()
    return ''.join(seen.add(char) or char for char in s if char not in seen)

