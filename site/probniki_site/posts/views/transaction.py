from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.views import View


class TransactionView(View):
    def get(self, request):
        return render(request, 'transaction.html')

    def post(self, request):
        number = request.POST.get('number')
        with transaction.atomic():
            row1 = Row.objects.get(id=1)
            row2 = Row.objects.get(id=2)
            row1.number += int(number)
            row2.number -= int(number)
            row1.save()
            row2.save()
        return HttpResponse("Transaction completed successfully")
