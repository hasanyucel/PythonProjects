from twocaptcha import TwoCaptcha
solver = TwoCaptcha('62bb86c9bba1329fb3e04e9d126c3071')

def captch_solve(path):
    result = solver.normal('captchas/2.png')
    return result

def get_balance():
    balance = solver.balance()
    return balance