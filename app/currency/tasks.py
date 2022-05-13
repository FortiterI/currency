import requests
from decimal import Decimal
from celery import shared_task
from bs4 import BeautifulSoup
import currency.model_choises as mch


def round_decimal(value: str) -> Decimal:
    places = Decimal(10) ** -2
    return Decimal(value).quantize(places)


@shared_task
def pars_privatbank():
    from currency.models import Rate, Source

    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()
    source = Source.objects.get_or_create(code_name=mch.SourceCodeName.PRIVATBANK)[0]
    available_currencies = {
        'BTC': mch.RateType.BTC,
        'USD': mch.RateType.USD,
        'EUR': mch.RateType.EUR,
        'UAH': mch.RateType.UAH
    }

    for rate in rates:
        if rate['ccy'] not in available_currencies:
            continue

        base_currency_type = available_currencies.get(rate['base_ccy'])
        currency_type = rate['ccy']
        buy = round_decimal(rate['buy'])
        sale = round_decimal(rate['sale'])
        # try:
        #     source = Source.objects.get(code_name=mch.SourceCodeName.PRIVATBANK)
        # except Source.DoesNotExist:
        #     source = Source.objects.create(code_name=mch.SourceCodeName.PRIVATBANK)

        last_rate = Rate.objects.filter(source=source, currency_type=currency_type).order_by('-created').first()

        if (last_rate is None   # if rates does not exist in tables
                or last_rate.sale != sale or last_rate.buy != buy):
            Rate.objects.create(
                currency_type=currency_type,
                base_type=base_currency_type,
                buy=buy,
                sale=sale,
                source=source,
            )


@shared_task
def pars_monobank():
    from currency.models import Rate, Source

    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()
    source = Source.objects.get_or_create(code_name=mch.SourceCodeName.MONOBANK)[0]

    available_currencies = {
        840: mch.RateType.USD,
        978: mch.RateType.EUR,
        980: mch.RateType.UAH
    }

    for rate in rates:
        if rate['currencyCodeA'] not in available_currencies:
            continue
        base_currency_type = available_currencies.get(rate['currencyCodeB'])
        currency_type = available_currencies.get(rate['currencyCodeA'])
        buy = round_decimal(rate['rateBuy'])
        sale = round_decimal(rate['rateSell'])

        last_rate = Rate.objects.filter(source=source, currency_type=currency_type, base_type=base_currency_type).\
            order_by('-created').first()

        if (last_rate is None  # if rates does not exist in tables
                or last_rate.sale != sale or last_rate.buy != buy):
            Rate.objects.create(
                currency_type=currency_type,
                base_type=base_currency_type,
                buy=buy,
                sale=sale,
                source=source,
            )


@shared_task
def pars_vkurse():
    from currency.models import Rate, Source

    url = 'http://vkurse.dp.ua/course.json'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()
    source = Source.objects.get_or_create(code_name=mch.SourceCodeName.VKURSE)[0]
    available_currencies = {
        'Dollar': mch.RateType.USD,
        'Euro': mch.RateType.EUR,
    }

    for rate in rates:
        if rate not in available_currencies:
            continue

        base_currency_type = mch.RateType.UAH
        currency_type = rate
        buy = round_decimal(rates[rate]["buy"])
        sale = round_decimal(rates[rate]["buy"])

        last_rate = Rate.objects.filter(source=source, currency_type=currency_type).order_by('-created').first()

        if (last_rate is None   # if rates does not exist in tables
                or last_rate.sale != sale or last_rate.buy != buy):
            Rate.objects.create(
                currency_type=currency_type,
                base_type=base_currency_type,
                buy=buy,
                sale=sale,
                source=source,
            )

