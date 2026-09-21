from django.urls import path

from main.views import (
    show_main, 
    show_experience, 
    show_education, 
    show_projects, 
    create_project, 
    create_experience,
    get_projects_json, 
    edit_project,
    edit_experience,
    delete_project,
    delete_experience,
    )

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("projects/add/", create_project, name="create_project"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path('edit-experience/<uuid:id>/', edit_experience, name='edit_experience'),
    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
    path("projects/", show_projects, name="show_projects"),
    path("education/", show_education, name="show_education"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path('edit-project/<uuid:id>/', edit_project, name='edit_project'),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project")
]