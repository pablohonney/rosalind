import typing as T
from collections import defaultdict


def get_overlap_graphs(records: list, size: int = 3) -> T.List[T.Tuple[str, str]]:
    adjacency_list = []

    tail_prefixes = defaultdict(list)
    for rec in records:
        tail_prefixes[rec.text[:size]].append(rec)

    for head in records:
        head_suffix = head.text[-size:]

        for tail in tail_prefixes.get(head_suffix, []):
            if head.name != tail.name:
                adjacency_list.append((head.name, tail.name))

    return adjacency_list


# Har8's implementation
def get_overlap_graphs_naive(records: list):
    for i in records:
        for j in records:
            if i.name == j.name:
                continue
            elif i.text[-3:] == j.text[:3]:
                yield i.name, j.name
