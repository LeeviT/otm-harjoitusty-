# OTM-harjoitustyö

**Käytän harjoitustyössä kielenä Pythonia.**

[vaatimusmäärittelydokumentti](https://github.com/LeeviT/otm-harjoitustyo/blob/master/dokumentaatio/vaatimusMaarittely.md)

[työaikakirjanpito](https://github.com/LeeviT/otm-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

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