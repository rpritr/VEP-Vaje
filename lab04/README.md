# Upravljanje osebnih identitet

📅 **Trajanje: 2 uri**

V digitalnem svetu so osebne identitete eden izmed ključnih elementov, ki omogočajo našo prisotnost in delovanje v kibernetskem prostoru. Gesla in prijavni podatki so pogosto edina ovira med našimi podatki in morebitnim napadalcem, zato je pravilno ravnanje z njimi ključno za varnost posameznika. 

Žal je uporaba šibkih, ponavljajočih se gesel in zanemarjanje dodatnih varnostnih mehanizmov, kot je dvofaktorska avtentikacija (MFA), še vedno pogosta praksa med uporabniki, kar predstavlja veliko tveganje.


# 🧪 Upravljanje osebnih identitet

V tej vaji se bomo naučili osnovnih tehnik za varno upravljanje osebnih identitet v kibernetskem prostoru. 

Namen te vaje je, da se študentje naučimo osnovnih dobrih praks pri upravljanju osebnih identitet. V prvem delu bomo spoznali, kako ustvariti kompleksna in varna gesla, ter jih ocenili z namenskimi orodji. V drugem delu bomo izvedli praktično nastavitev MFA na priljubljenih storitvah, kot sta Gmail ali Slack, in spoznali, kako dodatni varnostni koraki bistveno zmanjšajo možnosti za uspešen napad. Vaja naslavlja tako tehnični kot tudi osebnostni vidik odgovornega ravnanja z identitetami v kibernetskem prostoru.

## 1️⃣ Uvod: Upravljanje osebnih identitet

Cilj je, da se kot uporabniki naučimo kako:
✅ ustvariti varna gesla,  
✅ preveriti njihovo kompleksnost in odpornost na napade,  
✅ nastaviti dvofaktorsko avtentikacijo (MFA) za boljšo zaščito računov.

### Osebne identitete in varna gesla

Vsak uporabnik interneta v kibernetskem prostoru nastopa s svojo osebno identiteto. To so vsi podatki, ki vas identificirajo pri uporabi spletnih storitev: uporabniška imena, e‑poštni naslovi, gesla, varnostna vprašanja, profilne slike, telefonske številke, celo vedenjski vzorci. 

Naša identiteta je pogosto razpršena čez veliko različnih platform, zato je njeno varovanje zahtevno, a izjemno pomembno. Zloraba osebne identitete lahko vodi do kraje podatkov, dostopa do bančnih računov, širjenja lažnih informacij v našem imenu ali celo izsiljevanja.

Najpogostejši način za zaščito svoje identitete so še vedno gesla, ki so prva obrambna linija pred nepooblaščenim dostopom. Žal raziskave kažejo, da uporabniki pogosto uporabljajo prekratka gesla, preprosta zaporedja znakov ali enaka gesla na več storitvah. To napadalcem omogoča, da z metodo slovarjev (dictionary attack), z grobo silo (brute force) ali z že razkritimi podatkovnimi bazami hitro pridobijo dostop. Zato morajo biti gesla dovolj dolga, nepredvidljiva, sestavljena iz velikih in malih črk, številk in posebnih znakov. Še bolje je, če za vsako storitev uporabljamo drugo geslo in si pri tem pomagamo z upravljalnikom gesel.

Pomembno je tudi razumeti, da nobeno geslo ni popolnoma varno, če ga ne spremljajo dodatni varnostni mehanizmi. Zato vedno, ko je mogoče, vključimo dvofaktorsko avtentikacijo (MFA), ki doda še en sloj zaščite — npr. enkratno kodo, ki jo prejmemo na telefon ali ustvarimo z aplikacijo. Tako postane napad na račun bistveno težji, saj napadalec potrebuje še nekaj, kar imamo fizično pri sebi.

## 2️⃣ Aktivnost: Uporaba Bitwarden generatorja in ocenjevalnika varnosti gesel

### 🔐 Password Generator

Na strani **Password Generator** nastavite različne parametre in za vsako nastavitev ustvarite eno geslo.  
Gesla sproti kopirajte in jih zapišite na list ali v dokument.

### ✅ Primeri, ki jih morate ustvariti

| Geslo | Dolžina       | Znakovni nabor                          |
|-------|---------------|-----------------------------------------|
| G1    | 8 znakov      | samo črke (male in velike)              |
| G2    | 12 znakov     | črke + številke                         |
| G3    | 16 znakov     | črke + številke + posebni znaki         |
| G4    | 24 znakov     | vse možno                               |
| G5    | Passphrase    | 4 besede (ločene s presledki ali pomišljaji) |

Vsako od zgornjih gesel preverite na strani **Password Strength Tester**.
Za vsako geslo si zapišite oceno:

barvni indikator (npr. rdeč, oranžen, zelen)

približno število let za razbitje (če je prikazano)

### 📝 Analiza in poročilo

Za vsako geslo si zabeležite:
- Ustvarjeno geslo.
- Katere nastavitve ste izbrali.
- Je geslo varno za uporabo in kaj bi spremenili, da bi bilo še bolj varno?

## 3️⃣ Refleksija in analiza

- Kako se povečuje ocena varnosti, ko dodajate dolžino?
- Kako vplivajo posebni znaki na oceno?
- Kako se ocenjuje “passphrase” v primerjavi s klasičnim geslom?
- Katero geslo bi priporočili za vsakodnevno uporabo in zakaj?
