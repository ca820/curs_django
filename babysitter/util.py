
def save_customer(customer, form):
    """сохраняем валидированные данные из формы в экземпляр объекта Customer"""
    if form.cleaned_data:
        cd = form.cleaned_data
        customer.email = cd['email']
        customer.phone = cd['phone']
        customer.count_children = cd['count_children']
        customer.date = cd['datetime'].date()
        customer.time = cd['datetime'].time()
        customer.save()
    else:
        return print(False)
