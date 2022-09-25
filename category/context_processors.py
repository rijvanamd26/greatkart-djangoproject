from .models import Category

def menu_links(request):
    links=Category.objects.all()
    #stores links in links variable
    return dict(links=links)