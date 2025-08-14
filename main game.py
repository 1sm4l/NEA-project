# library imports
import pygame
import pygame_gui
import random
import textwrap

pygame.init() # initialises pygame


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
        if self.hand: # if hand is not empty
            for card in selected_cards:
                if card in self.hand:
                    self.hand.remove(card) # remove card from hand
                    self.discard_pile.append(card) # appends to discard_pile
                else:
                    print("Card not found in hand.")
            selected_cards.clear() # clear selected cards for next player
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

# panel blueprint
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

    def setname(self, gname):
        self.name = str(gname)
        if self.label:
            self.label.set_text(self.name)

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
            relative_rect = pygame.Rect((centered_x, centered_y), (self.width, self.height)),
            text=self.name,
            manager = self.manager
        )
        return self.ui_button


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
        self.ui_button.set_relative_position((new_x - (self.width / 2), new_y - (self.height / 2)))

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
    selected_cards.clear()
    current_player, opponent = check_current_player()
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
    current_player, _ = check_current_player()

    result = apply_card_effect()

    if result is None:
        print("Turn not ended. Not enough energy.")
        return  # player must modify selection and try again
    else:
        total_damage, total_heal, total_energy_cost = result # take total_damage, total_heal, total_energy_cost as parameters to change ui
        print(f"Used {total_energy_cost} energy, dealt {total_damage} damage, healed {total_heal} HP.")

        current_player.draw_card()
        new_game.next_turn()  
        switch_turn()



# checks if a player hits 0 health, then sets the other player as the winner and sets game as over
def check_game_over():
    current_player, opponent = check_current_player()

    if current_player.gethealth() == 0 and opponent.gethealth() == 0: # if both players die
        new_game.setwinner("DRAW.")
        new_game.setgame_over()
        return True
    
    elif new_game.getturn_counter() > 15: # if turn counter > max rounds (if no one dies)

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
        
    elif opponent.gethealth() == 0: # if opponent dies
        new_game.setwinner(f"{current_player.getname()} WINS.")
        new_game.setgame_over()
        return True
    
    elif current_player.gethealth() == 0: # if current player kills themself
        new_game.setwinner(f"{opponent.getname()} WINS.")
        new_game.setgame_over()
        return True
    
    else:
         return False

#---------------------------------------------------------------------------------------


