from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as px 
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objs as go
from dash import Dash, Input, Output
import numpy as np

app = Dash(__name__) # criando o seu aplicativo Dash
server = app.server


teste_df = pd.read_excel('assets/teste.xlsx')
teste_df_ipdo = pd.read_excel('assets/testeipdo.xlsx')
df_ultima_update_pld_bd0 = pd.read_excel('assets/testepld.xlsx')

df_rdh_ipdo = pd.merge(teste_df, teste_df_ipdo, how = 'left', on = 'data')
df_rdh_ipdo.to_excel('assets/teste_rdh_ipdo.xlsx')
df_rdh_ipdo = df_rdh_ipdo.fillna(method='ffill')
#print('df_rdh_ipdo')
#display(df_rdh_ipdo)
df_ultima_update_pld_bd0 = df_ultima_update_pld_bd0.round(2)
df_final = pd.merge(df_ultima_update_pld_bd0, df_rdh_ipdo, how = 'left', on = 'data')
#print(df_ultima_update_pld_bd0)

dfmercado = pd.read_excel(r'assets/me3.xlsx')
df_final = pd.merge(df_final, dfmercado, how = 'left', on = 'data')
df_final.fillna(method='ffill', inplace=True)


#display(df_ultima_update_pld_bd0)
df_final.to_excel('assets/df_final.xlsx')
#display(df_final)
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


fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['FEN - SE CON ANU JAN/24 DEZ/24 - Preço Fixo'], name="PM 2024"),
    secondary_y=True,)

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['FEN - SE CON ANU JAN/25 DEZ/25 - Preço Fixo'], name="PM 2025"),
    secondary_y=True,)

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['FEN - SE CON ANU JAN/26 DEZ/26 - Preço Fixo'], name="PM 2026"),
    secondary_y=True,)

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['FEN - SE CON ANU JAN/27 DEZ/27 - Preço Fixo'], name="PM 2027"),
    secondary_y=True,)

fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['FEN - SE CON ANU JAN/28 DEZ/28 - Preço Fixo'], name="PM 2028"),
    secondary_y=True,)


fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['FEN - SE CON SEM JAN/24 JUN/24 - Preço Fixo'], name="PM 1S24"),
    secondary_y=True,)


fig.add_trace(
    go.Scatter(x=df_final['data'], y=df_final['FEN - SE CON SEM JUL/24 DEZ/24 - Preço Fixo'], name="PM 2S24"),
    secondary_y=True,)


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

import locale

locale.setlocale(locale.LC_TIME, 'C')

# Configurar o local para português do Brasil
#locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')




# DataFrame CAR
df2_data = {'mes_x': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
            'Curva C': ['24.6', '32.9', '41.3', '42.7', '42.1', '40.5', '37.8', '33.9', '29.4', '23.8', '21.4', '21.9'],
            'Curva B': ['34.3', '42', '49.7', '50.2', '48.9', '46.6', '43', '38.2', '33', '25.9', '21.4', '28.1'],
            'Curva A': ['45', '51.8', '58.6', '58.6', '56.9', '54.4', '50', '43.5', '37.6', '28.7', '21.4', '39.5']}

df2 = pd.DataFrame(df2_data)

df2['mes_x'] = df2['mes_x'].astype('int')
df_final['mes_x'] = df_final['mes_x'].astype('int')

#Mesclar os DataFrames df1 e df2
df_final = pd.merge(df_final, df2.set_index('mes_x'), left_on='mes_x', right_index=True)

#df_final = df_final.drop('Unnamed: 0.1', axis=1)

df_final['data'] = pd.to_datetime(df_final['data'], format='%d/%m/%Y')

df_final = df_final.sort_values(by='data')

df_final['data'] = df_final['data'].dt.strftime('%d/%m/%Y')

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

df_filtro_ano = df_final[(df_final['ano_x'] == 2023)]
trace6= go.Scatter(x=df_filtro_ano['mes_extenso'],
                    y=df_filtro_ano['Curva A'],
                    mode = 'markers+lines',
                    name = 'Curva C',
                    marker=dict(color='gray', size=6),
                    line=dict(color='gray', width=2, dash='dash'));

df_filtro_ano = df_final[(df_final['ano_x'] == 2023)]
trace7= go.Scatter(x=df_filtro_ano['mes_extenso'],
                    y=df_filtro_ano['Curva B'],
                    mode = 'markers+lines',
                    name = 'Curva B',
                    marker=dict(color='Tan', size=6),
                    line=dict(color='Tan', width=2, dash='dash'));

