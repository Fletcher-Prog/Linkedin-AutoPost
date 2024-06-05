import requests

url = "https://app.magicpost.in/signup"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://app.magicpost.in/signup",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://app.magicpost.in",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
}

cookies = {
    "_gcl_au": "1.1.857268770.1716992813",
    "_ga_5GH8V6JV0R": "GS1.1.1717595052.3.1.1717595226.58.0.157783593",
    "_ga": "GA1.1.1503998300.1716992813",
    "_fbp": "fb.1.1716992813910.2131107125",
    "_clck": "1sdpdta|2|fm7|0|1610",
    "session": ".eJwtT8tOAzEM_JXI5wou5bJHigSCpeINEqoiK-vNRpvHkjhUatV_x93lZHs8Mx4fQfcey0AFmu8jKJYCgUpBS7CCJ09YSPlklYuKk0JjZKl4cEVNwrmA3Wm3EpNMZYCmR19IxolywEhR7DhXQWxK1pNOWHnQhZEJGmjN-2HNH2nf_n5uXnjcOryZ7sftw2F954Kcr4WyzmRS7rTrRCF9udq3gerPF1_f2uczicMGw4TOxpnRU87oNWc0o4v2n5Eiz3HgcgEeqXM1yJyyxejMgr6mms052pJ3Ad_kmVl4-gMoBGh2.ZmBr4g.sXp1BB3OPLMYjaWfUTw9i4vPpdY",
    "heroku-session-affinity": "ACyDaANoA24IAaLV//3///8HYgAJFG9iAAVgq2EBbAAAAAFtAAAABXdlYi4xaiIieAOo2YuuoOqiTR75VCJ7MkIt",
}

data = {
    "email"   : "yevoh37883@jahsec.com",
    "password": "folot64743@hutov.com",
    "timezone": "Europe/Paris",
}

response = requests.post(url, headers=headers, cookies=cookies, data=data)

print( response.status_code )
print( response.text )
print( response.cookies["session"])

for cookies in response.cookies :
    print ( f" {cookies.name} : {cookies.value}" )

