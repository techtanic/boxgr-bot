import random
from time import sleep

import requests
from bs4 import BeautifulSoup as bs
from RandomWordGenerator import RandomWord


def gen():
    word = RandomWord(max_word_size = 7).generate()+str(random.randint(0, 9))+str(random.randint(0, 9))
    word = word.lower()
    email = word+"@zetmail.com"

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'DNT': '1',
        'Host': 'account.cosmote.gr',
        'Origin': 'https://account.cosmote.gr',
        'Referer': 'https://account.cosmote.gr/register?nakedRegister&chid=foodboxweb&alt-theme=third-party',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {"username-autofill": "","password-autofill": "","csm-email": email,"csm-name": "fVictor","csm-surname": "fbrown","csm-password": "TECHTANIC#8090","csm-recovery-asset": "free@techtanic.com","csm-mail": "free@techtanic.com"}

    s = requests.session()
    s.get("https://account.cosmote.gr/el/register?nakedRegister&chid=foodboxweb&alt-theme=third-party")
    cosmote="https://account.cosmote.gr/register?p_p_id=Cosmoteid_INSTANCE_ElwamDfwl07C&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=registerUserNaked&p_p_cacheability=cacheLevelPage"
    s.post(url=cosmote, data = data, headers = headers)

    sleep(1)

    token = []
    while token == []:
        token = s.get(f"https://getnada.com/api/v1/inboxes/{email}").json()
        token = token["msgs"]
    token=token[0]["uid"]

    html = s.get(f"https://getnada.com/api/v1/messages/html/{token}").content
    print(html)
    soup = bs(html,"html5lib")
    url = soup.find("a",attrs={'id': 'emailSubmitImageUrl'})['href']

    s.get(url)
    data = {"IDToken1": f"{email}","IDToken2": "TECHTANIC#8090","realm": "hub","goto": "https://account.cosmote.gr/user-login","gotoOnFail": "https://account.cosmote.gr/user-login?p_p_id=CosmoteLogin_INSTANCE_XQ2b6cwTiH8w&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_CosmoteLogin_INSTANCE_XQ2b6cwTiH8w_loginError=true&channelLoginError=true&chid=ACCOUNTS&"}
    s.post("https://idmextsso.ote.gr/opensso/OTECloudLogin", data = data)
    #verify
    s.get("https://box.gr/")

    data = {"IDToken1": f"{email}","IDToken2": "TECHTANIC#8090","realm": "hub","goto": "https%3A%2F%2Fidmextsso.cosmote.gr%2Fauth%2Frealms%2Fhub%2Fprotocol%2Fopenid-connect%2Fauth%3Fresponse_type%3Dcode%26scope%3Dopenid%26client_id%3Dboxweb%26redirect_uri%3Dhttps%3A%2F%2Fbox.gr%2Flogin","gotoOnFail": "https://account.cosmote.gr/el/modalloginextended?p_p_id=CosmoteModalLoginExtended&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_CosmoteModalLoginExtended_fullPageRedirect=true&_CosmoteModalLoginExtended_loginError=true"}
    headers ={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "DNT": "1",
        "Host": "idmextsso.ote.gr",
        "Origin": "https://box.gr",
        "Referer": "https://box.gr/",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70"}
    s.post("https://idmextsso.ote.gr/opensso/OTECloudLogin",data = data, headers = headers)
    ###
    r = s.get("https://idmextsso.ote.gr/opensso/OTECloudLogin?target=https%3A%2F%2Fidmextsso.cosmote.gr%2Fauth%2Frealms%2Fhub%2Fprotocol%2Fopenid-connect%2Fauth%3Fresponse_type%3Dcode%26scope%3Dopenid%26client_id%3Dboxweb%26redirect_uri%3Dhttps%3A%2F%2Fbox.gr%2Flogin&realm=hub&stage=1")

    #data = {"address":[{"type":"Σπίτι","latitude":"38.04623159999999","longitude":"23.8183371","city":"Μαρούσι","streetNo":"75","street":"Μεσογείων","region":"Περιφερειακή ενότητα Βορείου Τομέα Αθηνών","postalCode":"15126","floor":"2","nameAtBell":"γιαννης","comments":"null","firstName":"fVictor","lastName":"fbrown"}]}

    return email