df_filtro_ano = df_final[(df_final['ano_x'] == 2023)]
trace8= go.Scatter(x=df_filtro_ano['mes_extenso'],
                    y=df_filtro_ano['Curva C'],
                    mode = 'markers+lines',
                    name = 'Curva A',
                    marker=dict(color='black', size=6),
                    line=dict(color='black', width=2, dash='dash'));



data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8]

#layout = go.layout(title:'% do Armazenamento máximo dos reservatórios (MWm) %EARmáx', yaxis={'%EARmáx'})

#layout = go.layout(title:'% do Armazenamento máximo dos reservatórios (MWm) %EARmáx', yaxis={'%EARmáx'})

fig3 = go.Figure(
    data=data,
    layout=go.Layout(
        title=go.layout.Title(text="% do Armazenamento máximo dos reservatórios (MWm) %EARmáx"),
        yaxis=dict(title="% EARmáx"),
        annotations=[
            dict(
                xref='paper', yref='paper',
                x=0.5, y=-0.1,
                xanchor='right', yanchor='top',
                text='Curva C = Mínimo de 9,3 GWm de Térmicas \n, Curva B = Mínimo de 14 GWm de Térmicas \n, Curva A = Mínimo de 18 GWm de Térmicas',
                showarrow=False,
                font=dict(size=12)
            )
        ]
    )
)


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
fig8.update_layout(title_text="PLDs SUBMERCADO - MÉDIA DIÁRIA (R$/MWh)", template='plotly')
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

fig9.update_layout(title_text="PLDs SUBMERCADO - MÉDIA DIÁRIA (R$/MWh)", template='plotly')

# Calcular média mensal

df = pd.read_excel(r'assets/testepld.xlsx')

df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
df.set_index('data', inplace=True)
df_resampled = df.resample('M').mean()
df_resampled = df_resampled.round(2)
df_resampled['MesAno'] = df_resampled.index.strftime('%b/%Y')

# Calcular média anual
df_resampled_anual = df.resample('Y').mean()
df_resampled_anual['Ano'] = df_resampled_anual.index.year.astype(int)
df_resampled_anual = df_resampled_anual.round(2)

# Criar nova coluna de ano para garantir apenas anos inteiros
df_resampled_anual['AnoInteiro'] = df_resampled_anual.index.to_period('Y').astype(str)

# Plotar gráfico plotly mensal

fig10 = make_subplots(specs=[[{"secondary_y": False}]])

fig10.add_trace(
    go.Scatter(x=df_resampled['MesAno'], y=df_resampled['PLD_SECO'], name="PLD_SECO"),)

fig10.add_trace(
    go.Scatter(x=df_resampled['MesAno'], y=df_resampled['PLD_SUL'], name="PLD_SUL"),)

fig10.add_trace(
    go.Scatter(x=df_resampled['MesAno'], y=df_resampled['PLD_NE'], name="PLD_NE"),)

fig10.add_trace(
    go.Scatter(x=df_resampled['MesAno'], y=df_resampled['PLD_N'], name="PLD_NORTE"),)

for trace in fig10.data:
    trace.mode = 'markers+lines'

#Add figure title
fig10.update_layout(title_text="PLDs SUBMERCADO - MÉDIA MENSAL (R$/MWh)", template='plotly')
#Set x-axis title
#fig.update_xaxes(title_text="xaxis title")
#Set y-axes titles
fig10.update_yaxes(title_text="<b>PLD</b> (R$/MWh)")

#py.offline.plot(fig, filename="C:\\Users\\Bernardo\\Downloads\\ena_carga_pld.html")


###PLDs MENSAIS SUBMERCADO
###PLDs MENSAIS SUBMERCADO
###PLDs MENSAIS SUBMERCADO



fig11 = go.Figure(data=[go.Table(header=dict(values=['MesAno', 'PLD_SECO', 'PLD_SUL', 'PLD_NE', 'PLD_NORTE']),
                 cells=dict(values=[df_resampled['MesAno'], df_resampled['PLD_SECO'], df_resampled['PLD_SUL'], df_resampled['PLD_NE'], df_resampled['PLD_N']]))
                     ])

