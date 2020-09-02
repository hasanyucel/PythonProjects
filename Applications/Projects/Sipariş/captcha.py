from twocaptcha import TwoCaptcha
solver = TwoCaptcha('62bb86c9bba1329fb3e04e9d126c3071')

def captcha_solve(path): #captchanın yolunu alır.
    result = solver.normal(path)
    return result.get("code")

def get_balance(): #apide kalan bakiyeyi getirir.
    return solver.balance()