def normalize_label(label: str) -> str:
    return label.strip().lower()


def normalize_labels(labels: list[str]) -> list[str]:
    return [normalize_label(label) for label in labels]
