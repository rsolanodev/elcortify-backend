from django_filters import CharFilter


class SearchFilter(CharFilter):
    def filter(self, qs, value):
        if hasattr(qs, "search"):
            return qs.search(query=value)
        return qs
