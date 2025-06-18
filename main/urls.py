from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
from .views import LogoutGetView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutGetView.as_view(), name='logout'),  # Allows GET logout


    # CRUD
    path('notes/', NoteListView.as_view(), name='note_list'),
    path('notes/new/', NoteCreateView.as_view(), name='note_create'),
    path('notes/<int:pk>/edit/', NoteUpdateView.as_view(), name='note_edit'),
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
    
]
