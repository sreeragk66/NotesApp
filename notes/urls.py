from django.urls import path
from notes import views

urlpatterns=[
    path("",views.NoteCreateView.as_view(),name="home"),
    path("add",views.NoteCreateView.as_view(),name="home"),
    path("display",views.NoteDisplayView.as_view(),name="display"),
    path("update/<int:note_id>",views.NoteEditView.as_view(),name="update"),
    path("remove/<int:note_id>",views.DeleteNote,name="remove")
]