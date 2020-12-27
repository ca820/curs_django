from django.shortcuts import render, redirect
from django.views import View

from babysitter.forms import CustomerForm
from babysitter.models import Customer
from babysitter.util import save_customer


class IndexView(View):
    #запрос GET. Отдаём пользователю статичную страничку
    @staticmethod
    def get(request):
        return render(request, 'babysitter/index.html')



    # Запрос POST. Получаем от пользователя данные и сохраняем в БД
    @staticmethod
    def post(request):
        form = CustomerForm(request.POST)
        customer = Customer()

        if form.is_valid():
            save_customer(form, customer)

            return redirect('index_url')

