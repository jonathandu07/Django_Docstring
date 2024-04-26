from django.shortcuts import render
import re
# Create your views here.
def dev(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    is_mobile = bool(re.search('Mobi', user_agent))
    return render(request, 'dev/index.html', {'is_mobile': is_mobile})