#----------------------------------------UI SECTION-------------------------------------
def draw_startup():
    screen.fill([150, 0, 0])  # background colour

    # TITLE TEXT
    pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((width // 2 - 300, height // 2 - 200), (600, 100)),
        text="Twine",
        manager=manager
    )

    # GREY BACKGROUND BOXES
    # middle box
    middle_box =panel(" ", width // 2, int(3 * height / 4), 880, 140, manager).create_panel()

    # left box
    left_box = panel(" ", (width // 4) - 200, int(3 * height / 4), 140, 140, manager).create_panel()

    # right box
    right_box = panel(" ", width - (width // 4) + 200, int(3 * height / 4), 140, 140, manager).create_panel()

    # BUTTONS
    play_button = button("PLAY", width // 2 - 320, int(3 * height / 4), 200, 100, manager).create_box()
    instructions_button = button("INSTRUCTIONS", width // 2 - 105, int(3 * height / 4) + 10, 180, 80, manager).create_box()
    exit_button = button("EXIT", width // 2 + 105, int(3 * height / 4) + 10, 180, 80, manager).create_box()
    edit_deck = button("EDIT DECK", width // 2 + 320, int(3 * height / 4), 200, 100, manager).create_box()
    player_select_button = button(current_profile, (width // 4) - 200, int(3 * height / 4), 100, 100, manager).create_box()
    settings_button = button("SETTINGS", width - (width // 4) + 200, int(3 * height / 4), 100, 100, manager).create_box()

    # add to active elements
    active_ui_elements.extend([
        # panels
        middle_box,
        left_box,
        right_box,

        # buttons
        play_button,
        instructions_button,
        exit_button,
        edit_deck,
        player_select_button,
        settings_button
    ])

    return play_button, instructions_button, exit_button, edit_deck, player_select_button, settings_button


def draw_deck():
    screen.fill([150, 0, 0])  # background colour

    # background panel
    background = panel(" ", width // 2, int(height / 2), 1000, 800, manager).create_panel()

    # change top card
    deck_left = button("<  ", width // 2 - 450, int(height / 2) + 120, 50, 50, manager).create_box()
    deck_right = button(">", width // 2 + 450, int(height / 2) + 120, 50, 50, manager).create_box()

    # cards 
    # fourth row
    card_temp1 = button(" ", width // 2 - 350, int(height / 2) + 120, 125, 225, manager).create_box()
    card_temp2 = button(" ", width // 2 + 350, int(height / 2) + 120, 125, 225, manager).create_box()

    # third row
    card_temp3 = button(" ", width // 2 - 250, int(height / 2) + 120, 150, 250, manager).create_box()
    card_temp4 = button(" ", width // 2 + 250, int(height / 2) + 120, 150, 250, manager).create_box()

    # second row
    card_temp5 = button(" ", width // 2 - 150, int(height / 2) + 120, 175, 275, manager).create_box()
    card_temp6 = button(" ", width // 2 + 150, int(height / 2) + 120, 175, 275, manager).create_box()

    # top
    top_card = card_button(" ", width // 2, int(height / 2) + 120, 200, 300, manager, "")
    top_card_ui = top_card.create_box()

    # race
    race_temp1 = panel("Races", width // 2 - 325, int(height / 2) - 350, 275, 60, manager).create_panel()
    race_temp2 = panel(" ", width // 2 - 325, int(height / 2) - 175, 275, 275, manager).create_panel()

    human = button("human", width // 2 - 385, int(height / 2) - 235, 110, 110, manager).create_box()
    elf = button("elf", width // 2 - 265, int(height / 2) - 235, 110, 110, manager).create_box()
    dwarf = button("dwarf", width // 2 - 385, int(height / 2) - 115, 110, 110, manager).create_box()
    undead = button("undead", width // 2 - 265, int(height / 2) - 115, 110, 110, manager).create_box()

    # description
    description_temp = panel("Card Description", width // 2, int(height / 2) - 350, 350, 60, manager).create_panel()
    description = panel(" ", width // 2, int(height / 2) - 175, 350, 250, manager)
    description_panel = description.create_panel()


    # card select
    card_select_temp1 = panel("Choose Card", width // 2 + 325, int(height / 2) - 350, 275, 60, manager).create_panel()
    card_select_temp2 = panel(" ", width // 2 + 325, int(height / 2) - 175, 275, 275, manager).create_panel()

    current_race_card = card_button(" ", width // 2 + 325, int(height / 2) - 208, 125, 175, manager, " ")
    current_race_card_button = current_race_card.create_box()

    race_right = button(">", width // 2 + 423, int(height / 2) - 208, 50, 50, manager).create_box()
    race_left = button("<  ", width // 2 + 227, int(height / 2) - 208, 50, 50, manager).create_box()

    player_select_button = button(current_profile, width // 2 - 450, int(height / 2), 60, 40, manager).create_box()

    deck_size_panel = panel(" ", width // 2 + 450, int(height / 2), 60, 40, manager)
    deck_size_count = deck_size_panel.create_panel()

    select = button("Select", width // 2 + 325, int(height / 2) - 80, 250, 60, manager).create_box()

    # close button   
    close_button = button("Back To Menu", width // 2, int(height / 2) + 330, 900, 80, manager).create_box()

    # add to active elements
    active_ui_elements.extend([
        # labels
        background,
        
        card_temp1,
        card_temp2,
        card_temp3,
        card_temp4,
        card_temp5,
        card_temp6,

        race_temp1,
        race_temp2,

        description_temp,
        description_panel,

        card_select_temp1,
        card_select_temp2,

        # buttons
        deck_size_count,
        deck_left,
        deck_right, 
        top_card_ui,
        human, 
        elf, 
        dwarf, 
        undead,  
        current_race_card_button, 
        race_right, 
        race_left, 
        player_select_button,
        select, 
        close_button
    ])

    return  deck_size_panel, deck_left, deck_right, card_temp1, card_temp2, card_temp3, card_temp4, card_temp5, card_temp6, top_card_ui, human, elf, dwarf, undead, description, current_race_card, current_race_card_button, race_right, race_left, player_select_button, select, close_button
    

def draw_instructions():
    screen.fill([150, 0, 0])  # background colour

    # background panel
    background = panel(" ", width // 2, int(height / 2), 1000, 800, manager).create_panel()

    # text box
    instruction_box = panel(" ", width // 2, int(height / 2) - 50, 900, 600, manager)
    text_temp = instruction_box.create_panel()

    # close button   
    close_button = button("Back To Menu", width // 2, int(height / 2) + 330, 900, 80, manager).create_box()

    # add to active element
    active_ui_elements.extend([
        # labels
        background,
        text_temp,

        # buttons
        close_button
    ])
    
    return close_button, instruction_box


def draw_playing():
    screen.fill([150, 0, 0])  # background colour


    # GREY BACKGROUND BOXES
    # left box
    left = panel(" ", (width // 4) - 200, height / 2, 500, height, manager).create_panel()

    # settings button
    pause_button = button("Settings", (width // 4) - 387, height / 2 - 470, 75, 75, manager).create_box()

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
    timer = panel("Timer", (width // 4) - 200, (height / 2) + 300, 450, 75, manager).create_panel()

    # end round
    end_round = button("End Round", (width // 4) - 200, height / 2 + 430, 450, 125, manager).create_box()


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
        timer,
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
    ])

    return pause_button, end_round, card_1, card_2, card_3, card_4, card_5, card_1_button, card_2_button, card_3_button, card_4_button, card_5_button, description, op_health, p_health, p_energy, op_energy, round_info, p_label, op_label


def draw_game_ended():
    screen.fill([150, 0, 0])  # background colour

    # background panel
    background = panel(" ", width // 2, int(height / 2), 1000, 800, manager).create_panel()

    # win/lose
    w_l = panel(new_game.getwinner(), width // 2, int(height / 2) - 150, 800, 240, manager).create_panel()

    # replay button
    replay = button("Replay", width // 2, int(height / 2) + 150, 800, 80, manager).create_box()

    # close button
    close_button = button("Back To Menu", width // 2, int(height / 2) + 250, 800, 80, manager).create_box()

    # add to active elements
    active_ui_elements.extend([
        # panels
        background,
        w_l,
        
        # buttons
        replay,
        close_button
    ])

    return close_button


def draw_pause_menu():
    screen.fill([150, 0, 0])  # background colour

    # background panel
    background = panel(" ", width // 2, int(height / 2), 1000, 800, manager).create_panel()

    # resume button
    resume = button("Resume Game", width // 2, int(height / 2) -50, 800, 80, manager).create_box()
    # close button
    close_button = button("Back To Menu", width // 2, int(height / 2) + 50, 800, 80, manager).create_box()

    # add to active elements
    active_ui_elements.extend([
        # panels
        background,

        # buttons
        resume,
        close_button
    ])

    return background, resume, close_button

#---------------------------------------------------------------------------------------


#-----------------------------------DECLARE FUNCTIONS-----------------------------------

def declare_cards():
    # Human cards
    greedy_medic = card("Greedy Medic", "Human", 0, 20, 2, "Heals big but drains your wallet.", 1)
    soldier = card("Soldier", "Human", 10, 0, 1, "Reliable and cheap.", 2)
    combat_medic = card("Combat Medic", "Human", 10, 10, 2, "Supportive all-rounder.", 3)
    sergeant = card("Sergeant", "Human", 20, 0, 2, "Clean strike.", 4)
    alchemist = card("Alchemist", "Human", 30, -15, 3, "Risky gamble for burst.", 5)

    human_cards = [greedy_medic, soldier, combat_medic, sergeant, alchemist]

    # Elf cards
    grand_elf = card("Grand Elf", "Elf", 5, 15, 2, "Graceful and precise.", 6)
    natures_touch = card("Nature's Touch", "Elf", 0, 25, 2, "Great stall tool.", 7)
    moonblade = card("Moonblade", "Elf", 10, 5, 1, "Nimble strike.", 8)
    arcane_warden = card("Arcane Warden", "Elf", 15, 10, 2, "Versatile role.", 9)
    lifeweaver = card("Lifeweaver", "Elf", 5, 30, 3, "Big sustain.", 10)

    elf_cards = [grand_elf, natures_touch, moonblade, arcane_warden, lifeweaver]

    # Dwarf cards
    urdunnir = card("Urdunnir", "Dwarf", 15, 0, 1, "Strong basic hit.", 11)
    war_smith = card("War Smith", "Dwarf", 25, 0, 2, "Smashes through defences.", 12)
    iron_veteran = card("Iron Veteran", "Dwarf", 20, 5, 2, "Battle-hardened support.", 13)
    brewmaster = card("Brewmaster", "Dwarf", 10, 15, 3, "Heavy hitter and healer.", 14)
    anvil_guard = card("Anvil Guard", "Dwarf", 30, 0, 4, "Titan strike.", 15)

    dwarf_cards = [urdunnir, war_smith, iron_veteran, brewmaster, anvil_guard]

    # Undead cards
    skeleton = card("Skeleton", "Undead", 10, 0, 1, "Cheap and effective.", 16)
    blood_pact = card("Blood Pact", "Undead", 20, -10, 2, "Burn yourself to burn others.", 17)
    wraith_blade = card("Wraith Blade", "Undead", 30, -20, 3, "Glass cannon peak.", 18)
    ghoul = card("Ghoul", "Undead", 15, -5, 2, "Harms enemies and self slightly.", 19)
    death_priest = card("Death Priest", "Undead", 5, 15, 2, "Dark support.", 20)

    undead_cards = [skeleton, blood_pact, wraith_blade, ghoul, death_priest]

    race_card_length = 5

    return human_cards, elf_cards, dwarf_cards, undead_cards, race_card_length


def declare_variables():
    game_state = "startup"
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
    exit_button = None
    edit_deck = None
    player_select_button = None
    settings_button = None
    deck_left = None
    deck_right = None
    human = None
    elf = None
    dwarf = None
    undead = None
    current_race_card_button = None
    race_right = None
    race_left = None
    select = None
    replay = None
    pause_button = None
    background = None
    resume = None
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

    return instruction_box, attack, heal, cost, description_txt, card_1_button, card_2_button, card_3_button, card_4_button, card_5_button, game_state, screen_drawn, current_race, play_button, instructions_button, exit_button, edit_deck, player_select_button, settings_button, deck_left, deck_right, top_card_ui, human, elf, dwarf, undead, current_race_card_button, race_right, race_left, select, replay, pause_button, background, resume, close_button, card_slot1, card_slot2, card_slot3, card_slot4, card_slot5, card_slot6, end_round


def set_default_cards(human_cards, elf_cards, dwarf_cards, undead_cards):
    for card in human_cards:
        player_1.addtodeck(card)
        player_2.addtodeck(card)

    for card in elf_cards:
        player_1.addtodeck(card)
        player_2.addtodeck(card)

    for card in dwarf_cards:
        player_1.addtodeck(card)
        player_2.addtodeck(card)

    for card in undead_cards:
        player_1.addtodeck(card)
        player_2.addtodeck(card)

#---------------------------------------------------------------------------------------


#-----------------------------------PLAYING FUNCTIONS-----------------------------------

def update_playing_info(op_health, p_health, p_energy, op_energy, round_info, p_label, op_label):
    current_player, opponent = check_current_player()

    op_health.setname(f"Opponent Health: {opponent.gethealth()}")
    p_health.setname(f"Player Health: {current_player.gethealth()}")
    p_energy.setname(f"{current_player.getenergy()} Energy")
    op_energy.setname(f"{opponent.getenergy()} Energy")

    if new_game.getturn_counter() <= 15:
        round_info.setname(f"Round {new_game.getturn_counter()}")

    p_label.setname(current_player.getname())
    op_label.setname(opponent.getname())


def update_hand_cards(card_1, card_2, card_3, card_4, card_5, card_1_button, card_2_button, card_3_button, card_4_button, card_5_button):
    current_player, _ = check_current_player()
    
    card_1.setcard(current_player.gethand()[0])
    card_2.setcard(current_player.gethand()[1])
    card_3.setcard(current_player.gethand()[2])
    card_4.setcard(current_player.gethand()[3]) 
    card_5.setcard(current_player.gethand()[4]) 

    card_1_button.set_text(current_player.gethand()[0].getname())
    card_2_button.set_text(current_player.gethand()[1].getname()) 
    card_3_button.set_text(current_player.gethand()[2].getname()) 
    card_4_button.set_text(current_player.gethand()[3].getname()) 
    card_5_button.set_text(current_player.gethand()[4].getname())  


def move_card(current_player, card, index):
    x = card.getx()
    original_y = int(3 * height / 4) + 100
    new_y = int(height / 2) - 150

    if current_player.gethand()[index] in selected_cards:
        card.move_to(x, original_y)

        # removes selected card to clicked_cards list
        select_card(current_player.gethand()[index])

    else:
        card.move_to(x, new_y)

        # adds selected card to clicked_cards list
        select_card(current_player.gethand()[index])    

    screen.fill([150, 0, 0])

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

#---------------------------------------------------------------------------------------


#------------------------------------DECK FUNCTIONS-------------------------------------

def update_current_race_card(current_race, current_race_card, current_race_card_button, index):
    current_race_card.setcard(current_race[index])
    current_race_card.setname(current_race[index].getname())
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

    for i, idx in enumerate(indices):
        card = current_deck[idx]
        if card is not None:
            deck_card_boxes[i].set_text(card.getname())
        else:
            deck_card_boxes[i].set_text(" ")


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
    f"Each card contains a cost to play, damage and heal (if it is a support card). <br>"
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
clicked_card = None
selected_cards = []
new_game = None
active_ui_elements = []
new_game = None
current_profile = "P1"
deck_card_boxes = None

# main loop
def main():
    run = True

    human_cards, elf_cards, dwarf_cards, undead_cards, race_card_length = declare_cards()
    instruction_box, attack, heal, cost, description_txt, card_1_button, card_2_button, card_3_button, card_4_button, card_5_button, game_state, screen_drawn, current_race, play_button, instructions_button, exit_button, edit_deck, player_select_button, settings_button, deck_left, deck_right, top_card_ui, human, elf, dwarf, undead, current_race_card_button, race_right, race_left, select, replay, pause_button, background, resume, close_button, card_slot1, card_slot2, card_slot3, card_slot4, card_slot5, card_slot6, end_round = declare_variables()
    
    global new_game # assigning new_game as a global variable for use in main game function
    global current_profile
    global deck_card_boxes
    global clicked_card
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
                    else:
                        current_profile = "P1"

                    player_select_button.set_text(current_profile)
                    current_deck = update_current_deck()

                    if deck_card_boxes:
                        update_deck_ui(current_deck, front_pointer, back_pointer, deck_card_boxes)
                        deck_size = update_deck_size(current_deck)
                        deck_size_panel.setname(f"{deck_size}/20 ")

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

                elif event.ui_element == exit_button:
                    print("Game Closed.")
                    screen_drawn = False
                    run = False

                elif event.ui_element == edit_deck:
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

                    # applies card effects and switches turn
                    take_turn()

                    # updates ui elements
                    update_playing_info(op_health, p_health, p_energy, op_energy, round_info, p_label, op_label)
                    update_hand_cards(card_1, card_2, card_3, card_4, card_5, card_1_button, card_2_button, card_3_button, card_4_button, card_5_button)

                    # checks if game is over
                    if check_game_over():
                        game_state = "game_ended"

                        # hides player label bc its a quick fix 
                        p_label.setname(" ")
                        op_energy.setname(" ")

                        screen_drawn = False

                    else:
                        # enables ui
                        for element in active_ui_elements:
                            element.enable()

                elif event.ui_element == card_1_button:
                    current_player, _ = check_current_player()

                    # updates description
                    attack, heal, cost, description_txt = get_hand_card_vals(card_1.getcard())
                    description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                    # moves card to/from playing area

                    move_card(current_player, card_1, 0)


                elif event.ui_element == card_2_button:
                    current_player, _ = check_current_player()

                    # updates description
                    attack, heal, cost, description_txt = get_hand_card_vals(card_2.getcard())
                    description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                    # moves card to/from playing area
                    move_card(current_player, card_2, 1)


                elif event.ui_element == card_3_button:
                    current_player, _ = check_current_player()

                    # updates description
                    attack, heal, cost, description_txt = get_hand_card_vals(card_3.getcard())
                    description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                    # moves card to/from playing area
                    move_card(current_player, card_3, 2)


                elif event.ui_element == card_4_button:
                    current_player, _ = check_current_player()

                    # updates description
                    attack, heal, cost, description_txt = get_hand_card_vals(card_4.getcard())
                    description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                    # moves card to/from playing area
                    move_card(current_player, card_4, 3)


                elif event.ui_element == card_5_button:
                    current_player, _ = check_current_player() 

                    # updates description
                    attack, heal, cost, description_txt = get_hand_card_vals(card_5.getcard())
                    description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                    # moves card to/from playing area
                    move_card(current_player, card_5, 4)


                # DECK BUILDER BUTTON HANDLING
                elif event.ui_element == human:
                    current_race = human_cards
                    race_index = 0
                    current_race_card, current_race_card_button = update_current_race_card(current_race, current_race_card, current_race_card_button, race_index)

                    # updates description
                    attack, heal, cost, description_txt = get_race_card_vals(current_race_card)
                    description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                elif event.ui_element == elf:
                    current_race = elf_cards
                    race_index = 0
                    current_race_card, current_race_card_button = update_current_race_card(current_race, current_race_card, current_race_card_button, race_index)

                    # updates description
                    attack, heal, cost, description_txt = get_race_card_vals(current_race_card)
                    description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                elif event.ui_element == dwarf:
                    current_race = dwarf_cards
                    race_index = 0
                    current_race_card, current_race_card_button = update_current_race_card(current_race, current_race_card, current_race_card_button, race_index)

                    # updates description
                    attack, heal, cost, description_txt = get_race_card_vals(current_race_card)
                    description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                elif event.ui_element == undead:
                    current_race = undead_cards
                    race_index = 0
                    current_race_card, current_race_card_button = update_current_race_card(current_race, current_race_card, current_race_card_button, race_index)

                    # updates description
                    attack, heal, cost, description_txt = get_race_card_vals(current_race_card)
                    description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                elif event.ui_element == race_left:
                    if race_index == 0:
                        race_index = race_card_length - 1 # goes from 0 to length - 1 
                    else:
                        race_index -= 1

                    if current_race:
                        current_race_card, current_race_card_button = update_current_race_card(current_race, current_race_card, current_race_card_button, race_index)

                        # updates description
                        attack, heal, cost, description_txt = get_race_card_vals(current_race_card)
                        description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                elif event.ui_element == race_right:
                    if race_index == race_card_length - 1: # goes from 0 to length - 1 
                        race_index = 0
                    else:
                        race_index += 1

                    if current_race: 
                        current_race_card, current_race_card_button = update_current_race_card(current_race, current_race_card, current_race_card_button, race_index)
                        # updates description
                        attack, heal, cost, description_txt = get_race_card_vals(current_race_card)
                        description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                elif event.ui_element == select:
                    # logic for adding a card into top card slot
                    if not current_deck:
                        current_deck.insert(front_pointer, current_race_card)
                    elif current_deck[front_pointer] != current_race_card:
                        current_deck[front_pointer] = current_race_card.getcard().clone()

                    update_deck_ui(current_deck, front_pointer, back_pointer, deck_card_boxes)

                    deck_size = update_deck_size(current_deck)
                    deck_size_panel.setname(f"{deck_size}/20 ")

                    print(f"Card Added to {current_profile} Deck: {current_race_card.getname()}")

                elif event.ui_element == deck_left:
                    deck_len = len(current_deck)
                    front_pointer = (front_pointer - 1) % deck_len
                    back_pointer = (back_pointer - 1) % deck_len
                    update_deck_ui(current_deck, front_pointer, back_pointer, deck_card_boxes)

                elif event.ui_element == deck_right:
                    deck_len = len(current_deck)
                    front_pointer = (front_pointer + 1) % deck_len
                    back_pointer = (back_pointer + 1) % deck_len
                    update_deck_ui(current_deck, front_pointer, back_pointer, deck_card_boxes)

                # PLAYING BUTTON HANDLING
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


                elif event.ui_element == resume:
                    
                    background.kill()
                    resume.kill()
                    close_button.kill()

                    screen.fill([155, 0, 0])

                    update_playing_info(op_health, p_health, p_energy, op_energy, round_info, p_label, op_label)

                    # enables background ui
                    for element in active_ui_elements:
                        element.enable()
    

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
                    return_cards_to_deck()
                    deck_card_boxes = None
                    game_state = "startup"
                    screen_drawn = False


        # game logic
        if game_state == "startup":
            if not screen_drawn:
                play_button, instructions_button, exit_button, edit_deck, player_select_button, settings_button = draw_startup()
                screen_drawn = True
        
        elif game_state == "deck":
            if not screen_drawn:
                deck_size_panel, deck_left, deck_right, card_slot1, card_slot6, card_slot2, card_slot5, card_slot3, card_slot4, top_card_ui, human, elf, dwarf, undead, description, current_race_card, current_race_card_button, race_right, race_left, player_select_button, select, close_button = draw_deck()

                # updates the current race when first opening the deck builder
                current_race = human_cards
                race_index = 0
                current_race_card, current_race_card_button = update_current_race_card(current_race, current_race_card, current_race_card_button, race_index)

                attack, heal, cost, description_txt = get_race_card_vals(current_race_card)
                description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                # sets order of cards in deck
                deck_card_boxes = [card_slot1, card_slot2, card_slot3, top_card_ui, card_slot4, card_slot5, card_slot6]
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
                pause_button, end_round, card_1, card_2, card_3, card_4, card_5, card_1_button, card_2_button, card_3_button, card_4_button, card_5_button, description,  op_health, p_health, p_energy, op_energy, round_info, p_label, op_label = draw_playing()

                # updates
                update_hand_cards(card_1, card_2, card_3, card_4, card_5, card_1_button, card_2_button, card_3_button, card_4_button, card_5_button)
                update_playing_info(op_health, p_health, p_energy, op_energy, round_info, p_label, op_label)

                # updates description
                attack, heal, cost, description_txt = get_hand_card_vals(card_1.getcard())
                description_text_label = update_description_text(attack, heal, cost, description_txt, description)

                screen_drawn = True
            
             
        elif game_state == "game_ended":
            if not screen_drawn:
                close_button = draw_game_ended()
                screen_drawn = True

        elif game_state == "pause_menu":
            if not screen_drawn:
                background, resume, close_button = draw_pause_menu()
                screen_drawn = True

        else:
            print("Game state error.")


        # draw ui
        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.flip()

    pygame.quit()

main()