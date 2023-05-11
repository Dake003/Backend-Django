from django.shortcuts import render, redirect


def main(request):

    return render(request, 'Main/base.html')
def detail(request):

    return render(request, 'Main/details.html')

def loginpage():
    return None


def cartpage():
    return None


def man():
    return None


def woman():
    return None