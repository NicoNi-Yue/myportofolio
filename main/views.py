from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Education, Project
from main.forms import ProjectForm, ExperienceForm


def show_main(request):
    context = {
        "name": "Nicholas",
        "npm": "2506537165",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada dunia game development dan pendidikan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Nicholas",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "experience baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Nicholas",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def edit_experience(request, id):
    # Retrieve/recall objek yang mau di-update berdasarkan ID
    experience = get_object_or_404(Experience, pk=id)

    if request.method == "POST":
        # Pass instance=experience supaya Django tahu ini UPDATE, bukan ADD
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('main:show_experience')
    else:
        # Isi form dengan data awal dari objek tersebut
        form = ExperienceForm(instance=experience)

    context = {
        'form': form,
        'experience': experience,
    }
    return render(request, 'experience_form.html', context)

def show_education(request):
    context = {
        "name": "Nicholas",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Nicholas",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Nicholas",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def edit_project(request, id):
    # Retrieve/recall objek yang mau di-update berdasarkan ID
    project = get_object_or_404(Project, pk=id)

    if request.method == "POST":
        # Pass instance=project supaya Django tahu ini UPDATE, bukan ADD
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('main:show_projects')
    else:
        # Isi form dengan data awal dari objek tersebut
        form = ProjectForm(instance=project)

    context = {
        'form': form,
        'project': project,
    }
    return render(request, 'projects_form.html', context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")