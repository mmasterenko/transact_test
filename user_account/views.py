from decimal import Decimal

from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import F
from .forms import UserAccountForm
from .models import UserAccount


def home(request):
    form = UserAccountForm()
    context = {'form': form}
    return render(request, 'user_account/home.html', context=context)


def validate(request):
    """
    request POST: user_id, summa, inns
    """
    error = {'status': 'error', 'msg': ''}

    user_id = request.POST.get('user_id')
    summa = request.POST.get('summa')
    inns = request.POST.get('inns')

    if user_id in (None, ''):
        error.update(msg='Укажите пользователя')
        return JsonResponse(error)

    if summa in (None, ''):
        error.update(msg='Введите сумму')
        return JsonResponse(error)

    user = UserAccount.objects.get(pk=user_id)
    if user.account < Decimal(summa):
        error.update(msg='Не достаточно средств. Остаток: %s' % user.account)
        return JsonResponse(error)

    if inns in (None, ''):
        error.update(msg='Введите ИНН пользователей')
        return JsonResponse(error)

    users_qs = UserAccount.objects.filter(inn__in=inns.split())
    if not users_qs.exists():
        error.update(msg='Пользователей с такими ИНН не существует: %s' % ','.join(inns.split()))
        return JsonResponse(error)

    ok = {'status': 'ok'}
    return JsonResponse(ok)


def do_transact(request):
    """
    request POST: user_id, summa, inns
    """

    user_id = request.POST.get('user_id')
    summa = request.POST.get('summa')
    inns = request.POST.get('inns')

    user = UserAccount.objects.get(pk=user_id)
    user.account = F('account') - Decimal(summa)
    user.save()

    users_qs = UserAccount.objects.filter(inn__in=inns.split())
    one_share = Decimal(summa) / len(users_qs)
    for payee in users_qs:
        payee.account = F('account') + one_share
        payee.save()

    ok = {'status': 'ok'}
    return JsonResponse(ok)
