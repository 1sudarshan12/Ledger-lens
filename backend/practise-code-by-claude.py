from functools import wraps
from typing import Callable, TypedDict


class Document:
    def __init__(self, title: str, amount: float, status: str = "pending") -> None:
        self.title = title
        self.amount = amount
        self.status = status

    def is_large(self) -> bool:
        return self.amount > 1000


class Summary(TypedDict):          # like a TS interface for a dict
    count: int
    titles: list[str]


def log_call(func: Callable) -> Callable:
    @wraps(func)                
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@log_call
def summarize(docs: list[Document]) -> Summary:
    titles = [doc.title for doc in docs if doc.is_large()]
    return {"count": len(titles), "titles": titles}


if __name__ == "__main__":         # runs only when executed directly, not on import
    docs = [
        Document("Invoice A", 1500),
        Document("Invoice B", 300, "paid"),
        Document("Tax form", 2200),
    ]
    result = summarize(docs)
    print(f"{result['count']} large documents: {', '.join(result['titles'])}")