fig11.update_layout(title_text="PLDs SUBMERCADO - MÉDIA MENSAL (R$/MWh)", template='plotly')




# Plotar gráfico plotly anual

fig12 = make_subplots(specs=[[{"secondary_y": False}]])

fig12.add_trace(
    go.Scatter(x=df_resampled_anual['AnoInteiro'], y=df_resampled_anual['PLD_SECO'], name="PLD_SECO"),)

fig12.add_trace(
    go.Scatter(x=df_resampled_anual['AnoInteiro'], y=df_resampled_anual['PLD_SUL'], name="PLD_SUL"),)

fig12.add_trace(
    go.Scatter(x=df_resampled_anual['AnoInteiro'], y=df_resampled_anual['PLD_NE'], name="PLD_NE"),)

fig12.add_trace(
    go.Scatter(x=df_resampled_anual['AnoInteiro'], y=df_resampled_anual['PLD_N'], name="PLD_NORTE"),)


#Add figure title
fig12.update_layout(title_text="PLDs SUBMERCADO - MÉDIA ANUAL (R$/MWh)", template='plotly')
#Set x-axis title
#fig.update_xaxes(title_text="xaxis title")
#Set y-axes titles
fig12.update_yaxes(title_text="<b>PLD</b> (R$/MWh)")

#py.offline.plot(fig, filename="C:\\Users\\Bernardo\\Downloads\\ena_carga_pld.html")

###PLDs ANUAIS SUBMERCADO
###PLDs ANUAIS SUBMERCADO
###PLDs ANUAIS SUBMERCADO



fig13 = go.Figure(data=[go.Table(header=dict(values=['Ano', 'PLD_SECO', 'PLD_SUL', 'PLD_NE', 'PLD_NORTE']),
                 cells=dict(values=[df_resampled_anual['Ano'], df_resampled_anual['PLD_SECO'], df_resampled_anual['PLD_SUL'], df_resampled_anual['PLD_NE'], df_resampled_anual['PLD_N']]))
                     ])

fig13.update_layout(title_text="PLDs SUBMERCADO - MÉDIA ANUAL (R$/MWh)", template='plotly')




# css
layout1 = html.Div(children=[
    
    html.Img(src='assets/vale.PNG', alt='image', width = '650'),
    
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
    dcc.Graph(id='vendas_por_loja10',figure=fig10),
    dcc.Graph(id='vendas_por_loja11',figure=fig11),
    dcc.Graph(id='vendas_por_loja12',figure=fig12),
    dcc.Graph(id='vendas_por_loja13',figure=fig13),    
    
])


# callbacks
# Adicione a rota raiz para o Dash
#app.config.suppress_callback_exceptions = True


######################### comeca aqui o segundo dash########################


#import dash
#from dash import dcc, html
#from dash.dependencies import Input, Output
#import plotly.graph_objects as go
#import pandas as pd
import plotly.express as px
#
# Função para converter datas explicitamente
def convert_date(date_str):
    try:
        return pd.to_datetime(date_str, format='%d/%m/%Y', dayfirst=True)
    except ValueError:
        # Se não for possível converter para data, retorna a string original
        return date_str

# DataFrame
df = pd.read_csv(r'assets/csv_historico_pld.csv', sep=';', decimal=',', converters={'Hora': convert_date})

# Lista de colunas de datas
colunas_datas = [coluna for coluna in df.columns if (coluna != 'Hora' and coluna != 'Submercado')]

# Paleta de cores automática do Plotly
cores_series = px.colors.qualitative.Set1  # Você pode escolher outras paletas do Plotly


# Layout da aplicação
layout2 = html.Div([
    html.H3("PLD Horário - Submercado (R$/MWh)", style={'font-family': 'Arial, sans-serif', 'font-weight': 'normal'}),
    html.Label("Selecione o dia:", style={'font-family': 'Arial, sans-serif', 'font-weight': 'normal'}),
    dcc.Dropdown(
        id='variavel-dropdown',
        options=[
            {'label': coluna, 'value': coluna} for coluna in colunas_datas
        ],
        value=colunas_datas[-1] if colunas_datas else None  # Valor padrão se houver colunas_datas, caso contrário, None
    ),
    dcc.Graph(id='line-plot')
])

