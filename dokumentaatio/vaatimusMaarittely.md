# Vaatimusmäärittely

## Sovelluksen konsepti ja tarkoitus
Sovellus on simulaatio fysiikasta tutusta _N_-kappaleen ongelmasta (engl. _N_
-body problem). Se käyttää Barnes-Hut-algoritmia diskretisoidakseen tarkastellun
avaruuden quadtree-rakenteen avulla ja approksimoidakseen laskuja mielekkäämmän
laskenta-ajan saavuttamiseksi. Ainakaan alkuvaiheessa sovelluksen _ei ole_
tarkoitus olla fysiikan kannalta hyödyllinen, vaan demonstroida tapaa ja
konseptia, jolla tutkimuksessa käytettyjä simulaatioita rakennetaan.

## Perusversion tarjoama toiminallisuus
### Alkutilanteen lukeminen tiedostosta
* sovellus lukee kappaleiden massat ja sijainnit
tiedostosta, jonka käyttäjä valitsee aloitusnäkymässä
* käyttäjä valitsee tarkkuuden jolla haluaa simulaation suoritettavan sekä
aika-askelten määrän
### Simulaation suorittaminen
#### Yhden aika-askeleen sisällä
* saamansa alkutilanteen datan perusteella sovellus luo quadtree-rakenteen
* quadtreen perusteella sovellus laskee voimat kappaleiden välillä
* kappaleiden sijainteja muutetaan sen perusteella kuinka suuri voima niihin
kohdistuu
* kappaleiden muuttuneet sijainnit talletetaan johonkin tietorakenteeseen
(esim. tiedosto)
* sovellus palaa loopin alkuun ja luo uuden quadtreen edellisestä aika-
askeleesta saadun datan perusteella
### Simulaation suorittamisen jälkeen
* kun simulaatio, eli kaikki aika-askeleet on suoritettu, sovellus antaa
käyttäjälle mahdollisuuden poistua sovelluksesta, tai visualisoida
simulaation
* visualisointi tapahtuu animaationa, jossa kappaleiden paikat esitetään
pisteinä pinnalla jokaisella aika-askeleella

## Jatkokehitysideoita
* ohjelma antaa käyttäjälle simulaation aikana infoa siitä, kuinka monennessa
aika-askeleessa ollaan menossa
* käyttäjä voi graafisesti asetella kappaleita "kartalle"
* kappaleiden nopeudet otetaan huomioon simulaatiossa
* ohjelma laskee alussa laskennallisen vaativuuden simulaatiolla
* datan säilömistä aika-askelten välillä järkevöitetään
* projektin alussa käytetään komentoriviä, myöhemmin toteutetaan graafinen
käyttöliittymä
* laskennallisesti vaativien osien parallellisointi
