from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import Vendor
from .serializers import VendorSerializer, UserSignupSerializer
from rest_framework.permissions import IsAuthenticated 
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User



# Create your views here.
class VendorListCreateView(ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]

    # Override perform_create to associate the vendor with the logged-in user
    def perform_create(self,serializer):
        # Automatically associate the vendor with the logged-in user
        serializer.save(user=self.request.user)

#  --- Fetches Onboarded users ---
class OnboardedVendorListView(ListAPIView):
    queryset = Vendor.objects.filter(is_onboarded=True)
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated] #Authenticates users


#  ---- Vendor Detail View ----
class VendorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]


#  ---- Signup View ----
class UserSignupView(CreateAPIView):
    serializer_class = UserSignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # --- Automatically log in the user after signup ---
        login(request, user)

        return Response({
            "message": "Signup successful",
            "user": {
                "full_name": user.get_full_name(), # ---storing full name ---
                "email": user.email,
            }
        }, status=status.HTTP_201_CREATED)


#  ---- Login View ----
class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get("email")

        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Log the user in (creates a session)
        login(request, user)

        return Response({
            "message": "Login successful",
            "user": {
                "full_name": user.get_full_name(),
                "email": user.email
            }
        }, status=status.HTTP_200_OK)


#  ---- Logout View ----
class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request) # This will clear the session
        return Response({
            "message": "Logged out successfully"
        }, status=status.HTTP_200_OK)