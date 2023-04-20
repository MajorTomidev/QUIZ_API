from django.urls import path
from .views import AllQuestions, RandomQuestion, CourseQuestion

urlpatterns = [
    path('course/<str:topic>/', CourseQuestion.as_view(), name='coursequestionapi'),
    path('random/<str:topic>/', RandomQuestion.as_view(), name='randomapi' ),
    path('', AllQuestions.as_view(), name='allquestionsapi'),
    
]