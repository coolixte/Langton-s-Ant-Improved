# ✦ LANGTON'S ANT IMPROVED ✦ --------------------- Calixte Lamotte ----------------------------------
#-----------------------------------------------------------------------------------------------------

# "Pas" display not shadeable like a button


# MODULES ✦ -----------------------------------------------------------------------------------------

import pygame
import numpy as np
import sys
import os
import webbrowser

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize the mixer for audio playback


# CONSTANTS ✦ ---------------------------------------------------------------------------------------

# Général
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 5  # Initial cell size in pixels
GRID_WIDTH = 200  # Number of cells in the grid width
GRID_HEIGHT = 200  # Number of cells in  the grid height
BG_COLOR = (255, 255, 255)  # White
ANT_COLOR = (255, 0, 0)  # Red
CELL_ON_COLOR = (0, 0, 0)  # Black
CELL_OFF_COLOR = (255, 255, 255)  # White
FPS = 60

# Button constants
BUTTON_WIDTH = 80
BUTTON_HEIGHT = 30
BUTTON_MARGIN = 10
BUTTON_COLOR = (0, 0, 0)  # Black
BUTTON_HOVER_COLOR = (100, 100, 100)  # Light grey
BUTTON_TEXT_COLOR = (255, 255, 255)  # White
BUTTON_FONT_SIZE = 14
BUTTON_BORDER_RADIUS = 5

# Exit button constants
EXIT_BUTTON_X = WINDOW_WIDTH - BUTTON_WIDTH - BUTTON_MARGIN
EXIT_BUTTON_Y = BUTTON_MARGIN
EXIT_BUTTON_TEXT = "EXIT"

# Info button constants
INFO_BUTTON_X = WINDOW_WIDTH - BUTTON_WIDTH - BUTTON_MARGIN
INFO_BUTTON_Y = EXIT_BUTTON_Y + BUTTON_HEIGHT + BUTTON_MARGIN
INFO_BUTTON_TEXT = "INFO"

# Menu button constants
MENU_BUTTON_X = WINDOW_WIDTH - BUTTON_WIDTH - BUTTON_MARGIN
MENU_BUTTON_Y = INFO_BUTTON_Y + BUTTON_HEIGHT + BUTTON_MARGIN
MENU_BUTTON_TEXT = "MENU"

# Menu options constants
MENU_OPEN = False  # Track if menu is open
SPEED_BUTTON_X = MENU_BUTTON_X + -95
SPEED_BUTTON_Y = MENU_BUTTON_Y + BUTTON_HEIGHT + BUTTON_MARGIN
SPEED_BUTTON_WIDTH = 120
SPEED_BUTTON_HEIGHT = BUTTON_HEIGHT
SPEED_BUTTON_TEXT = "SPEED"

# Speed input field
SPEED_INPUT_X = SPEED_BUTTON_X + SPEED_BUTTON_WIDTH + 5
SPEED_INPUT_Y = SPEED_BUTTON_Y
SPEED_INPUT_WIDTH = 50
SPEED_INPUT_HEIGHT = BUTTON_HEIGHT
SPEED_INPUT_ACTIVE = False
SPEED_INPUT_TEXT = "1"

# Pause/Play button
PAUSE_BUTTON_X = MENU_BUTTON_X
PAUSE_BUTTON_Y = SPEED_BUTTON_Y + BUTTON_HEIGHT + BUTTON_MARGIN
PAUSE_BUTTON_WIDTH = BUTTON_WIDTH
PAUSE_BUTTON_HEIGHT = BUTTON_HEIGHT
PAUSE_BUTTON_TEXT = "PAUSE"
PLAY_BUTTON_TEXT = "PLAY"

# Modify pixels button
MODIFY_BUTTON_X = MENU_BUTTON_X + -40
MODIFY_BUTTON_Y = PAUSE_BUTTON_Y + BUTTON_HEIGHT + BUTTON_MARGIN
MODIFY_BUTTON_WIDTH = BUTTON_WIDTH + 40
MODIFY_BUTTON_HEIGHT = BUTTON_HEIGHT
MODIFY_BUTTON_TEXT = "MODIFY PIXELS"
MODIFY_MODE = False  # Track if in modify mode
MODIFY_HIGHLIGHT_COLOR = (170, 0, 170)  # Mauve color for highlighting

