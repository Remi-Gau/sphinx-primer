def foo() -> None:
    """Public function should appear in the doc.

    Return ``None``."""
    return None

def _bar():
    """Private function should not appear in the doc."""
    ...