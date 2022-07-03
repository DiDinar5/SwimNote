from django.http import HttpResponse
from django.template import loader
from athletes.models import Athlete,PersonalBest
def index(request):
    all = Athlete.objects.order_by('birthday')[:]
    template = loader.get_template('index.html')
    context = {
        'athletes': all,
    }
    #str = ', '.join([a.name for a in all])
    return HttpResponse(template.render(context, request))




