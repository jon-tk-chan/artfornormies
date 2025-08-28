import plotly.graph_objects as go
# from io import BytesIO #TEST IF NEEDED ON PACKAGE V0.0.3

# Colors were selected using imagecolorpicker.com
#colors from selected photos from Greg Girard's photography work: https://bluelotus-gallery.com/#/greg-girard/
ggBeige = '#c8a398'
ggBlack = '#18171a'
ggBrownLight = '#78554e'
ggGreenLight = '#73a8a8'
ggGreenDark = '#466863'
ggRedDark = '#b2263f'
ggRedLight = '#f39591'
ggBrownDark = '#4e3832'
ggBlueLight = '#597f9e'
ggBlueDark = '#485061'
#colors inspired by Chinatown in Vancouver, BC
yvr_medYellow = '#fcbe11'
yvr_medGreen = '#197059'
yvr_darkRed = '#b80807'
yvr_darkWhite = '#e9e3dc'
yvr_darkYellow = '#f4a002'
#ORIGINAL: color codes for HK Taxis
hk_red = "#A8102A"
hk_green = '#7bedda'
hk_blue = '#1076a8'

# hk_pm = [ggBeige, ggBlack, ggBrownLight, ggGreenLight, ggGreenDark, ggRedDark, ggRedLight, ggBrownDark, ggBlueLight, ggBlueDark]
color_combos = {
    "Espresso (brown/black)": [ggBrownLight, ggBlack],
    "Pinky (pink/green)": [ggRedLight, ggGreenDark],
    "Blush (pink/red)":[ggRedLight, ggRedDark],
    "Pacific (blue/green)" : [ggBlueDark, ggGreenLight],
    # "HK Taxi MUTED (blue/red)" :[ggBlueLight,ggRedDark],
    "Nougat (beige/brown)": [ggBeige, ggBrownDark],
    "HK Taxi (blue/red)":[hk_blue, hk_red],
    "Chinatown Bakery (yellow/turquoise)": [yvr_medYellow, yvr_medGreen],
    "Dim Sum (yellow/red)": [yvr_darkYellow, yvr_darkRed]
 }

#colorschemes for MARKERS
hk_redgreen = [[0, 'rgb(168,16,42)' ],
                 [0.5, 'rgb(255,255,255)'],
                [1, "rgb(16,168,142)"]]

hk_redblue = [[0, 'rgb(168,16,42)' ],
                 [0.5, 'rgb(255,255,255)'],
                [1, "rgb(16,118,168)"]]

hk_bluered = [[0, "rgb(16,118,168)" ],
#                  [0.5, 'rgb(255,255,255)'],
                [1, 'rgb(168,16,42)']]

hk_greenred = [[0, "rgb(16,168,142)" ],
                 [0.5, 'rgb(255,255,255)'],
                [1, 'rgb(168,16,42)']]

#individual colors
hk_red = 'rgb(168,16,42)' #A8102A
hk_green = 'rgb(16,168,142)' #7bedda
hk_blue = 'rgb(16,118,168)'

hk_red_light = "rgb(240, 125, 144)"
hk_green_light = "rgb(123, 237, 218)"
hk_blue_light = "rgb(126, 203, 242)"

hk_redgreen_l = [[0, hk_red_light ],
                 [0.5, 'rgb(255,255,255)'],
                [1, hk_green_light]]

# off_white='#e4dfce'
off_white="white"
off_black='#242424'

sand_823 = "#adab8b"
salmon_823 = "#ad8b8f"
blue_823 = "#8b93ad"

triad_1 = [sand_823, salmon_823, blue_823]

color_list = list(color_combos.values())
data_font='Futura'
title_font='Futura'
anno_text_default = "Source: <i>https://github.com/jon-tk-chan</i><br><i>Instagram: @artfornormies</i>"

#NEWLINED FUNCTION - for inserting breaks into text labels for graphs
def newlined(input_string, max_line_len=12):
    """Return a string with line breaks added when line length reaches max_line_len.
    
    This function is useful for formatting individual plotly labels, especially when
    dealing with scatter plots.
    
    Args:
        input_string (str): The input string to be formatted.
        max_line_len (int, optional): The maximum desired line length before adding a line break.
            Defaults to 12.
    
    Returns:
        str: The formatted string with line breaks added.
    """
    
    curr_line_len = 0
    out_str = ""
    for i, char in enumerate(input_string):
        curr_line_len += 1
        if char == " " and curr_line_len >= max_line_len:
            out_str += "<br>"
            curr_line_len = 0
        else: 
            out_str += char
        
    return out_str

