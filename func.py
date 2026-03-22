from datetime import datetime

def today():
    today = datetime.now()
    return 

today()


def verify_due(date_ref):
    if today() > date_ref:
        return True
    else:
        return False
    