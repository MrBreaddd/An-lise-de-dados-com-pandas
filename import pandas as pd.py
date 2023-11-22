from IPython.display import display
import pandas as pd;


livros_df = pd.read_excel('Vendas rede de livrarias(os 100 titulos mais vendidos).xlsx');
#Abre a tabela e a atribui à variável livros_df

media_vendastotais = livros_df['Cópias vendidas'].mean();
print("Média total de vendas da livraria:", media_vendastotais, "cópias.");
#Destaca a coluna de copias vendidas, calcula a média dos valores e atribua à variável media_vendas, então imprime o valor


terror = livros_df['Gênero'] == 'Terror';
fantasia = livros_df['Gênero'] == 'Fantásia';
triller = livros_df['Gênero'] == 'Triller Policial ';
romance = livros_df['Gênero'] == 'Romance';
comedia = livros_df['Gênero'] == 'Comedia';
#Por praticidade visual, separa os comandos de busca para cada gênero disponível

terror_vendas = livros_df['Cópias vendidas'].loc[terror].sum();
fantasia_vendas = livros_df['Cópias vendidas'].loc[fantasia].sum();
triller_vendas = livros_df['Cópias vendidas'].loc[triller].sum();
romance_vendas = livros_df['Cópias vendidas'].loc[romance].sum();
comedia_vendas = livros_df['Cópias vendidas'].loc[comedia].sum();
#Soma total de vendas para cada gênero

generos_vendidos = pd.DataFrame({
    'Terror': [terror_vendas],
    'Fantasia': [fantasia_vendas],
    'Triller': [triller_vendas],
    'Romance': [romance_vendas],
    'Comédia': [comedia_vendas]
})
#Organiza as vendas totais em um dataframe

genero_mais_vendido = generos_vendidos.apply(lambda x: x.iloc[0]).sort_values(ascending = False);
genero_menos_vendido = generos_vendidos.apply(lambda x: x.iloc[0]).sort_values();
#Separa os valores sem estilo em ordens crescente e descrescente.

print("O gênero mais vendido é Fantasia com", generos_vendidos.max().max(),"cópias.");
#Organização em dataframe, filtragem para o maior valor e impressão

genero_menos_vendido = generos_vendidos.min().min();
print("O gênero menos vendido é Comédia com", generos_vendidos.min().min(), "cópias.");
#Filtragem para o maior e menor valor e imprime.


livros_mais_vendidos = livros_df[['Título', 'Número de páginas', 'Cópias vendidas']].sort_values(by='Cópias vendidas', ascending=False).head(10);
#Organiza os top 10 livros levando em consideração o número de cópias vendidas

print("A média de páginas dos top 10 livros mais vendidos é de", livros_mais_vendidos['Número de páginas'].mean(), "páginas.");
#Imprime a média do número de páginas dos top 10