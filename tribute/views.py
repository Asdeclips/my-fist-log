from django.shortcuts import render

def post_list(request):
    return render(request, 'tribute/post_list.html', {})