# ✦ FOURMI DE LANGTON AMÉLIORÉE ✦ --------------------- Calixte Lamotte -----------------------------
#-----------------------------------------------------------------------------------------------------


# MODULES ✦ -----------------------------------------------------------------------------------------

import pygame
import numpy as np
import sys
import os
import webbrowser
import base64
import zlib

# Initialisation de Pygame
pygame.init()
pygame.mixer.init()  # Initialisation du mixeur pour la lecture audio


# CONSTANTES ✦ --------------------------------------------------------------------------------------

# Général
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 5  # Taille initiale d'une cellule en pixels
GRID_WIDTH = 200  # Nombre de cellules dans la largeur de la grille
GRID_HEIGHT = 200  # Nombre de cellules dans la hauteur de la grille
BG_COLOR = (255, 255, 255)  # Blanc
ANT_COLOR = (255, 0, 0)  # Rouge
CELL_ON_COLOR = (0, 0, 0)  # Noir
FPS = 60

# Constantes des boutons
BUTTON_WIDTH = 80
BUTTON_HEIGHT = 30
BUTTON_MARGIN = 10
BUTTON_COLOR = (0, 0, 0)  # Noir
BUTTON_HOVER_COLOR = (100, 100, 100)  # Gris clair
BUTTON_TEXT_COLOR = (255, 255, 255)  # Blanc
BUTTON_FONT_SIZE = 14
BUTTON_BORDER_RADIUS = 5

# Constantes du bouton de sortie
EXIT_BUTTON_X = WINDOW_WIDTH - BUTTON_WIDTH - BUTTON_MARGIN
EXIT_BUTTON_Y = BUTTON_MARGIN
EXIT_BUTTON_TEXT = "EXIT"

# Constantes du bouton d'information
INFO_BUTTON_X = WINDOW_WIDTH - BUTTON_WIDTH - BUTTON_MARGIN
INFO_BUTTON_Y = EXIT_BUTTON_Y + BUTTON_HEIGHT + BUTTON_MARGIN
INFO_BUTTON_TEXT = "INFO"

# Constantes du bouton de menu
MENU_BUTTON_X = WINDOW_WIDTH - BUTTON_WIDTH - BUTTON_MARGIN
MENU_BUTTON_Y = INFO_BUTTON_Y + BUTTON_HEIGHT + BUTTON_MARGIN
MENU_BUTTON_TEXT = "MENU"

# Constantes des options du menu
MENU_OPEN = False  # Suivi de l'état d'ouverture du menu
SPEED_BUTTON_X = MENU_BUTTON_X + -95
SPEED_BUTTON_Y = MENU_BUTTON_Y + BUTTON_HEIGHT + BUTTON_MARGIN
SPEED_BUTTON_WIDTH = 120
SPEED_BUTTON_HEIGHT = BUTTON_HEIGHT
SPEED_BUTTON_TEXT = "VITESSE"

# Champ de saisie de vitesse
SPEED_INPUT_X = SPEED_BUTTON_X + SPEED_BUTTON_WIDTH + 5
SPEED_INPUT_Y = SPEED_BUTTON_Y
SPEED_INPUT_WIDTH = 50
SPEED_INPUT_HEIGHT = BUTTON_HEIGHT
SPEED_INPUT_ACTIVE = False
SPEED_INPUT_TEXT = "0.3"

# Bouton Pause/Lecture
PAUSE_BUTTON_X = MENU_BUTTON_X
PAUSE_BUTTON_Y = SPEED_BUTTON_Y + BUTTON_HEIGHT + BUTTON_MARGIN
PAUSE_BUTTON_WIDTH = BUTTON_WIDTH
PAUSE_BUTTON_HEIGHT = BUTTON_HEIGHT
PAUSE_BUTTON_TEXT = "PAUSE"
PLAY_BUTTON_TEXT = "PLAY"

# Bouton de modification des pixels
MODIFY_BUTTON_X = MENU_BUTTON_X + -40
MODIFY_BUTTON_Y = PAUSE_BUTTON_Y + BUTTON_HEIGHT + BUTTON_MARGIN
MODIFY_BUTTON_WIDTH = BUTTON_WIDTH + 40
MODIFY_BUTTON_HEIGHT = BUTTON_HEIGHT
MODIFY_BUTTON_TEXT = "MODIFY PIXELS"
MODIFY_MODE = False  # Suivi du mode de modification
MODIFY_HIGHLIGHT_COLOR = (170, 0, 170)  # Couleur mauve pour le surlignage

# Bouton de réinitialisation
RESET_BUTTON_X = MENU_BUTTON_X
RESET_BUTTON_Y = MODIFY_BUTTON_Y + BUTTON_HEIGHT + BUTTON_MARGIN
RESET_BUTTON_WIDTH = BUTTON_WIDTH
RESET_BUTTON_HEIGHT = BUTTON_HEIGHT
RESET_BUTTON_TEXT = "RESET"

# Constantes du bouton de sentier
TRAIL_BUTTON_X = MENU_BUTTON_X
TRAIL_BUTTON_Y = RESET_BUTTON_Y + BUTTON_HEIGHT + BUTTON_MARGIN
TRAIL_BUTTON_WIDTH = BUTTON_WIDTH
TRAIL_BUTTON_HEIGHT = BUTTON_HEIGHT
TRAIL_BUTTON_TEXT = "TRAIL"
TRAIL_COLOR = (255, 0, 0)  # Rouge

# Constantes des boutons d'import/export
EXPORT_BUTTON_X = MENU_BUTTON_X
EXPORT_BUTTON_Y = TRAIL_BUTTON_Y + BUTTON_HEIGHT + BUTTON_MARGIN
EXPORT_BUTTON_WIDTH = BUTTON_WIDTH
EXPORT_BUTTON_HEIGHT = BUTTON_HEIGHT
EXPORT_BUTTON_TEXT = "EXPORT"

IMPORT_BUTTON_X = MENU_BUTTON_X
IMPORT_BUTTON_Y = EXPORT_BUTTON_Y + BUTTON_HEIGHT + BUTTON_MARGIN
IMPORT_BUTTON_WIDTH = BUTTON_WIDTH
IMPORT_BUTTON_HEIGHT = BUTTON_HEIGHT
IMPORT_BUTTON_TEXT = "IMPORT"

# Constantes des champs de texte
TEXT_FIELD_WIDTH = 200
TEXT_FIELD_HEIGHT = BUTTON_HEIGHT
TEXT_FIELD_X = EXPORT_BUTTON_X - TEXT_FIELD_WIDTH - 5  # 5 pixels de marge
TEXT_FIELD_COLOR = (100, 100, 100)  # Même couleur que les boutons
TEXT_FIELD_ACTIVE_COLOR = (255, 255, 255)  # Blanc
TEXT_FIELD_TEXT_COLOR = (0, 0, 0)  # Noir
TEXT_FIELD_FONT_SIZE = 12

# Constantes de l'écran d'information
INFO_MODE = False  # Suivi de l'affichage de l'écran d'information
INFO_IMAGE_PATH = os.path.join("assets", "Info.png")
INFO_IMAGE_WIDTH = 500  # Largeur de l'image d'information
INFO_IMAGE_HEIGHT = 500  # Hauteur de l'image d'information
INFO_IMAGE_X = WINDOW_WIDTH // 2 - INFO_IMAGE_WIDTH // 2  # Centré horizontalement
INFO_IMAGE_Y = WINDOW_HEIGHT // 2 - INFO_IMAGE_HEIGHT // 2  # Centré verticalement

