from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as px 
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import numpy as np

app = Dash(__name__) # criando o seu aplicativo Dash
server = app.server


teste_df = pd.read_excel('assets/teste.xlsx')
teste_df_ipdo = pd.read_excel('assets/testeipdo.xlsx')
df_ultima_update_pld_bd0 = pd.read_excel('assets/testepld.xlsx')

df_rdh_ipdo = pd.merge(teste_df, teste_df_ipdo, how = 'left', on = 'data')
df_rdh_ipdo.to_excel('assets/teste_rdh_ipdo.xlsx')
df_rdh_ipdo = df_rdh_ipdo.fillna(method='ffill')
print('df_rdh_ipdo')
display(df_rdh_ipdo)
df_ultima_update_pld_bd0 = df_ultima_update_pld_bd0.round(2)
df_final = pd.merge(df_ultima_update_pld_bd0, df_rdh_ipdo, how = 'left', on = 'data')
print(df_ultima_update_pld_bd0)
display(df_ultima_update_pld_bd0)
df_final.to_excel('assets/df_final.xlsx')
display(df_final)
df_final.describe()
df_final.info()




fig = make_subplots(specs=[[{"secondary_y": True}]])

#Gráfico com todas as premissas
#Gráfico com todas as premissas
#Gráfico com todas as premissas
#Gráfico com todas as premissas

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['enasinabs_x'], name="Afluência Brasil (MWm)"),
    secondary_y=False,)

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['enasinmlt_x'], name="Afluência mlt Brasil (MWm)"),
    secondary_y=False,)

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['carga'], name="Carga Brasil (MWm)"),
    secondary_y=False,)

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['solar'], name="Solar (MWm)"),
    secondary_y=False,)

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['eolica'], name="Eólica (MWm)"),
    secondary_y=False,)

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['hidro_total'], name="Hidro Total (MWm)"),
    secondary_y=False,)

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['ute_total'], name="UTE Total (MWm)"),
    secondary_y=False,)

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['PLD_SECO'], name="PLD (R$/MWh)"),
    secondary_y=True,)

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['demanda_max_dia'], name="demanda_max_dia"),
    secondary_y=False,)

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['demanda_max'], name="demanda_max_histórica"),
    secondary_y=False,)

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['earsin']*2930, name="earsin"),
    secondary_y=False,)

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['intercambio_SE'], name="intercambio_SE"),
    secondary_y=False,)

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['intercambio_SUL'], name="intercambio_SUL"),
    secondary_y=False,)

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['intercambio_NE'], name="intercambio_NE"),
    secondary_y=False,)

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['intercambio_N'], name="intercambio_N"),
    secondary_y=False,)


#Add figure title
fig.update_layout(title_text="PLD (R$/MWh), Geração e Afluência (MWm)", template='plotly')
#Set x-axis title
#fig.update_xaxes(title_text="xaxis title")
#Set y-axes titles
fig.update_yaxes(title_text="<b>Energia</b> (MWm)", secondary_y=False)
fig.update_yaxes(title_text="<b>PLD</b> (R$/MMh)", secondary_y=True)
#fig.show()#(fig, filename="C:\\Users\\Bernardo\\Downloads\\ena_carga_pld.html")
#py.offline.plot(fig, filename="C:\\Users\\Bernardo\\Downloads\\ena_carga_pld.html")


#Gráfico Balaço de energia
#Gráfico Balaço de energia
#Gráfico Balaço de energia
#Gráfico Balaço de energia


import plotly.graph_objects as px 
  
fig2 = px.Figure() 

fig2.add_trace(go.Scatter( 
    name = 'intercâmbio_internacional', 
    line=dict(color='gray'),
    x = df_rdh_ipdo['data'], 
    y = df_rdh_ipdo['i_internacional'], 
    stackgroup='one',
   )) 

fig2.add_trace(go.Scatter( 
    name = 'solar', 
    line=dict(color='yellow'),
    x =  df_rdh_ipdo['data'], 
    y = df_rdh_ipdo['solar'], 
    stackgroup='one'
   )) 
  
fig2.add_trace(go.Scatter( 
    name = 'eolica', 
    line=dict(color='green'),
    x = df_rdh_ipdo['data'], 
    y = df_rdh_ipdo['eolica'], 
    stackgroup='one'
   )) 

fig2.add_trace(go.Scatter( 
    name = 'ute_total',
    line=dict(color='red'),
    x = df_rdh_ipdo['data'], 
    y = df_rdh_ipdo['ute_total'], 
    stackgroup='one'
   ))

