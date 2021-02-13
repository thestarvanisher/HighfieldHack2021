from django.core.paginator import Paginator


def get_objects(Model, page):
    objects = Model.objects.all()

    paginator = Paginator(objects, 25)

    page = paginator.get_page(page)

    return page, paginator


def get_page(request):
    current_page = request.GET.get("p", "")

    if current_page == "":
        current_page = 1
    else:
        current_page = int(current_page)
        current_page = max(current_page, 1)

    return current_page
