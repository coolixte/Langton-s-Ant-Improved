# ✦ LANGTON'S ANT IMPROVED ✦ ------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------

# NOTES ✦ ---------------------------------------------------------------------------------------------

# Info button, settings button, exit button

# MODULES ✦ -------------------------------------------------------------------------------------------
import pygame
import numpy as np
import sys

# Initialize Pygame
pygame.init()

# CONSTANTS ✦ -----------------------------------------------------------------------------------------
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 5  # Initial cell size in pixels
GRID_WIDTH = 200  # Number of cells in the grid width
GRID_HEIGHT = 200  # Number of cells in the grid height
BG_COLOR = (255, 255, 255)  # White
ANT_COLOR = (255, 0, 0)  # Red
CELL_ON_COLOR = (0, 0, 0)  # Black
CELL_OFF_COLOR = (255, 255, 255)  # White
FPS = 60

# Attribution text constants
ATTRIBUTION_TEXT = "2025 · @Calixte Lamotte"
ATTRIBUTION_X = WINDOW_WIDTH // 2  # Centered horizontally
ATTRIBUTION_Y = WINDOW_HEIGHT - 15  # 15 pixels from bottom

# Title text constants
TITLE_TEXT = "LANGTON'S ANT IMPROVED"
TITLE_X = WINDOW_WIDTH // 2  # Centered horizontally
TITLE_Y = 25  # 30 pixels from top
TITLE_SIZE = 25  # Font size
TITLE_FONT = "Lobster"  # Fancy font for title

# Instruction text constants
INSTRUCTION_TEXT = "ZOOM / PAN AVEC LA SOURIS"
INSTRUCTION_X = WINDOW_WIDTH // 2  # Centered horizontally
INSTRUCTION_Y = 50  # Adjusted to be below title
INSTRUCTION_SIZE = 12  # Font size

# Simulation parameters
SIMULATION_SPEED = 0.1  # Steps per frame (now supports fractional values)

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
        
        # Turn right on white (0), left on black (1)
        if current_cell == 0:
            self.direction = (self.direction + 1) % 4  # Turn right (clockwise)
        else:
            self.direction = (self.direction - 1) % 4  # Turn left (counter-clockwise)
        
        # Move forward
        dx, dy = self.movement[self.direction]
        self.ant_x = (self.ant_x + dx) % self.grid.shape[0]
        self.ant_y = (self.ant_y + dy) % self.grid.shape[1]
        
        self.steps += 1

class Simulation:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
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
        
        # Simulation state
        self.running = True
        self.paused = False
        
        # For handling fractional speeds
        self.step_accumulator = 0.0
        
        # Set default cursor to open hand
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        
        # Prepare fonts
        self.attribution_font = pygame.font.SysFont("Arial", 10)
        self.instruction_font = pygame.font.SysFont("Arial", INSTRUCTION_SIZE)
        self.title_font = pygame.font.SysFont("Arial", TITLE_SIZE, bold=True)
    
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
            
            # Mouse controls for panning (now default with left mouse button)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    self.panning = True
                    self.last_mouse_pos = event.pos
                    # Change cursor to closed/grabbing hand when panning
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEALL)
                
                # Zoom with scroll wheel centered on cursor position
                elif event.button == 4:  # Scroll up (zoom in)
                    self.zoom_at_point(event.pos, 1)
                elif event.button == 5:  # Scroll down (zoom out)
                    self.zoom_at_point(event.pos, -1)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    self.panning = False
                    # Change cursor back to open hand when not panning
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            
            elif event.type == pygame.MOUSEMOTION:
                if self.panning:
                    dx = event.pos[0] - self.last_mouse_pos[0]
                    dy = event.pos[1] - self.last_mouse_pos[1]
                    self.offset_x += dx
                    self.offset_y += dy
                    self.last_mouse_pos = event.pos

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
                if self.ant.grid[x, y] == 1:  # Only draw colored cells (black ones)
                    cell_rect = pygame.Rect(
                        int(self.offset_x + x * self.zoom), 
                        int(self.offset_y + y * self.zoom), 
                        int(self.zoom), 
                        int(self.zoom)
                    )
                    
                    # Draw rounded rectangle
                    radius = max(1, min(int(self.zoom * 0.3), 10))  # Scale radius with zoom, but cap it
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
        
        pygame.display.flip()
    
    def run(self):
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

