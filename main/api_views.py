from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Education, Experience, Project
from main.permissions import IsPortfolioOwnerOrEditorOrReadOnly
from main.serializers import EducationSerializer, ExperienceSerializer, ProjectSerializer


def collection_view(request, model, serializer_class, search_field="title", prefetch=()):
    if request.method in ("GET", "HEAD"):
        queryset = model.objects.all()
        if prefetch:
            queryset = queryset.prefetch_related(*prefetch)
        query = request.query_params.get("title", "").strip()
        if query:
            queryset = queryset.filter(**{f"{search_field}__icontains": query})
        serializer = serializer_class(queryset.order_by("title", "id"), many=True,
                                      context={"request": request})
        return Response(serializer.data)
    serializer = serializer_class(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


def detail_view(request, model, serializer_class, object_id):
    obj = get_object_or_404(model, pk=object_id)
    if request.method in ("GET", "HEAD"):
        return Response(serializer_class(obj, context={"request": request}).data)
    if request.method == "DELETE":
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = serializer_class(obj, data=request.data, partial=request.method == "PATCH",
                                  context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def project_list(request):
    return collection_view(request, Project, ProjectSerializer, prefetch=("starred_by",))


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def project_detail(request, project_id):
    return detail_view(request, Project, ProjectSerializer, project_id)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def project_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if project.starred_by.filter(pk=request.user.pk).exists():
        project.starred_by.remove(request.user)
    else:
        project.starred_by.add(request.user)
    return Response(ProjectSerializer(project, context={"request": request}).data)


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def experience_list(request):
    return collection_view(request, Experience, ExperienceSerializer)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def experience_detail(request, experience_id):
    return detail_view(request, Experience, ExperienceSerializer, experience_id)


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def education_list(request):
    return collection_view(request, Education, EducationSerializer)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def education_detail(request, education_id):
    return detail_view(request, Education, EducationSerializer, education_id)
