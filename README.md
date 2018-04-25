# N-kappaleen ongelma -simulaatio

Sovellus simuloi usean kappaleen v�list� gravitaatiovuorovaikutusta.

**K�yt�n harjoitusty�ss� kielen� Pythonia.**

## Dokumentaatio

[vaatimusm��rittelydokumentti](https://github.com/LeeviT/otm-harjoitustyo/blob/master/dokumentaatio/vaatimusMaarittely.md)

[ty�aikakirjanpito](https://github.com/LeeviT/otm-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[arkkitehtuuridokkari](https://github.com/LeeviT/otm-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Releaset
[viikon 5 release](https://github.com/LeeviT/otm-harjoitustyo/releases/tag/v0.1-alpha)

## Komentorivitoiminnot
### Virtuaaliymp�rist�
Sovellusta ajetaan (mieluiten) virtuaaliymp�rist�ss� _virtualenv_ ill�. Sen voit k�ynnist�� projektin juuressa _otm-harjoitustyo/_ komennolla
```
source venv/bin/activate
```

### Testaus
Koodia testataan PyBuilderin avulla (tulee _venv_-kansion mukana). Checkstylen tekeminen _flake8_:lla, sek� yksikk� testien ett� testauskattavuuden generoiminen tapahtuu komennolla
```
pyb analyze
```
Ensin PyBuilder tulostaa outputissa checkstyle-virheiden m��r�n. Sitten _unittest_ ajaa yksikk�testit ja _coverage.py_ viel� generoi testauskattavuusraportin. Testauskattavuusraportin voi avata esim. Chromiumilla komennolla 
```
chromium target/reports/coverage_html/index.html 
```
Ja mik�li checkstyle-virheit� on, on checkstyle-raportin polku _target/reports/flake8_.

### Suoritettavan whl:n generointi ja ohjelman suorittaminen
Projektin juuressa eli _otm-harjoitustyo/_ suorita komento 
```
pyb publish
```
jolloin _.whl_-tiedosto generoituu _target_-kansion alakansioon. Voit suorittaa _wheelin_ kommennolla
```
python3.6 target/dist/nbodysim-1.0.dev0/dist/nbodysim-1.0.dev0-py3-none-any.whl 
```

