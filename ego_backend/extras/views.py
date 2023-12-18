from rest_framework.generics import ListAPIView
from .models import Activity, Financing
from .serializers import ActivitySerializer, FinancingSerializer

# Activity View
class ActivityListAPIView(ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

# Financing View
class FinancingListAPIView(ListAPIView):
    queryset = Financing.objects.all()
    serializer_class = FinancingSerializer