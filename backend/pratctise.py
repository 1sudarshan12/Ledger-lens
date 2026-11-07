
# Create a Document class with title, amount and status (default "pending"), plus a method is_large() that returns True if amount > 1000
class Document:
    def __init__(self, title, amount, status="pending"):
        self.title = title
        self.amount = amount
        self.status = status

    def isLarge(self):
        return self.amount > 1000

    


#     Write a decorator log_call that prints the function’s name before running it. Apply it to a function summarize(docs).
# Inside summarize, use a list comprehension to get the titles of the large documents, and return a dict like {"count": 2, "titles": [...]}.
# Print the result with an f-string.
# Add type hints everywhere.
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def summarize(docs: list[Document]) -> dict:
    large_docs = [doc for doc in docs if doc.isLarge()]
    return {"count": len(large_docs), "titles": [doc.title for doc in large_docs]}