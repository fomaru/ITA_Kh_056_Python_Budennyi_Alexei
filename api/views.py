from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class IndexView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'index': 'placeholder'}
        return Response(content)