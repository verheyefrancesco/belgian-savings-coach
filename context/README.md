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
| `telecom/` | [`providers.md`](telecom/providers.md): telecomaanbieders actief in België |

## Afspraken

- Alleen feitelijke, controleerbare informatie, met bron en datum van laatste
  controle bovenaan elk bestand.
- Officiële Belgische bronnen eerst (bv. BIPT/bestetarief.be voor telecom,
  CREG/VREG voor energie).
- Geen prijzen hier: die veranderen te snel en horen live geverifieerd te worden.
- Onzeker of niet bevestigd? Markeer het expliciet (`?`) in plaats van te gokken.
- Skill-specifieke info blijft in `skills/<naam>/references/`; wat meerdere
  skills nodig hebben, hoort hier.
