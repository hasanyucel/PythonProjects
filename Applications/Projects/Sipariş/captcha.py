from twocaptcha import TwoCaptcha
solver = TwoCaptcha('62bb86c9bba1329fb3e04e9d126c3071')

def captcha_solve(path):
    result = solver.normal(path)
    return result.get("code")

def get_balance():
    balance = solver.balance()
    return balance

# print(get_balance())
# a = captcha_solve("30.png")
# print(a)
