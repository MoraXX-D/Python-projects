class settings():
    '''Setting module for alien invader game'''
    def __init__(self):
        '''Initialize the game settings.'''
        # screen setting
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230,230,230)

        # ship setting
        self.ship_speed_factor = 1.5

        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60