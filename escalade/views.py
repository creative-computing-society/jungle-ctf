#To be implemented when the project is done
# 404 page

from django.shortcuts import render
def page_not_found_view(request, exception):
    return render(request, 'game/404.html', status=404)
