# Context

Gecentraliseerde, algemene achtergrondinformatie die over skills heen gedeeld
wordt: marktoverzichten, aanbieders, regelgeving, officiële bronnen, ...

## Structuur

```
context/
  <domein>/          # bv. telecom, energie, verzekeringen
    <onderwerp>.md   # één onderwerp per bestand
```

| Domein | Bestanden |
|---|---|
| `telecom/` | [`providers.md`](telecom/providers.md): telecomaanbieders actief in België<br>[`affiliate-links.md`](telecom/affiliate-links.md): actieve affiliatelinks (leeg zolang er geen programma loopt) |

## Afspraken

- Alleen feitelijke, controleerbare informatie, met bron en datum van laatste
  controle bovenaan elk bestand.
- Officiële Belgische bronnen eerst (bv. BIPT/bestetarief.be voor telecom,
  CREG/VREG voor energie).
- Geen prijzen hier: die veranderen te snel en horen live geverifieerd te worden.
- Geen commissiebedragen in `affiliate-links.md`: wat de skill niet leest, kan
  zijn advies ook niet sturen.
- Onzeker of niet bevestigd? Markeer het expliciet (`?`) in plaats van te gokken.
- Een skill neemt een contextbestand mee via een symlink in
  `skills/<naam>/references/`. Hernoem of verplaats je een bestand, pas dan ook
  die link aan (de validatie vangt kapotte links op).
- Skill-specifieke info blijft in `skills/<naam>/references/`; wat meerdere
  skills nodig hebben, hoort hier.
