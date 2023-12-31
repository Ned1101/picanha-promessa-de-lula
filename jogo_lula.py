#importando a biblioteca pygame
import pygame
#importando submodulo que contem as constantes e funções que será usado
from pygame.locals import *
#importando a função, que fecha a janela
from sys import exit
#importandoa random
import random

#iniciando todas as funções e variaveis do pygame
pygame.init()

#criando e definindo a janela
largura = 768
altura = 384
tela = pygame.display.set_mode((largura, altura))

#sprite de fundo
fundo = pygame.image.load('/storage/emulated/0/Pictures/PixelStation/fundoJogoLula.png')

#mudando o tamanho da imagem de fundo
largura_fundo = 128*6
altura_fundo = 64*6
sprite_fundo_redimensionada = pygame.transform.scale(fundo, (largura_fundo, altura_fundo))

#colocando um nome na janela
pygame.display.set_caption('Picanha: A Promessa de Lula')

#posição do lula
x = 20
y = 50

# Classe Lula
class Player(pygame.sprite.Sprite): # Herdando de uma outra classe, os atributos, métodos dessa classe.
	def __init__(self):
		# Inícializando a classe herdada
		pygame.sprite.Sprite.__init__(self)
		# Criando uma lista para armazenar as sprites
		self.sprite = [pygame.image.load('/storage/emulated/0/Pictures/PixelStation/lula.png')]
		self.image = self.sprite[0] # Atributos da classe sprite que vai receber o primeiro elemento da lista (o papai lula)
		self.image = pygame.transform.scale(self.image, (32*7, 32*7)) # Redimencionando o sprite
		 
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y) # Definindo a posição.
	
	# Metodo
	def andar(self, event):
		# Operando no celular
		if event.type == KEYDOWN:
			if event.key == K_a:
				self.rect.x -= 25
			elif event.key == K_d:
				self.rect.x += 25
			elif event.key == K_s:
				self.rect.y += 25
			elif event.key == K_w:
				self.rect.y -= 25
		'''
		#Operando no computador
		# Pressionando a tecla
		if event.key.get_pressed()[K_a]:
			self.rect.x = self.rect.x + 10
		elif event.key.get_pressed()[K_d]:
			self.rect.x = self.rect.x + 10
		elif event.key.get_pressed()[K_s]:
			self.rect.y = self.rect.y + 10
		elif event.key.get_pressed()[K_w]:
			self.rect.y = self.rect.y - 10
		'''
