# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError


# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


# def hello(request):
#     return HttpResponse("Happy I")

def send_email(request):
    subject = request.POST.get('subject', 'hullalal')
    message = request.POST.get('message', 'hey there')
    from_email = request.POST.get('happyshandilya@gmail.com', 'ok')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['happyshandilya@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')