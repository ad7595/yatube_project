from django.http import HttpResponse


# Create your views here.
def group_posts(request, slug):
    return HttpResponse(f'Сгруппированные посты {slug}')


def index(request):
    return HttpResponse('Главная страница')
# Create your views here.