# Classe picanha
class Picanha(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.sprite = [pygame.image.load('/storage/emulated/0/Pictures/PixelStation/picanha.png')]
		self.image = self.sprite[0]
		self.image = pygame.transform.scale(self.image, (32*7, 32*7))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		
	# Método para aparecer picanha
	def aparecer(self, event):
		todas_as_sprites.add(self)
				
		
# Classe Npc
class Npc(pygame.sprite.Sprite):
	def __init__(self, sprite_path, posicao_x, posicao_y):
		pygame.sprite.Sprite.__init__(self)
		self.sprite = pygame.image.load(sprite_path)
		self.posicao_x = posicao_x
		self.posicao_y = posicao_y
		self.sprite = pygame.transform.scale(self.sprite, (32*7, 32*7))
		self.image = self.sprite
		self.rect = self.image.get_rect()
		self.rect.topleft = (posicao_x, posicao_y)


# Jogador e todos os npc
lula = Player()
picanha = Picanha()
npc_loira = Npc('/storage/emulated/0/Pictures/PixelStation/npcLula01.png', posicao_x = random.randint(192, 550), posicao_y = random.randint(0, 200))
npc_petista1 = Npc('/storage/emulated/0/Pictures/PixelStation/npcPetistaFanatico.png', posicao_x = random.randint(192, 550), posicao_y = random.randint(0, 200))
'''
npc_petista2 =Npc('/storage/emulated/0/Pictures/PixelStation/npcPetistaFanatica.png', posicao_x = random.randint(192, 550), posicao_y = random.randint(0, 200))
npc_bolsonarista1 = Npc('/storage/emulated/0/Pictures/PixelStation/npcBolsonarista01.png', posicao_x = random.randint(192, 550), posicao_y = random.randint(0, 200))
npc_bolsonarista2 = Npc('/storage/emulated/0/Pictures/PixelStation/npcBolsonarista02.png', posicao_x = random.randint(192, 550), posicao_y = random.randint(0, 200))
'''
npc_morena = Npc('/storage/emulated/0/Pictures/PixelStation/npcLula04.png', posicao_x = random.randint(192, 550), posicao_y = random.randint(0, 200))
npc_moreno = Npc('/storage/emulated/0/Pictures/PixelStation/npcLula02.png', posicao_x = random.randint(192, 550), posicao_y = random.randint(0, 200))
'''
npc_ruiva_falsa = Npc('/storage/emulated/0/Pictures/PixelStation/npcLula03.png', posicao_x = random.randint(192, 550), posicao_y = random.randint(0, 200))
npc_tio_da_cerveja = Npc('/storage/emulated/0/Pictures/PixelStation/npcTioCerveja.png', posicao_x = random.randint(192, 550), posicao_y = random.randint(0, 200))
'''
# Criando um grupo onde irá ficar todas as sprites
todas_as_sprites = pygame.sprite.Group()
todas_as_sprites.add(lula) # Adicionando o Lula nas sprites
#todas_as_sprites.add(npc_morena)
todas_as_sprites.add(npc_moreno)
todas_as_sprites.add(npc_loira)
todas_as_sprites.add(npc_petista1)

#para o frame do jogo
relogio = pygame.time.Clock()


# Variáveis responsáveis pelo manuseio da picanha, gosto de chama-los de interruptores.
picanha_nao_parada = True
movimentar_picanha= False
ativar_posicao_picanha = True
ativado = False

# Velocidade do movimento da picanha
velocidade = 5

# Criando o loop infinito e principal do jogo
while True:
    # Controlando os frames do jogo
    relogio.tick(60)
    # Limpando a tela e deixando de fundo preto
    tela.fill((0, 0, 0))
    
    if ativado:
    	ativar_posicao_picanha = False
    
    # Se estiver True, é porque a picanha não apareceu na tela e a posição da picanha é a mesma do Lula
    if picanha_nao_parada:
	    x_lula = lula.rect.x
	    y_lula = lula.rect.y
	    
	# Passando a posição do lula para a picanha
	# Se estiver desligado é porque a picanha apareceu na tela
    if ativar_posicao_picanha:
        picanha.rect.x = x_lula
        picanha.rect.y = y_lula
        
    # Loop que verifica se algum evento ocorreu
    for event in pygame.event.get():
        # Condição para fechar o jogo
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        if event.type == KEYDOWN:
        	lula.andar(event) # Chama o método 'andar' do objeto lula
        	if event.key == K_p:
        		picanha.aparecer(event)
        		movimentar_picanha = True
        		
    if movimentar_picanha:
        picanha.rect.x += velocidade
        picanha_nao_parada = False
        ativado = True
		     		
    tela.blit(sprite_fundo_redimensionada, (0, 0))
    todas_as_sprites.update()
    todas_as_sprites.draw(tela) # Desenhando todas as sprites na tela.
    # Atualizando a tela
    pygame.display.flip()
    
'''
algoritmo que irá fazer os npc aparecer aleatóriamente:
ele se basea em números aleatorios, cada npc será vinculado a um ou mais números. Se cair o número, o npc vinculados irá aparecer.

petistas = homem[1,3, 10], mulher[13]
bolsonaristas = homem[2] mulher[22]
npc loira = 4
npc moreno = 5
npc morena = 6
npc tio da cerveja = 7

 só pode aparecer um total de 3 npc na tela.
 
talvez o algoritmo tenha que ser implementado no grupo de sprites dentro do loop quando for desenhado com várias condições.
'''
