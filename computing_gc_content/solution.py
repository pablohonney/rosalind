def process_input(text: str) -> list:
    lines = text.split(">")

    records = []
    for line in lines:
        if not line:
            continue
        name, _line = line.strip().split("\n", 1)
        cleaned_line = _line.replace("\n", "")
        records.append((name, cleaned_line))
    return records


def get_gc_content(line: str) -> float:
    return (line.count("G") + line.count("C")) / len(line) * 100


def get_max_record(records: list):
    max_score = -1
    max_name = ""

    for name, value in records:
        new_score = get_gc_content(value)
        if new_score > max_score:
            max_score = new_score
            max_name = name

    return max_name, max_score


def solve(text: str) -> tuple:
    records = process_input(text)
    return get_max_record(records)
