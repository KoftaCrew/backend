from rest_framework import mixins, viewsets, response
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password


# Create your views here.
class CreateUserView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    lookup_field = 'id'
    __required_fields = [
        'username', 'email', 'password', 'confirm_password', 'first_name', 'last_name'
    ]

    def get_missing_fields(self, request) -> list:
        return_list = []
        for field in self.__required_fields:
            try:
                request.data[field]
            except KeyError:
                return_list.append(field)
        return return_list

    def create(self, request, *args, **kwargs) -> response.Response:
        missing_fields = self.get_missing_fields(request)
        if len(missing_fields) != 0:
            ret = {}
            for field in missing_fields:
                ret[field] = "This field is required."
            return response.Response(ret)

        if request.data['password'] != request.data['confirm_password']:
            return response.Response({
                'details': "Passwords doesn't match"
            })
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)
