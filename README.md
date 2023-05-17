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

fig = art.create_venn_2(
    venn_labels=["What feels like a waste of time",
                "What you'll regret not doing in 10 years",
                "That personal project that makes you feel like yourself"
                ],
    main_title="",
    fill_venn=True,
    night_mode=True
)

fig.write_image("images/ex_plot.png")
```
![Example Plot](images/ex_plot.png)

## References

Artfornormies was built on top of Plotly visualization libaray: [Plotly - Python Documentation](https://plotly.com/python/)

TO DO - AUTHOR:
- Rework readme - add explanations
    - add docs for each fn
    - Add images for each banner
- explore test for each fn
- refactor colorscheme variables
- 