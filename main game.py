# library imports
import os
import pygame
import pygame_gui
import random

pygame.init() # initialises pygame
pygame.mixer.init()

#-------------------------------------GAME CLASSES---------------------------------------
# class card
class card:
    # constructor 
    def __init__(self, nname, ntype, ndmg, nheal, ncost, ndescription, nid):
        self.name = str(nname)
        self.type = str(ntype)
        self.dmg = int(ndmg)
        self.heal = int(nheal)
        self.cost = int(ncost)
        self.description = str(ndescription)
        self.id = int(nid)

# getters and setters
    def getname(self):
        return self.name
    

    def gettype(self):
        return self.type


    def getdmg(self):
        return self.dmg
    
    def setdmg(self, gdmg):
        self.dmg = gdmg


    def getheal(self):
        return self.heal
    
    def setheal(self, gheal):
        self.heal = gheal


    def getcost(self):
        return self.cost
    

    def getdescription(self):
        return self.description


    def getid(self):
        return self.id
    
    def clone(self):
        return card(self.name, self.type, self.dmg, self.heal, self.cost, self.description, self.id)
    

# class player
class player:
        # constructor 
    def __init__(self, nname, nhealth, nenergy, nis_turn):
        self.name = str(nname)
        self.health = int(nhealth)
        self.energy = int(nenergy)
        self.deck = []
        self.hand = []
        self.discard_pile = []
        self.status_effects = None
        self.is_turn = bool(nis_turn)

# getters and setters
    def getname(self):
        return self.name


    def setname(self, gname):
        self.name = gname


    def gethealth(self):
        return self.health
    

    def sethealth(self, ghealth):
        self.health = ghealth


    def getenergy(self):
        return self.energy
    

    def setenergy(self, genergy):
        self.energy = genergy


    def getdeck(self):
        return self.deck
    

    def setdeck(self, gdeck):
        self.deck = gdeck


    def addtodeck(self, gcard):
        self.deck.append(gcard)


    def gethand(self):
        return self.hand
    

    def gethandlength(self):
        return len(self.hand)
    

    def sethand(self, ghand):
        self.hand = ghand


    def addtohand(self, gcard):
        self.hand.append(gcard)    


    def getdiscard_pile(self):
        return self.discard_pile
    

    def setdiscard_pile(self, gdiscard_pile):
        self.discard_pile = gdiscard_pile


    def getstatus_effects(self):
        return self.status_effects
    

    def setstatus_effects(self, gstatus_effects):
        self.status_effects = gstatus_effects


    def getis_turn(self):
        return self.is_turn
    

    def setis_turn(self, gis_turn):
        self.is_turn = gis_turn


    def replenish_deck(self):
        self.deck.extend(self.hand)
        self.deck.extend(self.discard_pile)
        self.hand.clear()
        self.discard_pile.clear()


    # methods
    def draw_card(self):
        if self.deck: # if deck is not empty
            if len(self.hand) < 5: # if hand isn't full
                self.hand.append(self.deck.pop(0)) # remove top card from deck and append to hand
            else:
                print("Hand is full.")
        else:
            self.shuffle_deck()
            if self.deck:
                self.hand.append(self.deck.pop(0))
            else:
                print("No cards in game.")


    def discard_card(self):
        if self.hand: 
            # ensure only valid cards
            self.hand = [c for c in self.hand if isinstance(c, card)]
            for card in selected_cards:
                if card in self.hand:
                    self.hand.remove(card)
                    self.discard_pile.append(card)  # guaranteed instance
                else:
                    print("Card not found in hand.")
            selected_cards.clear()
        else:
            print("Hand is empty.")


    def shuffle_deck(self):
        if self.deck: # checks if there are cards in deck
            random.shuffle(self.deck)
        elif self.discard_pile: 
            self.setdeck(self.discard_pile[:]) # copies discard_pile into deck (else when discard_pile gets deleted, so does deck)
            self.setdiscard_pile([])
            random.shuffle(self.deck)
        else:
            print("No cards to shuffle.")	
            

# class game
class game:
    # constructor 
    def __init__(self, nturn_counter, ncurrent_player_index):
        self.players = None
        self.turn_counter = int(nturn_counter)
        self.current_player_index = int(ncurrent_player_index)
        self.game_over = False
        self.winner = None

# getters and setters
    def getplayers(self):
        return self.players
    
    def setplayers(self, gplayers):
        self.players = gplayers


    def getturn_counter(self):
        return self.turn_counter
    
    def setturn_counter(self, gturn_counter):
        self.type = gturn_counter


    def getcurrent_player_index(self):
        return self.current_player_index


    def switch_current_player(self):
        if self.current_player_index == 1:
            self.current_player_index = 2
        else:
            self.current_player_index = 1


    def getgame_over(self):
        return self.game_over
    
    def setgame_over(self):
        self.game_over = True


    def getwinner(self):
        return self.winner

    def setwinner(self, gwinner):
        self.winner = str(gwinner)


    # methods
    def next_turn(self):
        if self.current_player_index == 2:
            self.turn_counter += 1


class panel:
    def __init__(self, nname, nx, ny, nwidth, nheight, nmanager):
        self.name = nname
        self.x = nx
        self.y = ny
        self.width = nwidth
        self.height = nheight
        self.manager = nmanager
        self.box = None
        self.label = None
        self.text_label = None
        self.image = None  # store reference to image

    def setname(self, gname):
        self.name = str(gname)
        if self.label:
            self.label.set_text(self.name)

    def getname(self):
        return self.name

    def create_panel(self):
        centered_x = self.x - (self.width / 2)
        centered_y = self.y - (self.height / 2)

        self.box = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((centered_x, centered_y), (self.width, self.height)),
            manager=self.manager
        )

        label_width = 200
        label_height = 30
        label_x = (self.width - label_width) // 2
        label_y = (self.height - label_height) // 2

        self.label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((label_x, label_y), (label_width, label_height)),
            text=self.name,
            manager=self.manager,
            container=self.box
        )

        return self.box

    def create_image(self, image_surface, width=None, height=None):

        # if a path is given, load it into a pygame Surface
        if isinstance(image_surface, str):
            image_surface = pygame.image.load(image_surface).convert_alpha()

        if width is None:
            width = image_surface.get_width()
        if height is None:
            height = image_surface.get_height()

        img_x = (self.width - width) // 2
        img_y = (self.height - height) // 2

        self.image = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((img_x, img_y), (width, height)),
            image_surface=image_surface,
            manager=self.manager,
            container=self.box
        )

        return self.image
    
    def add_text_block(self, text):
        if not self.box:
            raise Exception("Panel must be created before adding text.")

        # removes existing label if it exists
        if self.text_label:
            self.text_label.kill()

        padding = 25
        box_width = self.width - 2 * padding
        box_height = self.height - 2 * padding

        self.text_label = pygame_gui.elements.UITextBox(
            html_text=text.replace("\n", "<br>"),
            relative_rect=pygame.Rect((padding, padding), (box_width, box_height)),
            manager=self.manager,
            container=self.box,
            anchors={
                'top': 'top',
                'left': 'left'
            }
        )

        return self.text_label


# blueprint for every button
class button:
    # constructor 
    def __init__(self, nname, nx, ny, nwidth, nheight, nmanager):
        self.name = nname
        self.x = nx
        self.y = ny
        self.width = nwidth
        self.height = nheight
        self.manager = nmanager
        self.ui_button = None
        self.image_element = None

    def setname(self, gname):
        self.name = str(gname)

    def getname(self):
        return self.name
    
    def getx(self):
        return self.x
    
    def gety(self):
        return self.y

    def create_box(self):
        centered_x = self.x - (self.width / 2)
        centered_y = self.y - (self.height / 2)

        self.ui_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((centered_x, centered_y), (self.width, self.height)),
            text=self.name,
            manager=self.manager
        )
        return self.ui_button
    
    def create_image(self, image_filename):
        centered_x = self.x - (self.width / 2)
        centered_y = self.y - (self.height / 2)

        image_path = os.path.join("ASSETS", image_filename)
        image_surface = pygame.image.load(image_path).convert_alpha()
        image_surface = pygame.transform.scale(image_surface, (self.width, self.height))

        self.image_element = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((centered_x, centered_y), (self.width, self.height)),
            image_surface=image_surface,
            manager=self.manager
        )
        return self.image_element