fig2.add_trace(go.Scatter( 
    name = 'hidro_total',
    line=dict(color='blue'),
    x = df_rdh_ipdo['data'], 
    y = df_rdh_ipdo['hidro_total'], 
    stackgroup='one',
   )) 

#layout=go.Layout(
#        title=go.layout.Title(text="A Figure Specified By A Graph Object")

fig2.add_trace(go.Scatter( 
    name = 'carga', 
    line=dict(color='purple'),
    x = df_rdh_ipdo['data'], 
    y = df_rdh_ipdo['carga'], 
    mode = 'lines',
   )) 

fig2.update_yaxes(title_text="Energia (MWm)")
fig2.update_layout(title_text="Balanço de energia (MWm)")


#Gráfico reservatórios
#Gráfico reservatórios
#Gráfico reservatórios
#Gráfico reservatórios


condicoes = [(df_final['mes_x'] == 1), 
             (df_final['mes_x'] == 2), 
             (df_final['mes_x'] == 3),
             (df_final['mes_x'] == 4),
             (df_final['mes_x'] == 5),
             (df_final['mes_x'] == 6),
             (df_final['mes_x'] == 7),
             (df_final['mes_x'] == 8),
             (df_final['mes_x'] == 9),
             (df_final['mes_x'] == 10),
             (df_final['mes_x'] == 11),
             (df_final['mes_x'] == 12),]

opcoes = ['JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']

df_final['mes_extenso'] = np.select(condicoes, opcoes)

# Gráfico usando apenas marcadores
df_filtro_ano = df_final[(df_final['ano_x'] == 2020)]
trace1 = go.Scatter(x=df_filtro_ano['mes_extenso'],
                    y=df_filtro_ano['earsin'],
                    mode = 'markers+lines',
                    name = 'earsin_2020',);

df_filtro_ano = df_final[(df_final['ano_x'] == 2021)]
trace2 = go.Scatter(x=df_filtro_ano['mes_extenso'],
                    y=df_filtro_ano['earsin'],
                    mode = 'markers+lines',
                    name = 'earsin_2021',);

df_filtro_ano = df_final[(df_final['ano_x'] == 2022)]
trace3 = go.Scatter(x=df_filtro_ano['mes_extenso'],
                    y=df_filtro_ano['earsin'],
                    mode = 'markers+lines',
                    name = 'earsin_2022',);

df_filtro_ano = df_final[(df_final['ano_x'] == 2023)]
trace4 = go.Scatter(x=df_filtro_ano['mes_extenso'],
                    y=df_filtro_ano['earsin'],
                    mode = 'markers+lines',
                    name = 'earsin_2023',);

df_filtro_ano = df_final[(df_final['ano_x'] == 2024)]
trace5 = go.Scatter(x=df_filtro_ano['mes_extenso'],
                    y=df_filtro_ano['earsin'],
                    mode = 'markers+lines',
                    name = 'earsin_2024',);

data = [trace1, trace2, trace3, trace4, trace5]

#layout = go.layout(title:'% do Armazenamento máximo dos reservatórios (MWm) %EARmáx', yaxis={'%EARmáx'})

fig3 = go.Figure(data=data, layout=go.Layout(title=go.layout.Title(text="% do Armazenamento máximo dos reservatórios (MWm) %EARmáx")))

fig3.update_yaxes(title = "% EARmáx")

#df_final = df_final.astype({"dia_x": int, "mes_x": int})
df_final = df_final.astype({"dia_x": str, "mes_x": str})
df_final['mes_dia'] = df_final['dia_x'] + '/' + df_final['mes_extenso']

df_final['tx_var_ear_sin_rolling'] = df_final['tx_var_ear_sin'].rolling(7, min_periods=1).mean()

#taxa de variação diária

# Gráfico usando apenas marcadores
df_filtro_ano = df_final[(df_final['ano_x'] == 2020)]
trace1 = go.Scatter(x=df_filtro_ano['mes_dia'],
                    y=df_filtro_ano['tx_var_ear_sin'],
                    mode = 'lines',
                    name = 'earsin_2020',);

df_filtro_ano = df_final[(df_final['ano_x'] == 2020)]
trace11 = go.Scatter(x=df_filtro_ano['mes_dia'],
                    y=df_filtro_ano['tx_var_ear_sin_rolling'],
                    mode = 'lines',
                    name = 'MM_7d_earsin_2020',);

