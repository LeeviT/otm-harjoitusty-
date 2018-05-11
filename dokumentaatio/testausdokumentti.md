# Testausdokumentti
Ohjelmaa on testattu Pythonin automaattisilla _unittest_-testeillä sekä manuaalisilla järjestelmätesteillä kolmessa eri käyttöjärjestelmässä.
## Yksikkötestaus 
### Sovelluslogiikka 
Automatisoidut yksikkötestit edustavat pääasiassa ohjelman "ydintä", eli quadtreen rakentamiseen liittyviä metodeja sekä datan lukemista input-tiedostosta. Testit sisältävät myös integraatiotestaamista eli luokkien käyttämistä jonkin toisen luokan kanssa. Testit sijaitsevat tiedostossa [nbodysim_tests.py](https://github.com/LeeviT/otm-harjoitustyo/blob/master/src/unittest/python/nbodysim_tests.py). Testien tekeminen ja testauskattavuusraportin generoiminen on kuvattu [README](https://github.com/LeeviT/otm-harjoitustyo/blob/master/README.md)ssä.
### Testauskattavuus
Rivitestauskattavuus on noin 58% luokkaa (prosentit tulostuvat komentoriville), sillä en onnistunut jättämään pois graafisen käyttöliittymän luokkia testauskattavuuden generoinnista pitkällisenkään konffaamisen jälkeen. Mikäli GUI-luokat jättäisi pois, olisi rivitestauskattavuus noin 70% luokkaa ja sinällään riittävähkö.
## Järjestelmätestaus
Sovelluksen järjestelmätestaus suoritettiin manuaalisesti.
### Asennus ja konffaaminen
Sovellus on ladattu ja asennettu kolmeen eri ympäristöön (Ubuntu, Arch Linux ja Windows 10 Bash) [README](https://github.com/LeeviT/otm-harjoitustyo/blob/master/README.md)n kuvaamalla tavalla. 
### Toiminallisuudet 
Sovellusta on myös testattu antamalla virheellisiä syötteitä ensimmäisen käyttöliittymänäkymän aikana. Virheelliset syötteet kuitenkin kaatavat sovelluksen eikä kunnon error handlingia ole toteutettu.
