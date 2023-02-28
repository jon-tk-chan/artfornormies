# Artfornormies
Generate data visualizations - Pypi version

## Instructions:

1. Install: 
```
pip install artfornormies
```

2. Generate a visual using one of the listed functions:
```
from artfornormies import functions as art

#
out_name = "example_venn.png"
fig = art.create_venn_2()
fig.write_image(out_name)
```

TO DO - AUTHOR:
- Rework readme - add explanations
    - add docs for each fn
    - Add images for each banner
- explore test for each fn
- refactor colorscheme variables
- 