from rest_framework import filters
from django.core.exceptions import ValidationError


class IsExamFilterBackendForGetMethodL1(filters.BaseFilterBackend):
    """
    Filter that checks returns the questions of the required exam only
    """

    def filter_queryset(self, request, queryset, view):
        if request.method != "GET":
            return queryset
        try:
            return queryset.filter(question__exam=request.GET['exam'])
        except KeyError:
            raise ValidationError("exam field is required")


class IsExamFilterBackendForDeleteMethod(filters.BaseFilterBackend):
    """
    Filter that checks returns the questions of the required exam only
    """

    def filter_queryset(self, request, queryset, view):
        if request.method != "DELETE":
            return queryset
        try:
            return queryset.filter(exam=request.GET['exam'])
        except KeyError:
            raise ValidationError("exam field is required")

