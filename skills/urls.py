from django.urls import path
from skills import views

urlpatterns = [
    path('skills/',views.list_skills),
    path('skills/create/',views.create_skill),
    path('freelancer/skills/add/',views.add_user_skill),
    path('freelancer/skills/remove/<int:id>/',views.remove_user_skill),
    path('freelancer/<int:user_id>/skills/',views.freelancer_skills),
]