# Constantes du bouton de lien vidéo
VIDEO_BUTTON_WIDTH = 120
VIDEO_BUTTON_HEIGHT = 40
VIDEO_BUTTON_X = WINDOW_WIDTH // 2 - VIDEO_BUTTON_WIDTH // 2 + 100 # Centré horizontalement
VIDEO_BUTTON_Y = INFO_IMAGE_Y + INFO_IMAGE_HEIGHT + -130  # En dessous de l'image d'information
VIDEO_BUTTON_TEXT = "LIEN VIDEO"
VIDEO_URL = "https://youtu.be/qZRYGxF6D3w?si=XcB8ibW5AP98eqRa"

# Fichiers sonores
START_SOUND = pygame.mixer.Sound(os.path.join("assets", "start.mp3"))
WHITE_TO_BLACK_SOUND = pygame.mixer.Sound(os.path.join("assets", "2-bell.mp3"))
BLACK_TO_WHITE_SOUND = pygame.mixer.Sound(os.path.join("assets", "1-bell.mp3"))

# Constantes du texte d'attribution
ATTRIBUTION_TEXT = "2025 · @Calixte Lamotte"
ATTRIBUTION_X = WINDOW_WIDTH // 2  # Centré horizontalement
ATTRIBUTION_Y = WINDOW_HEIGHT - 15  # 15 pixels du bas

# Constantes du bouton compteur de pas
STEPS_BUTTON_WIDTH = BUTTON_WIDTH + 40
STEPS_BUTTON_X = WINDOW_WIDTH // 2 - STEPS_BUTTON_WIDTH // 2  # Centré en utilisant la largeur du bouton
STEPS_BUTTON_Y = ATTRIBUTION_Y - BUTTON_HEIGHT - 10  # Au-dessus de l'attribution avec une marge de 10px
STEPS_BUTTON_HEIGHT = BUTTON_HEIGHT

# Constantes du bouton multiplicateur de vitesse
SPEED_MULT_BUTTON_WIDTH = BUTTON_WIDTH
SPEED_MULT_BUTTON_X = 10  # 10 pixels du bord gauche
SPEED_MULT_BUTTON_Y = WINDOW_HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN  # Même hauteur que le bouton EXIT
SPEED_MULT_BUTTON_HEIGHT = BUTTON_HEIGHT
SPEED_MULT_BUTTON_TEXT = "×6"

# Constantes du texte du titre
TITLE_TEXT = "FOURMI DE LANGTON AMÉLIORÉE"
TITLE_X = WINDOW_WIDTH // 2  # Centré horizontalement
TITLE_Y = 25  # 30 pixels du haut
TITLE_SIZE = 25  # Taille de police

# Constantes du texte d'instruction
INSTRUCTION_TEXT = "ZOOM / PAN AVEC LA SOURIS"
INSTRUCTION_X = WINDOW_WIDTH // 2  # Centré horizontalement
INSTRUCTION_Y = 50  # Ajusté pour être sous le titre
INSTRUCTION_SIZE = 12  # Taille de police

# Paramètres de simulation
SIMULATION_SPEED = 0.3  # Pas par image (supporte maintenant les valeurs fractionnaires)


# MAIN ✦ ---------------------------------------------------------------------------------------

class LangtonAnt:
    def __init__(self, grid_width, grid_height):
        # Initialisation de la grille avec toutes les cellules éteintes (0)
        self.grid = np.zeros((grid_width, grid_height), dtype=int)
        
        # Placer la fourmi au milieu de la grille
        self.ant_x = grid_width // 2
        self.ant_y = grid_height // 2
        
        # Direction: 0=haut, 1=droite, 2=bas, 3=gauche
        self.direction = 0
        
        # Vecteurs de mouvement pour chaque direction
        self.movement = [
            (0, -1),  # Haut
            (1, 0),   # Droite
            (0, 1),   # Bas
            (-1, 0)   # Gauche
        ]
        
        self.steps = 0
        
        # Liste pour stocker les positions du sentier
        self.trail = []
    
    def step(self):
        """Effectue une étape de l'algorithme de la fourmi de Langton"""
        # Obtenir l'état actuel de la cellule
        current_cell = self.grid[self.ant_x, self.ant_y]
        
        # Inverser l'état de la cellule
        self.grid[self.ant_x, self.ant_y] = 1 - current_cell
        
        # Jouer le son approprié en fonction de la transition
        if current_cell == 0:
            # Transition blanc vers noir
            WHITE_TO_BLACK_SOUND.play()
            self.direction = (self.direction + 1) % 4  # Tourner à droite (sens horaire)
        else:
            # Transition noir vers blanc
            BLACK_TO_WHITE_SOUND.play()
            self.direction = (self.direction - 1) % 4  # Tourner à gauche (sens anti-horaire)
        
        # Ajouter la position actuelle au sentier avant de se déplacer
        self.trail.append((self.ant_x, self.ant_y))
        
        # Avancer
        dx, dy = self.movement[self.direction]
        self.ant_x = (self.ant_x + dx) % self.grid.shape[0]
        self.ant_y = (self.ant_y + dy) % self.grid.shape[1]
        
        self.steps += 1
    
    def clear_trail(self):
        """Efface le sentier de la fourmi"""
        self.trail = []

