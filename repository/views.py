from django.shortcuts import render
from django.views.generic import TemplateView # TemplateView is a set of class methods, not a function
# So in urls.py we have to point the URL to the as_view() class method

from .models import Results
from django.http.response import HttpResponse

# Create your views here.

class home(TemplateView):
    template_name = 'home.html'

# class demographicresults(TemplateView):
#   template_name = 'demographicresults.html'

class about(TemplateView):
    template_name = 'about.html'

class departmentalresults(TemplateView):
    template_name = 'departmentalresults.html'
    def get_context_data(self, **kwargs):
        context = super(departmentalresults, self).get_context_data(**kwargs)
        # below's the difference that allows querysets to be pulled in with {{ }}. views.py must aslo be set to as_view
        context['files'] = Results.objects.all().order_by('code') # Orders department links alpahbetically
        return context

class intersectionalresults(TemplateView):
    template_name = 'intersectionalresults.html'
    def get_context_data(self, **kwargs):
        context = super(intersectionalresults, self).get_context_data(**kwargs)
        # below's the difference that allows querysets to be pulled in with {{ }}. views.py must aslo be set to as_view
        context['files'] = Results.objects.all()
        return context

class overallresults(TemplateView):
   template_name = 'overallresults.html'
   def get_context_data(self, **kwargs):
       context = super(overallresults, self).get_context_data(**kwargs)
       # below's the difference that allows querysets to be pulled in with {{ }}. views.py must aslo be set to as_view
       context['files'] = Results.objects.all()
       return context

class warranty(TemplateView):
    template_name = 'warranty.html'

class demographicresults(TemplateView):
   template_name = 'demographicresults.html'
   def get_context_data(self, **kwargs):
       context = super(demographicresults, self).get_context_data(**kwargs)
       # below's the difference that allows querysets to be pulled in with {{ }}. views.py must aslo be set to as_view
       context['files'] = Results.objects.filter(filter='0')
       return context

def download_file(request):
    # fill these variables with real values that appear in intersectionalresults.html
    filename = request.GET.get('downloaded_file_name')
    fl_path = 'data/data/' + filename

    fl = open(fl_path, 'rb')
#    mime_type, _ = mimetypes.guess_type(fl_path) # Not needed if mime_type is known (ms-excel)
    response = HttpResponse(fl, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="%s"' % filename # printf-style formatting
    return response