df_filtro_ano = df_final[(df_final['ano_x'] == 2021)]
trace2 = go.Scatter(x=df_filtro_ano['mes_dia'],
                    y=df_filtro_ano['tx_var_ear_sin'],
                    mode = 'lines',
                    name = 'earsin_2021',);

df_filtro_ano = df_final[(df_final['ano_x'] == 2021)]
trace22 = go.Scatter(x=df_filtro_ano['mes_dia'],
                    y=df_filtro_ano['tx_var_ear_sin_rolling'],
                    mode = 'lines',
                    name = 'MM_7d_earsin_2021',);

df_filtro_ano = df_final[(df_final['ano_x'] == 2022)]
trace3 = go.Scatter(x=df_filtro_ano['mes_dia'],
                    y=df_filtro_ano['tx_var_ear_sin'],
                    mode = 'lines',
                    name = 'earsin_2022',);

df_filtro_ano = df_final[(df_final['ano_x'] == 2022)]
trace33 = go.Scatter(x=df_filtro_ano['mes_dia'],
                    y=df_filtro_ano['tx_var_ear_sin_rolling'],
                    mode = 'lines',
                    name = 'MM_7d_earsin_2022',);


df_filtro_ano = df_final[(df_final['ano_x'] == 2023)]
trace4 = go.Scatter(x=df_filtro_ano['mes_dia'],
                    y=df_filtro_ano['tx_var_ear_sin'],
                    mode = 'lines',
                    name = 'earsin_2023',);

df_filtro_ano = df_final[(df_final['ano_x'] == 2023)]
trace44 = go.Scatter(x=df_filtro_ano['mes_dia'],
                    y=df_filtro_ano['tx_var_ear_sin_rolling'],
                    mode = 'lines',
                    name = 'MM_7d_earsin_2023',);


df_filtro_ano = df_final[(df_final['ano_x'] == 2024)]
trace5 = go.Scatter(x=df_filtro_ano['mes_dia'],
                    y=df_filtro_ano['tx_var_ear_sin'],
                    mode = 'lines',
                    name = 'earsin_2024',);

df_filtro_ano = df_final[(df_final['ano_x'] == 2024)]
trace55 = go.Scatter(x=df_filtro_ano['mes_dia'],
                    y=df_filtro_ano['tx_var_ear_sin_rolling'],
                    mode = 'lines',
                    name = 'MM_7d_earsin_2024',);


data = [trace1, trace2, trace3, trace4, trace5, trace11, trace22, trace33, trace44, trace55]

#layout = go.layout(title:'% do Armazenamento máximo dos reservatórios (MWm) %EARmáx', yaxis={'%EARmáx'})

fig7 = go.Figure(data=data, layout=go.Layout(title=go.layout.Title(text="taxa de variação da EAR diária (%)")))

fig7.update_yaxes(title = "% EAR")





#Gráfico com as ENAs dos submrecados
#Gráfico com as ENAs dos submrecados
#Gráfico com as ENAs dos submrecados
#Gráfico com as ENAs dos submrecados

fig4 = make_subplots(rows=2, cols=2, subplot_titles=("ENA SUDESTE/CENTRO-OESTE", "ENA SUL", "ENA NORDESTE", "ENA NORTE"), start_cell="bottom-left")

fig4.add_trace(go.Scatter(x=df_final['data'], y=df_final['enaseabs_x']),
              row=1, col=1)
fig4.add_trace(go.Scatter(x=df_final['data'], y=df_final['enasemlt_x']),
              row=1, col=1)

fig4.add_trace(go.Scatter(x=df_final['data'], y=df_final['enasuabs_x']),
              row=1, col=2)
fig4.add_trace(go.Scatter(x=df_final['data'], y=df_final['enasunmlt_x']),
              row=1, col=2)

fig4.add_trace(go.Scatter(x=df_final['data'], y=df_final['enaneabs_x']),
              row=2, col=1)
fig4.add_trace(go.Scatter(x=df_final['data'], y=df_final['enanenmlt_x']),
              row=2, col=1)

fig4.add_trace(go.Scatter(x=df_final['data'], y=df_final['enanabs_x']),
              row=2, col=2)
fig4.add_trace(go.Scatter(x=df_final['data'], y=df_final['enannmlt_x']),
              row=2, col=2)




