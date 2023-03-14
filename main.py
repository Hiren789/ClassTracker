import requests,time
bot_token = "5864748291:AAFn_GXCM_eNdAeFmXlDZhxvf6KLFMYD-bU"
group_chat_id = "-1001849130325"

def sendtxt(teext):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": group_chat_id, "text": teext}
    response = requests.post(url, data=data)

def single(classno):
    url = f"https://eadvs-cscc-catalog-api.apps.asu.edu/catalog-microservices/api/v1/search/classes?keywords={classno}&refine=Y&campusOrOnlineSelection=A&honors=F&level=grad&promod=F&searchType=open&subject=IFT&term=2237"
    s = requests.Session()
    s.headers.update({'Authorization': 'Bearer null'})
    r = s.get(url)
    k = r.json()
    return k["classes"][0]["seatInfo"]["ENRL_CAP"]-k["classes"][0]["seatInfo"]["ENRL_TOT"]

clsno = 75407

while True:
    k = single(clsno)
    if k != 0:
        sendtxt(k)
    time.sleep(5)