def create_heatmap(x_ticks=['LEFT TICK', 'RIGHT TICK'], y_ticks=['BOTTOM TICK', 'TOP TICK'],
                   text_labels=[["bottom left", "bottom right"],["top left", "top right"]],
                    main_title='HEATMAP_TITLE',x_title='X_TITLE', y_title='Y_TITLE', anno_text = anno_text_default,
                   main_colorscale=hk_bluered, night_mode=True):
    """
    Returns a Plotly Graph Object as a styled heatmap
    
    Assume text values have NO line breaks beforehand - assigned using newlined() function
    
    Parameters:
        x_ticks: list of 2 str vals
        y ticks: list of 2 str vals
        text_labs: list of list of str vals [2x2]
        main_title: str
        x_title: str
        y_title: str
        
        night_mode: boolean to change colorscheme
        z_vals: list of list of int vals
    """
    #Change font sizes
    tick_size = 20
    label_size = 24
    axis_size= 29
    title_size=28 #not reference
    anno_size=16 #controls annotation size at bottom of graph

    
    z_vals = [[0, 1], [1, 0]] 
    if text_labels[0][0] != "bottom_left":
        text_labels=[[newlined(text_labels[0][0]),newlined(text_labels[0][1])], [newlined(text_labels[1][0]), newlined(text_labels[1][1])]]

    if not night_mode:
        axis_color=off_black
        line_color=off_black
        outline_color=off_black
        font_color=off_black
        bg_color=off_white
    else:
        axis_color=off_white
        line_color=off_white
        outline_color=off_white
        font_color=off_white
        bg_color=off_black 
        
    fig = go.Figure(data=go.Heatmap(z=z_vals,x=x_ticks,y=y_ticks,
       hoverongaps = False,colorscale=main_colorscale,opacity=0.65,  showlegend=False)
    )
    
    fig.update_traces(text=text_labels,
        texttemplate="%{text}",textfont={"size":label_size},
        textfont_color=font_color,showscale=False                  
    )
    
    #update plot element colors
    fig.update_layout(
        title=main_title,
        font=dict(family=data_font, size=tick_size,color=font_color),
        paper_bgcolor=bg_color, plot_bgcolor=bg_color,
        xaxis=dict(linecolor=axis_color,showgrid=False,showticklabels=True, showline=True, linewidth=3,
                  title=x_title, title_font=dict(family=title_font, size=axis_size)),
        yaxis=dict(linecolor=axis_color,showgrid=False, showticklabels=True, showline=True, linewidth=3,
                  title=y_title, title_font=dict(family=title_font, size=axis_size), tickangle=-90),
        width=fig_width,
        height=fig_height,
        margin=dict(l=90, r=70, b=150,t=100)
    )
    #add annotation
    fig.add_annotation(
        text = anno_text, showarrow=False,
        x = -0.04, y = -0.1125, #controls how far from axes 
        xref='paper', yref='paper' , xanchor='left', yanchor='bottom'
#         , xshift=-1
#         , yshift=-6.5
        , font=dict(size=anno_size), align="left",
    )
    
    return fig