class Simulation:
    def __init__(self):
        # Créer une fenêtre sans bordure
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.NOFRAME)
        pygame.display.set_caption("Fourmi de Langton Améliorée")
        self.clock = pygame.time.Clock()
        
        self.ant = LangtonAnt(GRID_WIDTH, GRID_HEIGHT)
        
        # Paramètres de vue
        self.offset_x = WINDOW_WIDTH // 2 - GRID_WIDTH * GRID_SIZE // 2
        self.offset_y = WINDOW_HEIGHT // 2 - GRID_HEIGHT * GRID_SIZE // 2
        self.zoom = GRID_SIZE
        
        # État de la souris
        self.panning = False
        self.last_mouse_pos = (0, 0)
        self.hovered_cell = (-1, -1)  # Suivi de la cellule actuellement survolée
        self.hovered_button = None  # Suivi du bouton actuellement survolé
        self.mouse_button_down = False  # Suivi si le bouton de la souris est maintenu enfoncé
        self.last_modified_cell = None  # Suivi de la dernière cellule modifiée
        self.speed_mult_button_pressed = False  # Suivi de l'état du bouton multiplicateur de vitesse
        
        # État de la simulation
        self.running = True
        self.paused = False
        
        # État du menu
        self.menu_open = MENU_OPEN
        self.speed_input_active = SPEED_INPUT_ACTIVE
        self.speed_input_text = SPEED_INPUT_TEXT
        self.modify_mode = MODIFY_MODE
        self.modify_cooldown = 0  # Minuteur de délai pour le mode de modification
        
        # État du sentier
        self.trail_active = False
        
        # État des champs d'import/export
        self.export_field_active = False
        self.import_field_active = False
        self.export_text = ""
        self.import_text = ""
        
        # État de l'info
        self.info_mode = INFO_MODE
        # Charger l'image d'information
        try:
            self.info_image = pygame.image.load(INFO_IMAGE_PATH)
            self.info_image = pygame.transform.scale(self.info_image, (INFO_IMAGE_WIDTH, INFO_IMAGE_HEIGHT))
        except pygame.error:
            # Créer un espace réservé si l'image ne peut pas être chargée
            self.info_image = pygame.Surface((INFO_IMAGE_WIDTH, INFO_IMAGE_HEIGHT))
            self.info_image.fill((200, 200, 200))  # Fond gris clair
            font = pygame.font.SysFont("Arial", 30)
            text = font.render("Image d'Info Non Trouvée", True, (0, 0, 0))
            text_rect = text.get_rect(center=(INFO_IMAGE_WIDTH//2, INFO_IMAGE_HEIGHT//2))
            self.info_image.blit(text, text_rect)
        
        # Pour gérer les vitesses fractionnaires
        self.step_accumulator = 0.0
        
        # Définir le curseur par défaut sur une main ouverte
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        
        # Préparer les polices
        self.attribution_font = pygame.font.SysFont("Arial", 10)
        self.instruction_font = pygame.font.SysFont("Arial", INSTRUCTION_SIZE)
        self.title_font = pygame.font.SysFont("Arial", TITLE_SIZE, bold=True)
        self.button_font = pygame.font.SysFont("Arial", BUTTON_FONT_SIZE, bold=True)
    
    def modify_cell(self, grid_x, grid_y):
        """Fonction d'aide pour modifier une cellule et jouer le son approprié"""
        if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
            current_cell = self.ant.grid[grid_x, grid_y]
            self.ant.grid[grid_x, grid_y] = 1 - current_cell
            
            # Jouer le son approprié en fonction de la transition
            if current_cell == 0:
                # Transition blanc vers noir
                WHITE_TO_BLACK_SOUND.play()
            else:
                # Transition noir vers blanc
                BLACK_TO_WHITE_SOUND.play()
            
            return True
        return False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_r:
                    self.ant = LangtonAnt(GRID_WIDTH, GRID_HEIGHT)
                    self.step_accumulator = 0.0  # Réinitialiser l'accumulateur lors de la réinitialisation
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
                
                # Gérer le champ de saisie de vitesse
                if self.speed_input_active:
                    if event.key == pygame.K_RETURN:
                        # Soumettre la valeur de vitesse
                        try:
                            new_speed = float(self.speed_input_text)
                            if new_speed > 0:
                                global SIMULATION_SPEED
                                SIMULATION_SPEED = new_speed
                        except ValueError:
                            # Entrée invalide, réinitialiser à la vitesse actuelle
                            self.speed_input_text = str(SIMULATION_SPEED)
                        self.speed_input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.speed_input_text = self.speed_input_text[:-1]
                    else:
                        # N'ajouter que des chiffres et le point décimal
                        if event.unicode.isdigit() or event.unicode == '.':
                            self.speed_input_text += event.unicode
                
                # Gérer le champ d'importation
                elif self.import_field_active:
                    if event.key == pygame.K_RETURN:
                        # Tenter d'importer le modèle
                        self.import_design()
                        self.import_field_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.import_text = self.import_text[:-1]
                    elif event.key == pygame.K_v and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                        # Coller le contenu du presse-papiers lors de Ctrl+V
                        try:
                            pygame.scrap.init()
                            clipboard_content = pygame.scrap.get(pygame.SCRAP_TEXT)
                            if clipboard_content:
                                # Décoder le contenu du presse-papiers et le nettoyer
                                clipboard_text = clipboard_content.decode('utf-8').strip()
                                self.import_text = clipboard_text
                                print(f"Collé depuis le presse-papiers: {len(clipboard_text)} caractères")
                        except Exception as e:
                            print(f"Erreur lors du collage: {e}")
                    else:
                        # Autoriser tous les caractères pour le code d'import
                        # Mais limiter la longueur pour éviter les problèmes de rendu
                        if len(self.import_text) < 1000:  # Limite raisonnable
                            self.import_text += event.unicode
            
            # Contrôles de souris pour les boutons et le déplacement
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                # Vérifier si le bouton multiplicateur de vitesse est cliqué
                if self.is_point_in_rect(mouse_pos, (SPEED_MULT_BUTTON_X, SPEED_MULT_BUTTON_Y, SPEED_MULT_BUTTON_WIDTH, SPEED_MULT_BUTTON_HEIGHT)):
                    self.speed_mult_button_pressed = True
                    return
                
                # Gérer les événements de la molette de souris
                if event.button in (4, 5):  # Molette vers le haut/bas
                    self.zoom_at_point(mouse_pos, 1 if event.button == 4 else -1)
                # Gérer le bouton gauche de la souris
                elif event.button == pygame.BUTTON_LEFT:
                    self.mouse_button_down = True  # Définir l'état du bouton de la souris comme enfoncé
                    self.last_modified_cell = None  # Réinitialiser la dernière cellule modifiée
                    
                    # Vérifier d'abord les clics sur les boutons
                    if self.is_point_in_rect(mouse_pos, (EXIT_BUTTON_X, EXIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)):
                        # Bouton de sortie cliqué
                        self.running = False
                    elif self.is_point_in_rect(mouse_pos, (INFO_BUTTON_X, INFO_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)):
                        # Bouton d'info cliqué - afficher l'écran d'info
                        if self.menu_open:
                            self.menu_open = False  # Fermer le menu
                        self.info_mode = not self.info_mode  # Basculer le mode info
                    elif self.info_mode and self.is_point_in_rect(mouse_pos, (VIDEO_BUTTON_X, VIDEO_BUTTON_Y, VIDEO_BUTTON_WIDTH, VIDEO_BUTTON_HEIGHT)):
                        # Bouton vidéo cliqué - ouvrir l'URL
                        webbrowser.open(VIDEO_URL)
                    elif self.is_point_in_rect(mouse_pos, (MENU_BUTTON_X, MENU_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)):
                        # Bouton menu cliqué - basculer le menu
                        self.menu_open = not self.menu_open
                    elif self.menu_open:
                        # Vérifier les boutons d'options du menu uniquement si le menu est ouvert
                        if self.is_point_in_rect(mouse_pos, (SPEED_BUTTON_X, SPEED_BUTTON_Y, SPEED_BUTTON_WIDTH, SPEED_BUTTON_HEIGHT)):
                            # Bouton de vitesse cliqué - pas de fonctionnalité autre que la mise en évidence du champ de saisie
                            pass
                        elif self.is_point_in_rect(mouse_pos, (SPEED_INPUT_X, SPEED_INPUT_Y, SPEED_INPUT_WIDTH, SPEED_INPUT_HEIGHT)):
                            # Champ de saisie de vitesse cliqué
                            self.speed_input_active = True
                            # Réinitialiser le texte de saisie s'il s'agit de la valeur par défaut
                            if self.speed_input_text == "0.3" and SIMULATION_SPEED != 0.3:
                                self.speed_input_text = str(SIMULATION_SPEED)
                        elif self.is_point_in_rect(mouse_pos, (PAUSE_BUTTON_X, PAUSE_BUTTON_Y, PAUSE_BUTTON_WIDTH, PAUSE_BUTTON_HEIGHT)):
                            # Bouton Pause/Lecture cliqué
                            self.paused = not self.paused
                        elif self.is_point_in_rect(mouse_pos, (MODIFY_BUTTON_X, MODIFY_BUTTON_Y, MODIFY_BUTTON_WIDTH, MODIFY_BUTTON_HEIGHT)):
                            # Basculer le mode de modification et définir le délai
                            self.modify_mode = not self.modify_mode
                            self.modify_cooldown = 10  # Définir le délai à 10 images (environ 1/6 de seconde)
                        elif self.is_point_in_rect(mouse_pos, (RESET_BUTTON_X, RESET_BUTTON_Y, RESET_BUTTON_WIDTH, RESET_BUTTON_HEIGHT)):
                            # Bouton de réinitialisation cliqué
                            self.ant = LangtonAnt(GRID_WIDTH, GRID_HEIGHT)
                            self.step_accumulator = 0.0  # Réinitialiser l'accumulateur lors de la réinitialisation
                        elif self.is_point_in_rect(mouse_pos, (TRAIL_BUTTON_X, TRAIL_BUTTON_Y, TRAIL_BUTTON_WIDTH, TRAIL_BUTTON_HEIGHT)):
                            # Bouton de sentier cliqué
                            self.trail_active = not self.trail_active
                            if self.trail_active:
                                # Démarrer un nouveau sentier à partir de la position actuelle
                                self.ant.clear_trail()
                                # Ajouter uniquement la position actuelle comme point de départ
                                self.ant.trail.append((self.ant.ant_x, self.ant.ant_y))
                            else:
                                # Effacer le sentier si désactivé
                                self.ant.clear_trail()
                        elif self.is_point_in_rect(mouse_pos, (EXPORT_BUTTON_X, EXPORT_BUTTON_Y, EXPORT_BUTTON_WIDTH, EXPORT_BUTTON_HEIGHT)):
                            # Bouton d'exportation cliqué
                            self.export_field_active = not self.export_field_active
                            if self.export_field_active:
                                # Générer le code d'exportation
                                self.export_text = self.export_design()
                                # Désactiver le champ d'importation si actif
                                self.import_field_active = False
                        elif self.is_point_in_rect(mouse_pos, (IMPORT_BUTTON_X, IMPORT_BUTTON_Y, IMPORT_BUTTON_WIDTH, IMPORT_BUTTON_HEIGHT)):
                            # Bouton d'importation cliqué
                            self.import_field_active = not self.import_field_active
                            if self.import_field_active:
                                # Réinitialiser le texte d'importation
                                self.import_text = ""
                                # Désactiver le champ d'exportation si actif
                                self.export_field_active = False
                        # Vérifier si un champ de texte est cliqué
                        elif self.export_field_active and self.is_point_in_rect(mouse_pos, (TEXT_FIELD_X, EXPORT_BUTTON_Y, TEXT_FIELD_WIDTH, TEXT_FIELD_HEIGHT)):
                            # Sélectionner tout le texte pour faciliter la copie
                            try:
                                # Initialiser le presse-papiers et copier le texte
                                pygame.scrap.init()
                                pygame.scrap.put(pygame.SCRAP_TEXT, self.export_text.encode())
                                print("Code d'exportation copié dans le presse-papiers.")
                            except Exception as e:
                                print(f"Erreur lors de la copie: {e}")
                        elif self.import_field_active and self.is_point_in_rect(mouse_pos, (TEXT_FIELD_X, IMPORT_BUTTON_Y, TEXT_FIELD_WIDTH, TEXT_FIELD_HEIGHT)):
                            # Activer le champ d'importation pour la saisie
                            pass
                        # Si aucun des boutons du menu n'a été cliqué, continuer avec d'autres vérifications
                        else:
                            # Gérer d'autres actions de la souris
                            self.handle_other_mouse_actions(event, mouse_pos)
                    else:
                        # Si aucun bouton n'est cliqué, gérer d'autres actions de la souris
                        self.handle_other_mouse_actions(event, mouse_pos)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:  # Ne gérer que le bouton gauche de la souris
                    self.panning = False
                    self.mouse_button_down = False  # Définir l'état du bouton de la souris comme relâché
                    self.last_modified_cell = None  # Réinitialiser la dernière cellule modifiée
                    self.speed_mult_button_pressed = False  # Réinitialiser l'état du bouton multiplicateur
                    # Changer le curseur en main ouverte lorsqu'il n'y a pas de déplacement
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            
            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                
                # Mettre à jour la cellule survolée
                if self.modify_mode:
                    # Convertir les coordonnées de l'écran en coordonnées de grille
                    grid_x = int((mouse_pos[0] - self.offset_x) / self.zoom)
                    grid_y = int((mouse_pos[1] - self.offset_y) / self.zoom)
                    
                    # Vérifier si c'est dans les limites de la grille
                    if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                        self.hovered_cell = (grid_x, grid_y)
                        
                        # Si le bouton de la souris est enfoncé, gérer la modification continue
                        if self.mouse_button_down and self.modify_cooldown <= 0:
                            current_cell = (grid_x, grid_y)
                            
                            # Si c'est une nouvelle cellule et pas la dernière modifiée
                            if current_cell != self.last_modified_cell:
                                # Modifier la cellule actuelle
                                if self.modify_cell(grid_x, grid_y):
                                    self.last_modified_cell = current_cell
                                    
                                    # Si nous avons une dernière cellule modifiée, interpoler entre les positions
                                    if self.last_modified_cell is not None:
                                        last_x, last_y = self.last_modified_cell
                                        # Calculer la distance entre les cellules
                                        dx = grid_x - last_x
                                        dy = grid_y - last_y
                                        
                                        # Si la distance est supérieure à 1, interpoler
                                        if abs(dx) > 1 or abs(dy) > 1:
                                            # Calculer le nombre d'étapes nécessaires
                                            steps = max(abs(dx), abs(dy))
                                            for i in range(1, steps):
                                                # Calculer la position intermédiaire
                                                inter_x = last_x + (dx * i) // steps
                                                inter_y = last_y + (dy * i) // steps
                                                # Modifier la cellule intermédiaire
                                                self.modify_cell(inter_x, inter_y)
                    else:
                        self.hovered_cell = (-1, -1)
                else:
                    # Réinitialiser la cellule survolée lorsqu'il n'est pas en mode de modification
                    self.hovered_cell = (-1, -1)
                
                # Mettre à jour l'état du bouton survolé
                self.update_hovered_button(mouse_pos)
                
                if self.panning:
                    dx = mouse_pos[0] - self.last_mouse_pos[0]
                    dy = mouse_pos[1] - self.last_mouse_pos[1]
                    self.offset_x += dx
                    self.offset_y += dy
                    self.last_mouse_pos = mouse_pos
    
    def is_point_in_rect(self, point, rect):
        """Vérifie si un point est à l'intérieur d'un rectangle défini par (x, y, largeur, hauteur)"""
        x, y = point
        rect_x, rect_y, rect_width, rect_height = rect
        return rect_x <= x <= rect_x + rect_width and rect_y <= y <= rect_y + rect_height
    
    def zoom_at_point(self, pos, zoom_change):
        """Zoomer ou dézoomer centré sur la position du curseur"""
        # Obtenir la position de la souris avant le zoom
        mouse_x, mouse_y = pos
        
        # Convertir les coordonnées de l'écran en coordonnées de grille
        grid_x = (mouse_x - self.offset_x) / self.zoom
        grid_y = (mouse_y - self.offset_y) / self.zoom
        
        # Appliquer le changement de zoom
        old_zoom = self.zoom
        self.zoom = max(1, min(50, self.zoom + zoom_change))
        
        # Calculer le nouveau décalage pour garder le point sous le curseur au même endroit
        self.offset_x = int(mouse_x - grid_x * self.zoom)
        self.offset_y = int(mouse_y - grid_y * self.zoom)
    
    def update(self):
        if not self.paused:
            # Calculer la vitesse effective en fonction de l'état du bouton multiplicateur
            effective_speed = SIMULATION_SPEED * 4 if self.speed_mult_button_pressed else SIMULATION_SPEED
            
            # Accumuler les pas en fonction de la vitesse de simulation
            self.step_accumulator += effective_speed
            
            # Effectuer des pas entiers lorsque l'accumulateur atteint ou dépasse 1.0
            while self.step_accumulator >= 1.0:
                self.ant.step()
                self.step_accumulator -= 1.0
        
        # Mettre à jour le délai du mode de modification
        if self.modify_cooldown > 0:
            self.modify_cooldown -= 1
    
    def render(self):
        self.screen.fill(BG_COLOR)
        
        # Calculer la partie visible de la grille
        visible_start_x = max(0, int(-self.offset_x // self.zoom))
        visible_end_x = min(GRID_WIDTH, int(visible_start_x + (WINDOW_WIDTH // self.zoom) + 2))
        visible_start_y = max(0, int(-self.offset_y // self.zoom))
        visible_end_y = min(GRID_HEIGHT, int(visible_start_y + (WINDOW_HEIGHT // self.zoom) + 2))
        
        # Dessiner les cellules de la grille avec des coins arrondis
        for x in range(visible_start_x, visible_end_x):
            for y in range(visible_start_y, visible_end_y):
                # Créer le rectangle de la cellule
                cell_rect = pygame.Rect(
                    int(self.offset_x + x * self.zoom), 
                    int(self.offset_y + y * self.zoom), 
                    int(self.zoom), 
                    int(self.zoom)
                )
                
                # Définir le rayon pour les coins arrondis
                radius = max(1, min(int(self.zoom * 0.3), 10))  # Mettre à l'échelle le rayon avec le zoom, mais le plafonner
                
                # Déterminer la couleur de la cellule en fonction de l'état et du survol
                if self.modify_mode and self.hovered_cell == (x, y):
                    # Dessiner la cellule survolée avec la couleur de surbrillance
                    pygame.draw.rect(self.screen, MODIFY_HIGHLIGHT_COLOR, cell_rect, border_radius=radius)
                elif self.ant.grid[x, y] == 1:
                    # Dessiner la cellule noire
                    pygame.draw.rect(self.screen, CELL_ON_COLOR, cell_rect, border_radius=radius)
        
        # Dessiner le sentier de la fourmi si actif
        if self.trail_active and len(self.ant.trail) > 1:
            # Convertir les positions du sentier en coordonnées de l'écran
            screen_points = []
            for x, y in self.ant.trail:
                screen_x = int(self.offset_x + x * self.zoom + self.zoom // 2)
                screen_y = int(self.offset_y + y * self.zoom + self.zoom // 2)
                screen_points.append((screen_x, screen_y))
            
            # Dessiner le sentier comme une ligne rouge
            if len(screen_points) > 1:
                pygame.draw.lines(self.screen, TRAIL_COLOR, False, screen_points, max(1, int(self.zoom // 10)))
        
        # Dessiner la fourmi comme un carré rouge arrondi
        ant_screen_x = int(self.offset_x + self.ant.ant_x * self.zoom)
        ant_screen_y = int(self.offset_y + self.ant.ant_y * self.zoom)
        
        # Ne dessiner la fourmi que si elle est dans la zone visible
        if (0 <= ant_screen_x < WINDOW_WIDTH and 0 <= ant_screen_y < WINDOW_HEIGHT):
            # Créer le rectangle de la fourmi
            ant_rect = pygame.Rect(
                ant_screen_x,
                ant_screen_y,
                int(self.zoom),
                int(self.zoom)
            )
            
            # Dessiner la fourmi avec le même style que les cellules mais en rouge
            radius = max(1, min(int(self.zoom * 0.3), 10))  # Même rayon que les cellules
            pygame.draw.rect(self.screen, ANT_COLOR, ant_rect, border_radius=radius)
        
        # Rendre le texte du titre au centre supérieur
        title_surface = self.title_font.render(TITLE_TEXT, True, (0, 0, 0))
        title_rect = title_surface.get_rect(center=(TITLE_X, TITLE_Y))
        self.screen.blit(title_surface, title_rect)
        
        # Rendre le texte d'instruction au centre supérieur (sous le titre)
        instruction_surface = self.instruction_font.render(INSTRUCTION_TEXT, True, (0, 0, 0))
        instruction_rect = instruction_surface.get_rect(center=(INSTRUCTION_X, INSTRUCTION_Y))
        self.screen.blit(instruction_surface, instruction_rect)
        
        # Rendre le texte d'attribution au centre inférieur
        attribution_surface = self.attribution_font.render(ATTRIBUTION_TEXT, True, (0, 0, 0))
        attribution_rect = attribution_surface.get_rect(center=(ATTRIBUTION_X, ATTRIBUTION_Y))
        self.screen.blit(attribution_surface, attribution_rect)
        
        # Dessiner le bouton compteur de pas
        steps_text = f"PAS: {self.ant.steps}"
        self.draw_button(STEPS_BUTTON_X, STEPS_BUTTON_Y, STEPS_BUTTON_WIDTH, STEPS_BUTTON_HEIGHT, steps_text)
        
        # Dessiner les boutons
        self.draw_button(EXIT_BUTTON_X, EXIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, EXIT_BUTTON_TEXT)
        self.draw_button(MENU_BUTTON_X, MENU_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, MENU_BUTTON_TEXT)
        
        # Dessiner les options du menu si le menu est ouvert
        if self.menu_open:
            # Bouton de vitesse et champ de saisie
            self.draw_button(SPEED_BUTTON_X, SPEED_BUTTON_Y, SPEED_BUTTON_WIDTH, SPEED_BUTTON_HEIGHT, SPEED_BUTTON_TEXT)
            
            # Dessiner le champ de saisie de vitesse
            input_color = (50, 50, 50) if self.speed_input_active else (100, 100, 100)
            input_rect = pygame.Rect(SPEED_INPUT_X, SPEED_INPUT_Y, SPEED_INPUT_WIDTH, SPEED_INPUT_HEIGHT)
            pygame.draw.rect(self.screen, input_color, input_rect, border_radius=BUTTON_BORDER_RADIUS)
            
            # Dessiner le texte de saisie
            input_text_surface = self.button_font.render(self.speed_input_text, True, BUTTON_TEXT_COLOR)
            input_text_rect = input_text_surface.get_rect(center=(SPEED_INPUT_X + SPEED_INPUT_WIDTH // 2, SPEED_INPUT_Y + SPEED_INPUT_HEIGHT // 2))
            self.screen.blit(input_text_surface, input_text_rect)
            
            # Dessiner le bouton pause/lecture avec le texte approprié
            pause_text = PLAY_BUTTON_TEXT if self.paused else PAUSE_BUTTON_TEXT
            self.draw_button(PAUSE_BUTTON_X, PAUSE_BUTTON_Y, PAUSE_BUTTON_WIDTH, PAUSE_BUTTON_HEIGHT, pause_text)
            
            # Dessiner le bouton de modification des pixels avec surlignage si actif, sinon permettre l'effet de survol
            if self.modify_mode:
                # Quand actif, toujours utiliser la couleur de surbrillance (pas d'effet de survol)
                self.draw_button(MODIFY_BUTTON_X, MODIFY_BUTTON_Y, MODIFY_BUTTON_WIDTH, MODIFY_BUTTON_HEIGHT, 
                                MODIFY_BUTTON_TEXT, override_color=MODIFY_HIGHLIGHT_COLOR)
            else:
                # Quand inactif, ne pas utiliser de couleur de remplacement pour que l'effet de survol puisse fonctionner
                self.draw_button(MODIFY_BUTTON_X, MODIFY_BUTTON_Y, MODIFY_BUTTON_WIDTH, MODIFY_BUTTON_HEIGHT, 
                                MODIFY_BUTTON_TEXT)
            
            # Dessiner le bouton de réinitialisation
            self.draw_button(RESET_BUTTON_X, RESET_BUTTON_Y, RESET_BUTTON_WIDTH, RESET_BUTTON_HEIGHT, RESET_BUTTON_TEXT)
            
            # Dessiner le bouton de sentier avec le texte approprié
            if self.trail_active:
                # Quand actif, utiliser la couleur rouge
                self.draw_button(TRAIL_BUTTON_X, TRAIL_BUTTON_Y, TRAIL_BUTTON_WIDTH, TRAIL_BUTTON_HEIGHT, 
                               TRAIL_BUTTON_TEXT, override_color=TRAIL_COLOR)
            else:
                # Quand inactif, utiliser le comportement normal
                self.draw_button(TRAIL_BUTTON_X, TRAIL_BUTTON_Y, TRAIL_BUTTON_WIDTH, TRAIL_BUTTON_HEIGHT, TRAIL_BUTTON_TEXT)
            
            # Dessiner les boutons d'import/export
            self.draw_button(EXPORT_BUTTON_X, EXPORT_BUTTON_Y, EXPORT_BUTTON_WIDTH, EXPORT_BUTTON_HEIGHT, EXPORT_BUTTON_TEXT)
            self.draw_button(IMPORT_BUTTON_X, IMPORT_BUTTON_Y, IMPORT_BUTTON_WIDTH, IMPORT_BUTTON_HEIGHT, IMPORT_BUTTON_TEXT)
            
            # Dessiner les champs de texte si actifs
            if self.export_field_active:
                # Dessiner le champ d'exportation
                export_field_rect = pygame.Rect(TEXT_FIELD_X, EXPORT_BUTTON_Y, TEXT_FIELD_WIDTH, TEXT_FIELD_HEIGHT)
                pygame.draw.rect(self.screen, TEXT_FIELD_ACTIVE_COLOR, export_field_rect, border_radius=BUTTON_BORDER_RADIUS)
                pygame.draw.rect(self.screen, BUTTON_COLOR, export_field_rect, width=2, border_radius=BUTTON_BORDER_RADIUS)
                
                # Rendre le texte d'exportation (avec troncature si nécessaire)
                font = pygame.font.SysFont("Arial", TEXT_FIELD_FONT_SIZE)
                display_text = self.export_text
                if font.size(display_text)[0] > TEXT_FIELD_WIDTH - 10:  # 10 pixels de marge
                    # Tronquer le texte et ajouter "..." à la fin
                    while font.size(display_text + "...")[0] > TEXT_FIELD_WIDTH - 10 and len(display_text) > 0:
                        display_text = display_text[:-1]
                    display_text += "..."
                
                text_surface = font.render(display_text, True, TEXT_FIELD_TEXT_COLOR)
                text_rect = text_surface.get_rect(midleft=(TEXT_FIELD_X + 5, EXPORT_BUTTON_Y + TEXT_FIELD_HEIGHT // 2))
                self.screen.blit(text_surface, text_rect)
                
                # Ajouter un texte d'instruction pour la copie
                hint_font = pygame.font.SysFont("Arial", 10)
                hint_text = "Cliquer pour copier"
                hint_surface = hint_font.render(hint_text, True, (100, 100, 100))
                hint_rect = hint_surface.get_rect(midleft=(TEXT_FIELD_X + 5, EXPORT_BUTTON_Y + TEXT_FIELD_HEIGHT + 8))
                self.screen.blit(hint_surface, hint_rect)
                
                # Afficher la longueur du code exporté
                length_text = f"{len(self.export_text)} caractères"
                length_surface = hint_font.render(length_text, True, (100, 100, 100))
                length_rect = length_surface.get_rect(midright=(TEXT_FIELD_X + TEXT_FIELD_WIDTH - 5, EXPORT_BUTTON_Y + TEXT_FIELD_HEIGHT + 8))
                self.screen.blit(length_surface, length_rect)
            
            if self.import_field_active:
                # Dessiner le champ d'importation
                import_field_rect = pygame.Rect(TEXT_FIELD_X, IMPORT_BUTTON_Y, TEXT_FIELD_WIDTH, TEXT_FIELD_HEIGHT)
                pygame.draw.rect(self.screen, TEXT_FIELD_ACTIVE_COLOR, import_field_rect, border_radius=BUTTON_BORDER_RADIUS)
                pygame.draw.rect(self.screen, BUTTON_COLOR, import_field_rect, width=2, border_radius=BUTTON_BORDER_RADIUS)
                
                # Rendre le texte d'importation (avec troncature si nécessaire)
                font = pygame.font.SysFont("Arial", TEXT_FIELD_FONT_SIZE)
                
                # Afficher un indicateur si le texte est présent mais non affiché
                if self.import_text:
                    display_text = f"[Code: {len(self.import_text)} caractères]"
                else:
                    display_text = "Coller avec Ctrl+V"
                    
                text_surface = font.render(display_text, True, TEXT_FIELD_TEXT_COLOR)
                text_rect = text_surface.get_rect(midleft=(TEXT_FIELD_X + 5, IMPORT_BUTTON_Y + TEXT_FIELD_HEIGHT // 2))
                self.screen.blit(text_surface, text_rect)
                
                # Ajouter un texte d'instruction pour l'importation
                hint_font = pygame.font.SysFont("Arial", 10)
                hint_text = "Ctrl+V pour coller, Entrée pour importer"
                hint_surface = hint_font.render(hint_text, True, (100, 100, 100))
                hint_rect = hint_surface.get_rect(midleft=(TEXT_FIELD_X + 5, IMPORT_BUTTON_Y + TEXT_FIELD_HEIGHT + 8))
                self.screen.blit(hint_surface, hint_rect)
        
        # Dessiner l'écran d'information si en mode info
        if self.info_mode:
            # Dessiner un fond noir semi-transparent pour assombrir l'écran principal
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))  # Noir avec 70% d'opacité
            self.screen.blit(overlay, (0, 0))
            
            # Dessiner l'image d'information au centre
            self.screen.blit(self.info_image, (INFO_IMAGE_X, INFO_IMAGE_Y))
            
            # Dessiner le bouton de lien vidéo
            self.draw_button(VIDEO_BUTTON_X, VIDEO_BUTTON_Y, VIDEO_BUTTON_WIDTH, VIDEO_BUTTON_HEIGHT, VIDEO_BUTTON_TEXT)
        
        # Dessiner le bouton d'info en dernier pour qu'il ne soit pas affecté par la superposition
        self.draw_button(INFO_BUTTON_X, INFO_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, INFO_BUTTON_TEXT)
        
        # Dessiner le bouton multiplicateur de vitesse
        if self.speed_mult_button_pressed:
            # Utiliser la couleur violette quand le bouton est pressé
            self.draw_button(SPEED_MULT_BUTTON_X, SPEED_MULT_BUTTON_Y, SPEED_MULT_BUTTON_WIDTH, SPEED_MULT_BUTTON_HEIGHT, 
                           SPEED_MULT_BUTTON_TEXT, override_color=MODIFY_HIGHLIGHT_COLOR)
        else:
            # Utiliser le comportement normal (gris au survol) quand non pressé
            self.draw_button(SPEED_MULT_BUTTON_X, SPEED_MULT_BUTTON_Y, SPEED_MULT_BUTTON_WIDTH, SPEED_MULT_BUTTON_HEIGHT, 
                           SPEED_MULT_BUTTON_TEXT)
        
        pygame.display.flip()
    
    def draw_button(self, x, y, width, height, text, override_color=None):
        """Dessiner un bouton avec du texte centré dessus"""
        # Déterminer le nom du bouton pour l'effet de survol
        button_name = None
        if (x, y, width, height) == (EXIT_BUTTON_X, EXIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT):
            button_name = "EXIT"
        elif (x, y, width, height) == (INFO_BUTTON_X, INFO_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT):
            button_name = "INFO"
        elif (x, y, width, height) == (MENU_BUTTON_X, MENU_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT):
            button_name = "MENU"
        elif (x, y, width, height) == (SPEED_BUTTON_X, SPEED_BUTTON_Y, SPEED_BUTTON_WIDTH, SPEED_BUTTON_HEIGHT):
            button_name = "SPEED"
        elif (x, y, width, height) == (SPEED_INPUT_X, SPEED_INPUT_Y, SPEED_INPUT_WIDTH, SPEED_INPUT_HEIGHT):
            button_name = "SPEED_INPUT"
        elif (x, y, width, height) == (PAUSE_BUTTON_X, PAUSE_BUTTON_Y, PAUSE_BUTTON_WIDTH, PAUSE_BUTTON_HEIGHT):
            button_name = "PAUSE"
        elif (x, y, width, height) == (MODIFY_BUTTON_X, MODIFY_BUTTON_Y, MODIFY_BUTTON_WIDTH, MODIFY_BUTTON_HEIGHT):
            button_name = "MODIFY"
        elif (x, y, width, height) == (RESET_BUTTON_X, RESET_BUTTON_Y, RESET_BUTTON_WIDTH, RESET_BUTTON_HEIGHT):
            button_name = "RESET"
        elif (x, y, width, height) == (STEPS_BUTTON_X, STEPS_BUTTON_Y, STEPS_BUTTON_WIDTH, STEPS_BUTTON_HEIGHT):
            button_name = "STEPS"
        elif (x, y, width, height) == (VIDEO_BUTTON_X, VIDEO_BUTTON_Y, VIDEO_BUTTON_WIDTH, VIDEO_BUTTON_HEIGHT):
            button_name = "VIDEO"
        elif (x, y, width, height) == (SPEED_MULT_BUTTON_X, SPEED_MULT_BUTTON_Y, SPEED_MULT_BUTTON_WIDTH, SPEED_MULT_BUTTON_HEIGHT):
            button_name = "SPEED_MULT"
        elif (x, y, width, height) == (TRAIL_BUTTON_X, TRAIL_BUTTON_Y, TRAIL_BUTTON_WIDTH, TRAIL_BUTTON_HEIGHT):
            button_name = "TRAIL"
        elif (x, y, width, height) == (EXPORT_BUTTON_X, EXPORT_BUTTON_Y, EXPORT_BUTTON_WIDTH, EXPORT_BUTTON_HEIGHT):
            button_name = "EXPORT"
        elif (x, y, width, height) == (IMPORT_BUTTON_X, IMPORT_BUTTON_Y, IMPORT_BUTTON_WIDTH, IMPORT_BUTTON_HEIGHT):
            button_name = "IMPORT"
        
        # Déterminer la couleur du bouton en fonction du survol et du remplacement
        if override_color:
            button_color = override_color
        elif button_name == "INFO" and self.info_mode:
            # Utiliser la couleur violette pour le bouton d'info lorsque le mode info est actif
            button_color = MODIFY_HIGHLIGHT_COLOR
        elif button_name == "MENU" and self.menu_open:
            # Utiliser la couleur violette pour le bouton menu lorsque le menu est ouvert
            button_color = MODIFY_HIGHLIGHT_COLOR
        elif self.hovered_button == button_name and button_name != "SPEED" and button_name != "STEPS":
            # Appliquer l'effet de survol à tous les boutons sauf SPEED et STEPS
            button_color = BUTTON_HOVER_COLOR
        else:
            button_color = BUTTON_COLOR
        
        # Dessiner le rectangle du bouton
        button_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, button_color, button_rect, border_radius=BUTTON_BORDER_RADIUS)
        
        # Dessiner le texte centré sur le bouton
        text_surface = self.button_font.render(text, True, BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
        self.screen.blit(text_surface, text_rect)
    
    def handle_other_mouse_actions(self, event, mouse_pos):
        """Gérer les actions de la souris qui ne sont pas des clics de bouton (déplacement, zoom, modification de pixels)"""
        # Gérer la modification de pixels lorsqu'en mode de modification et délai terminé
        if self.modify_mode and event.button == pygame.BUTTON_LEFT and self.modify_cooldown <= 0:
            # Convertir les coordonnées de l'écran en coordonnées de grille
            grid_x = int((mouse_pos[0] - self.offset_x) / self.zoom)
            grid_y = int((mouse_pos[1] - self.offset_y) / self.zoom)
            
            # Vérifier si c'est dans les limites de la grille
            if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                # Modifier la cellule initiale
                if self.modify_cell(grid_x, grid_y):
                    self.last_modified_cell = (grid_x, grid_y)
        
        # Gérer le déplacement avec le bouton gauche de la souris (uniquement lorsque pas en mode de modification)
        elif not self.modify_mode and event.button == pygame.BUTTON_LEFT:
            self.panning = True
            self.last_mouse_pos = mouse_pos
            # Changer le curseur en main fermée/saisie lors du déplacement
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEALL)
        
        # Zoom avec la molette de la souris centré sur la position du curseur - permettre dans n'importe quel mode
        elif event.button == 4:  # Molette vers le haut (zoom avant)
            self.zoom_at_point(mouse_pos, 1)
        elif event.button == 5:  # Molette vers le bas (zoom arrière)
            self.zoom_at_point(mouse_pos, -1)
    
    def update_hovered_button(self, mouse_pos):
        """Mettre à jour quel bouton est actuellement survolé"""
        # Définir toutes les régions des boutons
        button_regions = {
            "EXIT": (EXIT_BUTTON_X, EXIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT),
            "INFO": (INFO_BUTTON_X, INFO_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT),
            "MENU": (MENU_BUTTON_X, MENU_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT),
            "STEPS": (STEPS_BUTTON_X, STEPS_BUTTON_Y, STEPS_BUTTON_WIDTH, STEPS_BUTTON_HEIGHT),
            "SPEED_MULT": (SPEED_MULT_BUTTON_X, SPEED_MULT_BUTTON_Y, SPEED_MULT_BUTTON_WIDTH, SPEED_MULT_BUTTON_HEIGHT)
        }
        
        # Ajouter le bouton vidéo si en mode info
        if self.info_mode:
            button_regions["VIDEO"] = (VIDEO_BUTTON_X, VIDEO_BUTTON_Y, VIDEO_BUTTON_WIDTH, VIDEO_BUTTON_HEIGHT)
        
        # Ajouter les boutons d'options du menu si le menu est ouvert
        if self.menu_open:
            button_regions.update({
                "SPEED": (SPEED_BUTTON_X, SPEED_BUTTON_Y, SPEED_BUTTON_WIDTH, SPEED_BUTTON_HEIGHT),
                "SPEED_INPUT": (SPEED_INPUT_X, SPEED_INPUT_Y, SPEED_INPUT_WIDTH, SPEED_INPUT_HEIGHT),
                "PAUSE": (PAUSE_BUTTON_X, PAUSE_BUTTON_Y, PAUSE_BUTTON_WIDTH, PAUSE_BUTTON_HEIGHT),
                "MODIFY": (MODIFY_BUTTON_X, MODIFY_BUTTON_Y, MODIFY_BUTTON_WIDTH, MODIFY_BUTTON_HEIGHT),
                "RESET": (RESET_BUTTON_X, RESET_BUTTON_Y, RESET_BUTTON_WIDTH, RESET_BUTTON_HEIGHT),
                "TRAIL": (TRAIL_BUTTON_X, TRAIL_BUTTON_Y, TRAIL_BUTTON_WIDTH, TRAIL_BUTTON_HEIGHT),
                "EXPORT": (EXPORT_BUTTON_X, EXPORT_BUTTON_Y, EXPORT_BUTTON_WIDTH, EXPORT_BUTTON_HEIGHT),
                "IMPORT": (IMPORT_BUTTON_X, IMPORT_BUTTON_Y, IMPORT_BUTTON_WIDTH, IMPORT_BUTTON_HEIGHT)
            })
        
        # Vérifier si la souris est sur un bouton
        for button_name, rect in button_regions.items():
            if self.is_point_in_rect(mouse_pos, rect):
                self.hovered_button = button_name
                return
        
        # Aucun bouton n'est survolé
        self.hovered_button = None
    
    def run(self):
        # Jouer le son de démarrage lorsque la simulation commence
        START_SOUND.play()
        
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

    def export_design(self):
        """Exporte le design actuel sous forme de chaîne encodée"""
        try:
            # Convertir la grille en bytes
            grid_bytes = self.ant.grid.tobytes()
            
            # Compresser les données
            compressed_data = zlib.compress(grid_bytes, level=9)
            
            # Encoder en base64 pour obtenir une chaîne de caractères
            encoded_data = base64.b64encode(compressed_data).decode('utf-8')
            
            # Préfixer avec la taille de la grille et le nombre de pas pour la reconstruction
            export_code = f"{GRID_WIDTH},{GRID_HEIGHT},{self.ant.steps}:{encoded_data}"
            
            print(f"Design exporté avec succès! Longueur du code: {len(export_code)} caractères")
            return export_code
            
        except Exception as e:
            print(f"Erreur lors de l'exportation du design: {e}")
            return "ERREUR"
    
    def import_design(self):
        """Importe un design à partir d'une chaîne encodée"""
        try:
            # Vérifier que le texte d'importation n'est pas vide
            if not self.import_text:
                print("Erreur: Le code d'importation est vide.")
                return
            
            # Vérifier si le format est correct (doit contenir ":")
            if ":" not in self.import_text:
                print("Erreur: Format de code invalide. Le code doit contenir le caractère ':'")
                return
            
            # Séparer les métadonnées des données
            metadata, encoded_data = self.import_text.split(":", 1)  # Limite à 1 split pour gérer les ':' dans le code base64
            
            # Vérifier si les métadonnées sont au bon format
            metadata_parts = metadata.split(",")
            if len(metadata_parts) < 2:
                print("Erreur: Format de métadonnées invalide. Les dimensions doivent être séparées par une virgule.")
                return
                
            # Extraire les dimensions et le nombre de pas (s'il existe)
            try:
                width = int(metadata_parts[0])
                height = int(metadata_parts[1])
                steps = int(metadata_parts[2]) if len(metadata_parts) > 2 else 0
            except ValueError:
                print(f"Erreur: Impossible de lire les dimensions ou le nombre de pas: {metadata}")
                return
            
            # Vérifier que les dimensions correspondent
            if width != GRID_WIDTH or height != GRID_HEIGHT:
                print(f"Erreur: Les dimensions ne correspondent pas. Attendu: {GRID_WIDTH}x{GRID_HEIGHT}, Reçu: {width}x{height}")
                return
            
            try:
                # Décoder les données
                decoded_data = base64.b64decode(encoded_data)
                
                # Décompresser les données
                decompressed_data = zlib.decompress(decoded_data)
                
                # Reconstruire la grille
                grid_array = np.frombuffer(decompressed_data, dtype=int).reshape(width, height)
                
                # Créer une nouvelle instance de fourmi avec la grille importée
                new_ant = LangtonAnt(width, height)
                new_ant.grid = grid_array.copy()
                
                # Placer la fourmi au milieu
                new_ant.ant_x = width // 2
                new_ant.ant_y = height // 2
                new_ant.direction = 0
                
                # Définir le compteur de pas avec la valeur importée
                new_ant.steps = steps
                
                # Remplacer l'ancienne fourmi par la nouvelle
                self.ant = new_ant
                
                # Réinitialiser l'accumulateur de pas
                self.step_accumulator = 0.0
                
                # Réinitialiser le sentier et désactiver le mode sentier
                self.trail_active = False
                
                print(f"Design importé avec succès! Nombre de pas: {steps}")
                
            except base64.binascii.Error:
                print("Erreur: Code base64 invalide.")
            except zlib.error:
                print("Erreur: Impossible de décompresser les données.")
            except ValueError as e:
                print(f"Erreur lors de la reconstruction de la grille: {e}")
                
        except Exception as e:
            print(f"Erreur lors de l'importation du design: {e}")
            import traceback
            traceback.print_exc()

# Point d'entrée principal
if __name__ == "__main__":
    simulation = Simulation()
    simulation.run()