# Reset button
RESET_BUTTON_X = MENU_BUTTON_X
RESET_BUTTON_Y = MODIFY_BUTTON_Y + BUTTON_HEIGHT + BUTTON_MARGIN
RESET_BUTTON_WIDTH = BUTTON_WIDTH
RESET_BUTTON_HEIGHT = BUTTON_HEIGHT
RESET_BUTTON_TEXT = "RESET"

# Info screen constants
INFO_MODE = False  # Track if info screen is displayed
INFO_IMAGE_PATH = os.path.join("assets", "Info.png")
INFO_IMAGE_WIDTH = 500  # Width of info image
INFO_IMAGE_HEIGHT = 500  # Height of info image
INFO_IMAGE_X = WINDOW_WIDTH // 2 - INFO_IMAGE_WIDTH // 2  # Centered horizontally
INFO_IMAGE_Y = WINDOW_HEIGHT // 2 - INFO_IMAGE_HEIGHT // 2  # Centered vertically

# Video link button constants
VIDEO_BUTTON_WIDTH = 120
VIDEO_BUTTON_HEIGHT = 40
VIDEO_BUTTON_X = WINDOW_WIDTH // 2 - VIDEO_BUTTON_WIDTH // 2 + 100 # Centered horizontally
VIDEO_BUTTON_Y = INFO_IMAGE_Y + INFO_IMAGE_HEIGHT + -130  # Below info image
VIDEO_BUTTON_TEXT = "LIEN VIDEO"
VIDEO_URL = "https://youtu.be/qZRYGxF6D3w?si=XcB8ibW5AP98eqRa"

# Sound files
START_SOUND = pygame.mixer.Sound(os.path.join("assets", "start.mp3"))
WHITE_TO_BLACK_SOUND = pygame.mixer.Sound(os.path.join("assets", "2-bell.mp3"))
BLACK_TO_WHITE_SOUND = pygame.mixer.Sound(os.path.join("assets", "1-bell.mp3"))

# Attribution text constants
ATTRIBUTION_TEXT = "2025 · @Calixte Lamotte"
ATTRIBUTION_X = WINDOW_WIDTH // 2  # Centered horizontally
ATTRIBUTION_Y = WINDOW_HEIGHT - 15  # 15 pixels from bottom

# Steps counter button constants
STEPS_BUTTON_WIDTH = BUTTON_WIDTH + 40
STEPS_BUTTON_X = WINDOW_WIDTH // 2 - STEPS_BUTTON_WIDTH // 2  # Centered using button's own width
STEPS_BUTTON_Y = ATTRIBUTION_Y - BUTTON_HEIGHT - 10  # Above attribution with 10px margin
STEPS_BUTTON_HEIGHT = BUTTON_HEIGHT

# Title text constants
TITLE_TEXT = "LANGTON'S ANT IMPROVED"
TITLE_X = WINDOW_WIDTH // 2  # Centered horizontally
TITLE_Y = 25  # 30 pixels from top
TITLE_SIZE = 25  # Font size

# Instruction text constants
INSTRUCTION_TEXT = "ZOOM / PAN AVEC LA SOURIS"
INSTRUCTION_X = WINDOW_WIDTH // 2  # Centered horizontally
INSTRUCTION_Y = 50  # Adjusted to be below title
INSTRUCTION_SIZE = 12  # Font size

# Simulation parameters
SIMULATION_SPEED = 1  # Steps per frame (now supports fractional values)


# MAIN ✦ ---------------------------------------------------------------------------------------------

