from django.shortcuts import render

# Create your views here.
from django.views import View

from driver.models import Advice


class Home(View):
    def get(self, request):
        weeks_advice = Advice.objects.filter(weeks_advice=True).latest(field_name="created_date")
        if not weeks_advice:
            weeks_advice = Advice.objects.latest(field_name="created_date")
        advices_not_passed = Advice.objects.exclude(passed=request.user).exclude(weeks_advice)
        context = {'weeks_advice': weeks_advice, 'advices_not_passed': advices_not_passed}
        return render(request, 'driver/home.html', context)