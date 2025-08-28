import plotly.graph_objects as go


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

#boilerplate figure

class Chart():
    def __init__(self, fig_width=750, fig_height= 600, night_mode=True, opacity_val=0.75,
                # main_title="MAIN TITLE", 
                 label_charlen = 10,
                 title_size=20,axis_label_size=20, tick_label_size=16, label_size= 18, anno_size=10, 
                anno_text= "Source: <i>https://github.com/jon-tk-chan</i><br><i>Instagram: @artfornormies</i>"):
        #create attributes
        self.fig_width = fig_width
        self.fig_height = fig_height
        self.night_mode = night_mode

        #MOVE TO EACH METHOD
        # self.main_title = main_title 
        self.anno_text = anno_text
        self.label_charlen = label_charlen
        self.opacity_val = opacity_val
        
        self.data_font='Futura'
        self.title_font='Futura'
        #
        self.title_size = title_size
        self.axis_label_size = axis_label_size
        self.tick_label_size = tick_label_size
        self.label_size = label_size
        self.anno_size = anno_size
        ### Create base figure as method to read in correct night_mode variables    
    def create_base(self):
        if not self.night_mode:
            self.axis_color = "black"
            self.outline_color="black"
            self.font_color="black"
            self.bg_color="white"
            # self.opacity_val = 0.55
            self.line_color="black"
           
        else:
            self.axis_color = "white"
            self.outline_color="white"
            self.font_color="white"
            self.bg_color="black"
            # self.opacity_val = 0.7
            self.line_color="white"
            
        ### BASELINE FIG - using all attributes from self and those set by night_mode boolean
        fig = go.Figure()
        # fig.update_shapes(opacity = self.opacity_val)
        fig.update_xaxes(showticklabels=False,showgrid=False,zeroline=False)
        fig.update_yaxes(showticklabels=False,showgrid=False,zeroline=False)
        fig.update_layout(
            # title=self.main_title,
            font=dict(family=self.data_font, size=self.title_size,color=self.font_color),
            plot_bgcolor=self.bg_color, paper_bgcolor=self.bg_color,
            height=self.fig_height, #use width for height so that image is not stretched
            width=self.fig_width,
            margin=dict(l=50, r=50, b=100),
        )
        #add annotation
        fig.add_annotation(
            text = self.anno_text, showarrow=False,
            x = 0.00, y = -0.1725, #controls how far from axes 
            xref='paper', yref='paper' , xanchor='left', yanchor='bottom',
            font=dict(size=self.anno_size), align="left",)
        self.fig = fig
        return self.fig

    def create_venn_2(self, text_labels=["LEFT", "RIGHT","MID"],fill_venn=True,
                      main_title="MAIN_TITLE_VENN",
                     left_color='rgb(168,16,42)', right_color='rgb(16,118,168)'):
        """Create 2-circle venn diagram using text_labels, left_color, and right_color'"""
        data_dict = {
            "x": [1,2,3],
            "y": [1,1,1],
            "text": [newlined(text_labels[0], self.label_charlen), 
                     newlined(text_labels[2],self.label_charlen),
                     newlined(text_labels[1],self.label_charlen)]
        }
        if not fill_venn:
            self.left_fill = None
            self.right_fill = None
            self.line_weight=7

        else:
            self.left_fill = left_color
            self.right_fill = right_color
            self.line_weight=3
        ### Call create_base()
        venn = self.create_base()
        #Add circle shapes - use line_weight, line_color, left_fill OR right_fill from self
        venn.add_shape(type="circle",
            line_color=self.line_color, line_width=self.line_weight, fillcolor=self.left_fill,
            x0=0.5, y0=0, x1=2.5, y1=2,layer='below')
        venn.add_shape(type="circle",
            line_color=self.line_color, line_width=self.line_weight, fillcolor=self.right_fill,
            x0=1.5, y0=0, x1=3.5, y1=2,layer='below')
        venn.update_shapes(opacity = self.opacity_val)

        #Add text labels
        venn.add_trace(go.Scatter(
            x = data_dict["x"], y = data_dict["y"],text = data_dict['text'],mode="text",
            textfont=dict(color=self.font_color, size=self.label_size, family=self.data_font)))
        venn.update_layout(margin=dict(l=100, r=100, b=200), title=main_title)
        self.venn = venn
        return self.venn

    def create_heatmap(self, x_ticks=['LEFT TICK', 'RIGHT TICK'], y_ticks=['BOTTOM TICK', 'TOP TICK'],
                   text_labels=[["bottom left", "bottom right"],["top left", "top right"]],
                       x_title='X_TITLE', y_title='Y_TITLE', main_title="MAIN_TITLE_HEATMAP",
                      # main_colorscale=[[0, "rgb(16,118,168)" ],[1, 'rgb(168,16,42)']]
                       color_1 = "rgb(16,118,168)", color_2='rgb(168,16,42)'
                      ):
        self.main_colorscale = [[0, color_1 ],[1, color_2]]
        z_vals = [[0, 1], [1, 0]] 
        # if text_labels[0][0] != "bottom_left":
        text_labels=[[newlined(text_labels[0][0]),newlined(text_labels[0][1])], [newlined(text_labels[1][0]), newlined(text_labels[1][1])]]
        self.main_title = main_title
        heatmap = self.create_base()
        #Add heatmap trace 
        heatmap.add_trace(go.Heatmap(z=z_vals,x=x_ticks,y=y_ticks,
               hoverongaps = False,colorscale=self.main_colorscale,opacity=self.opacity_val, showlegend=False)
            )
        #add formatting of axis
        heatmap.update_traces(textfont_size=self.label_size)
        heatmap.update_layout(title=main_title,
                              title_font=dict(
                # family=self.data_font, 
                size=self.title_size),
            font=dict(family=self.data_font, 
                      # size=self.label_size,
                      color=self.font_color),
            paper_bgcolor=self.bg_color, plot_bgcolor=self.bg_color,
            xaxis=dict(linecolor=self.axis_color,showgrid=False,showticklabels=True, showline=True, linewidth=3,
                      title=x_title, title_font=dict(family=self.title_font, size=self.axis_label_size),
                      tickfont=dict(size=self.tick_label_size)),
            yaxis=dict(linecolor=self.axis_color,showgrid=False, showticklabels=True, showline=True, linewidth=3,
                      title=y_title, title_font=dict(family=self.title_font, size=self.axis_label_size), tickangle=-90,
                      tickfont=dict(size=self.tick_label_size)),
            width=self.fig_width,height=self.fig_height,margin=dict(l=90, r=70, b=150,t=100))
        #ADD text labels
        heatmap.update_traces(text=text_labels,
            texttemplate="%{text}",textfont={"size":self.label_size},
            textfont_color=self.font_color,showscale=False)
        # heatmap.update_traces(textfont_size=self.label_size)
        heatmap.update_layout(margin=dict(l=100, r=100, b=300))
        self.heatmap = heatmap
        return self.heatmap

    def create_scatter(self,x_vals=[1.0, 8.8, 5.0, 1.0, 8.8], y_vals=[9.0, 9.0, 5.0, 1.0, 1.0], 
                   text_vals= ['TOP LEFT', "TOP RIGHT", "CENTER", "BOTTOM LEFT", "BOTTOM RIGHT"], 
                   color_by_y=True,
                       x_title='X_TITLE', y_title='Y_TITLE', main_title="MAIN_TITLE_SCATTER",
                       color_1 = 'rgb(168,16,42)', color_2="rgb(16,168,142)"
                      ):
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
        self.main_colorscale = [[0, color_1 ],[0.5, 'rgb(255,255,255)'],[1, color_2]]
        text_pos="top center"  
        if color_by_y:
            colorscale_by=y_vals
        else:
            colorscale_by=x_vals #rework later - catch errors
        
        text_vals=[newlined(x,self.label_charlen) for x in text_vals]
            
        ### Call create_base()
        scatter = self.create_base()
        # marker_dict=dict(size=16, colorscale=dot_colors,line=dict(color='black', width=2))
        scatter.add_trace(go.Scatter(x=x_vals, y=y_vals,
                                text=text_vals,
                                 textposition=text_pos,
                                 mode='markers+text',
                                 marker=dict(size=30,
                                             color=colorscale_by,
                                             colorscale=self.main_colorscale,
                                             line=dict(color=self.line_color, width=2))
                                )
                     )
        scatter.update_traces(textfont_size=self.label_size)
        scatter.update_layout(
            font=dict(family=self.data_font,color=self.font_color),
            title=main_title, 
            title_font=dict(
                # family=self.data_font, 
                size=self.title_size),
            xaxis_title=x_title, xaxis=dict(showgrid=False,showticklabels=False, linecolor=self.axis_color,
                                            showline=True, linewidth=2,range=[-0.1,10],
                                           title_font=dict(family=self.title_font, size=self.axis_label_size)),
            yaxis_title=y_title,yaxis=dict(showgrid=False, showticklabels=False, linecolor=self.axis_color,
                                           showline=True, linewidth=2,range=[-0.1,10],
                                          title_font=dict(
                                              # family=self.title_font, 
                                              size=self.axis_label_size)),
            paper_bgcolor=self.bg_color, plot_bgcolor=self.bg_color,
            height=self.fig_height,
            width=self.fig_width,
            margin=dict(l=70, r=70, b=150,t=100),
        )
        
        self.scatter = scatter
        return self.scatter

    def create_bar(self, y_vals=[9.0, 7.0, 5.0, 3.0, 1.0],
                  text_vals=["BAR1", "BAR2", "BAR3", "BAR4", "BAR5"],
                    main_title='MAIN_TITLE_BAR',
                   x_title='X_TITLE', y_title='Y_TITLE', 
                    bar_color=hk_green, 
                   # label_charlen=8,label_size=18
                  ):
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
        # axis_size= 27
        # title_size=41
        # anno_size=14
        
        additional_y_room = 1 #controls how to extend y range to allow for bigger labels
        max_y = 10 + additional_y_room
        text_vals=[newlined(x,self.label_charlen) for x in text_vals]
            
        # fig = go.Figure()
        bar= self.create_base()
        bar.add_trace(
            go.Bar(x=text_vals, y=y_vals, marker=dict(color=bar_color,
                                     line=dict(color=self.outline_color, width=2)),
                                       text=text_vals,textposition='outside',
                  )
        )
        bar.update_traces(textfont_size=self.label_size)
        bar.update_layout(
            font=dict(color=self.font_color,family=self.data_font, ),
            title_font=dict(
                # family=self.data_font, 
                size=self.title_size),
            title=main_title,
            xaxis_title=x_title,
            yaxis_title=y_title,
            paper_bgcolor=self.bg_color, plot_bgcolor=self.bg_color,
            xaxis=dict(linecolor=self.axis_color, showgrid=False,showticklabels=False, showline=True, linewidth=2,
                      title_font=dict(family=self.title_font, size=self.axis_label_size)),
            yaxis=dict(linecolor=self.axis_color, showgrid=False,showticklabels=False, showline=True, linewidth=2, range=[0,max_y],
                      title_font=dict(family=self.title_font, size=self.axis_label_size)),
            height=self.fig_height,width=self.fig_width,
            margin=dict(l=70, r=70, b=150,t=100),
        )
        self.bar = bar
        return self.bar