class LangtonAnt:
    def __init__(self, grid_width, grid_height):
        # Initialize grid with all cells off (0)
        self.grid = np.zeros((grid_width, grid_height), dtype=int)
        
        # Place ant in the middle of the grid
        self.ant_x = grid_width // 2
        self.ant_y = grid_height // 2
        
        # Direction: 0=up, 1=right, 2=down, 3=left
        self.direction = 0
        
        # Movement vectors for each direction
        self.movement = [
            (0, -1),  # Up
            (1, 0),   # Right
            (0, 1),   # Down
            (-1, 0)   # Left
        ]
        
        self.steps = 0
    
    def step(self):
        """Perform one step of the Langton's Ant algorithm"""
        # Get current cell state
        current_cell = self.grid[self.ant_x, self.ant_y]
        
        # Flip the cell state
        self.grid[self.ant_x, self.ant_y] = 1 - current_cell
        
        # Play appropriate sound based on the transition
        if current_cell == 0:
            # White to black transition
            WHITE_TO_BLACK_SOUND.play()
            self.direction = (self.direction + 1) % 4  # Turn right (clockwise)
        else:
            # Black to white transition
            BLACK_TO_WHITE_SOUND.play()
            self.direction = (self.direction - 1) % 4  # Turn left (counter-clockwise)
        
        # Move forward
        dx, dy = self.movement[self.direction]
        self.ant_x = (self.ant_x + dx) % self.grid.shape[0]
        self.ant_y = (self.ant_y + dy) % self.grid.shape[1]
        
        self.steps += 1

