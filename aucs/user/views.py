from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .models import CleanupReport, User
from .serializers import CleanupReportSerializer,UserSerializer
from .task import cleanup_inactive_users
from rest_framework.pagination import PageNumberPagination


def health_check(request):
    return JsonResponse({"status": "ok"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def latest_report(request):
    report = CleanupReport.objects.last()
    if report:
        return Response(CleanupReportSerializer(report).data)
    return Response({"message": "No reports found"}, status=404)

@api_view(['GET'])
def all_reports(request):
    reports = CleanupReport.objects.all().order_by('-id') 
    
    if not reports.exists():
        return Response({"message": "No reports found"}, status=404)
    
    # Set up pagination
    paginator = PageNumberPagination()
    paginator.page_size = 10  # number of items per page
    paginated_reports = paginator.paginate_queryset(reports, request)
    
    # Serialize paginated data
    serializer = CleanupReportSerializer(paginated_reports, many=True)
    
    # Include total count in response
    response_data = {
        "totalCount": reports.count(),
        "page": paginator.page.number,
        "pageSize": paginator.page.paginator.per_page,
        "totalPages": paginator.page.paginator.num_pages,
        "results": serializer.data,
    }
    return Response(response_data)



@api_view(['GET'])
def users(request):
    users = User.objects.all()
    if users:
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    return Response({"message": "No users found"}, status=404)


@api_view(['POST'])
def trigger_cleanup(request):
    cleanup_inactive_users.delay()
    return Response({"message": "Cleanup task triggered"})

@api_view(['POST'])
def register(request):
    email = request.data.get("email")
    password = request.data.get("password")
    if not email or not password:
        return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)

    user = User(email=email)
    user.set_password(password)  
    user.save()

    return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)