from django.db import models
from django.utils.translation import ugettext as _


class RequestStatuses(models.IntegerChoices):
    PENDING = 0, _('در انتظار')
    CONFIRMED = 1, _('تایید شده')
    REJECTED = 2, _('رد شده')


class RequestTypes(models.IntegerChoices):
    REFERRER_VISIT_REWARD = 0
    REFERRER_SIGNUP_REWARD = 1
    REFERRER_PURCHASE_REWARD = 2
    PURCHASE_REWARD = 3
    BUY_FROM_NAKHLL = 4
    WITHDRAW = 5
    DEPOSIT = 6
    FUND_TO_BANK = 7


COIN_RIAL_RATIO = 100_000
WITHDRAW_BALANCE_LIMIT = 21
SYSTEMIC_ACCOUNTS_ID_UPPER_LIMIT = 0
BANK_ACCOUNT_ID = -1
FUND_ACCOUNT_ID = -2
CASHABLE_REQUEST_TYPES = [
    RequestTypes.REFERRER_VISIT_REWARD,
    RequestTypes.REFERRER_SIGNUP_REWARD,
    RequestTypes.REFERRER_PURCHASE_REWARD,
    RequestTypes.PURCHASE_REWARD,
]
AUTOMATIC_CONFIRM_REQUEST_TYPES = [
    RequestTypes.REFERRER_VISIT_REWARD,
    RequestTypes.REFERRER_SIGNUP_REWARD,
    RequestTypes.REFERRER_PURCHASE_REWARD,
    RequestTypes.PURCHASE_REWARD,
]