# Callback para atualizar o gráfico com base na variável selecionada
@app.callback(
    Output('line-plot', 'figure'),
    [Input('variavel-dropdown', 'value')]
)
def update_graph(selected_variavel):
    if not selected_variavel:
        # Se não houver variável selecionada, retorne um gráfico vazio
        return go.Figure()

    fig = go.Figure()

    for i, submercado in enumerate(df['Submercado'].unique()):
        filtered_df = df[df['Submercado'] == submercado]
        cor_serie = cores_series[i % len(cores_series)]  # Ciclo de cores para as séries
        fig.add_trace(go.Scatter(x=filtered_df['Hora'], y=filtered_df[selected_variavel].astype(float), mode='lines+markers', name=submercado, line=dict(color=cor_serie)))

    # Adicionar marcador para a média após a última hora
    media_por_submercado = df.groupby('Submercado')[selected_variavel].apply(lambda x: x.astype(float).mean())
    for submercado, media in media_por_submercado.items():
        cor_serie = cores_series[df['Submercado'].unique().tolist().index(submercado) % len(cores_series)]  # Obter a cor correspondente
        fig.add_trace(go.Scatter(x=[24], y=[media], mode='markers', marker=dict(color=cor_serie), name=f'Média {submercado}', showlegend=False))

    fig.update_layout(
        title=f'Gráfico do PLD do dia {selected_variavel}',
        xaxis_title='Hora',
        yaxis_title='R$/MWh',
        xaxis=dict(
            tickmode='array',
            tickvals=list(range(24)) + [24],
            ticktext=list(map(str, range(24))) + ['Média'],
            tickangle=-40
        )
    )

    return fig

#########################################

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go



dfmercado = pd.read_excel(r'assets/me3.xlsx')


# Callback para atualizar o gráfico com base nas colunas selecionadas
@app.callback(
    Output('line-plot2', 'figure'),
    [Input('column-dropdown2', 'value')]
)
def update_graph(selected_columns):
    trace_list = []
    for col in selected_columns:
        trace = dict(
            x=dfmercado['data'],
            y=dfmercado[col],
            mode='lines',
            name=col
        )
        trace_list.append(trace)

    layout = dict(
        title='Preço de Mercado',
        xaxis=dict(tickangle=-80,tickformat='%d-%m-%Y', tickfont=dict(size=10)),
        yaxis=dict(title='R$/MWh'),
        hovermode='closest'
    )


    # Criando um gráfico responsivo
    figure = go.Figure(data=trace_list, layout=layout)

    return figure

    #return dict(data=trace_list, layout=layout)


# Layout3 - Responsivo usando Bootstrap
layout3 = html.Div([
    html.H3("Preço de Mercado (R$/MWh)", style={'font-family': 'Arial, sans-serif', 'font-weight': 'normal'}),  # Título do gráfico
    html.Label("Selecione o produto:", style={'font-family': 'Arial, sans-serif', 'font-weight': 'normal'}),
    dcc.Dropdown(
        id='column-dropdown2',
        options=[{'label': col, 'value': col} for col in dfmercado.columns[1:]],
        value=['FEN - SE CON ANU JAN/24 DEZ/24 - Preço Fixo'],
        multi=True
    ),
    dcc.Graph(id='line-plot2')
])


## Layout do aplicativo
#layout3 = html.Div([
#    html.Label("Selecione o produto:"),
#    dcc.Dropdown(
#        id='column-dropdown2',
#        options=[{'label': col, 'value': col} for col in dfmercado.columns[1:]],
#        value=['FEN - SE CON ANU JAN/24 DEZ/24 - Preço Fixo'],
#        multi=True
#    ),
#    dcc.Graph(id='line-plot2')
#])



##########################################
###GRáfico com as projeções###############
##########################################

from datetime import datetime
import locale
from locale import setlocale, LC_TIME

locale.setlocale(locale.LC_TIME, 'C')
#setlocale(LC_TIME, 'pt_BR.utf-8')

df_bd = pd.read_excel(r'assets/bd_rodada.xlsx')

# DataFrame A
A_data = {
    'Time': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01', '2024-06-01', '2024-07-01', '2024-08-01', '2024-09-01', '2024-10-01', '2024-11-01', '2024-12-01'],
    'mes_x': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
    'Curva A': ['24.6', '32.9', '41.3', '42.7', '42.1', '40.5', '37.8', '33.9', '29.4', '23.8', '21.4', '21.9'],
    'Curva B': ['34.3', '42', '49.7', '50.2', '48.9', '46.6', '43', '38.2', '33', '25.9', '21.4', '28.1'],
    'Curva C': ['45', '51.8', '58.6', '58.6', '56.9', '54.4', '50', '43.5', '37.6', '28.7', '21.4', '39.5'],
    'Variável': ['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0'],
    'Valor': [0.0] * 12
}

