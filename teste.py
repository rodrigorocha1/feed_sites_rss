from src.painel.model.noticias_model import NoticasModel


nm = NoticasModel()

noticias = nm.obter_todas_noticias()
print(type(noticias))
print(noticias)
for noticia in noticias:
    print(noticia)
