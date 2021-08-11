from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'dashboard/index.html')


def alert(request):
    return render(request,'dashboard/alert.html')


def button(request):
    return render(request,'dashboard/button.html')


def badge(request):
    return render(request,'dashboard/badges.html')


def pagination(request):
    return render(request,'dashboard/pagination.html')


def card(request):
    return render(request,'dashboard/card.html')


def collapse(request):
    return render(request,'dashboard/collapse.html')


def carousel(request):
    return render(request,'dashboard/carousel.html')


def grid(request):
    return render(request,'dashboard/grid.html')


def progress(request):
    return render(request,'dashboard/progress.html')


def modal(request):
    return render(request,'dashboard/modal.html')


def spinner(request):
    return render(request,'dashboard/spinner.html')


def tabs(request):
    return render(request,'dashboard/tabs.html')


def typography(request):
    return render(request,'dashboard/typography.html')


def tooltip(request):
    return render(request,'dashboard/tooltip.html')


def toast(request):
    return render(request,'dashboard/toast.html')


def form(request):
    return render(request,'dashboard/form_elements.html')


def table(request):
    return render(request,'dashboard/tbl_bootstrap.html')


def chart(request):
    return render(request,'dashboard/chart-apex.html')


def map(request):
    return render(request,'dashboard/map-google.html')


def login(request):
    return render(request,'dashboard/auth-signin.html')


def register(request):
    return render(request,'dashboard/auth-signup.html')