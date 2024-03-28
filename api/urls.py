from django.urls import path
from .views import FormSubmitView, FormPageView,index

urlpatterns = [
    path('submit/', FormSubmitView.as_view(), name='submit'),
    path('form-page/', FormPageView.as_view(), name='form_page'),
    path('',index)
]
