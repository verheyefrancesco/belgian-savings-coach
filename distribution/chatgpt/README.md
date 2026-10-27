# Telecom Savings Coach als Custom GPT (ChatGPT)

Zo zet je de telecomcoach op als Custom GPT, zodat consumenten hem met één link
kunnen gebruiken, zonder een prompt te kopiëren.

> **Let op (stand 27/10/2026):** volgens meerdere berichten stopt OpenAI op
> 11/12/2026 met Custom GPTs en vervangt het ze door *plugins*; bestaande GPTs
> zijn dan om te zetten via *My GPTs → Migrate to plugin* (instructies worden een
> skill, knowledge-bestanden gaan mee, deelinstellingen niet). Controleer de
> actuele situatie in de OpenAI Help Center voor je hier tijd in steekt.
> Een GPT *maken* vraagt een betaald abonnement; *gebruiken* kan gratis.

> De schermen van ChatGPT veranderen geregeld. Heten knoppen anders, zoek dan
> naar de equivalenten: *Instructions*, *Knowledge*, *Capabilities* en *Share*.

## Wat je nodig hebt

- Een **betaald ChatGPT-abonnement** (Plus of hoger) om een GPT te *maken*.
  Gebruikers met een gratis account kunnen hem wel *gebruiken* (met lagere limieten).
- Deze bestanden uit de repo:

| Waar in de GPT | Bestand |
|---|---|
| Instructions (plakken) | [`telecom-savings-coach-instructions.md`](telecom-savings-coach-instructions.md) |
| Knowledge (uploaden) | [`skills/telecom-savings-coach/SKILL.md`](../../skills/telecom-savings-coach/SKILL.md) |
| Knowledge (uploaden) | [`context/telecom/providers.md`](../../context/telecom/providers.md) |
| Knowledge (uploaden) | [`context/telecom/affiliate-links.md`](../../context/telecom/affiliate-links.md) |

Het veld *Instructions* is beperkt tot 8.000 tekens; de volledige skill is
langer. Daarom staat de kern in de instructietekst en gaat de volledige
werkwijze mee als knowledge-bestand. Upload de bestanden met hun originele naam:
de instructietekst verwijst naar `SKILL.md`, `providers.md` en `affiliate-links.md`.

## Stappen

1. Ga naar [chatgpt.com/gpts/editor](https://chatgpt.com/gpts/editor), of in
   ChatGPT naar **GPTs → + Create**.
2. Kies het tabblad **Configure** (niet *Create*: dat is een chatassistent die
   je tekst zelf herschrijft).
3. Vul in:
   - **Name:** `Telecom Besparingscoach België`
   - **Description:** `Onafhankelijke check of je gezin kan besparen op internet, tv en gsm. Vergelijkt geverifieerde Belgische aanbiedingen en rekent je besparing uit.`
   - **Instructions:** plak de volledige inhoud van
     `telecom-savings-coach-instructions.md`.
   - **Conversation starters:**
     - `Betaal ik te veel voor internet en tv?`
     - `Kan ons gezin besparen op gsm-abonnementen?`
     - `Check mijn volledige telecompakket`
     - `Am I paying too much for telecom in Belgium?`
4. **Knowledge:** upload de drie bestanden uit de tabel hierboven.
5. **Recommended model:** kies een model met redeneervermogen als die optie er
   is; de vergelijking en berekeningen hebben er baat bij.
6. **Capabilities:**
   - **Web Search: aan.** Onmisbaar: zonder webzoeken kan de coach geen actuele
     prijzen controleren.
   - **Code Interpreter & Data Analysis:** aan (optioneel). Handig om de
     berekeningen na te rekenen.
   - **Image Generation** en **Canvas:** uit; niet nodig.
7. **Actions:** niets toevoegen.
8. Onder **Additional settings**: zet *Use conversation data in your GPT to
   improve our models* uit als je dat niet wilt voor de gesprekken van je gebruikers.
9. Geef de GPT een eenvoudig icoon (bv. een spaarvarken of een gsm). Gebruik
   geen logo's van telecomaanbieders.
10. Test eerst in het **Preview**-venster rechts (zie [Testen](#testen)).
11. Klik op **Create** of **Update** en kies wie hem mag gebruiken:
    - **Only me:** om eerst zelf te testen.
    - **Anyone with the link:** om te delen via je website, sociale media of nieuwsbrief.
    - **GPT Store:** vindbaar voor iedereen. Daarvoor moet je builderprofiel
      geverifieerd zijn (naam of eigen domein, via *Settings → Builder profile*).

## Testen

Speel een paar gesprekken na in het Preview-venster, in het Nederlands en het
Engels, en controleer:

- [ ] Begint hij met de categorievraag en stelt hij genummerde meerkeuzevragen?
- [ ] Noemt hij geen aanbieders of prijzen vóór je de samenvatting bevestigd hebt?
- [ ] Zoekt hij op bestetarief.be en de officiële sites, met datum en bronlinks?
- [ ] Toont hij besparing in jaar 1 en besparing per jaar daarna apart?
- [ ] Vermenigvuldigt hij een promoprijs van 6 maanden niet met 12?
- [ ] Eindigt hij met het standaard eindrapport?
- [ ] Weigert hij netjes vragen over energie of verzekeringen?
- [ ] Gebruikt hij niets uit eerdere chats (ChatGPT-geheugen)?

## Bijwerken

De GPT werkt met een kopie van de bestanden: een wijziging in de repo komt er
niet vanzelf in. Na een wijziging aan de skill of de contextbestanden:

1. Open de GPT via **GPTs → My GPTs → bewerken**.
2. Vervang de gewijzigde knowledge-bestanden (oud verwijderen, nieuw uploaden).
3. Plak de instructietekst opnieuw als die gewijzigd is.
4. Klik op **Update**. De link blijft dezelfde.

Komt er een affiliateprogramma bij, upload dan het bijgewerkte
`affiliate-links.md` opnieuw.

## Goed om te weten

- Het verbruik loopt via het ChatGPT-account van de gebruiker; jij betaalt niets per gesprek.
- Je ziet de gesprekken van je gebruikers niet; OpenAI verwerkt ze volgens zijn
  eigen voorwaarden. Vermeld dat in de uitleg bij je link.
- Zet bij het delen een korte disclaimer, bv.: *"De coach geeft indicatieve
  informatie. Controleer prijzen en voorwaarden altijd bij de aanbieder of op
  bestetarief.be."* Werk je later met affiliatelinks, vermeld dat dan ook.
- Gebruikers kunnen de instructies soms uit een GPT lospraten. Dat is hier geen
  probleem: de werkwijze is publiek in deze repo.