A = pd.DataFrame(A_data)

# DataFrame B
B_data = {
    'mes_x': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
    'Curva A': ['24.6', '32.9', '41.3', '42.7', '42.1', '40.5', '37.8', '33.9', '29.4', '23.8', '21.4', '21.9'],
    'Curva B': ['34.3', '42', '49.7', '50.2', '48.9', '46.6', '43', '38.2', '33', '25.9', '21.4', '28.1'],
    'Curva C': ['45', '51.8', '58.6', '58.6', '56.9', '54.4', '50', '43.5', '37.6', '28.7', '21.4', '39.5']
}

B = pd.DataFrame(B_data)



# Listas de colunas para cada Curva
curvas = ['Curva A', 'Curva B', 'Curva C']

# Dicionário para armazenar DataFrames resultantes
resultados = {}

# Loop para criar DataFrames C, D, e E
for curva in curvas:
    # Criar DataFrame temporário
    df_temp = pd.DataFrame({'Time': A['Time'], 'Variável': curva, 'Valor': A[curva]})
    
    # Adicionar ao dicionário de resultados
    resultados[curva] = df_temp[['Time', 'Variável', 'Valor']]
    
    
nomes_das_chaves = resultados.keys()
#print(nomes_das_chaves)

# Exibir DataFrames resultantes
#for curva, df_resultante in resultados.items():
    #print(f'\nDataFrame {curva}:\n{df_resultante}')

#valor_da_chave1 = resultados['Curva A']
#print(valor_da_chave1)  # Saída: valor1

df_C = resultados['Curva C']
df_C['Time'] = pd.to_datetime(df_C['Time']).dt.strftime('%b/%Y')
#print(df_C)

# Dicionário de tradução dos meses
#meses_em_ingles = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#meses_em_portugues = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

#traducao_meses = dict(zip(meses_em_portugues, meses_em_ingles))

## Substitua 'seu_dataframe' pelo nome real do seu DataFrame
#df_C['Time'] = df_C['Time'].apply(lambda x: datetime.strptime(x, '%b/%Y').replace(month=meses_em_portugues.index(x[:3]) + 1).strftime('%b/%Y').capitalize())



df_B = resultados['Curva B']
df_B['Time'] = pd.to_datetime(df_B['Time']).dt.strftime('%b/%Y')

df_A = resultados['Curva A']
df_A['Time'] = pd.to_datetime(df_A['Time']).dt.strftime('%b/%Y')


resultado_A = pd.concat([df_bd, resultados['Curva A']], axis=0)
resultado_B = pd.concat([resultado_A, resultados['Curva B']], axis=0)
resultado_C = pd.concat([resultado_B, df_C], axis=0)

print(resultado_C)

# Dicionário de tradução dos meses
traducao_meses = {'Jan': 'jan', 'Feb': 'fev', 'Mar': 'mar', 'Apr': 'abr', 'May': 'mai', 'Jun': 'jun', 'Jul': 'jul', 'Aug': 'ago', 'Sep': 'set', 'Oct': 'out', 'Nov': 'nov', 'Dec': 'dez'}

# Função para padronizar o formato das datas
def padronizar_data(data):
    # Separa o mês e o ano
    mes, ano = data.split('/')
    # Traduz o mês usando o dicionário
    mes_traduzido = traducao_meses.get(mes.capitalize(), mes)
    # Retorna a data formatada
    return f"{mes_traduzido}/{ano}"

# Aplica a função à coluna 'Time'
resultado_C['Time'] = resultado_C['Time'].apply(padronizar_data)

resultado_C['Valor'] = resultado_C['Valor'].astype('float') 

#resultado_C['Time'] = pd.to_datetime(resultado_C['Time'], format='%b/%Y')

#resultado_C['Time'] = pd.to_datetime(resultado_C['Time']).dt.strftime('%b/%Y')




dfbd = resultado_C


#display(df)

# Inicializando com a seleção de "PLD SE/CO VE"
variavel_selecionada = ["PLD SE/CO VE"]


