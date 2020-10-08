#!/usr/bin/env python3
import random

players = ['Fede', 'Flavio', 'Giovanni', 'Nico', 'Fabio', 'Ettore', 'Edo', 'Simo']

calciatori = {
    'portieri': [
        ['Szczesny','Donnarumma','Handanovic','Gollini','Strakosha','Silvestri','Mirante','Meret'],
        ['Musso','Sirigu','Consigli','Dragowski','Sepe','Skorupski','Cragno','Audero']
    ],
    'difensori': [
        ['Gosens','Hernandez T.','Hakimi','Acerbi','Koulibaly','De Vrij','De Ligt','Hateboer'],
        ['Milenkovic','Faraoni','Manolas','Bonucci','Criscito','Spinazzola','Romagnoli','Di Lorenzo'],
        ['Bastoni','Cuadrado','Smalling','N\'Koulou','Kolarov','Toloi','Alex Sandro','Chiellini',
        'Kumbulla','Ibanez','Mancini','Palomino','Tomiyasu','Romero','Godin','Djimsiti'],
        ['Young','Kjaer','Pezzella Ger.','Ferrari G.','Colley','Maksimovic','D\'Ambrosio','Izzo',
        'Gagliolo','Vojvoda','Caldirola','Toljan','Gunter','Stryger Larsen','Rodriguez R.','Lirola',
        'Skriniar','Bruno Peres','De Silvestri','Radu','Biraghi','Letizia','Ouwejan','Calabria','Yoshida',
        'Kyriakopoulos','Glik','Luiz Felipe','Nuytinck','Ceppitelli','Bruno Alves','Ansaldi']
    ],
    'centrocampisti': [
        ['Gomez','Kulusevski','Chiesa','Luis Alberto','Calhanoglu','Mkhitaryan','De Paul','Milinkovic-Savic'],
        ['Nainggolan','Vidal','Pasalic','Malinovskyi','Veretout','Castrovilli','Arthur','Eriksen'],
        ['Ruiz','Miranchuk','Pellegrini Lo.','Soriano','Ramirez','Bonaventura','Locatelli','Bentancur'],
        ['Djuricic','De Roon','Diaz B.','Zielinski','Brozovic','Pulgar','Verdi','Politano'],
        ['Miguel Veloso','Castillejo','Lazzari','Sensi','Barella','Kessie\'','Zaccagni','Callejon','Lazovic',
        'Barak','Linetty','Freuler','Perisic','Pereyra','Kucka','Zaniolo','Nandez','Elmas','Zajc','Jankto',
        'Verre','Kurtic','Pereiro','Amrabat','Tonali','Rabiot','Gagliardini','Bernardeschi','Diawara','Gojak',
        'Hernani','Bennacer']
    ],
    'attaccanti': [
        ['Ronaldo','Immobile','Lukaku','Zapata D.','Caputo','Ibrahimovic','Martinez L.','Belotti'],
        ['Dybala','Dzeko','Berardi','Muriel','Mertens','Joao Pedro','Rebic','Ilicic'],
        ['Osimhen','Pedro','Insigne','Morata','Barrow','Quagliarella','Correa','Ribery'],
        ['Boga','Simeone','Vlahovic','Lozano','Caicedo','Kouame\'','Inglese','Sanchez'],
        ['Rafael Leao','Orsolini','Lapadula','Destro','Pavoletti','Okaka','Simy','Lasagna',
        'Caprari','Kalinic','Carles Perez','Bonazzoli','Gervinho','Keita B.','Muriqi','Galabinov']
    ]
}

rose = { p:{ r:[] for r in calciatori } for p in players }
for role in calciatori:
    for tier in calciatori[role]:
        for i, c in enumerate(tier):
            if i % len(players) == 0:
                random.shuffle(players)
            rose[players[i % len(players)]][role].append(c)

print(str(rose))
