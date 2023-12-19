from django.shortcuts import render
from django.shortcuts import redirect, reverse
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.db.models import Q
from django.core.mail import send_mail
from django.http import JsonResponse
import json
from . import app

def student_profile_genetator_api(request):
    if request.method == "POST":
        try:
            received_data = json.loads(request.body.decode('utf-8'))
            profile_data = received_data.get('profileData')
            predicted_cata=app.main(profile_data)
            response_data = {
                'message': 'Data received and processed successfully',
                'predicted_cata':predicted_cata
                }
            
            
            return JsonResponse(response_data)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
        res = {'message': 'Hey N0'}
        return JsonResponse(res)