# Update yaxis properties
fig4.update_yaxes(title_text="ENA (MWm)", row=1, col=1)
fig4.update_yaxes(title_text="ENA (MWm)", row=1, col=2)
fig4.update_yaxes(title_text="ENA (MWm)", row=2, col=1)
fig4.update_yaxes(title_text="ENA (MWm)", row=2, col=2)





fig4.update_layout(height=700, width=1100, title_text="Energia Natural Afluênte dos Submercados (ENAs)", showlegend=False)



###Tabela com as ENAS por submercado
###Tabela com as ENAS por submercado
###Tabela com as ENAS por submercado



fig5 = go.Figure(data=[go.Table(header=dict(values=['Data', 'ENA SE/CO', 'ENA SUL', 'ENA NORDESTE', 'ENA NORTE', 'ENA SIN']),
                 cells=dict(values=[teste_df['data'], teste_df['enasepp'], teste_df['enasupp'], teste_df['enanepp'], teste_df['enanpp'], teste_df['enasinpp']]))
                     ])

fig5.update_layout(title_text="ENAs (%MLT)", template='plotly')



fig6 = go.Figure(data=[go.Table(header=dict(values=['Data', 'EAR SE/CO', 'EAR SUL', 'EAR NORDESTE', 'EAR NORTE', 'EAR SIN']),
                 cells=dict(values=[teste_df['data'], teste_df['earse'], teste_df['earsu'], teste_df['earne'], teste_df['earn'], teste_df['earsin']]))
                     ])

fig6.update_layout(title_text="ENERGIA ARMAZENADA - EAR (%EARmáx)", template='plotly')


#fig2 = px.scatter(df, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)


#Gráfico com todas as premissas
#Gráfico com todas as premissas
#Gráfico com todas as premissas
#Gráfico com todas as premissas

fig8 = make_subplots(specs=[[{"secondary_y": False}]])

fig8.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['PLD_SECO'], name="PLD_SECO"),)

fig8.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['PLD_SUL'], name="PLD_SUL"),)

fig8.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['PLD_NE'], name="PLD_NE"),)

fig8.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['PLD_N'], name="PLD_NORTE"),)

#Add figure title
fig8.update_layout(title_text="PLDs SUBMERCADO (R$/MWh)", template='plotly')
#Set x-axis title
#fig.update_xaxes(title_text="xaxis title")
#Set y-axes titles
fig8.update_yaxes(title_text="<b>PLD</b> (R$/MWh)")
#fig.show()#(fig, filename="C:\\Users\\Bernardo\\Downloads\\ena_carga_pld.html")
#py.offline.plot(fig, filename="C:\\Users\\Bernardo\\Downloads\\ena_carga_pld.html")


###Tabela com as ENAS por submercado
###Tabela com as ENAS por submercado
###Tabela com as ENAS por submercado



fig9 = go.Figure(data=[go.Table(header=dict(values=['Data', 'PLD_SECO', 'PLD_SUL', 'PLD_NE', 'PLD_NORTE']),
                 cells=dict(values=[df_final['data'], df_final['PLD_SECO'], df_final['PLD_SUL'], df_final['PLD_NE'], df_final['PLD_N']]))
                     ])

fig9.update_layout(title_text="PLDs SUBMERCADO (R$/MWh)", template='plotly')

# css
app.layout = html.Div(children=[
    
    html.Img(src='assets/vale3.png', alt='image', width = '650'),
    
    #html.H1(children='RDH - IPDO - PLD', style={"text-align": "center"}),

    #html.h2(children='''
    #    Dashboard de Vendas em Python
    #'''),
    
    #html.H3(children="Vendas de cada Produto por Loja"),
    
   
    dcc.Graph(id='grafico2', figure=fig2),
    dcc.Graph(id='grafico3', figure=fig3),
    dcc.Graph(id='vendas_por_loja1',figure=fig6),
    dcc.Graph(id='vendas_por_loja2',figure=fig7),
    dcc.Graph(id='vendas_por_loja3',figure=fig),
    dcc.Graph(id='vendas_por_loja4',figure=fig4),
    dcc.Graph(id='vendas_por_loja5',figure=fig5),
    dcc.Graph(id='vendas_por_loja6',figure=fig8),
    dcc.Graph(id='vendas_por_loja7',figure=fig9),
    
    
])

# callbacks
# Adicione a rota raiz para o Dash
app.config.suppress_callback_exceptions = True

# Imprime o link para acesso
#print("Running on http://127.0.0.1:8053/")

if __name__ == '__main__':
    app.run_server(debug=True)#, use_reloader=False, port=8053)