# N-kappaleen ongelma -simulaatio

Sovellus simuloi usean kappaleen välistä gravitaatiovuorovaikutusta.

**Käytän harjoitustyössä kielenä Pythonia.**

## Dokumentaatio

[vaatimusmäärittelydokumentti](https://github.com/LeeviT/otm-harjoitustyo/blob/master/dokumentaatio/vaatimusMaarittely.md)

[työaikakirjanpito](https://github.com/LeeviT/otm-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[arkkitehtuuridokkari](https://github.com/LeeviT/otm-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Releaset
[viikon 5 release](https://github.com/LeeviT/otm-harjoitustyo/releases/tag/v0.1-alpha)

## Komentorivitoiminnot
### Virtuaaliympäristö
Sovellusta ajetaan (mieluiten) virtuaaliympäristössä _virtualenv_ illä. Sen voit käynnistää projektin juuressa _otm-harjoitustyo/_ komennolla
```
source venv/bin/activate
```

### Testaus
Koodia testataan PyBuilderin avulla (tulee _venv_-kansion mukana). Checkstylen tekeminen _flake8_:lla, sekä yksikkö testien että testauskattavuuden generoiminen tapahtuu komennolla
```
pyb analyze
```
Ensin PyBuilder tulostaa outputissa checkstyle-virheiden määrän. Sitten _unittest_ ajaa yksikkötestit ja _coverage.py_ vielä generoi testauskattavuusraportin. Testauskattavuusraportin voi avata esim. Chromiumilla komennolla 
```
chromium target/reports/coverage_html/index.html 
```
Ja mikäli checkstyle-virheitä on, on checkstyle-raportin polku _target/reports/flake8_.

### Suoritettavan whl:n generointi ja ohjelman suorittaminen
Projektin juuressa eli _otm-harjoitustyo/_ suorita komento 
```
pyb publish
```
jolloin _.whl_-tiedosto generoituu _target_-kansion alakansioon. Voit suorittaa _wheelin_ kommennolla
```
python3.6 target/dist/nbodysim-1.0.dev0/dist/nbodysim-1.0.dev0-py3-none-any.whl 
```

