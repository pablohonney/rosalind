def get_gc_content(line: str) -> float:
    return (line.count("G") + line.count("C")) / len(line) * 100


def get_max_record(records: list) -> tuple:
    max_score = -1
    max_name = ""

    for name, value in records:
        new_score = get_gc_content(value)
        if new_score > max_score:
            max_score = new_score
            max_name = name

    return max_name, max_score
