import socket
import os
print(""" 


|NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN|
|NNNNNNNNNNNNNNNNNNNNNNmdhyyssyyhdmNNNNNNNNNNNNNNNNNNNNNN|
|NNNNNNNNNNNNNNNNNmho:.            .:ohmNNNNNNNNNNNNNNNNN|
|NNNNNNNNNNNNNNms:`                    `:smNNNNNNNNNNNNNN|
|NNNNNNNNNNNNm+`                          `+mNNNNNNNNNNNN|
|NNNNNNNNNNmo` `::`    ``........``    `::` `omNNNNNNNNNN|
|NNNNNNNNNd-`/+m+   ..``` `````` ```..   +m+/.-dNNNNNNNNN|
|NNNNNNNNd.-m/ys. .` `-```.-/+/-```-` `. .sy/m-.dNNNNNNNN|
|NNNNNNNm.h+dys.`.   .   .`-:oy`.   .   .`.syh+h.mNNNNNNN|
|NNNNNNN/:N+sy:`.```..`  .  .-  .  `..```.`:ys+N:/NNNNNNN|
|NNNNNNm`:msd/ .    .  ``-``++``-``  .    . /dsm:`mNNNNNN|
|NNNNNNy-y+y+/``    .    .--ss--.    .    ``/+s+y-yNNNNNN|
|NNNNNNy`moom``.````-/+oyds +o sdyo+/-````.``moom`yNNNNNN|
|NNNNNNd-/dd/o .    +NNNNN+ ss +NNNNN+    . o/dd/-dNNNNNN|
|NNNNNNN-hos/m`.` ``sNNNNNm.hh.mNNNNNs`` `.`m/soh-NNNNNNN|
|NNNNNNNy`ydoN:+.`  dNNNNNNmmmmNNNNNNd  `.+:Nody`yNNNNNNN|
|NNNNNNNNo/+oh+ho```NNNNNNNNNNNNNNNNNN.``od+ho+/oNNNNNNNN|
|NNNNNNNNNo:yys+m+o+NNNNNNNNNNNNNNNNNN+o+mosyy:oNNNNNNNNN|
|NNNNNNNNNNh.:sssy+hNNNNNNNNNNNNNNNNNNh+ysss:.hNNNNNNNNNN|
|NNNNNNNnNNNmo-+shhhyysmNNNNNNNNNNmsyyhhhs+-omNNNNNNNNNNN|
|NNNNNNNNNNNNNms::+oyhdNNNNNNNNNNNNdhyo+::smNNNNNNNNNNNNN|
|NNNNNNNNNNNNnNNNds:. `NNNNNNNNNNNN. .:sdNNNNNNNNNNNNNNNN|
|NNNNNNNNNNNNNNNNNNNNmhNNNNNNNNNNNNhdNNNNNNNNNNNNNNNNNNNN|
|NNNNNNNNNNNNNNNNNNNNNN ☭ 𐌋σgαя ☭ NNNNNNNNNNNNNNNNNNNNNN|
|NN Uyarı Türkçe ifadeler girilmez mesela; ş,İ,ö, gibi NN|
|NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN|

""")
ad = input("Kullanıcı adın nedir>> ")
soket = socket.socket()
host = input("Ngrok link gir>> ")
port = int(input("Ngrok port gir>> "))
soket.connect((host,port))
while True:
    data = str(soket.recv(1024))[1:]
    if data:
        print("Karsi taraf: {}".format(data))
        respond = input(ad+": ").encode("utf-8")
        if respond == b"C":
            exit()
        else:
            soket.sendall(bytes(respond))