# Layout do aplicativo
layout4 = html.Div([
     html.H3("Resultados simulação - Selecione uma variável", style={'font-family': 'Arial, sans-serif', 'font-weight': 'normal'}),  # Título do gráfico
     html.Label("Selecione a variável:", style={'font-family': 'Arial, sans-serif', 'font-weight': 'normal'}),
    # Dropdown para selecionar variável (múltipla seleção)
    dcc.Dropdown(
        id='variavel-dropdown4',
        options=[{'label': variavel, 'value': variavel} for variavel in dfbd['Variável'].unique()],
        value=variavel_selecionada,
        multi=True,
    ),
    # Gráfico de linhas e marcadores (scatter plot)
    dcc.Graph(id='line-plot4'),
])

# Callback para atualizar o gráfico com base na variável selecionada
@app.callback(
    Output('line-plot4', 'figure'),
    [Input('variavel-dropdown4', 'value')]
)
def update_line_plot(selected_variaveis):
    # Filtrando o DataFrame com base nas variáveis selecionadas
    filtered_df = dfbd[dfbd['Variável'].isin(selected_variaveis)]

    # Criando o gráfico de linhas e marcadores
    fig = go.Figure()
    for variavel in selected_variaveis:
        temp_df = filtered_df[filtered_df['Variável'] == variavel]
        fig.add_trace(go.Scatter(y=temp_df['Valor'], x=temp_df['Time'],mode='lines+markers', name=variavel))

    # Configurando o título dinâmico para o eixo y
    y_axis_title = " "#f'{",".join(selected_variaveis)}'
    fig.update_layout(yaxis_title=y_axis_title)

    return fig

##########################################
####CMARG MENSAL###
##########################################

colunas = []
for i in range(0, 61, 1):
    colunas.append(i)

print(colunas)
    

# Leitura do arquivo Excel
cmarg = pd.read_excel('assets/Produtos Novo.xlsx', sheet_name='cmarg001', usecols=colunas, nrows=2001)
cmarg = cmarg.drop('Unnamed: 0', axis=1)

# Criando faixas de valores
bins = [0, 62, 100, 200, 300, float('inf')]
labels = ['0-62 R$/MWh', '62.01-100 R$/MWh', '101-200 R$/MWh', '201-300 R$/MWh', '400+ R$/MWh']

# Inicializando os dados do gráfico
fig_data = []

# Loop pelas faixas de valores
for label in labels:
    # Inicializando dados para a faixa atual
    trace_data = []
    
    # Loop pelos meses
    for col in cmarg.columns:
        # Calculando percentuais para cada faixa de valores
        counts = pd.cut(cmarg[col], bins=bins, labels=labels, right=False, include_lowest=True).value_counts(sort=False).reindex(labels) / len(cmarg[col]) * 100
        
        # Criando o trace para o mês atual
        trace = go.Bar(
            x=[col],
            y=[counts[label].mean()],
            name=f'{col} - {label}',
            text=[f'{counts[label].mean():.2f}%'],
            textposition='auto'
        )
        trace_data.append(trace)
    
    # Consolidando a barra para a faixa atual no final de cada ano
    trace_consolidado = go.Bar(
        x=cmarg.columns,
        y=[trace.y[0] for trace in trace_data],
        name=f'{label}',
        text=[trace.text[0] for trace in trace_data],
        textposition='auto'
    )
    
    # Adicionando a barra consolidada aos dados do gráfico
    fig_data.append(trace_consolidado)

# Criando o layout do gráfico
layoutx = go.Layout(
    title='Cenário VE - Distribuição MENSAL do PLD SE/CO',
    #xaxis=dict(title='Mês'),
    yaxis=dict(title='Porcentagem (%)'),
    barmode='stack',
    
)

# Criando a figura do gráfico
fig = go.Figure(data=fig_data, layout=layoutx)

layout5 = html.Div(children=[dcc.Graph(figure=fig),])


################################################
##################Anual#########################
################################################


# Lista de anos
anos = cmarg.columns.str.extract('(\d{4})').squeeze().unique()

# Inicializando os dados do gráfico
fig_data = []