def create_venn_2(venn_labels=["LEFT", "RIGHT","MID"], fill_venn=False, 
                  left_color=hk_blue, right_color=hk_red, opacity_val = 0.5,
                  label_charlen=10,
                  main_title="VENN_TITLE",anno_text=anno_text_default,night_mode=False,
                  fig_width=1000, fig_height=1200, label_size=28):
    """Generate a Plotly Figure of a 2-circle Venn diagram with labeled regions.
    
    Args:
        venn_labels (list): Labels for the Venn diagram regions [left, right, middle intersection].
            Default is ["LEFT", "RIGHT", "MID"].
        fill_venn (bool): Whether to fill Venn diagram regions with colors. Default is False.
        left_color (str): Predefined color for the left Venn region. Default is hk_blue.
        right_color (str): Predefined color for the right Venn region. Default is hk_red.
        label_charlen (int): Maximum character length for each label. Default is 10.
        main_title (str): Title for the Venn diagram figure. Default is "VENN_TITLE".
        anno_text (str): Annotation text displayed below the Venn diagram. Default is anno_text_default.
        night_mode (bool): Use night mode color scheme. Default is False.
        fig_width (int): Width of the figure in pixels. Default is 1000.
        fig_height (int): Height of the figure in pixels. Default is 1200.
        label_size (int): Font size for the labels. Default is 28.
    
    Returns:
        go.Figure: A Plotly Figure containing the 2-circle Venn diagram.
    """
    title_size = 32 #not referenced?
    # label_size = 30
    anno_size = 14
    if not night_mode:
        outline_color="black"
        font_color="black"
        bg_color="white"
        # opacity_val = 0.25
        line_color="black"
       
    else:
        outline_color="white"
        font_color="white"
        bg_color="black"
        # opacity_val = 0.7
        line_color="white"
        
    if not fill_venn:
        left_fill = None
        right_fill = None
        line_weight=7
    else:
        left_fill = left_color
        right_fill = right_color
        line_weight=3
    data_dict = {
        "x": [1,2,3],
        "y": [1,1,1],
            "text": [newlined(venn_labels[0], label_charlen), newlined(venn_labels[2],label_charlen),newlined(venn_labels[1],label_charlen)]
    }
    fig = go.Figure()

    ### ADD VENN DIAGRAMS
    fig.add_trace(go.Scatter(
        x = data_dict["x"],
        y = data_dict["y"],
        text = data_dict['text'],
        mode="text",
        textfont=dict(
            color=font_color,
            size=label_size,
            family=data_font,
        )
    ))
    fig.add_shape(type="circle",
        line_color=line_color, line_width=line_weight,
                  fillcolor=left_fill,
        x0=0.5, y0=0, x1=2.5, y1=2,
                  layer='below'
    )
    fig.add_shape(type="circle",
        line_color=line_color, line_width=line_weight,
                  fillcolor=right_fill,
        x0=1.5, y0=0, x1=3.5, y1=2,
                  layer='below'
    )

    fig.update_shapes(opacity=opacity_val, xref="x", yref="y")

    # Update axes properties
    fig.update_xaxes(showticklabels=False,showgrid=False,zeroline=False,
    )

    fig.update_yaxes(showticklabels=False,showgrid=False,zeroline=False,
    )

    fig.update_layout(
        title=main_title,
        font=dict(family=data_font, size=title_size,color=font_color),
        plot_bgcolor=bg_color, paper_bgcolor=bg_color,
        height=fig_height, #use width for height so that image is not stretched
        width=fig_width,
        margin=dict(l=20, r=20, b=100),
    )

    #add annotation
    fig.add_annotation(
        text = anno_text, showarrow=False,
        x = 0.04, y = -0.1125, #controls how far from axes 
        xref='paper', yref='paper' , xanchor='left', yanchor='bottom',
        font=dict(size=anno_size), align="left",
    )

    return fig

def create_scatter(x_vals=[1.0, 8.8, 5.0, 1.0, 8.8], y_vals=[9.0, 9.0, 5.0, 1.0, 1.0], 
                   text_vals= ['TOP LEFT', "TOP RIGHT", "CENTER", "BOTTOM LEFT", "BOTTOM RIGHT"], 
                   color_by_y=True,
                  main_title='MAIN_TITLE',x_title='X_TITLE', y_title='Y_TITLE', anno_text=anno_text_default,
                  main_colorscale=hk_greenred, night_mode=True,
                  label_size = 24, label_charlen=10):
    """Returns a Plotly Graph Object as a styled scatter plot
    
    Assume text values have NO line breaks beforehand - assigned using newlined() function if not using default text
    Assume that x_vals, y_vals, and text_vals all have same number of items
    Parameters:
        x_vals: list of floats
        y ticks: list of floats
        text_vals: list of strings
        color_by_y: boolean indicating to vary marker fill color vertically (True) or horizontally (False)
        main_title: str
        x_title: str
        y_title: str
        
        main_colorscale: list of 3 strings in the format 'rgb(<INT>, <INT>, <INT>)'
        night_mode: boolean to change colorscheme
    
    """
    text_pos="top center"  
    #UPDATE FONT
    data_font="Futura"
    title_font= "Futura" #affects the x and y axis title as well
    
    axis_size= 26
    title_size=28
    marker_size=30
    anno_size=14
    
    if not night_mode:
        axis_color=off_black
        line_color=off_black
        outline_color=off_black
        font_color=off_black
        bg_color=off_white
    else:
        axis_color=off_white
        line_color=off_white
        outline_color=off_white
        font_color=off_white
        bg_color=off_black 
        
    if color_by_y:
        colorscale_by=y_vals
    else:
        colorscale_by=x_vals #rework later - catch errors
    
    if text_vals[0] != "TOP LEFT":
        text_vals=[newlined(x,label_charlen) for x in text_vals]
        
    fig = go.Figure()
    # marker_dict=dict(size=16, colorscale=dot_colors,line=dict(color='black', width=2))
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals,
                            text=text_vals,
                             textposition=text_pos,
                             mode='markers+text',
                             marker=dict(size=marker_size,
                                         color=colorscale_by,
                                         colorscale=main_colorscale,
                                         line=dict(color=outline_color, width=2))
                            )
                 )
    fig.update_layout(
        font=dict(family=data_font, size=label_size, color=font_color),
        title=main_title, title_font=dict(family=data_font,size=title_size),
        xaxis_title=x_title, xaxis=dict(showgrid=False,showticklabels=False, linecolor=axis_color,
                                        showline=True, linewidth=2,range=[0,10],
                                       title_font=dict(family=title_font, size=axis_size)),
        yaxis_title=y_title,yaxis=dict(showgrid=False, showticklabels=False, linecolor=axis_color,
                                       showline=True, linewidth=2,range=[0,10],
                                      title_font=dict(family=title_font, size=axis_size)),
        paper_bgcolor=bg_color, plot_bgcolor=bg_color,
        height=fig_height,
        width=fig_width,
        margin=dict(l=70, r=70, b=150,t=100),
    )
    
    #add annotation
    fig.add_annotation(
        text = anno_text, showarrow=False,
        x = -0.027, y = -0.1125, #controls how far from axes 
        xref='paper', yref='paper' , xanchor='left', yanchor='bottom'
        , font=dict(size=anno_size), align="left",
    )
    return fig

