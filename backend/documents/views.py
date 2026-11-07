from django.http import JsonResponse
from .models import Document

def document_list(request):
    documents = Document.objects.values(
        "id", "title", "status", "owner__email", "created_at","file", "updated_at"
    )
    return JsonResponse({ "documents": list(documents) })