# N-kappaleen ongelma -simulaatio

Sovellus simuloi usean kappaleen v�listägravitaatiovuorovaikutusta.

**Käytän harjoitustyössä kielenä Pythonia.**

## Dokumentaatio

[vaatimusmäärittelydokumentti](https://github.com/LeeviT/otm-harjoitustyo/blob/master/dokumentaatio/vaatimusMaarittely.md)

[työaikakirjanpito](https://github.com/LeeviT/otm-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

## Komentorivitoiminnot
### Virtuaaliymp�ristö
Sovellusta ajetaan (mieluiten) virtuaaliymp�rist�ssä_virtualenv_ill�. Sen voit k�ynnist�� projektin juuressa _otm-harjoitustyo/_ komennolla
```
source venv/bin/activate
```

### Testaus
Koodia testataan PyBuilderin avulla (tulee _venv_-kansion mukana). Checkstylen tekeminen _flake8_:lla, sekäyksikk�testien ettätestauskattavuuden generoiminen tapahtuu komennolla
```
pyb analyze
```
Ensin PyBuilder tulostaa outputissa checkstyle-virheiden m��r�n. Sitten _unittest_ ajaa yksikk�testit ja _coverage.py_ viel� generoi testauskattavuusraportin. Testauskattavuusraportin voi avata esim. Chromiumilla komennolla 
```
chromium target/reports/coverage_html/index.html 
```
Ja mik�li checkstyle-virheit� on, löytyycheckstyle-raportin polku _target/reports/flake8_.

### Ohjelman suorittaminen
Toistaiseksi _.egg_iäei ole vielägeneroitavissa, joten ohjelma suoritetaan yksinkertaisesti komennolla
```
python3.6 src/main/python/mainDao/__main__.py 
```

Koodiin toteutettiin input-tiedoston lukemiseen tarvittava luokka, simulaation kappaleita kuvaavaa luokka, sekä luokka
joka rakentaa quadtreen adaptiivisesti lisättävien kappaleiden pohjalta. Tämän hetken toteutuksessa tosin luodaan kolme
testikappaletta joiden perusteella ohjelma luo quadtreen ja lopuksi printtaa kaikki olemassa olevat nodet. Koodin itse
tekninen toteutus on edistynyt suht. aikataulun mukaisesti ja ensi viikolla graafista käyttöliittymää lukuunottamatta
koodi lienee täysin käyttövalmis.

Projekti luotiin PyBuilder-projektina virtualenvillä, eli kyseessä on Maven-tyylinen projekti. PyBuilder ei lähtenyt
kuitenkaan toimimaan edes tuskallisten tuntien jälkeen (ei löydä esim. moduulia/kansiota src/), joten tällä hetkellä
koodi ja ainoa testi on ajettavissa vain PyCharmilla (tai vastaavalla IDEllä). PyCharmilla avataan suoraan kansio
/otm-harjoitustyo ja asetetaan se PyCharmin asetuksista content rootiksi (ellei ole jo). Nyt quadtree.py kansiossa
/src/main/python/structures/ on suoritettavissa Run-napista kuten myös testi firstTest.py kansiossa
/src/unittest/python/.
