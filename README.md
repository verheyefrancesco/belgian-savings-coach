# Belgian Savings Coach

Een verzameling AI-skills die Belgische gezinnen helpt besparen op hun vaste
kosten. Elke skill is een *savings coach* voor één domein (telecom, energie,
verzekeringen, ...): hij brengt de huidige situatie van het gezin in kaart,
vergelijkt geverifieerde alternatieven via officiële Belgische bronnen en rekent
uit wat een overstap echt oplevert.

De skills volgen het formaat van [Claude Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview):
een map met een `SKILL.md` met YAML-frontmatter (`name`, `description`) en de
instructies voor Claude.

## Skills

| Skill | Domein | Status |
|---|---|---|
| [`telecom-savings-coach`](skills/telecom-savings-coach/SKILL.md) | Telecom: mobiel, internet, bundels | MVP |
| _energy-savings-coach_ | Energie: elektriciteit en gas | Idee |
| _insurance-savings-coach_ | Verzekeringen: auto, woning, familiale | Idee |

## Mappenstructuur

```
skills/                    # één map per besparingsdomein
  <domein>-savings-coach/
    SKILL.md               # frontmatter + instructies (verplicht)
    references/            # optioneel: achtergrondinfo die de skill kan inladen
                           # (mag een symlink naar context/ zijn)
context/                   # gedeelde algemene info, één map per domein
  telecom/
    providers.md           # telecomaanbieders actief in België
    affiliate-links.md     # actieve affiliatelinks (leeg zolang er geen programma loopt)
distribution/
  chatgpt/                 # Custom GPT-versie: instructietekst + handleiding
templates/
  SKILL.template.md        # vertrekpunt voor een nieuwe skill
scripts/
  validate_skills.py       # controleert de frontmatter van elke skill
.claude/skills -> ../skills  # zodat Claude Code de skills in deze repo meteen kent
```

## Gebruiken

- **Claude Code:** open deze repo; de skills staan via `.claude/skills` meteen
  ter beschikking.
- **Claude.ai / Claude-app:** zip de map van een skill (bv.
  `skills/telecom-savings-coach/`) en upload hem bij *Settings → Capabilities → Skills*.
- **Persoonlijk in Claude Code:** kopieer de map naar `~/.claude/skills/`.
- **ChatGPT (Custom GPT):** deel de coach met consumenten via één link; zie
  [`distribution/chatgpt/`](distribution/chatgpt/README.md).

## Een nieuwe skill toevoegen

1. Kopieer `templates/SKILL.template.md` naar `skills/<domein>-savings-coach/SKILL.md`
   (bv. `skills/energy-savings-coach/SKILL.md`).
2. Zorg dat `name` in de frontmatter gelijk is aan de mapnaam: kebab-case en
   eindigend op `-savings-coach`. Eén skill per domein; een skill geeft geen advies
   buiten zijn eigen domein.
3. Behoud de gedeelde principes: geen verzonnen prijzen, officiële bronnen eerst,
   aannames expliciet, geen gevoelige persoonsgegevens vragen, onafhankelijk advies.
4. Controleer met `python3 scripts/validate_skills.py`.
5. Voeg de skill toe aan de tabel hierboven.

## Affiliatelinks

Een skill mag affiliatelinks tonen, maar het advies blijft onafhankelijk. Elke
skill rangschikt eerst zonder naar de links te kijken, toont daarna naast de
officiële link eventueel een affiliatelink en meldt dat altijd in het antwoord.
De links staan per domein in `context/<domein>/affiliate-links.md`, zonder
commissiebedragen. Een programma toevoegen = een rij in dat bestand.

Laat vooraf nakijken wat de regels zijn: transparantie is verplicht (Wetboek
van economisch recht), doorverwijzen naar verzekeraars of kredietgevers tegen
vergoeding kan gereglementeerde bemiddeling zijn (FSMA), en bij terugkerende
inkomsten ben je wellicht zelfstandige in bijberoep.

## Controleren

```bash
python3 scripts/validate_skills.py
```

Dezelfde controle draait via GitHub Actions bij elke pull request.
