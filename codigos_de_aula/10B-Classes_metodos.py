#%% [markdown]
# ---
# ## Métodos Especiais

#%% [markdown]
# ---
# ##### Método `__init__`
# %%

class Playlist():
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        print(f"{musica} adicionada em {self.nome}!")
        self.musicas.append(musica)

mpb = Playlist(nome = "MPB")

mpb.adicionar_musica("A flor e o Espinho")        
mpb.adicionar_musica("Samba em preludio")

print(mpb.musicas)

#%% [markdown]
# ---
# ##### Método `__str__`
#%%
class Playlist():
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        print(f"{musica} adicionada em {self.nome}!")
        self.musicas.append(musica)

    def __str__(self):
        "É invocado sempre que se usar"
        "a função str() no objeto"

        return self.nome
        

mpb = Playlist(nome = "MPB")

mpb.adicionar_musica("A flor e o Espinho")        
mpb.adicionar_musica("Samba em preludio")

print(mpb)

#%% [markdown]
# ---
# ##### Método `__len__`
#%%
class Playlist():
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        print(f"{musica} adicionada em {self.nome}!")
        self.musicas.append(musica)

    def __str__(self):
        "É invocado sempre que se usar"
        "a função str() no objeto"

        return self.nome
    
    def __len__(self):
        "É invocado sempre que se usar"
        "a função len() no objeto"

        return len(self.musicas)

        

mpb = Playlist(nome = "MPB")

mpb.adicionar_musica("A flor e o Espinho")        
mpb.adicionar_musica("Samba em preludio")

print(len(mpb))

#%% [markdown]
# ---
# ##### Método `__getitem__`
#%%

class Playlist():
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        print(f"{musica} adicionada em {self.nome}!")
        self.musicas.append(musica)

    def __str__(self):
        "É invocado sempre que se usar"
        "a função str() no objeto"

        return self.nome
    
    def __len__(self):
        "É invocado sempre que se usar"
        "a função len() no objeto"

        return len(self.musicas)
    
    def __getitem__(self, index):

        return self.musicas[index]



mpb = Playlist(nome = "MPB")

mpb.adicionar_musica("A flor e o Espinho")        
mpb.adicionar_musica("Samba em preludio")
mpb.adicionar_musica("Trem das onze")

print(mpb[-1])

#%% [markdown]
# ---
# ##### Método `__add__`
#%%


class Playlist():
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        print(f"{musica} adicionada em {self.nome}!")
        self.musicas.append(musica)

    def print_musicas(self):
        for musica in self.musicas:
            print(musica)

    def __str__(self):
        "É invocado sempre que se usar"
        "a função str() no objeto"

        return self.nome
    
    def __len__(self):
        "É invocado sempre que se usar"
        "a função len() no objeto"

        return len(self.musicas)
    
    def __getitem__(self, index):

        return self.musicas[index]
    
    def __add__(self, outro_objeto):
        """Será invocado na operação +"""

        # checar se outro_objeto é uma playlist!
        if not isinstance(outro_objeto, type(self)):
            raise TypeError
        
        nova_playlist = Playlist(f"{self.nome} & {outro_objeto.nome}")
        nova_playlist.musicas = self.musicas + outro_objeto.musicas

        return nova_playlist



        

mpb = Playlist(nome = "MPB")

mpb.adicionar_musica("A flor e o Espinho")        
mpb.adicionar_musica("Samba em preludio")
mpb.adicionar_musica("Trem das onze")

rock = Playlist("Rock Nacional")

rock.adicionar_musica("Petróleo do Futuro")
rock.adicionar_musica("Eduardo e Mônica")
rock.adicionar_musica("Nessa terra de gigantes")

geral = mpb + rock

geral.print_musicas()