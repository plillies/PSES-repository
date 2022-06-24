# This is the urls.py in the repository app

from django.urls import path # same imports as in main repository. Needed here ?
from repository import views

app_name="repository"

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('about/', views.about.as_view(), name='about'),
    path('demographicresults/', views.demographicresults.as_view(), name='demographicresults'),
    path('departmentalresults/', views.departmentalresults.as_view(), name='departmentalresults'),
    path('intersectionalresults/', views.intersectionalresults.as_view(), name='intersectionalresults'),
    path('overallresults/', views.overallresults.as_view(), name='overallresults'),
    path('warranty/', views.warranty.as_view(), name='warranty'),
#   You need to have a template view (as_view) in order for {{}} to pull in querysets
#   A template view requires appropriate coding in views.py

    path('demographicresults/download_file/', views.download_file, name='download_file'),
    path('intersectionalresults/download_file/', views.download_file, name='download_file'),
#   Pages with forms need a download function that is defined in views.py
]