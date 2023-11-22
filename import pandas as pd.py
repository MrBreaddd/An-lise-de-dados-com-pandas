from IPython.display import display
import pandas as pd;


livros_df = pd.read_excel('Vendas rede de livrarias(os 100 titulos mais vendidos).xlsx');
#Abre a tabela e a atribui à variável livros_df

media_vendastotais = livros_df['Cópias vendidas'].mean();
#Destaca a coluna de copias vendidas, calcula a média dos valores e atribua à variável media_vendas


#display(livros_df['Gênero'].columns());