def create_bar(y_vals=[9.0, 7.0, 5.0, 3.0, 1.0],
              text_vals=["BAR1", "BAR2", "BAR3", "BAR4", "BAR5"],
                main_title='MAIN_TITLE',x_title='X_TITLE', y_title='Y_TITLE', anno_text=anno_text_default,
                bar_color=hk_green, night_mode=True, label_charlen=8,label_size=18):
    """Returns a stylized bar chart
    
    Assume that y_vals and text_vals are same length
    Parameters:
        y_vals: list of floats
        text_vals: list of strings
        
        main_title: str
        x_title: str
        y_title: str
        
        main_colorscale: list of 3 strings in the format 'rgb(<INT>, <INT>, <INT>)'
        night_mode: boolean to change colorscheme
        
    """
    text_pos="top center"
    # label_size = 18
    axis_size= 27
    title_size=41
    anno_size=14
    
    additional_y_room = 1 #controls how to extend y range to allow for bigger labels
    max_y = 10 + additional_y_room
    
    if not night_mode:
        axis_color=off_black
        line_color=off_black
        outline_color=off_black
        font_color=off_black
        bg_color=off_white
    else:
        axis_color=off_white
        line_color=off_white
        outline_color=off_white
        font_color=off_white
        bg_color=off_black 
        
    if text_vals[0] != "BAR1":
        text_vals=[newlined(x,label_charlen) for x in text_vals]
        
    fig = go.Figure()
    fig.add_trace(
        go.Bar(x=text_vals, y=y_vals, marker=dict(color=bar_color,
                                 line=dict(color=outline_color, width=2)),
                                   text=text_vals,textposition='outside',
              )
    )
    
    fig.update_layout(
        font=dict(color=font_color,family=data_font, size=label_size),
        title=main_title,
        xaxis_title=x_title,
        yaxis_title=y_title,
        paper_bgcolor=bg_color, plot_bgcolor=bg_color,
        xaxis=dict(linecolor=axis_color, showgrid=False,showticklabels=False, showline=True, linewidth=2,
                  title_font=dict(family=title_font, size=axis_size)),
        yaxis=dict(linecolor=axis_color, showgrid=False,showticklabels=False, showline=True, linewidth=2, range=[0,max_y],
                  title_font=dict(family=title_font, size=axis_size)),
        width=fig_width*1.2,
        height=fig_height,
        margin=dict(l=20, r=20, b=100),
    )
    #add annotation
    fig.add_annotation(
        text = anno_text, showarrow=False,
        x = 0.017, y = -0.0725, #controls how far from axes 
        xref='paper', yref='paper' , xanchor='left', yanchor='bottom'
        , font=dict(size=anno_size), align="left",
    )
    
    return fig

