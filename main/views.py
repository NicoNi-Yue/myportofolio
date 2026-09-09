from django.shortcuts import render

from main.models import Experience


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