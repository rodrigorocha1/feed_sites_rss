from src.painel.model.noticias_model import NoticasModel


nm = NoticasModel()

noticias = nm.obter_todas_noticias(nome_site='G1')
print(type(noticias))
print(noticias.info())

for notica in noticias.itertuples(index=False):
    print(notica)
    print()
print(noticias.shape)