class Simulation:
    def __init__(self):
        # Create a borderless window
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.NOFRAME)
        pygame.display.set_caption("Langton's Ant Simulation")
        self.clock = pygame.time.Clock()
        
        self.ant = LangtonAnt(GRID_WIDTH, GRID_HEIGHT)
        
        # View parameters
        self.offset_x = WINDOW_WIDTH // 2 - GRID_WIDTH * GRID_SIZE // 2
        self.offset_y = WINDOW_HEIGHT // 2 - GRID_HEIGHT * GRID_SIZE // 2
        self.zoom = GRID_SIZE
        
        # Mouse state
        self.panning = False
        self.last_mouse_pos = (0, 0)
        self.hovered_cell = (-1, -1)  # Track cell currently being hovered over
        self.hovered_button = None  # Track button currently being hovered over
        self.mouse_button_down = False  # Track if mouse button is being held down
        self.last_modified_cell = None  # Track the last cell that was modified
        
        # Simulation state
        self.running = True
        self.paused = False
        
        # Menu state
        self.menu_open = MENU_OPEN
        self.speed_input_active = SPEED_INPUT_ACTIVE
        self.speed_input_text = SPEED_INPUT_TEXT
        self.modify_mode = MODIFY_MODE
        self.modify_cooldown = 0  # Cooldown timer for modify mode
        
        # Info state
        self.info_mode = INFO_MODE
        # Load the info image
        try:
            self.info_image = pygame.image.load(INFO_IMAGE_PATH)
            self.info_image = pygame.transform.scale(self.info_image, (INFO_IMAGE_WIDTH, INFO_IMAGE_HEIGHT))
        except pygame.error:
            # Create a placeholder if image can't be loaded
            self.info_image = pygame.Surface((INFO_IMAGE_WIDTH, INFO_IMAGE_HEIGHT))
            self.info_image.fill((200, 200, 200))  # Light gray background
            font = pygame.font.SysFont("Arial", 30)
            text = font.render("Info Image Not Found", True, (0, 0, 0))
            text_rect = text.get_rect(center=(INFO_IMAGE_WIDTH//2, INFO_IMAGE_HEIGHT//2))
            self.info_image.blit(text, text_rect)
        
        # For handling fractional speeds
        self.step_accumulator = 0.0
        
        # Set default cursor to open hand
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        
        # Prepare fonts
        self.attribution_font = pygame.font.SysFont("Arial", 10)
        self.instruction_font = pygame.font.SysFont("Arial", INSTRUCTION_SIZE)
        self.title_font = pygame.font.SysFont("Arial", TITLE_SIZE, bold=True)
        self.button_font = pygame.font.SysFont("Arial", BUTTON_FONT_SIZE, bold=True)
    
    def modify_cell(self, grid_x, grid_y):
        """Helper function to modify a cell and play the appropriate sound"""
        if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
            current_cell = self.ant.grid[grid_x, grid_y]
            self.ant.grid[grid_x, grid_y] = 1 - current_cell
            
            # Play appropriate sound based on the transition
            if current_cell == 0:
                # White to black transition
                WHITE_TO_BLACK_SOUND.play()
            else:
                # Black to white transition
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
                    self.step_accumulator = 0.0  # Reset accumulator on reset
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
                
                # Handle speed input field
                if self.speed_input_active:
                    if event.key == pygame.K_RETURN:
                        # Submit speed value
                        try:
                            new_speed = float(self.speed_input_text)
                            if new_speed > 0:
                                global SIMULATION_SPEED
                                SIMULATION_SPEED = new_speed
                        except ValueError:
                            # Invalid input, reset to current speed
                            self.speed_input_text = str(SIMULATION_SPEED)
                        self.speed_input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.speed_input_text = self.speed_input_text[:-1]
                    else:
                        # Only add digit characters and decimal point
                        if event.unicode.isdigit() or event.unicode == '.':
                            self.speed_input_text += event.unicode
            
            # Mouse controls for buttons and panning
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                # Handle mouse wheel events
                if event.button in (4, 5):  # Mouse wheel up/down
                    self.zoom_at_point(mouse_pos, 1 if event.button == 4 else -1)
                # Handle left mouse button
                elif event.button == pygame.BUTTON_LEFT:
                    self.mouse_button_down = True  # Set mouse button state to down
                    self.last_modified_cell = None  # Reset last modified cell
                    
                    # First check for button clicks
                    if self.is_point_in_rect(mouse_pos, (EXIT_BUTTON_X, EXIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)):
                        # Exit button clicked
                        self.running = False
                    elif self.is_point_in_rect(mouse_pos, (INFO_BUTTON_X, INFO_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)):
                        # Info button clicked - show info screen
                        if self.menu_open:
                            self.menu_open = False  # Close the menu
                        self.info_mode = not self.info_mode  # Toggle info mode
                    elif self.info_mode and self.is_point_in_rect(mouse_pos, (VIDEO_BUTTON_X, VIDEO_BUTTON_Y, VIDEO_BUTTON_WIDTH, VIDEO_BUTTON_HEIGHT)):
                        # Video button clicked - open URL
                        webbrowser.open(VIDEO_URL)
                    elif self.is_point_in_rect(mouse_pos, (MENU_BUTTON_X, MENU_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)):
                        # Menu button clicked - toggle menu
                        self.menu_open = not self.menu_open
                    elif self.menu_open:
                        # Check menu option buttons only if menu is open
                        if self.is_point_in_rect(mouse_pos, (SPEED_BUTTON_X, SPEED_BUTTON_Y, SPEED_BUTTON_WIDTH, SPEED_BUTTON_HEIGHT)):
                            # Speed button clicked - no functionality other than highlighting input field
                            pass
                        elif self.is_point_in_rect(mouse_pos, (SPEED_INPUT_X, SPEED_INPUT_Y, SPEED_INPUT_WIDTH, SPEED_INPUT_HEIGHT)):
                            # Speed input field clicked
                            self.speed_input_active = True
                            # Reset input text if it's the default value
                            if self.speed_input_text == "1" and SIMULATION_SPEED != 1:
                                self.speed_input_text = str(SIMULATION_SPEED)
                        elif self.is_point_in_rect(mouse_pos, (PAUSE_BUTTON_X, PAUSE_BUTTON_Y, PAUSE_BUTTON_WIDTH, PAUSE_BUTTON_HEIGHT)):
                            # Pause/Play button clicked
                            self.paused = not self.paused
                        elif self.is_point_in_rect(mouse_pos, (MODIFY_BUTTON_X, MODIFY_BUTTON_Y, MODIFY_BUTTON_WIDTH, MODIFY_BUTTON_HEIGHT)):
                            # Toggle modify mode and set cooldown
                            self.modify_mode = not self.modify_mode
                            self.modify_cooldown = 10  # Set cooldown to 10 frames (about 1/6 of a second)
                        elif self.is_point_in_rect(mouse_pos, (RESET_BUTTON_X, RESET_BUTTON_Y, RESET_BUTTON_WIDTH, RESET_BUTTON_HEIGHT)):
                            # Reset button clicked
                            self.ant = LangtonAnt(GRID_WIDTH, GRID_HEIGHT)
                            self.step_accumulator = 0.0  # Reset accumulator on reset
                        # If none of the menu buttons were clicked, continue to other checks
                        else:
                            # Handle other mouse actions
                            self.handle_other_mouse_actions(event, mouse_pos)
                    else:
                        # If not clicking on any buttons, handle other mouse actions
                        self.handle_other_mouse_actions(event, mouse_pos)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:  # Only handle left mouse button
                    self.panning = False
                    self.mouse_button_down = False  # Set mouse button state to up
                    self.last_modified_cell = None  # Reset last modified cell
                    # Change cursor back to open hand when not panning
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            
            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                
                # Update hovered cell
                if self.modify_mode:
                    # Convert screen coordinates to grid coordinates
                    grid_x = int((mouse_pos[0] - self.offset_x) / self.zoom)
                    grid_y = int((mouse_pos[1] - self.offset_y) / self.zoom)
                    
                    # Check if within grid bounds
                    if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                        self.hovered_cell = (grid_x, grid_y)
                        
                        # If mouse button is down, handle continuous modification
                        if self.mouse_button_down and self.modify_cooldown <= 0:
                            current_cell = (grid_x, grid_y)
                            
                            # If this is a new cell and not the last modified one
                            if current_cell != self.last_modified_cell:
                                # Modify the current cell
                                if self.modify_cell(grid_x, grid_y):
                                    self.last_modified_cell = current_cell
                                    
                                    # If we have a last modified cell, interpolate between positions
                                    if self.last_modified_cell is not None:
                                        last_x, last_y = self.last_modified_cell
                                        # Calculate the distance between cells
                                        dx = grid_x - last_x
                                        dy = grid_y - last_y
                                        
                                        # If the distance is greater than 1, interpolate
                                        if abs(dx) > 1 or abs(dy) > 1:
                                            # Calculate the number of steps needed
                                            steps = max(abs(dx), abs(dy))
                                            for i in range(1, steps):
                                                # Calculate intermediate position
                                                inter_x = last_x + (dx * i) // steps
                                                inter_y = last_y + (dy * i) // steps
                                                # Modify the intermediate cell
                                                self.modify_cell(inter_x, inter_y)
                    else:
                        self.hovered_cell = (-1, -1)
                else:
                    # Reset hovered cell when not in modify mode
                    self.hovered_cell = (-1, -1)
                
                # Update hovered button state
                self.update_hovered_button(mouse_pos)
                
                if self.panning:
                    dx = mouse_pos[0] - self.last_mouse_pos[0]
                    dy = mouse_pos[1] - self.last_mouse_pos[1]
                    self.offset_x += dx
                    self.offset_y += dy
                    self.last_mouse_pos = mouse_pos
    
    def is_point_in_rect(self, point, rect):
        """Check if a point is inside a rectangle defined by (x, y, width, height)"""
        x, y = point
        rect_x, rect_y, rect_width, rect_height = rect
        return rect_x <= x <= rect_x + rect_width and rect_y <= y <= rect_y + rect_height
    
    def zoom_at_point(self, pos, zoom_change):
        """Zoom in or out centered on the cursor position"""
        # Get mouse position before zoom
        mouse_x, mouse_y = pos
        
        # Convert screen coordinates to grid coordinates
        grid_x = (mouse_x - self.offset_x) / self.zoom
        grid_y = (mouse_y - self.offset_y) / self.zoom
        
        # Apply zoom change
        old_zoom = self.zoom
        self.zoom = max(1, min(50, self.zoom + zoom_change))
        
        # Calculate new offset to keep the point under cursor at the same place
        self.offset_x = int(mouse_x - grid_x * self.zoom)
        self.offset_y = int(mouse_y - grid_y * self.zoom)
    
    def update(self):
        if not self.paused:
            # Accumulate steps based on simulation speed
            self.step_accumulator += SIMULATION_SPEED
            
            # Take whole steps when the accumulator reaches or exceeds 1.0
            while self.step_accumulator >= 1.0:
                self.ant.step()
                self.step_accumulator -= 1.0
        
        # Update modify mode cooldown
        if self.modify_cooldown > 0:
            self.modify_cooldown -= 1
    
    def render(self):
        self.screen.fill(BG_COLOR)
        
        # Calculate visible portion of the grid
        visible_start_x = max(0, int(-self.offset_x // self.zoom))
        visible_end_x = min(GRID_WIDTH, int(visible_start_x + (WINDOW_WIDTH // self.zoom) + 2))
        visible_start_y = max(0, int(-self.offset_y // self.zoom))
        visible_end_y = min(GRID_HEIGHT, int(visible_start_y + (WINDOW_HEIGHT // self.zoom) + 2))
        
        # Draw grid cells with rounded corners
        for x in range(visible_start_x, visible_end_x):
            for y in range(visible_start_y, visible_end_y):
                # Create cell rectangle
                cell_rect = pygame.Rect(
                    int(self.offset_x + x * self.zoom), 
                    int(self.offset_y + y * self.zoom), 
                    int(self.zoom), 
                    int(self.zoom)
                )
                
                # Set radius for rounded corners
                radius = max(1, min(int(self.zoom * 0.3), 10))  # Scale radius with zoom, but cap it
                
                # Determine cell color based on state and hover
                if self.modify_mode and self.hovered_cell == (x, y):
                    # Draw hovered cell with highlight color
                    pygame.draw.rect(self.screen, MODIFY_HIGHLIGHT_COLOR, cell_rect, border_radius=radius)
                elif self.ant.grid[x, y] == 1:
                    # Draw black cell
                    pygame.draw.rect(self.screen, CELL_ON_COLOR, cell_rect, border_radius=radius)
        
        # Draw the ant as a rounded red square
        ant_screen_x = int(self.offset_x + self.ant.ant_x * self.zoom)
        ant_screen_y = int(self.offset_y + self.ant.ant_y * self.zoom)
        
        # Only draw the ant if it's in the visible area
        if (0 <= ant_screen_x < WINDOW_WIDTH and 0 <= ant_screen_y < WINDOW_HEIGHT):
            # Create ant rectangle
            ant_rect = pygame.Rect(
                ant_screen_x,
                ant_screen_y,
                int(self.zoom),
                int(self.zoom)
            )
            
            # Draw ant with same style as cells but in red
            radius = max(1, min(int(self.zoom * 0.3), 10))  # Same radius as cells
            pygame.draw.rect(self.screen, ANT_COLOR, ant_rect, border_radius=radius)
        
        # Render title text at the top center
        title_surface = self.title_font.render(TITLE_TEXT, True, (0, 0, 0))
        title_rect = title_surface.get_rect(center=(TITLE_X, TITLE_Y))
        self.screen.blit(title_surface, title_rect)
        
        # Render instruction text at the top center (below title)
        instruction_surface = self.instruction_font.render(INSTRUCTION_TEXT, True, (0, 0, 0))
        instruction_rect = instruction_surface.get_rect(center=(INSTRUCTION_X, INSTRUCTION_Y))
        self.screen.blit(instruction_surface, instruction_rect)
        
        # Render attribution text at the bottom center
        attribution_surface = self.attribution_font.render(ATTRIBUTION_TEXT, True, (0, 0, 0))
        attribution_rect = attribution_surface.get_rect(center=(ATTRIBUTION_X, ATTRIBUTION_Y))
        self.screen.blit(attribution_surface, attribution_rect)
        
        # Draw steps counter button
        steps_text = f"PAS: {self.ant.steps}"
        self.draw_button(STEPS_BUTTON_X, STEPS_BUTTON_Y, STEPS_BUTTON_WIDTH, STEPS_BUTTON_HEIGHT, steps_text)
        
        # Draw buttons
        self.draw_button(EXIT_BUTTON_X, EXIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, EXIT_BUTTON_TEXT)
        self.draw_button(MENU_BUTTON_X, MENU_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, MENU_BUTTON_TEXT)
        
        # Draw menu options if menu is open
        if self.menu_open:
            # Speed button and input field
            self.draw_button(SPEED_BUTTON_X, SPEED_BUTTON_Y, SPEED_BUTTON_WIDTH, SPEED_BUTTON_HEIGHT, SPEED_BUTTON_TEXT)
            
            # Draw speed input field
            input_color = (50, 50, 50) if self.speed_input_active else (100, 100, 100)
            input_rect = pygame.Rect(SPEED_INPUT_X, SPEED_INPUT_Y, SPEED_INPUT_WIDTH, SPEED_INPUT_HEIGHT)
            pygame.draw.rect(self.screen, input_color, input_rect, border_radius=BUTTON_BORDER_RADIUS)
            
            # Draw input text
            input_text_surface = self.button_font.render(self.speed_input_text, True, BUTTON_TEXT_COLOR)
            input_text_rect = input_text_surface.get_rect(center=(SPEED_INPUT_X + SPEED_INPUT_WIDTH // 2, SPEED_INPUT_Y + SPEED_INPUT_HEIGHT // 2))
            self.screen.blit(input_text_surface, input_text_rect)
            
            # Draw pause/play button with appropriate text
            pause_text = PLAY_BUTTON_TEXT if self.paused else PAUSE_BUTTON_TEXT
            self.draw_button(PAUSE_BUTTON_X, PAUSE_BUTTON_Y, PAUSE_BUTTON_WIDTH, PAUSE_BUTTON_HEIGHT, pause_text)
            
            # Draw modify pixels button with highlight if active, otherwise allow hover effect
            if self.modify_mode:
                # When active, always use the highlight color (no hover effect)
                self.draw_button(MODIFY_BUTTON_X, MODIFY_BUTTON_Y, MODIFY_BUTTON_WIDTH, MODIFY_BUTTON_HEIGHT, 
                                MODIFY_BUTTON_TEXT, override_color=MODIFY_HIGHLIGHT_COLOR)
            else:
                # When inactive, don't use override color so hover effect can work
                self.draw_button(MODIFY_BUTTON_X, MODIFY_BUTTON_Y, MODIFY_BUTTON_WIDTH, MODIFY_BUTTON_HEIGHT, 
                                MODIFY_BUTTON_TEXT)
            
            # Draw reset button
            self.draw_button(RESET_BUTTON_X, RESET_BUTTON_Y, RESET_BUTTON_WIDTH, RESET_BUTTON_HEIGHT, RESET_BUTTON_TEXT)
        
        # Draw info screen if in info mode
        if self.info_mode:
            # Draw a semi-transparent black background to darken the main screen
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))  # Black with 70% opacity
            self.screen.blit(overlay, (0, 0))
            
            # Draw the info image in the center
            self.screen.blit(self.info_image, (INFO_IMAGE_X, INFO_IMAGE_Y))
            
            # Draw the video link button
            self.draw_button(VIDEO_BUTTON_X, VIDEO_BUTTON_Y, VIDEO_BUTTON_WIDTH, VIDEO_BUTTON_HEIGHT, VIDEO_BUTTON_TEXT)
        
        # Draw info button last so it's not affected by the overlay
        self.draw_button(INFO_BUTTON_X, INFO_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, INFO_BUTTON_TEXT)
        
        pygame.display.flip()
    
    def draw_button(self, x, y, width, height, text, override_color=None):
        """Draw a button with text centered on it"""
        # Determine button name for hover effect
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
        
        # Determine button color based on hover and override
        if override_color:
            button_color = override_color
        elif button_name == "INFO" and self.info_mode:
            # Use purple color for info button when info mode is active
            button_color = MODIFY_HIGHLIGHT_COLOR
        elif self.hovered_button == button_name and button_name != "SPEED" and button_name != "STEPS":
            # Apply hover effect to all buttons except SPEED and STEPS
            button_color = BUTTON_HOVER_COLOR
        else:
            button_color = BUTTON_COLOR
        
        # Draw the button rectangle
        button_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, button_color, button_rect, border_radius=BUTTON_BORDER_RADIUS)
        
        # Draw the text centered on the button
        text_surface = self.button_font.render(text, True, BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
        self.screen.blit(text_surface, text_rect)
    
    def handle_other_mouse_actions(self, event, mouse_pos):
        """Handle mouse actions that are not button clicks (panning, zooming, pixel modification)"""
        # Handle pixel modification when in modify mode and cooldown is over
        if self.modify_mode and event.button == pygame.BUTTON_LEFT and self.modify_cooldown <= 0:
            # Convert screen coordinates to grid coordinates
            grid_x = int((mouse_pos[0] - self.offset_x) / self.zoom)
            grid_y = int((mouse_pos[1] - self.offset_y) / self.zoom)
            
            # Check if within grid bounds
            if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                # Modify the initial cell
                if self.modify_cell(grid_x, grid_y):
                    self.last_modified_cell = (grid_x, grid_y)
        
        # Handle panning with left mouse button (only when not in modify mode)
        elif not self.modify_mode and event.button == pygame.BUTTON_LEFT:
            self.panning = True
            self.last_mouse_pos = mouse_pos
            # Change cursor to closed/grabbing hand when panning
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEALL)
        
        # Zoom with scroll wheel centered on cursor position - allow in any mode
        elif event.button == 4:  # Scroll up (zoom in)
            self.zoom_at_point(mouse_pos, 1)
        elif event.button == 5:  # Scroll down (zoom out)
            self.zoom_at_point(mouse_pos, -1)
    
    def update_hovered_button(self, mouse_pos):
        """Update which button is currently being hovered over"""
        # Define all button regions
        button_regions = {
            "EXIT": (EXIT_BUTTON_X, EXIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT),
            "INFO": (INFO_BUTTON_X, INFO_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT),
            "MENU": (MENU_BUTTON_X, MENU_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT),
            "STEPS": (STEPS_BUTTON_X, STEPS_BUTTON_Y, STEPS_BUTTON_WIDTH, STEPS_BUTTON_HEIGHT)
        }
        
        # Add video button if in info mode
        if self.info_mode:
            button_regions["VIDEO"] = (VIDEO_BUTTON_X, VIDEO_BUTTON_Y, VIDEO_BUTTON_WIDTH, VIDEO_BUTTON_HEIGHT)
        
        # Add menu option buttons if menu is open
        if self.menu_open:
            button_regions.update({
                "SPEED": (SPEED_BUTTON_X, SPEED_BUTTON_Y, SPEED_BUTTON_WIDTH, SPEED_BUTTON_HEIGHT),
                "SPEED_INPUT": (SPEED_INPUT_X, SPEED_INPUT_Y, SPEED_INPUT_WIDTH, SPEED_INPUT_HEIGHT),
                "PAUSE": (PAUSE_BUTTON_X, PAUSE_BUTTON_Y, PAUSE_BUTTON_WIDTH, PAUSE_BUTTON_HEIGHT),
                "MODIFY": (MODIFY_BUTTON_X, MODIFY_BUTTON_Y, MODIFY_BUTTON_WIDTH, MODIFY_BUTTON_HEIGHT),
                "RESET": (RESET_BUTTON_X, RESET_BUTTON_Y, RESET_BUTTON_WIDTH, RESET_BUTTON_HEIGHT)
            })
        
        # Check if mouse is over any button
        for button_name, rect in button_regions.items():
            if self.is_point_in_rect(mouse_pos, rect):
                self.hovered_button = button_name
                return
        
        # No button is hovered
        self.hovered_button = None
    
    def run(self):
        # Play the start sound when the simulation begins
        START_SOUND.play()
        
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

# Main entry point
if __name__ == "__main__":
    simulation = Simulation()
    simulation.run()