# Loop pelas faixas de valores
for label in labels:
    # Inicializando dados para a faixa atual
    trace_data = []
    
    # Loop pelos anos
    for ano in anos:
        # Filtrando dados do ano e faixa de valores
        cmarg_ano = cmarg.filter(regex=f"{ano}$")
        counts = pd.cut(cmarg_ano.values.flatten(), bins=bins, labels=labels, right=False, include_lowest=True).value_counts().reindex(labels) / len(cmarg_ano.values.flatten()) * 100
        
        # Criando o trace para o ano atual
        trace = go.Bar(
            x=[ano],
            y=[counts[label].mean()],
            name=f'{ano} - {label}',
            text=[f'{counts[label].mean():.2f}%'],
            textposition='auto'
        )
        trace_data.append(trace)
    
    # Consolidando a barra para a faixa atual no final de cada ano
    trace_consolidado = go.Bar(
        x=anos,
        y=[trace.y[0] for trace in trace_data],
        name=f'Total - {label}',
        text=[trace.text[0] for trace in trace_data],
        textposition='auto'
    )
    
    # Adicionando a barra consolidada aos dados do gráfico
    fig_data.append(trace_consolidado)

# Criando o layout do gráfico
layouty = go.Layout(
    title='Cenário VE - Distribuição ANUAL do PLD SE/CO',
    xaxis=dict(zeroline=False),
    yaxis=dict(title='Porcentagem (%)', zeroline=False),
    barmode='stack'
)

# Criando a figura do gráfico
fig = go.Figure(data=fig_data, layout=layouty)

layout6 = html.Div(children=[dcc.Graph(figure=fig),])


##########################
########GSF###############
##########################


# Leitura do arquivo Excel
cmarg = pd.read_excel('assets/Produtos Novo.xlsx', sheet_name='GSF', usecols=colunas, nrows=2001)
cmarg = cmarg.drop('Unnamed: 0', axis=1)

# Lista de anos
anos = cmarg.columns.str.extract('(\d{4})').squeeze().unique()

# Lista para armazenar os dados consolidados por ano
data_list = []

# Preparação dos dados
for ano in anos:
    cmarg_ano = cmarg.filter(regex=f"{ano}$")
    cmarg_ano_mean = cmarg_ano.mean(axis=1)
    data_list.append(pd.DataFrame({'Ano': [ano]*len(cmarg_ano_mean), 'GSF': cmarg_ano_mean}))

# Concatenação dos dados consolidados
cmarg_concatenado = pd.concat(data_list)

# Criação do box plot consolidado por ano
fig = px.box(cmarg_concatenado, x='Ano', y='GSF', points="all",
             title='Cenário VE - Distribuição ANUAL do GSF',
             labels={'GSF': 'GSF (%)'})

# Adição de uma linha de média ao gráfico
media_trace = go.Scatter(x=anos, y=cmarg_concatenado.groupby('Ano')['GSF'].mean(),
                         mode='lines+markers', name='Média')
fig.add_trace(media_trace)

# Atualização do layout
fig.update_layout(xaxis=dict(title=None,zeroline=False), yaxis=dict(title='GSF (%)', zeroline=False))

layout7 = html.Div(children=[dcc.Graph(figure=fig),])

####################################
##########   EAR   #################
####################################

# Leitura do arquivo Excel
cmarg = pd.read_excel('assets/Produtos Novo.xlsx', sheet_name='ear_sin', usecols=colunas, nrows=2001)
cmarg = cmarg.drop('Unnamed: 0', axis=1)

fig = px.box(cmarg, title="Cenário VE - Distribuição EMNSAL do EAR SIN", )  # points="all")
fig.update_layout(xaxis=dict(title=None, zeroline=False), boxmode='group')
fig.update_layout(yaxis=dict(title='EAR (%EARmáx)', zeroline=False), boxmode='group')

# Adição de uma linha de média ao gráfico
media_trace = go.Scatter(x=cmarg.columns, y=cmarg.mean(), mode='lines+markers', name='Média')
fig.add_trace(media_trace)

layout8 = html.Div(children=[dcc.Graph(figure=fig),])

##############################
##############################
##############################


# Layout geral
app.layout = html.Div(children=[
    
    # Áreas específicas de cada Dashboard
    layout1,
    layout2,
    layout3,
    layout5,
    layout6,
    layout7,
    layout8,
    layout4,
])


# callbacks
# Adicione a rota raiz para o Dash
app.config.suppress_callback_exceptions = True

# Imprime o link para acesso
#print("Running on http://127.0.0.1:8053/")

if __name__ == '__main__':
    app.run_server(debug=True)#, use_reloader=False, port=8053)