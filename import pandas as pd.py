from IPython.display import display
import pandas as pd;


livros_df = pd.read_excel('Vendas rede de livrarias(os 100 titulos mais vendidos).xlsx');
#Abre a tabela e a atribui à variável livros_df


##
#Qual a média de vendas da livraria?
##
media_vendastotais = livros_df['Cópias vendidas'].mean();
print("Média total de vendas da livraria:", media_vendastotais, "cópias.");
#Destaca a coluna de copias vendidas, calcula a média dos valores e atribua à variável media_vendas, então imprime o valor


###
#Qual o gênero que mais vendeu e o que menos vendeu?
###
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


###
#Qual a média de páginas dos top 10 livros?
###
livros_mais_vendidos = livros_df[['Título', 'Número de páginas', 'Cópias vendidas']].sort_values(by='Cópias vendidas', ascending=False).head(10);
#Organiza os top 10 livros levando em consideração o número de cópias vendidas

livros_mais_vendidos_media = livros_mais_vendidos['Número de páginas'].mean();
#Calcula a média de páginas e atribui à variável não estilizada

print("A média de páginas dos top 10 livros mais vendidos é de",livros_mais_vendidos_media , "páginas.");
#Imprime a média do número de páginas dos top 10


###
#Qual a editora que mais vendeu?
###
editora_vendas = livros_df[['Editora', 'Cópias vendidas']].groupby('Editora')['Cópias vendidas'].sum().reset_index();
#Organiza as vendas por nome de editora, forma alternativa e mais eficiente em comparação
# com o que foi feito com generos (linha 16 a 48).

editora_mais_vendas = editora_vendas.sort_values(by='Cópias vendidas', ascending=False).head(1).reset_index();
#Separa a editora com mais vendas.

print("A editora que mais vendeu é Intrínseca com", editora_mais_vendas['Cópias vendidas'].to_string(index=False), "cópias vendidas.");
#Imprime, forma alternativa de imprimir a partir de um dataframe


###
#Qual o autor que mais vendeu?
###
autor_vendas = livros_df[['Autor', 'Cópias vendidas']].groupby('Autor')['Cópias vendidas'].sum().reset_index();
#Organiza as vendas com base no nome do autor

autor_mais_vendas = autor_vendas.sort_values(by='Cópias vendidas', ascending=False).head(1);
#Separa o autor com mais vendas


print("O autor que mais vendeu é Stephen King com", autor_mais_vendas['Cópias vendidas'].to_string(index=False), "cópias vendidas.\n");

debug = input(str("Deseja ver os dados calculados não organizados? Y/F: "))
if debug == 'Y':
    print(media_vendastotais, ", ", genero_mais_vendido, ", ", genero_menos_vendido, ", ", livros_mais_vendidos_media, ", ", editora_mais_vendas, ", ", autor_mais_vendas);