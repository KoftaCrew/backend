from rest_framework import filters


class IsExamFilterBackend(filters.BaseFilterBackend):
    """
    Filter that checks returns the questions of the required exam only
    """
    def filter_queryset(self, request, queryset, view):
        try :
            return queryset.filter(exam=request.GET['exam'])
        except KeyError:
            return queryset
