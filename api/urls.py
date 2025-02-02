
from django.urls import path
from .views import CareerSuggestionView, UserProfileView, ProtectedView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

urlpatterns = [
    path('suggestions/', CareerSuggestionView.as_view(), name='career_suggestions'),
    path('user-profile/', UserProfileView.as_view(), name='user_profile'),
    path('protected/', ProtectedView.as_view(), name='protected'),
]
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You have access to this protected view!"})