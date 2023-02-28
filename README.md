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