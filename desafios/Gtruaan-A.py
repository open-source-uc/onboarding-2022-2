# Por Gtruaan

def cursed_multiply(a, b):
    '''
    Multiplica numeros a y b, con cierto error
    '''
    import requests

    return 10**(float(requests.request("GET", f"https://newton.now.sh/api/v2/log/10|{a}").json()["result"]) +
    float(requests.request("GET", f"https://newton.now.sh/api/v2/log/10|{b}").json()["result"]))

print(cursed_multiply(7, 9))
