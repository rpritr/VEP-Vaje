# Uporaba varne komunikacije

📅 **Trajanje: 2 uri**


Vsakodnevno komuniciramo prek elektronske pošte in sporočilnih aplikacij, vendar večina teh komunikacij ni zaščitena pred prisluškovanjem. Šifriranje sporočil omogoča, da vsebino vidijo samo pošiljatelj in prejemnik, s čimer varujemo zasebnost in zmanjšamo možnost kraje osebnih podatkov.

V tej vaji bomo praktično uporabili šifrirano e-pošto (PGP) in aplikacijo Signal za šifrirano sporočanje.


# 🧪 Uporaba varne komunikacije

Šifriranje je postopek pretvorbe besedila v neberljivo obliko (ciphertext), ki jo lahko dešifrira le pooblaščeni prejemnik.


## 1️⃣ Uvod: Varno komuniciranje

Cilj vaje je:  
✅ razumeti pomen šifriranja komunikacije. 
✅ ustvariti in uporabiti PGP ključ za šifrirano e-pošto. 
✅ uporabiti aplikacijo Signal za šifrirano sporočanje. 
✅ spoznati osnovne pojme: šifriranje, javni in zasebni ključ, digitalni podpis. 

### Šifriranje in varnost

#### Simetrično šifriranje
Uporablja en sam ključ za šifriranje in dešifriranje. Primer: AES.

#### Asimetrično šifriranje
Uporablja par ključev: javni in zasebni ključ.  
- Javni ključ deliš z drugimi.
- Zasebni ključ hraniš zase.  
Če ti nekdo pošlje šifrirano sporočilo z uporabo tvojega **javnega ključa**, ga lahko dešifriraš le ti z **zasebnim ključem**.  
PGP (Pretty Good Privacy) temelji na tem principu.

#### Digitalni podpis
S svojim zasebnim ključem podpišeš sporočilo. Prejemnik z javnim ključem preveri, da si ga res ti poslal.


## 2️⃣ Aktivnost: Šifrirana komunikacija v kibernetskem prostoru
### 🔷 Del A: Šifrirana e-pošta

✅ možnost 1: Thunderbird
1. Namesti [Thunderbird](https://www.thunderbird.net/) in nastavi svoj e-poštni račun.
2. V meniju pojdi na **Nastavitve šifriranja/OpenPGP** in ustvari nov ključni par.
3. Izvozi svoj javni ključ in ga pošlji kolegu.
4. Uvozi kolegov javni ključ.
5. Napiši in pošlji šifrirano in podpisano sporočilo kolegu.

✅ možnost 2: ProtonMail
1. Ustvari brezplačen račun na [ProtonMail](https://protonmail.com).
2. Prijavi se in omogoči šifriranje.
3. Pošlji šifrirano sporočilo kolegu.

---

### 🔷 Del B: Signal

1. Namesti Signal iz Google Play/Apple App Store.
2. Registriraj svojo številko.
3. Povabi kolega v pogovor.
4. Pošljita si nekaj sporočil.
5. Odprite **Varnostne podatke (safety number)** in preverita, ali sta pravilno usklajena.

---

### 📝 Analiza in poročilo

- Kakšne so prednosti uporabe šifrirane komunikacije?

## 3️⃣ Refleksija in analiza

- Kako bi razložili razliko med šifriranim in nešifriranim sporočilom? Zakaj je šifriranje pomembno?
- Kako bi svojim prijateljem ali sodelavcem priporočili, da zaščitijo svojo komunikacijo? Bi jim svetovali uporabo PGP, Signala, ali česa drugega? Zakaj?
- Ali menite, da bi morale biti šifrirane oblike komunikacije bolj razširjene tudi v vsakdanjem življenju? Zakaj da/ne?