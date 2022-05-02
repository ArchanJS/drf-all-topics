from rest_framework.throttling import UserRateThrottle

class ModRateThrottle(UserRateThrottle):
    scope='mod'