# in_game card button and for deck asw. when clicked, it calls select_card(card) with card val from getcard(self)
class card_button(button):
    #constructor 
    def __init__(self, nname, nx, ny, nwidth, nheight, nmanager, ncard): 
        self.card = ncard
        super().__init__(nname, nx, ny, nwidth, nheight, nmanager)

    #getters and setters
    def getcard(self):
        return self.card

    def setcard(self, gcard):
        self.card = gcard

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

        centered_pos = (new_x - (self.width // 2), new_y - (self.height // 2))

        # move button
        self.ui_button.set_relative_position(centered_pos)

        # move image too if one exists
        if hasattr(self, "image_element") and self.image_element is not None:
            self.image_element.set_relative_position(centered_pos)

#---------------------------------------------------------------------------------------


#-----------------------------------GAME LOGIC SECTION-----------------------------------
def start_game():
    new_game = game(1, 1)
    new_game.setplayers([player_1, player_2])

    for player in new_game.getplayers():
        player.sethealth(100)
        player.setenergy(10)
        player.shuffle_deck()

        for i in range(5):
            player.draw_card()
    
    player_1.setis_turn(True)
    player_2.setis_turn(False)

    return new_game


def check_current_player():
    if new_game.getcurrent_player_index() == 1:
        current_player = player_1
        opponent = player_2
    else:
        current_player = player_2
        opponent = player_1
    return current_player, opponent


def switch_turn():
    current_player, opponent = check_current_player()

    for x in selected_cards:
        if x in current_player.gethand():
            current_player.gethand().remove(x)
            current_player.getdiscard_pile().append(x)

    print(current_player.gethandlength())

    selected_cards.clear()
    current_player.draw_card()
    if current_player.getenergy() <= 8:
        current_player.setenergy(current_player.getenergy() + 2)

    new_game.switch_current_player()
    current_player, opponent = check_current_player()
    current_player.setis_turn(True)
    opponent.setis_turn(False)


# applies selected cards effects
def apply_card_effect():
    current_player, opponent = check_current_player()

    total_damage = 0
    total_heal = 0
    total_energy_cost = 0

    if selected_cards:
        for card in selected_cards:
            total_energy_cost += card.getcost()

    if current_player.getenergy() < total_energy_cost:
        print("Not enough energy to play all selected cards.")
        selected_cards.clear()
        return None  # don't apply effects

    for card in selected_cards:
        damage = card.getdmg()
        heal = card.getheal()
        cost = card.getcost()

        current_player.setenergy(current_player.getenergy() - cost)
        opponent.sethealth(opponent.gethealth() - damage)
        current_player.sethealth(current_player.gethealth() + heal)

        total_damage += damage
        total_heal += heal

    return total_damage, total_heal, total_energy_cost


# on click select and if clicked again deselect
def select_card(clicked_card): # clicked_card is selected from card in hand by click
    if clicked_card in selected_cards:
        selected_cards.remove(clicked_card)
    else:
        selected_cards.append(clicked_card)
    return selected_cards


def take_turn():
    result = apply_card_effect()

    if result is None:
        print("Turn not ended. Not enough energy.")

        return  False # player must modify selection and try again
    else:
        total_damage, total_heal, total_energy_cost = result # take total_damage, total_heal, total_energy_cost as parameters to change ui
        print(f"Used {total_energy_cost} energy, dealt {total_damage} damage, healed {total_heal} HP.")

        return True

# checks if a player hits 0 health, then sets the other player as the winner and sets game as over
def check_game_over():
    current_player, opponent = check_current_player()

    if current_player.gethealth() <= 0 and opponent.gethealth() <= 0: # if both players die
        new_game.setwinner("DRAW.")
        new_game.setgame_over()
        return True
    
    elif new_game.getturn_counter() > 10: # if turn counter > max rounds (if no one dies)

        if current_player.gethealth() > opponent.gethealth(): # if player has more health than opponent
            new_game.setwinner(f"{current_player.getname()} WINS.")
            new_game.setgame_over()
            return True
        
        elif current_player.gethealth() < opponent.gethealth():  # if opponent has more health than player
            new_game.setwinner(f"{opponent.getname()} WINS.")
            new_game.setgame_over() 
            return True
        
        else: # if they have the same health at the end of the game
            new_game.setwinner("Draw.")
            new_game.setgame_over()
            return True
        
    elif opponent.gethealth() <= 0: # if opponent dies
        new_game.setwinner(f"{current_player.getname()} WINS.")
        new_game.setgame_over()
        return True
    
    elif current_player.gethealth() <= 0: # if current player kills themself
        new_game.setwinner(f"{opponent.getname()} WINS.")
        new_game.setgame_over()
        return True
    
    else:
        return False

#---------------------------------------------------------------------------------------


#----------------------------------------UI SECTION-------------------------------------
def draw_startup():
    image_surface = pygame.image.load("ASSETS/TEXT/title text.png").convert_alpha()
    scaled_surface = pygame.transform.scale(image_surface, (1000, 250))

    title_text = pygame_gui.elements.UIImage(
        relative_rect=scaled_surface.get_rect(center=(width//2, (height//2) - 100)),
        image_surface=scaled_surface,
        manager=manager
    )

    active_ui_elements.append(title_text)

    # GREY BACKGROUND BOXES
    # middle box
    middle = panel(" ", width // 2, int(3 * height / 4), 880, 140, manager)
    middle_box = middle.create_panel()

    # left box
    left = panel(" ", (width // 4) - 200, int(3 * height / 4), 140, 140, manager)
    left_box = left.create_panel()  

    # right box
    right = panel(" ", width - (width // 4) + 200, int(3 * height / 4), 140, 140, manager)
    right_box = right.create_panel()

    # BUTTONS
    play = button(" ", width // 2 - 320, int(3 * height / 4), 200, 100, manager)
    play_button = play.create_box()
    play_image = play.create_image("BUTTONS/STARTUP/PLAY image.png")

    instructions = button(" ", width // 2 - 105, int(3 * height / 4) + 10, 180, 80, manager)
    instructions_button = instructions.create_box()
    instructions_image = instructions.create_image("BUTTONS/STARTUP/INSTRUCTIONS image.png")

    quit = button(" ", width // 2 + 105, int(3 * height / 4) + 10, 180, 80, manager)
    quit_button = quit.create_box()
    quit_image = quit.create_image("BUTTONS/STARTUP/QUIT image.png")

    edit_deck = button(" ", width // 2 + 320, int(3 * height / 4), 200, 100, manager)
    edit_deck_button = edit_deck.create_box()
    edit_deck_image = edit_deck.create_image("BUTTONS/STARTUP/EDIT DECK image.png")

    player_select = button(current_profile, (width // 4) - 200, int(3 * height / 4), 100, 100, manager)
    player_select_button = player_select.create_box()

    settings = button(" ", width - (width // 4) + 200, int(3 * height / 4), 100, 100, manager)
    settings_button = settings.create_box()
    settings_image = settings.create_image("BUTTONS/UNIVERSAL/SETTINGS image.png")

    # add to active elements
    active_ui_elements.extend([
        # panels
        middle_box,
        left_box,
        right_box,

        # buttons
        play_button,
        instructions_button,
        quit_button,
        edit_deck_button,
        player_select_button,
        settings_button,

        # images
        play_image,
        instructions_image,
        quit_image,
        edit_deck_image,
        settings_image

    ])

    return player_select, play_button, instructions_button, quit_button, edit_deck_button, player_select_button, settings_button


def draw_deck():
    # background panel
    background = panel(" ", width // 2, int(height / 2), 1000, 800, manager).create_panel()

    # change top card
    deck_left = button("<  ", width // 2 - 450, int(height / 2) + 120, 50, 50, manager)
    deck_left_button = deck_left.create_box()
    deck_left_image = deck_left.create_image("BUTTONS/DECK/LEFTARROW image.png")

    deck_right = button(">", width // 2 + 450, int(height / 2) + 120, 50, 50, manager)
    deck_right_button = deck_right.create_box()
    deck_right_image = deck_right.create_image("BUTTONS/DECK/RIGHTARROW image.png")

    # deck cards 
    card_slot1 = button(" ", width // 2 - 350, int(height / 2) + 120, 125, 225, manager)
    card_slot1_box = card_slot1.create_box()

    card_slot2 = button(" ", width // 2 - 250, int(height / 2) + 120, 150, 250, manager)
    card_slot2_box = card_slot2.create_box()

    card_slot3 = button(" ", width // 2 - 150, int(height / 2) + 120, 175, 275, manager)
    card_slot3_box = card_slot3.create_box()

    top_card = card_button(" ", width // 2, int(height / 2) + 120, 200, 300, manager, "")
    top_card_ui = top_card.create_box()

    card_slot4 = button(" ", width // 2 + 150, int(height / 2) + 120, 175, 275, manager)
    card_slot4_box = card_slot4.create_box()

    card_slot5 = button(" ", width // 2 + 250, int(height / 2) + 120, 150, 250, manager)
    card_slot5_box = card_slot5.create_box()

    card_slot6 = button(" ", width // 2 + 350, int(height / 2) + 120, 125, 225, manager)
    card_slot6_box = card_slot6.create_box()


    # race
    race_temp1 = panel("Races", width // 2 - 325, int(height / 2) - 350, 275, 60, manager).create_panel()
    race_temp2 = panel(" ", width // 2 - 325, int(height / 2) - 175, 275, 275, manager).create_panel()

    human = button("human", width // 2 - 385, int(height / 2) - 235, 110, 110, manager)
    human_button = human.create_box()
    human_image = human.create_image("BUTTONS/DECK/HUMAN image.png")

    elf = button("elf", width // 2 - 265, int(height / 2) - 235, 110, 110, manager)
    elf_button = elf.create_box()
    elf_image = elf.create_image("BUTTONS/DECK/ELF image.png")

    dwarf = button("dwarf", width // 2 - 385, int(height / 2) - 115, 110, 110, manager)
    dwarf_button = dwarf.create_box()
    dwarf_image = dwarf.create_image("BUTTONS/DECK/DWARF image.png")

    undead = button("undead", width // 2 - 265, int(height / 2) - 115, 110, 110, manager)
    undead_button = undead.create_box()
    undead_image = undead.create_image("BUTTONS/DECK/UNDEAD image.png")


    # description
    description_temp = panel("Card Description", width // 2, int(height / 2) - 350, 350, 60, manager).create_panel()
    description = panel(" ", width // 2, int(height / 2) - 175, 350, 250, manager)
    description_panel = description.create_panel()


    # card select
    card_select_temp1 = panel("Choose Card", width // 2 + 325, int(height / 2) - 350, 275, 60, manager).create_panel()
    card_select_temp2 = panel(" ", width // 2 + 325, int(height / 2) - 175, 275, 275, manager).create_panel()

    current_race_card = card_button(" ", width // 2 + 325, int(height / 2) - 208, 125, 175, manager, " ")
    current_race_card_button = current_race_card.create_box()

    race_right = button(">", width // 2 + 423, int(height / 2) - 208, 50, 50, manager)
    race_right_button = race_right.create_box()
    race_right_image = race_right.create_image("BUTTONS/DECK/RIGHTARROW image.png")

    race_left = button("<  ", width // 2 + 227, int(height / 2) - 208, 50, 50, manager)
    race_left_button = race_left.create_box()
    race_left_image = race_left.create_image("BUTTONS/DECK/LEFTARROW image.png")

    deck_player_select = button(current_profile, width // 2 - 450, int(height / 2), 60, 40, manager)
    deck_player_select_button = deck_player_select.create_box()

    deck_size_panel = panel(" ", width // 2 + 450, int(height / 2), 60, 40, manager)
    deck_size_count = deck_size_panel.create_panel()

    select = button("Select", width // 2 + 325, int(height / 2) - 80, 250, 60, manager)
    select_button = select.create_box()
    select_image = select.create_image("BUTTONS/DECK/SELECT image.png")

    # close button
    close = button("Back To Menu", width // 2, int(height / 2) + 330, 900, 80, manager)
    close_button = close.create_box()
    close_image = close.create_image("BUTTONS/DECK/BACK image.png")

    # add to active elements
    active_ui_elements.extend([
        # labels
        background,
        
        card_slot1_box,
        card_slot2_box,
        card_slot3_box,
        card_slot4_box,
        card_slot5_box,
        card_slot6_box,

        race_temp1,
        race_temp2,

        description_temp,
        description_panel,

        card_select_temp1,
        card_select_temp2,

        # buttons
        deck_size_count,
        deck_left_button,
        deck_right_button, 
        top_card_ui,
        human_button, 
        elf_button, 
        dwarf_button, 
        undead_button,  
        current_race_card_button, 
        race_right_button, 
        race_left_button, 
        deck_player_select_button,
        select_button, 
        close_button,

        # images
        select_image,
        race_right_image,
        race_left_image,
        deck_left_image,
        deck_right_image,
        close_image, 
        human_image,
        elf_image,
        dwarf_image,
        undead_image

    ])

    return deck_player_select, deck_player_select_button, deck_size_panel, deck_left_button, deck_right_button, card_slot1, card_slot2, card_slot3, card_slot4, card_slot5, card_slot6, top_card, human_button, elf_button, dwarf_button, undead_button, description, current_race_card, current_race_card_button, race_right_button, race_left_button, deck_player_select_button, select_button, close_button
    

def draw_instructions():
    startup_background_image, _, _ = declare_images()
    screen.blit(startup_background_image, (0, 0))  # background colour

    # background panel
    background = panel(" ", width // 2, int(height / 2), 1000, 800, manager).create_panel()

    # text box
    instruction_box = panel(" ", width // 2, int(height / 2) - 50, 900, 600, manager)
    text_temp = instruction_box.create_panel()

    # close button  
    close =  button("Back To Menu", width // 2, int(height / 2) + 330, 900, 80, manager)
    close_button = close.create_box()
    close_image = close.create_image("BUTTONS/DECK/BACK image.png")

    # add to active element
    active_ui_elements.extend([
        # labels
        background,
        text_temp,

        # buttons
        close_button,

        # images
        close_image

    ])
    
    return close_button, instruction_box


def draw_playing():
    # GREY BACKGROUND BOXES
    # left box
    left = panel(" ", (width // 4) - 200, height / 2, 500, height, manager).create_panel()

    # settings button
    pause = button("Settings", (width // 4) - 387, height / 2 - 470, 75, 75, manager)
    pause_button = pause.create_box()
    pause_image = pause.create_image("BUTTONS/UNIVERSAL/SETTINGS image.png")

    # round info
    round_info = panel("Current Round: ", (width // 4) - 75, height / 2 - 470, 200, 75, manager)
    round_info_panel = round_info.create_panel()

    # INFO PANELS
    # opponent health
    op_health = panel("Opponent Health: ", (width // 4) - 200, height / 2 - 370, 450, 75, manager)
    op_health_panel = op_health.create_panel()

    # player health
    p_health = panel("Player Health: ", (width // 4) - 200, height / 2 - 270, 450, 75, manager)
    p_health_panel = p_health.create_panel()

    p_energy = panel("Energy", width - (width // 4) + 150, int(3 * height / 4) - 140, 120, 75, manager)
    p_energy_panel = p_energy.create_panel()

    op_energy = panel("Energy", (width // 2) - 250, int(height / 2) - 370, 120, 75, manager)
    op_energy_panel = op_energy.create_panel()

    # chat box
    description = panel(" ", (width // 4) - 200, (height / 2) + 64, 450, 275, manager)
    description_box_background = description.create_panel()
    description_panel = panel("Card Description", (width // 4) - 200, height / 2 - 95, 450, 60, manager).create_panel()

    # timer
    timer = panel(f"1:00", (width // 4) - 200, (height / 2) + 300, 450, 75, manager)
    timer_panel = timer.create_panel()

    # end round
    end = button("End Round", (width // 4) - 200, height / 2 + 430, 450, 125, manager)
    end_round = end.create_box()
    end_image = end.create_image("BUTTONS/PLAYING/END ROUND image.png")
    

    # PLAYER LABELS
    # player
    p_label = panel("Player Name", width - (width // 4) - 720, int(height / 2) + 170, 200, 50, manager)
    p_label_panel = p_label.create_panel()

    # opponent
    op_label = panel("Opponent Name", width - (width // 4) + 280, int(height / 2) - 370, 200, 50, manager)
    op_label_panel = op_label.create_panel()

    # play area
    play_area = panel(" ", width - (width // 4) - 220, int(height / 2) - 150, 1240, 340, manager).create_panel()

    # CARD BOXES
    # player
    card_1 = card_button(" ", width - (width // 4) - 720, int(3 * height / 4) + 100, 200, 300, manager, " ")
    card_1_button = card_1.create_box()

    card_2 = card_button(" ", width - (width // 4) - 470, int(3 * height / 4) + 100, 200, 300, manager, " ")
    card_2_button = card_2.create_box()

    card_3 = card_button(" ", width - (width // 4) - 220, int(3 * height / 4) + 100, 200, 300, manager, " ")
    card_3_button = card_3.create_box()

    card_4 = card_button(" ", width - (width // 4) + 30, int(3 * height / 4) + 100, 200, 300, manager, " ")
    card_4_button = card_4.create_box()
    
    card_5 = card_button(" ", width - (width // 4) + 280, int(3 * height / 4) + 100, 200, 300, manager, " ")
    card_5_button = card_5.create_box()

    # opponent
    opponent_temp1 = panel(" ", width - (width // 4) - 720, int(height / 4) - 300, 200, 300, manager).create_panel()
    opponent_temp2 = panel(" ", width - (width // 4) - 470, int(height / 4) - 300, 200, 300, manager).create_panel()
    opponent_temp3 = panel(" ", width - (width // 4) - 220, int(height / 4) - 300, 200, 300, manager).create_panel()
    opponent_temp4 = panel(" ", width - (width // 4) + 30, int(height / 4) - 300, 200, 300, manager).create_panel()
    opponent_temp5 = panel(" ", width - (width // 4) + 280, int(height / 4) - 300, 200, 300, manager).create_panel()

    # deck
    deck_temp1 = panel(" ", width - (width // 4) + 280, int(3 * height / 4) - 140, 100, 150, manager).create_panel()
    deck_temp2 = panel(" ", width - (width // 4) + 280, int(3 * height / 4) - 145, 100, 150, manager).create_panel()
    deck_temp3 = panel(" ", width - (width // 4) + 280, int(3 * height / 4) - 150, 100, 150, manager).create_panel()
    deck_temp4 = panel(" ", width - (width // 4) + 280, int(3 * height / 4) - 155, 100, 150, manager).create_panel()
    top_of_deck = panel("deck", width - (width // 4) + 280, int(3 * height / 4) - 160, 100, 150, manager).create_panel()

    # discard pile
    discard_temp1 = panel(" ", width - (width // 4) + 400, int(3 * height / 4) - 140, 100, 150, manager).create_panel()
    discard_temp2 = panel(" ", width - (width // 4) + 400, int(3 * height / 4) - 145, 100, 150, manager).create_panel()
    discard_temp3 = panel(" ", width - (width // 4) + 400, int(3 * height / 4) - 150, 100, 150, manager).create_panel()
    discard_temp4 = panel(" ", width - (width // 4) + 400, int(3 * height / 4) - 155, 100, 150, manager).create_panel()
    top_of_discard_pile = panel("discard", width - (width // 4) + 400, int(3 * height / 4) - 160, 100, 150, manager).create_panel()

    # add to active elements
    active_ui_elements.extend([
        # panels
        left,
        round_info_panel,
        op_health_panel,
        p_health_panel,
        p_energy_panel,
        op_energy_panel,
        description_box_background,
        description_panel,
        timer_panel,
        p_label_panel,
        op_label_panel,
        play_area, 

        opponent_temp1,
        opponent_temp2,
        opponent_temp3,
        opponent_temp4,
        opponent_temp5,

        deck_temp1,
        deck_temp2,
        deck_temp3,
        deck_temp4,
        top_of_deck,

        discard_temp1,
        discard_temp2,
        discard_temp3,
        discard_temp4,
        top_of_discard_pile,

        # buttons
        pause_button,  
        end_round, 
        card_1_button, 
        card_2_button, 
        card_3_button, 
        card_4_button, 
        card_5_button, 

        # images
        pause_image,
        end_image

    ])

    return pause_button, end_round, card_1, card_2, card_3, card_4, card_5, card_1_button, card_2_button, card_3_button, card_4_button, card_5_button, description, op_health, p_health, p_energy, op_energy, round_info, p_label, op_label, timer


def draw_game_ended():
    # background panel
    background = panel(" ", width // 2, int(height / 2), 1000, 800, manager).create_panel()

    # win/lose
    w_l = panel(new_game.getwinner(), width // 2, int(height / 2) - 150, 800, 240, manager).create_panel()

    # replay button
    replay_instance = button("Replay", width // 2, int(height / 2) + 150, 800, 80, manager)
    replay = replay_instance.create_box()
    replay_image = replay_instance.create_image("BUTTONS/GAME_ENDED/REPLAY image.png")

    # close button
    close = button("Back To Menu", width // 2, int(height / 2) + 250, 800, 80, manager)
    close_button = close.create_box()
    close_image = close.create_image("BUTTONS/GAME_ENDED/BACK image.png")

    # add to active elements
    active_ui_elements.extend([
        # panels
        background,
        w_l,
        
        # buttons
        replay,
        close_button,

        # images
        replay_image,
        close_image 

    ])

    return close_button, replay


def draw_pause_menu():
    draw_playing_background()  # background colour

    # background panel
    background = panel(" ", width // 2, int(height / 2), 1000, 800, manager).create_panel()

    # resume button
    resume = button("Resume Game", width // 2, int(height / 2) -50, 800, 80, manager)
    resume_button = resume.create_box()
    resume_image = resume.create_image("BUTTONS/PAUSE_MENU/RESUME image.png")

    # close button
    close = button("Back To Menu", width // 2, int(height / 2) + 50, 800, 80, manager)
    close_button = close.create_box()
    close_image = close.create_image("BUTTONS/PAUSE_MENU/CLOSE image.png")

    # add to active elements
    active_ui_elements.extend([
        # panels
        background,

        # buttons
        resume_button,
        close_button,

        # image 
        close_image,
        resume_image

    ])

    return resume_image, close_image, background, resume_button, close_button

#---------------------------------------------------------------------------------------


#-----------------------------------DECLARE FUNCTIONS-----------------------------------

def declare_cards():
    # Human cards
    scheming_saint = card("Scheming Saint", "HUMAN", 0, 20, 2, "Heals big but drains your wallet.", 1)
    soldier = card("Soldier", "HUMAN", 10, 0, 1, "Reliable and cheap.", 2)
    combat_medic = card("Combat Medic", "HUMAN", 10, 10, 2, "Supportive all-rounder.", 3)
    sergeant = card("Sergeant", "HUMAN", 20, 0, 2, "Clean strike.", 4)
    alchemist = card("Alchemist", "HUMAN", 30, -15, 3, "Risky gamble for burst.", 5)

    human_cards = [scheming_saint, soldier, combat_medic, sergeant, alchemist]

    # Elf cards
    grand_elf = card("Grand Elf", "ELF", 5, 15, 2, "Graceful and precise.", 6)
    natures_touch = card("Nature's Touch", "ELF", 0, 25, 2, "Great stall tool.", 7)
    moonblade = card("Moonblade", "ELF", 10, 5, 1, "Nimble strike.", 8)
    arcane_warden = card("Arcane Warden", "ELF", 15, 10, 2, "Versatile role.", 9)
    lifeweaver = card("Life Weaver", "ELF", 5, 30, 3, "Big sustain.", 10)

    elf_cards = [grand_elf, natures_touch, moonblade, arcane_warden, lifeweaver]

    # Dwarf cards
    urdunnir = card("Urdunnir", "DWARF", 15, 0, 1, "Strong basic hit.", 11)
    war_smith = card("War Smith", "DWARF", 25, 0, 2, "Smashes through defences.", 12)
    iron_veteran = card("Iron Veteran", "DWARF", 20, 5, 2, "Battle-hardened support.", 13)
    brewmaster = card("Brewmaster", "DWARF", 10, 15, 3, "Heavy hitter and healer.", 14)
    anvil_guard = card("Anvil Guard", "DWARF", 30, 0, 4, "Titan strike.", 15)

    dwarf_cards = [urdunnir, war_smith, iron_veteran, brewmaster, anvil_guard]

    # Undead cards
    witch = card("Witch", "UNDEAD", 10, 0, 1, "Cheap and effective.", 16)
    blood_pact = card("Blood Pact", "UNDEAD", 20, -10, 2, "Burn yourself to burn others.", 17)
    wraith_blade = card("Wraith Blade", "UNDEAD", 30, -20, 3, "Glass cannon peak.", 18)
    ghoul = card("Ghoul", "UNDEAD", 15, -5, 2, "Harms enemies and self slightly.", 19)
    death_priest = card("Death Priest", "UNDEAD", 5, 15, 2, "Dark support.", 20)

    undead_cards = [witch, blood_pact, wraith_blade, ghoul, death_priest]

    race_card_length = 5

    return human_cards, elf_cards, dwarf_cards, undead_cards, race_card_length


def declare_variables():
    screen_drawn = False # condition check for drawing screen
    current_race = None

    # buttons
    card_1_button = None
    card_2_button = None
    card_3_button = None
    card_4_button = None
    card_5_button = None
    play_button = None
    instructions_button = None
    quit_button = None
    edit_deck_button = None
    player_select_button = None
    settings_button = None
    deck_left_button = None
    deck_right_button = None
    human_button = None
    elf_button = None
    dwarf_button = None
    undead_button = None
    current_race_card_button = None
    race_right_button = None
    race_left_button = None
    select_button = None
    replay = None
    pause_button = None
    background = None
    resume_button = None
    close_button = None
    card_slot1 = None
    card_slot2 = None
    card_slot3 = None
    top_card_ui = None
    card_slot4 = None
    card_slot5 = None
    card_slot6 = None
    end_round = None
    attack = None
    heal = None
    cost = None
    description_txt = None
    instruction_box = None
    timer = None
    player_select_image = None
    deck_player_select_image = None
    deck_player_select = None
    deck_player_select_button = None
    resume_image = None
    close_image = None

    return resume_image, close_image, deck_player_select, deck_player_select_button, player_select_image, deck_player_select_image, timer, instruction_box, attack, heal, cost, description_txt, card_1_button, card_2_button, card_3_button, card_4_button, card_5_button, screen_drawn, current_race, play_button, instructions_button, quit_button, edit_deck_button, player_select_button, settings_button, deck_left_button, deck_right_button, top_card_ui, human_button, elf_button, dwarf_button, undead_button, current_race_card_button, race_right_button, race_left_button, select_button, replay, pause_button, background, resume_button, close_button, card_slot1, card_slot2, card_slot3, card_slot4, card_slot5, card_slot6, end_round


def set_default_cards(human_cards, elf_cards, dwarf_cards, undead_cards):
    for c in human_cards:
        player_1.addtodeck(c.clone())
        player_2.addtodeck(c.clone())

    for c in elf_cards:
        player_1.addtodeck(c.clone())
        player_2.addtodeck(c.clone())

    for c in dwarf_cards:
        player_1.addtodeck(c.clone())
        player_2.addtodeck(c.clone())

    for c in undead_cards:
        player_1.addtodeck(c.clone())
        player_2.addtodeck(c.clone())


def declare_images():
    # draw startup background
    startup_background_image = pygame.image.load("ASSETS/BACKGROUNDS/startup_background.png").convert()
    # scale to window size
    startup_background_image = pygame.transform.scale(startup_background_image, (width, height))

    # draw startup background
    player_1_background_image = pygame.image.load("ASSETS/BACKGROUNDS/player_1_background.png").convert()
    # scale to window size
    player_1_background_image = pygame.transform.scale(player_1_background_image, (width, height))

    # draw startup background
    player_2_background_image = pygame.image.load("ASSETS/BACKGROUNDS/player_2_background.png").convert()
    # scale to window size
    player_2_background_image = pygame.transform.scale(player_2_background_image, (width, height))
    
    return startup_background_image, player_1_background_image, player_2_background_image

#---------------------------------------------------------------------------------------


#-----------------------------------STARTUP FUNCTIONS-----------------------------------

def change_profile_image(player_select, player_select_image, deck_player_select, deck_player_select_image):

    if player_select_image:

        if player_select_image in active_ui_elements:
            player_select_image.kill()
            active_ui_elements.remove(player_select_image)

    if deck_player_select_image:

        if deck_player_select_image in active_ui_elements:
            deck_player_select_image.kill()
            active_ui_elements.remove(deck_player_select_image)

    if current_profile == "P1":
        if game_state == "startup":
            # startup profile change
            player_select_image = player_select.create_image("BUTTONS/STARTUP/PROFILE 1 image.png")
            active_ui_elements.append(player_select_image) 

        else:
            # startup profile change
            player_select_image = player_select.create_image("BUTTONS/STARTUP/PROFILE 1 image.png")
            active_ui_elements.append(player_select_image) 

            deck_player_select_image = deck_player_select.create_image("BUTTONS/DECK/PROFILE 1 DECK image.png")
            active_ui_elements.append(deck_player_select_image) 

    else:
        if game_state == "startup":
            # startup profile change
            player_select_image = player_select.create_image("BUTTONS/STARTUP/PROFILE 2 image.png")
            active_ui_elements.append(player_select_image)

        else:
            # startup profile change
            player_select_image = player_select.create_image("BUTTONS/STARTUP/PROFILE 2 image.png")
            active_ui_elements.append(player_select_image)

            deck_player_select_image = deck_player_select.create_image("BUTTONS/DECK/PROFILE 2 DECK image.png")
            active_ui_elements.append(deck_player_select_image)

    return player_select_image, deck_player_select_image

#---------------------------------------------------------------------------------------


#-----------------------------------PLAYING FUNCTIONS-----------------------------------

def update_playing_info(op_health, p_health, p_energy, op_energy, round_info, p_label, op_label):
    current_player, opponent = check_current_player()

    draw_playing_background()

    op_health.setname(f"Opponent Health: {opponent.gethealth()}")
    p_health.setname(f"Player Health: {current_player.gethealth()}")
    p_energy.setname(f"{current_player.getenergy()} Energy")
    op_energy.setname(f"{opponent.getenergy()} Energy")

    if new_game.getturn_counter() <= 10:
        round_info.setname(f"Round {new_game.getturn_counter()}")

    p_label.setname(current_player.getname())
    op_label.setname(opponent.getname())


def update_hand_cards(card_1, card_2, card_3, card_4, card_5, card_1_button, card_2_button, card_3_button, card_4_button, card_5_button):
    current_player, _ = check_current_player()

    hand = current_player.gethand()

    for i in range(5):
        if i < len(hand):
            print(i, hand[i], type(hand[i]))

    cards = [card_1, card_2, card_3, card_4, card_5]
    buttons = [card_1_button, card_2_button, card_3_button, card_4_button, card_5_button]

    for i in range(5):
        if i < len(hand) and hand[i]:
            cards[i].setcard(hand[i])
            if len(hand) > i and hand[i]:
                image = cards[i].create_image(
                    f"CARDS/{cards[i].getcard().gettype()}/{cards[i].getcard().getname()}.png"
                )
                # attach a tag directly to the image object
                setattr(image, "_tag", f"cardimage_{i}_{hand[i].getname()}")
                active_ui_elements.append(image)
        else:
            buttons[i].set_text(" ")
            cards[i].setcard(" ")
            buttons[i].disable()


def move_card(current_player, card, index):
    x = card.getx()
    original_y = int(3 * height / 4) + 100
    new_y = int(height / 2) - 150

    if len(current_player.gethand()) > index:
        if current_player.gethand()[index] in selected_cards:
            card.move_to(x, original_y)

            # removes selected card to clicked_cards list
            select_card(current_player.gethand()[index])

        else:
            card.move_to(x, new_y)

            # adds selected card to clicked_cards list
            select_card(current_player.gethand()[index])    

        draw_playing_background()


def move_card_back(card):
    x = card.getx()
    original_y = int(3 * height / 4) + 100
    card.move_to(x, original_y)


def get_hand_card_vals(hand_card):
    attack = hand_card.getdmg()
    heal = hand_card.getheal()
    cost = hand_card.getcost()
    description_txt = hand_card.getdescription()
    
    return attack, heal, cost, description_txt 


def clear_card_images():
    global active_ui_elements
    to_remove = [e for e in active_ui_elements if getattr(e, "_tag", "").startswith("cardimage_")]

    for e in to_remove:
        if hasattr(e, "kill"):
            e.kill()  # remove from UI and screen
        elif hasattr(e, "disable"):
            e.disable()  # stop interaction

    # drop from registry
    active_ui_elements = [e for e in active_ui_elements if e not in to_remove]


def draw_playing_background():
    _, player_1_background_image, player_2_background_image = declare_images()

    if new_game.getcurrent_player_index() == 1:
        screen.blit(player_1_background_image, (0, 0))
    else:
        screen.blit(player_2_background_image, (0, 0))

#---------------------------------------------------------------------------------------


#------------------------------------DECK FUNCTIONS-------------------------------------

def update_current_race_card(current_race, current_race_card, current_race_card_button, index):
    current_race_card.setcard(current_race[index])
    current_race_card_image = current_race_card.create_image(f"CARDS/{current_race[index].gettype()}/{current_race[index].getname()}.png")
    active_ui_elements.append(current_race_card_image)
    current_race_card_button.set_text(current_race[index].getname())
    
    return current_race_card, current_race_card_button


def update_deck_size(current_deck):
    deck_size = 0

    for i in range(len(current_deck)):
        if current_deck[i] != None:
            deck_size += 1

    return deck_size


def update_current_deck():
    if current_profile == "P1":
        current_deck = player_1.getdeck()
    else:
        current_deck = player_2.getdeck()

    while len(current_deck) != 20:
        current_deck.append(None)

    return current_deck


def update_deck_ui(current_deck, front_pointer, back_pointer, deck_card_boxes):
    deck_len = len(current_deck)

    indices = [
        (back_pointer - 2) % deck_len,
        (back_pointer - 1) % deck_len,
        back_pointer % deck_len,
        front_pointer % deck_len,
        (front_pointer + 1) % deck_len,
        (front_pointer + 2) % deck_len,
        (front_pointer + 3) % deck_len,
    ]

    # draws left 3 cards
    indices = [
        (back_pointer - 2) % deck_len,
        (back_pointer - 1) % deck_len,
        back_pointer % deck_len,
    ]
    
    clear_card_images()

    for i, idx in enumerate(indices):
        card = current_deck[idx]
        if card is not None:
            element = deck_card_boxes[i].create_image(
                f"CARDS/{card.gettype()}/{card.getname()}.png"
            )
            setattr(element, "_tag", f"cardimage_{i}_{card.getname()}")
            active_ui_elements.append(element)
        else:
            deck_card_boxes[i].setname(" ")


    for offset in range(3, -1, -1):
        idx = (front_pointer + offset) % deck_len
        card = current_deck[idx]

        if card is not None:
            element = deck_card_boxes[3 + offset].create_image(
                f"CARDS/{card.gettype()}/{card.getname()}.png"
            )
            setattr(element, "_tag", f"cardimage_{3 + offset}_{card.getname()}")
            active_ui_elements.append(element)
            element.focus()


def return_cards_to_deck():
    player_1.replenish_deck()
    player_2.replenish_deck()


def get_race_card_vals(current_race_card):
    attack = current_race_card.getcard().getdmg()
    heal = current_race_card.getcard().getheal()
    cost = current_race_card.getcard().getcost()
    description_txt = current_race_card.getcard().getdescription()
    
    return attack, heal, cost, description_txt 


def update_description_text(attack, heal, cost, description_txt, description):

    txt =(
    f"ATTACK DAMAGE: {attack} <br>"
    f"HEALING: {heal} <br>"
    f"COST: {cost} <br>"
    f"DESCRIPTION: <br>"
    f"{description_txt} <br>"
    )

    description_text_label = description.add_text_block(txt)

    active_ui_elements.append(description_text_label)

    return description_text_label

#---------------------------------------------------------------------------------------


#---------------------------------INSTRUCTION FUNCTIONS---------------------------------

def create_instruction_text(instruction_box):

    txt = (
    f"HOW TO PLAY: <br>"
    f"1. Create a deck using the deck builder. <br>"
    f"2. Swap profile by pressing the 'P1' button to create player 2's deck. <br>"
    f"3. Play against a friend. <br>"
    f"4. Aim of the game is to get your opponent's health down to 0. <br>"

    f"CARDS: <br>"
    f"Each card is part of a race. Cards in a race may contain synergies or tactical combos that can be used to have an edge over the opponent. <br>"
    f"Each card contains a cost to play, damage and heal. <br>"
    )


    instruction_text_label = instruction_box.add_text_block(txt)

    active_ui_elements.append(instruction_text_label)

#---------------------------------------------------------------------------------------

# setup
fps = 60
clock = pygame.time.Clock()

info = pygame.display.Info()
width, height = info.current_w, info.current_h

screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Twine")

manager = pygame_gui.UIManager((width, height))


# game variables
player_1 = player("PLAYER 1", 100, 10, False)
player_2 = player("PLAYER 2", 100, 10, False)
game_state = "startup"
clicked_card = None
selected_cards = []
new_game = None
active_ui_elements = []
current_profile = "P1"
deck_card_boxes = None
time_left = 60  # in seconds
elapsed_time = 0  
timer_paused = False
soundtrack_playing = False

# main loop
def main():
    run = True

    human_cards, elf_cards, dwarf_cards, undead_cards, race_card_length = declare_cards()
    resume_image, close_image, deck_player_select, deck_player_select_button, player_select_image, deck_player_select_image, timer, instruction_box, attack, heal, cost, description_txt, card_1_button, card_2_button, card_3_button, card_4_button, card_5_button, screen_drawn, current_race, play_button, instructions_button, quit_button, edit_deck_button, player_select_button, settings_button, deck_left_button, deck_right_button, top_card_ui, human_button, elf_button, dwarf_button, undead_button, current_race_card_button, race_right_button, race_left_button, select_button, replay, pause_button, background, resume_button, close_button, card_slot1, card_slot2, card_slot3, card_slot4, card_slot5, card_slot6, end_round = declare_variables()
    startup_background_image, player_1_background_image, player_2_background_image = declare_images()

    global new_game
    global current_profile
    global deck_card_boxes
    global clicked_card
    global time_left
    global elapsed_time
    global timer_paused
    global active_ui_elements
    global soundtrack_playing
    global game_state
    set_default_cards(human_cards, elf_cards, dwarf_cards, undead_cards) # to remove hassle of adding all 40 cards from the get go

    while run:
        time_delta = clock.tick(fps) / 1000.0

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            manager.process_events(event)


            # input handling
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                
                # MAIN MENU BUTTON HANDLING
                if event.ui_element == player_select_button:
                    print("Profile swapped")

                    if current_profile == "P1":
                        current_profile = "P2"
                        player_select_image = change_profile_image(player_select, player_select_image, deck_player_select, deck_player_select_image)
                    else:
                        current_profile = "P1"
                        player_select_image = change_profile_image(player_select, player_select_image, deck_player_select, deck_player_select_image)

                    player_select_button.set_text(current_profile)

                elif event.ui_element == play_button:
                    print("Game started")

                    # clears current UI elements
                    for element in active_ui_elements:
                        element.kill()
                    
                    active_ui_elements.clear()

                    # does action
                    game_state = "playing"
                    screen_drawn = False

                elif event.ui_element == instructions_button:
                    print("Instructions menu opened.")

                    # disables background UI
                    for element in active_ui_elements:
                        element.disable()

                    game_state = "instructions"
                    screen_drawn = False

                elif event.ui_element == quit_button:
                    print("Game Closed.")
                    screen_drawn = False
                    run = False

                elif event.ui_element == edit_deck_button:
                    print("Entered deck builder")
                    current_race = None

                    # disables background UI
                    for element in active_ui_elements:
                        element.disable()

                    game_state = "deck"
                    screen_drawn = False


                # PLAYING BUTTON HANDLING
                elif event.ui_element == end_round:

                    # disables ui for transaction to take place
                    for element in active_ui_elements:
                        element.disable()

                    # move cards back to original position
                    move_card_back(card_1)
                    move_card_back(card_2)
                    move_card_back(card_3)
                    move_card_back(card_4)
                    move_card_back(card_5)

                    # applies card effects
                    if take_turn():

                        # clears card images from active ui elements
                        clear_card_images()
                        # redraw background
                        draw_playing_background()

                        # switches turn
                        new_game.next_turn()  
                        switch_turn()

                        # checks if game is over
                        if check_game_over():
                            game_state = "game_ended"

                            # hides player label bc its a quick fix 
                            description_text_label.kill()
                            p_label.setname(" ")
                            op_energy.setname(" ")

                            screen_drawn = False

                        else:
                            # enables ui
                            for element in active_ui_elements:
                                element.enable()

                            # resets timer
                            timer.setname("1:00")
                            time_left = 60
                            elapsed_time = 0

                            # updates ui elements
                            update_playing_info(op_health, p_health, p_energy, op_energy, round_info, p_label, op_label)
                            update_hand_cards(card_1, card_2, card_3, card_4, card_5, card_1_button, card_2_button, card_3_button, card_4_button, card_5_button)
                    
                    else:
                            # enables ui
                            for element in active_ui_elements:
                                element.enable()


                elif event.ui_element == card_1_button:
                    current_player, _ = check_current_player()

                    # updates description
                    if card_1.getcard() != " ":
                        attack, heal, cost, description_txt = get_hand_card_vals(card_1.getcard())
                        description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                        # moves card to/from playing area

                        move_card(current_player, card_1, 0)


                elif event.ui_element == card_2_button:
                    current_player, _ = check_current_player()

                    # updates description
                    if card_2.getcard() != " ":
                        attack, heal, cost, description_txt = get_hand_card_vals(card_2.getcard())
                        description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                        # moves card to/from playing area
                        move_card(current_player, card_2, 1)


                elif event.ui_element == card_3_button:
                    current_player, _ = check_current_player()

                    # updates description
                    if card_3.getcard() != " ":
                        attack, heal, cost, description_txt = get_hand_card_vals(card_3.getcard())
                        description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                        # moves card to/from playing area
                        move_card(current_player, card_3, 2)


                elif event.ui_element == card_4_button:
                    current_player, _ = check_current_player()

                    # updates description
                    if card_4.getcard() != " ":
                        attack, heal, cost, description_txt = get_hand_card_vals(card_4.getcard())
                        description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                        # moves card to/from playing area
                        move_card(current_player, card_4, 3)


                elif event.ui_element == card_5_button:
                    current_player, _ = check_current_player() 

                    # updates description
                    if card_5.getcard() != " ":
                        attack, heal, cost, description_txt = get_hand_card_vals(card_5.getcard())
                        description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                        # moves card to/from playing area
                        move_card(current_player, card_5, 4)


                # DECK BUILDER BUTTON HANDLING
                elif event.ui_element == deck_player_select_button:
                    print("Profile swapped")

                    if current_profile == "P1":
                        current_profile = "P2"
                        player_select_image = change_profile_image(player_select, player_select_image, deck_player_select, deck_player_select_image)
                    else:
                        current_profile = "P1"
                        player_select_image = change_profile_image(player_select, player_select_image, deck_player_select, deck_player_select_image)

                    player_select_button.set_text(current_profile)
                    current_deck = update_current_deck()

                    if deck_card_boxes:
                        update_deck_ui(current_deck, front_pointer, back_pointer, deck_card_boxes)
                        deck_size = update_deck_size(current_deck)
                        deck_size_panel.setname(f"{deck_size}/20 ")

                elif event.ui_element == human_button:
                    current_race = human_cards
                    race_index = 0
                    current_race_card, current_race_card_button = update_current_race_card(current_race, current_race_card, current_race_card_button, race_index)

                    # updates description
                    attack, heal, cost, description_txt = get_race_card_vals(current_race_card)
                    description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                elif event.ui_element == elf_button:
                    current_race = elf_cards
                    race_index = 0
                    current_race_card, current_race_card_button = update_current_race_card(current_race, current_race_card, current_race_card_button, race_index)

                    # updates description
                    attack, heal, cost, description_txt = get_race_card_vals(current_race_card)
                    description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                elif event.ui_element == dwarf_button:
                    current_race = dwarf_cards
                    race_index = 0
                    current_race_card, current_race_card_button = update_current_race_card(current_race, current_race_card, current_race_card_button, race_index)

                    # updates description
                    attack, heal, cost, description_txt = get_race_card_vals(current_race_card)
                    description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                elif event.ui_element == undead_button:
                    current_race = undead_cards
                    race_index = 0
                    current_race_card, current_race_card_button = update_current_race_card(current_race, current_race_card, current_race_card_button, race_index)

                    # updates description
                    attack, heal, cost, description_txt = get_race_card_vals(current_race_card)
                    description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                elif event.ui_element == race_left_button:
                    if race_index == 0:
                        race_index = race_card_length - 1 # goes from 0 to length - 1 
                    else:
                        race_index -= 1

                    if current_race:
                        current_race_card, current_race_card_button = update_current_race_card(current_race, current_race_card, current_race_card_button, race_index)

                        # updates description
                        attack, heal, cost, description_txt = get_race_card_vals(current_race_card)
                        description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                elif event.ui_element == race_right_button:
                    if race_index == race_card_length - 1: # goes from 0 to length - 1 
                        race_index = 0
                    else:
                        race_index += 1

                    if current_race: 
                        current_race_card, current_race_card_button = update_current_race_card(current_race, current_race_card, current_race_card_button, race_index)
                        # updates description
                        attack, heal, cost, description_txt = get_race_card_vals(current_race_card)
                        description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                elif event.ui_element == select_button:
                    # logic for adding a card into top card slot
                    if not current_deck:
                        current_deck.insert(front_pointer, current_race_card)
                    elif current_deck[front_pointer] != current_race_card:
                        current_deck[front_pointer] = current_race_card.getcard().clone()

                    update_deck_ui(current_deck, front_pointer, back_pointer, deck_card_boxes)

                    deck_size = update_deck_size(current_deck)
                    deck_size_panel.setname(f"{deck_size}/20 ")

                    print(f"Card Added to {current_profile} Deck: {current_race_card.getname()}")

                elif event.ui_element == deck_left_button:
                    deck_len = len(current_deck)
                    front_pointer = (front_pointer - 1) % deck_len
                    back_pointer = (back_pointer - 1) % deck_len
                    update_deck_ui(current_deck, front_pointer, back_pointer, deck_card_boxes)

                elif event.ui_element == deck_right_button:
                    deck_len = len(current_deck)
                    front_pointer = (front_pointer + 1) % deck_len
                    back_pointer = (back_pointer + 1) % deck_len
                    update_deck_ui(current_deck, front_pointer, back_pointer, deck_card_boxes)

                # PAUSE MENU BUTTON HANDLING
                elif event.ui_element == pause_button:

                    # disables background UI
                    for element in active_ui_elements:
                        element.disable()

                    # hides player label bc its a quick fix 
                    p_label.setname(" ")
                    op_energy.setname(" ")
                    description_text_label.kill()

                    print("Settings Opened")

                    game_state = "pause_menu"
                    screen_drawn = False


                elif event.ui_element == resume_button:
                    
                    background.kill()
                    resume_button.kill()
                    resume_image.kill()
                    close_button.kill()
                    close_image.kill()

                    draw_playing_background()

                    update_playing_info(op_health, p_health, p_energy, op_energy, round_info, p_label, op_label)

                    # enables background ui
                    for element in active_ui_elements:
                        element.enable()

                    game_state = "playing"
                    timer_paused = False

                elif event.ui_element == replay:
                    # disables background UI
                    for element in active_ui_elements:
                        element.enable()

                    # clears current UI elements
                    for element in active_ui_elements:
                        element.kill()
                    active_ui_elements.clear()

                    # does action
                    # resets timer
                    if timer:
                        timer.setname("1:00")
                        time_left = 60
                        elapsed_time = 0

                    return_cards_to_deck()
                    deck_card_boxes = None

                    print("Game started")

                    # clears current UI elements
                    for element in active_ui_elements:
                        element.kill()
                    
                    active_ui_elements.clear()

                    # does action
                    game_state = "playing"
                    screen_drawn = False

                # UNIVERSAL BUTTON HANDLING (shows up in multiple screens)
                elif event.ui_element == close_button:
                    print("Back to menu clicked")

                    # disables background UI
                    for element in active_ui_elements:
                        element.enable()

                    # clears current UI elements
                    for element in active_ui_elements:
                        element.kill()
                    active_ui_elements.clear()

                    # does action
                    # resets timer
                    if timer:
                        timer.setname("1:00")
                        time_left = 60
                        elapsed_time = 0

                    return_cards_to_deck()
                    deck_card_boxes = None
                    game_state = "startup"

                    screen_drawn = False


        # game logic
        if game_state == "startup":
            if not screen_drawn:
                
                # load background image
                screen.blit(startup_background_image, (0, 0)) 

                player_select, play_button, instructions_button, quit_button, edit_deck_button, player_select_button, settings_button = draw_startup()

                player_select_image, deck_player_select_image = change_profile_image(player_select, player_select_image, deck_player_select, deck_player_select_image)

                if not soundtrack_playing: 
                    pygame.mixer.music.load("ASSETS/SOUNDTRACKS/startup_soundtrack.mp3")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.3)
                    soundtrack_playing = True

                screen_drawn = True
        

        elif game_state == "deck":
            if not screen_drawn:

                # draws background
                screen.blit(startup_background_image, (0, 0))

                deck_player_select, deck_player_select_button, deck_size_panel, deck_left_button, deck_right_button, card_slot1, card_slot2, card_slot3, card_slot4, card_slot5, card_slot6, top_card, human_button, elf_button, dwarf_button, undead_button, description, current_race_card, current_race_card_button, race_right_button, race_left_button, deck_player_select_button, select_button, close_button = draw_deck()

                player_select_image, deck_player_select_image = change_profile_image(player_select, player_select_image, deck_player_select, deck_player_select_image)

                # updates the current race when first opening the deck builder
                current_race = human_cards
                race_index = 0
                current_race_card, current_race_card_button = update_current_race_card(current_race, current_race_card, current_race_card_button, race_index)

                attack, heal, cost, description_txt = get_race_card_vals(current_race_card)
                description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                # sets order of cards in deck
                deck_card_boxes = [card_slot1, card_slot2, card_slot3, top_card, card_slot4, card_slot5, card_slot6]
                front_pointer = 0
                back_pointer = 19
                current_deck = update_current_deck()

                update_deck_ui(current_deck, front_pointer, back_pointer, deck_card_boxes)

                # updates the current deck size counter
                deck_size = update_deck_size(current_deck)
                deck_size_panel.setname(f"{deck_size}/20 ")

                screen_drawn = True


        elif game_state == "instructions":
            if not screen_drawn:
                close_button, instruction_box = draw_instructions()
                create_instruction_text(instruction_box)
                screen_drawn = True


        elif game_state == "playing":
            if not screen_drawn:
                new_game = start_game()

                # draw background
                draw_playing_background()

                pause_button, end_round, card_1, card_2, card_3, card_4, card_5, card_1_button, card_2_button, card_3_button, card_4_button, card_5_button, description,  op_health, p_health, p_energy, op_energy, round_info, p_label, op_label, timer = draw_playing()

                # updates
                update_hand_cards(card_1, card_2, card_3, card_4, card_5, card_1_button, card_2_button, card_3_button, card_4_button, card_5_button)
                update_playing_info(op_health, p_health, p_energy, op_energy, round_info, p_label, op_label)

                # updates description
                attack, heal, cost, description_txt = get_hand_card_vals(card_1.getcard())
                description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                timer_paused = False
                screen_drawn = True

            if not timer_paused:
                elapsed_time += time_delta  # add seconds

                # reduces time_left when a full second has passed
                while elapsed_time >= 1:
                    time_left -= 1
                    elapsed_time -= 1  # keep leftover fraction

                    # updates timer display
                    minutes, seconds = divmod(time_left, 60)
                    timer.setname(f"{minutes}:{seconds:02d}")

                    # when timer reaches 0, switches turn and resets
                    if time_left <= 0:

                        # disables ui for transaction to take place
                        for element in active_ui_elements:
                            element.disable()

                        # move cards back to original position
                        move_card_back(card_1)
                        move_card_back(card_2)
                        move_card_back(card_3)
                        move_card_back(card_4)
                        move_card_back(card_5)

                        # applies card effects and switches turn
                        if take_turn():

                            # switches turn
                            new_game.next_turn()  
                            switch_turn()

                            # checks if game is over
                            if check_game_over():
                                game_state = "game_ended"

                                # hides player label bc its a quick fix 
                                description_text_label.kill()
                                p_label.setname(" ")
                                op_energy.setname(" ")

                                screen_drawn = False

                            else:
                                # enables ui
                                for element in active_ui_elements:
                                    element.enable()

                                # resets timer
                                timer.setname("1:00")
                                time_left = 60
                                elapsed_time = 0

                                # updates ui elements
                                update_playing_info(op_health, p_health, p_energy, op_energy, round_info, p_label, op_label)

                                # clear card ui images 
                                clear_card_images()

                                update_hand_cards(card_1, card_2, card_3, card_4, card_5, card_1_button, card_2_button, card_3_button, card_4_button, card_5_button)

                        else:
                            # enables ui
                            for element in active_ui_elements:
                                element.enable()


        elif game_state == "game_ended":

            if not screen_drawn:

                # draw background
                draw_playing_background()

                close_button, replay = draw_game_ended()
                screen_drawn = True


        elif game_state == "pause_menu":

            if not screen_drawn:
                resume_image, close_image, background, resume_button, close_button = draw_pause_menu()

                timer_paused = True
                screen_drawn = True


        else:
            print("Game state error.")


        # draw ui
        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.flip()

    pygame.quit()

main()