from django.views.generic import View

from bb_post.api.forms.post import CreateForm
from bb_post.api.mixins import PostAPIMixin
from bb_post.models import Post
from utils.api.exceptions import RequestValidationFailedAPIError
from utils.api.mixins import APIMixin

import bb_post.services.post

from bb_post.api.serializers.post import PostSerializer
from rest_framework import mixins
from rest_framework import generics


class Collection(mixins.ListModelMixin,
                 generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, parameters, *args, **kwargs):

        form = CreateForm(data=parameters)

        if not form.is_valid():
            raise RequestValidationFailedAPIError(form.errors)

        post = bb_post.services.post.create(**form.cleaned_data)

        return serialize_post(post)


class Single(APIMixin, PostAPIMixin, View):

    def get(self, request, parameters, *args, **kwargs):
        return serialize_post(self.post)
