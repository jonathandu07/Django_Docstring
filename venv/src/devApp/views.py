from django.shortcuts import render
from django_user_agents.utils import get_user_agent

def dev(request):
    user_agent = get_user_agent(request)
    is_mobile = user_agent.is_mobile
    is_tablet = user_agent.is_tablet
    is_desktop = not (is_mobile or is_tablet)

    context = {
        'is_mobile': is_mobile,
        'is_tablet': is_tablet,
        'is_desktop': is_desktop
    }
    return render(request, 'dev/index.html', context)
