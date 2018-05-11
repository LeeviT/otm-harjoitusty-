# N-kappaleen ongelma -simulaatio

Sovellus simuloi usean kappaleen välistä gravitaatiovuorovaikutusta.

**Käytän harjoitustyössä kielenä Pythonia.**

## Dokumentaatio

[vaatimusmäärittelydokumentti](https://github.com/LeeviT/otm-harjoitustyo/blob/master/dokumentaatio/vaatimusMaarittely.md)

[työaikakirjanpito](https://github.com/LeeviT/otm-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[arkkitehtuuridokkari](https://github.com/LeeviT/otm-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[sekvenssikaavio](https://github.com/LeeviT/otm-harjoitustyo/blob/master/dokumentaatio/sekvenssikaavio.md)

## Releaset
[viikon 5 release](https://github.com/LeeviT/otm-harjoitustyo/releases/tag/v0.1-alpha)

[viikon 6 release](https://github.com/LeeviT/otm-harjoitustyo/releases/tag/v0.2-alpha)

## Komentorivitoiminnot
### Virtuaaliympäristö
Sovellusta buildataan ja ajetaan (mieluiten) virtuaaliympäristössä _virtualenv_:illä. Mikäli se ei ole asennettuna, voit asentaa sen komennolla
```
pip install virtualenv
```
Virtuaaliympäristön puolestaan voit luoda projektin juuressa _otm-harjoitustyo/_ komennolla
```
virtualenv venv/
```
Ja virtuaaliympäristön aktivoiminen projektin juuressa tapahtuu
```
source venv/bin/activate
```

### Kirjastovaatimukset
Projektin buildaamiseen vaaditaan _pip_:n versiota 10.0.0 alempi versio sekä muutamia Pythonin standardikirjastojen ulkopuolisia kirjastoja. Tarvittavat kirjastot kuten _PyBuilderin_, _numpyn_ yms. saat asennettua aktivoimalla ensin virtuaaliympäristön (ks. yllä) ja sitten suorittamalla projektin juuressa komennon
```
pip install -r requirements.txt
```

### Testaus ja checkstylen tekeminen
Koodia testataan PyBuilderin avulla. Checkstylen tekeminen _flake8_:lla, sekä yksikkö testien että testauskattavuuden generoiminen tapahtuu komennolla
```
pyb analyze
```
Ensin PyBuilder tulostaa outputissa komentoriville checkstyle-virheiden määrän. Sitten _unittest_ ajaa yksikkötestit ja _coverage.py_ vielä generoi testauskattavuusraportin. Testauskattavuusraportin voi avata esim. Chromiumilla komennolla 
```
chromium target/reports/coverage_html/index.html 
```
Ja mikäli checkstyle-virheitä on, on checkstyle-raportin polku _target/reports/flake8_.

### Suoritettavan whl:n generointi ja ohjelman suorittaminen
Projektin juuressa eli _otm-harjoitustyo/_ suorita komento 
```
pyb publish
```
jolloin _.whl_-tiedosto generoituu polkuun _target/dist/nbodysim-1.0.dev0/dist/nbodysim-1.0.dev0-py3-none-any.whl_. Voit suorittaa _wheelin_ kommennolla
```
python3.6 target/dist/nbodysim-1.0.dev0/dist/nbodysim-1.0.dev0-py3-none-any.whl 
```

