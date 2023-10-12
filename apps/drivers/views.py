from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import Driver
from .serializers import DriverLocationSerializer

class DriverLocationUpdateView(APIView):
    """
    Update driver location.
    """
    @swagger_auto_schema(request_body=DriverLocationSerializer)
    def patch(self, request, pk=None):
        try:
            driver = Driver.objects.get(pk=pk)
        except Driver.DoesNotExist:
            return Response({"detail": "Driver not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DriverLocationSerializer(driver, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)