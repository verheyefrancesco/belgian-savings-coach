# CLAUDE.md

Richtlijnen voor Claude Code (claude.ai/code) bij het werken in deze repository.

## Project

**Belgian Savings Coach**: een AI-setup die Belgische gezinnen helpt besparen.
De repo bevat Claude Skills: per besparingsdomein (telecom, later energie,
verzekeringen, ...) één *savings coach* die de situatie van het gezin in kaart
brengt, geverifieerde alternatieven vergelijkt en de besparing uitrekent.

Er is (nog) geen applicatiecode: de "code" zijn de skill-instructies in Markdown.

## Mappenstructuur

- `skills/<naam>/SKILL.md`: één map per skill. Frontmatter met `name` (gelijk aan
  de mapnaam, kebab-case) en `description` (wanneer Claude de skill gebruikt).
  Optioneel `references/` voor achtergrondinfo die de skill kan inladen.
- `context/<domein>/`: gecentraliseerde algemene info die skills delen (bv.
  `context/telecom/providers.md`). Afspraken staan in `context/README.md`.
- `templates/SKILL.template.md`: vertrekpunt voor een nieuwe skill.
- `scripts/validate_skills.py`: valideert de frontmatter van alle skills.
- `.claude/skills` is een symlink naar `skills/`, zodat Claude Code de skills in
  deze repo meteen laadt. Leg skills dus altijd in `skills/`, niet in `.claude/`.
- `.github/workflows/validate-skills.yml`: draait de validatie bij elke PR.

## Commando's

- Valideren: `python3 scripts/validate_skills.py` (alleen standaardbibliotheek,
  niets te installeren). Draai dit na elke wijziging aan een skill.

## Werkafspraken

- Communiceer met de eigenaar in het **Nederlands**.
- Code, identifiers, commitberichten en skill-instructies in het Engels, tenzij
  anders afgesproken. De skills zelf antwoorden in de taal van de gebruiker
  (minstens Nederlands en Engels).
- Houd rekening met de Belgische context: bedragen in euro (€ 1.234,56), Belgische
  datumnotatie (dd/mm/jjjj) en Belgische fiscale regels rond sparen.
- Elke skill volgt dezelfde principes: nooit prijzen, voorwaarden of bronnen
  verzinnen; officiële Belgische bronnen eerst (bv. BIPT/bestetarief.be voor
  telecom, CREG/VREG voor energie); aannames expliciet; geen gevoelige
  persoonsgegevens vragen; geen gepersonaliseerd beleggingsadvies; onafhankelijk
  van commissies.
- Nieuwe skill: kopieer de template, voeg hem toe aan de tabel in `README.md` en
  laat de validatie slagen.
