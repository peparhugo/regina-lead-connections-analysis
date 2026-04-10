# Population Count Methodology
## Claim: Children on lead service connections
### Method
1 lead service connection = 1 household address.
Children per household = CT children (2021 Census) ÷ CT private dwellings.
Exposed children = connections × children per dwelling.

### Source
- Statistics Canada, 2021 Census of Population, Catalogue 98-316-X2021001
- SewerWaterCondition Lead+PolyB layer (3,692 records), spatially joined to CT boundaries

### Per-neighbourhood calculation

| Neighbourhood | CT | Pb connections | Replaced | Unreplaced | Dwellings (2021) | Children 0-14 (2021) | Children/dwelling | Children at risk | Children prevented |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| North Central | 7050018.00 | 459 | 239 | 220 | 2722 | 1180 | 0.434 | 95 | 104 |
| Cathedral (east) | 7050012.00 | 407 | 227 | 180 | 2695 | 855 | 0.317 | 57 | 72 |
| Cathedral (west) | 7050009.01 | 344 | 136 | 208 | 2000 | 675 | 0.338 | 70 | 46 |
| Heritage | 7050014.00 | 287 | 74 | 213 | 822 | 235 | 0.286 | 61 | 21 |
| North Central (south) | 7050019.00 | 204 | 90 | 114 | 2065 | 835 | 0.404 | 46 | 36 |
| Heritage (north) | 7050010.00 | 185 | 84 | 101 | 1654 | 415 | 0.251 | 25 | 21 |
| Old Lakeview | 7050005.00 | 140 | 44 | 96 | 1927 | 695 | 0.361 | 35 | 16 |
| Cathedral (south) | 7050008.01 | 137 | 50 | 87 | 2709 | 845 | 0.312 | 27 | 16 |
| Warehouse District | 7050017.00 | 112 | 76 | 36 | 950 | 455 | 0.479 | 17 | 36 |
| Downtown | 7050011.00 | 67 | 7 | 60 | 3277 | 180 | 0.055 | 3 | 0 |
| McNab | 7050022.01 | 56 | 10 | 46 | 1204 | 460 | 0.382 | 18 | 4 |
| Eastview | 7050020.00 | 55 | 18 | 37 | 1548 | 685 | 0.443 | 16 | 8 |
| Ross Industrial | 7050013.00 | 41 | 1 | 40 | 487 | 30 | 0.062 | 2 | 0 |
| Rosemont | 7050003.00 | 15 | 5 | 10 | 2384 | 935 | 0.392 | 4 | 2 |
| Centre Square | 7050015.00 | 9 | 0 | 9 | 931 | 385 | 0.414 | 4 | 0 |
| **TOTAL** | | **2,760** | **1,212** | **1,548** | | | | **480** | **382** |

### Verification
```python
# Reproduce: children_at_risk = sum(unreplaced × children_per_dwelling) across CTs
# Result: 480 at risk, 382 prevented
```

### Limitations
- 2021 Census demographics applied uniformly across all dwellings in a CT. Lead-connected homes (pre-1960) may have different household composition.
- CT 0004.00 (Al Ritchie) was split into three CTs in 2021. Demographics were merged back, which includes newer suburban development.
- 1 connection may serve multiple units in duplexes/fourplexes — this would undercount exposed children.
