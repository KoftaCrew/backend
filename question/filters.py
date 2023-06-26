from rest_framework import filters
from django.core.exceptions import ValidationError


class IsExamFilterBackend(filters.BaseFilterBackend):
    """
    Filter that checks returns the questions of the required exam only
    """

    def filter_queryset(self, request, queryset, view):
        if request.method != "GET":
            return queryset
        try:
            return queryset.filter(exam=request.GET['exam'])
        except KeyError:
            raise ValidationError("exam field is required")
