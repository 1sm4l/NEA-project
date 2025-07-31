# library imports
import pygame
import pygame_gui
import random

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


    def gethand(self):
        return self.hand
    
    def sethand(self, ghand):
        self.hand = ghand

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
        if self.hand: #if hand is not empty
            for card in selected_cards:
                if card in self.hand:
                    self.hand.remove(card) #remove card from hand
                    self.discard_pile.append(card) #appends to discard_pile
                else:
                    print("Card not found in hand.")
            selected_cards.clear() #clear selected cards for next player
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
        self.turn_counter += 1

# panel blueprint
class panel:
    # constructor 
    def __init__(self, nname, nx, ny, nwidth, nheight, nmanager):
        self.name = nname
        self.x = nx
        self.y = ny
        self.width = nwidth
        self.height = nheight
        self.manager = nmanager

    def create_panel(self):

        centered_x = self.x - (self.width / 2)
        centered_y = self.y - (self.height / 2)

        box = pygame_gui.elements.UIPanel(
            relative_rect = pygame.Rect((centered_x, centered_y), (self.width, self.height)),
            manager = self.manager
        )

        label_width, label_height = 200, 30
        label_x = (self.width - label_width) // 2
        label_y = (self.height - label_height) // 2

        label = pygame_gui.elements.UILabel(
            relative_rect = pygame.Rect((label_x, label_y), (label_width, label_height)),  # position relative to the box
            text = self.name,
            manager = self.manager,
            container = box  # attaches it to the box
        )
        return box 


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

#---------------------------------------------------------------------------------------


#-----------------------------------GAME LOGIC SECTION-----------------------------------
def start_game():
    new_game = game(1, 1)
    new_game.setplayers([player_1, player_2])

    dummy_card = card("Punch", "Attack", 5, 0, 1, "Basic attack", 1)

    for player in new_game.getplayers():
        player.setdeck([dummy_card] * 10)  # add 10 dummy cards
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
    current_player.draw_card()
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

    for card in selected_cards:
        total_energy_cost += card.getcost()

    if current_player.getenergy() < total_energy_cost:
        print("Not enough energy to play all selected cards.")
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

    # temp variables to prevent crashing
    card_clicked = False
    end_clicked = False

    if card_clicked:
        #if card is clicked then do this
        select_card(clicked_card)

    if end_clicked:
        #if end turn is clicked
        result = apply_card_effect()

        if result is None:
            print("Turn not ended. Not enough energy.")
            return  # player must modify selection and try again

        total_damage, total_heal, total_energy_cost = result # take total_damage, total_heal, total_energy_cost as parameters to change ui
        print(f"Used {total_energy_cost} energy, dealt {total_damage} damage, healed {total_heal} HP.")
    
        current_player.draw_card()
        new_game.next_turn()  
        switch_turn()


# checks if a player hits 0 health, then sets the other player as the winner and sets game as over
def check_game_over():
    current_player, opponent = check_current_player()

    if current_player.gethealth() == 0 and opponent.gethealth() == 0: # if both players die
        new_game.setwinner("Draw.")
        new_game.setgame_over()
        return True
    
    elif new_game.getturn_counter() == 11: # if turn counter = max rounds + 1 (if no one dies)

        if current_player.gethealth() > opponent.gethealth(): # if player has more health than opponent
            new_game.setwinner(current_player.getname())
            new_game.setgame_over()
            return True
        
        elif current_player.gethealth() < opponent.gethealth():  # if opponent has more health than player
            new_game.setwinner(opponent.getname())
            new_game.setgame_over()
            return True
        
        else: # if they have the same health at the end of the game
            new_game.setwinner("Draw.")
            new_game.setgame_over()
            return True
        
    elif opponent.gethealth() == 0: # if opponent dies
        new_game.setwinner(current_player.getname())
        new_game.setgame_over()
        return True
    
    elif current_player.gethealth() == 0: # if current player kills themself
        new_game.setwinner(opponent.getname())
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
    player_select_button = button("P1", (width // 4) - 200, int(3 * height / 4), 100, 100, manager).create_box()
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
    card_temp1 = panel(" ", width // 2 - 350, int(height / 2) + 120, 125, 225, manager).create_panel()
    card_temp2 = panel(" ", width // 2 + 350, int(height / 2) + 120, 125, 225, manager).create_panel()

    # third row
    card_temp3 = panel(" ", width // 2 - 250, int(height / 2) + 120, 150, 250, manager).create_panel()
    card_temp4 = panel(" ", width // 2 + 250, int(height / 2) + 120, 150, 250, manager).create_panel()

    # second row
    card_temp5 = panel(" ", width // 2 - 150, int(height / 2) + 120, 175, 275, manager).create_panel()
    card_temp6 = panel(" ", width // 2 + 150, int(height / 2) + 120, 175, 275, manager).create_panel()

    # top
    top_card = panel(" ", width // 2, int(height / 2) + 120, 200, 300, manager).create_panel()

    # suite
    suite_temp1 = panel("Suites", width // 2 - 325, int(height / 2) - 350, 275, 60, manager).create_panel()
    suite_temp2 = panel(" ", width // 2 - 325, int(height / 2) - 175, 275, 275, manager).create_panel()

    human = button("human", width // 2 - 385, int(height / 2) - 235, 110, 110, manager).create_box()
    elf = button("elf", width // 2 - 265, int(height / 2) - 235, 110, 110, manager).create_box()
    dwarf = button("dwarf", width // 2 - 385, int(height / 2) - 115, 110, 110, manager).create_box()
    undead = button("undead", width // 2 - 265, int(height / 2) - 115, 110, 110, manager).create_box()

    # description
    description_temp = panel("Card Description", width // 2, int(height / 2) - 350, 350, 60, manager).create_panel()
    description = panel(" ", width // 2, int(height / 2) - 175, 350, 250, manager).create_panel()

    # card select
    card_select_temp1 = panel("Choose Card", width // 2 + 325, int(height / 2) - 350, 275, 60, manager).create_panel()
    card_select_temp2 = panel(" ", width // 2 + 325, int(height / 2) - 175, 275, 275, manager).create_panel()

    current_suite_card = card_button(" ", width // 2 + 325, int(height / 2) - 208, 125, 175, manager, " ").create_box()

    suite_right = button(">", width // 2 + 423, int(height / 2) - 208, 50, 50, manager).create_box()
    suite_left = button("<  ", width // 2 + 227, int(height / 2) - 208, 50, 50, manager).create_box()

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

        suite_temp1,
        suite_temp2,

        description_temp,

        card_select_temp1,
        card_select_temp2,

        # buttons
        deck_left,
        deck_right, 
        top_card,
        human, 
        elf, 
        dwarf, 
        undead, 
        description, 
        current_suite_card, 
        suite_right, 
        suite_left, 
        select, 
        close_button
    ])

    return deck_left, deck_right, top_card, human, elf, dwarf, undead, description, current_suite_card, suite_right, suite_left, select, close_button
    

def draw_instructions():
    screen.fill([150, 0, 0])  # background colour

    # background panel
    background = panel(" ", width // 2, int(height / 2), 1000, 800, manager).create_panel()

    # text box
    text_temp = panel("instructions", width // 2, int(height / 2) - 50, 900, 600, manager).create_panel()

    # HOW TO PLAY: 
    #      1. Create a deck using the deck builder.
    #      2. Swap profile by pressing the 'P1' button to create player 2's deck.
    #      3. Play against a friend.
    #      4. Aim of the game is to get your opponent's health down to 0.
           
    #      CARDS:
    #      Each card are apart of a suite. Cards in a suite may contains synergies or tactical combos that can be used to have an edge over the opponent.
    #      Each card contains a cost to play, damage and heal (if it is a support card)

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
    
    return close_button


def draw_playing():
    screen.fill([150, 0, 0])  # background colour


    # GREY BACKGROUND BOXES
    # left box
    left = panel(" ", (width // 4) - 200, height / 2, 500, height, manager).create_panel()

    # settings button
    pause_button = button("Settings", (width // 4) - 387, height / 2 - 470, 75, 75, manager).create_box()

    # round info
    round_info = panel("Current Round: ", (width // 4) - 75, height / 2 - 470, 200, 75, manager).create_panel()

    # INFO PANELS
    # opponent health
    op_health = panel("Opponent Health: ", (width // 4) - 200, height / 2 - 370, 450, 75, manager).create_panel()

    # player health
    p_health = panel("Player Health: ", (width // 4) - 200, height / 2 - 270, 450, 75, manager).create_panel()

    # chat box
    chat_temp1 = panel(" ", (width // 4) - 200, height / 2, 450, 400, manager).create_panel()
    chat_temp2 = panel("Chat Box", (width // 4) - 200, height / 2 - 175, 450, 50, manager).create_panel() #chat box label
    type_button = button("Type Here", (width // 4) - 200, height / 2 + 175, 450, 50, manager).create_box()

    # timer
    timer = panel("Timer", (width // 4) - 200, height / 2 + 270, 450, 75, manager).create_panel()

    # end round
    end_round = button("End Round", (width // 4) - 200, height / 2 + 420, 450, 125, manager).create_box()


    # PLAYER LABELS
    # player
    p_label = panel("Player Name", width - (width // 4) - 720, int(height / 2) + 170, 200, 50, manager).create_panel()
    # opponent
    op_label = panel("Opponent Name", width - (width // 4) + 280, int(height / 2) - 370, 200, 50, manager).create_panel()

    # play area
    play_area = panel(" ", width - (width // 4) - 220, int(height / 2) - 150, 1240, 340, manager).create_panel()

    # CARD BOXES
    # player
    card_1 = card_button(" ", width - (width // 4) - 720, int(3 * height / 4) + 100, 200, 300, manager, " ").create_box()
    card_2 = card_button(" ", width - (width // 4) - 470, int(3 * height / 4) + 100, 200, 300, manager, " ").create_box()
    card_3 = card_button(" ", width - (width // 4) - 220, int(3 * height / 4) + 100, 200, 300, manager, " ").create_box()
    card_4 = card_button(" ", width - (width // 4) + 30, int(3 * height / 4) + 100, 200, 300, manager, " ").create_box()
    card_5 = card_button(" ", width - (width // 4) + 280, int(3 * height / 4) + 100, 200, 300, manager, " ").create_box()

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
    top_of_deck = card_button("deck", width - (width // 4) + 280, int(3 * height / 4) - 160, 100, 150, manager, " ").create_box()

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
        round_info,
        op_health,
        p_health,
        chat_temp1,
        chat_temp2,
        timer,
        p_label,
        op_label,
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

        discard_temp1,
        discard_temp2,
        discard_temp3,
        discard_temp4,

        # buttons
        pause_button, 
        type_button, 
        end_round, 
        card_1, 
        card_2, 
        card_3, 
        card_4, 
        card_5, 
        top_of_deck, 
        top_of_discard_pile
    ])

    return pause_button, type_button, end_round, card_1, card_2, card_3, card_4, card_5, top_of_deck, top_of_discard_pile


def draw_game_ended():
    screen.fill([150, 0, 0])  # background colour

    # background panel
    background = panel(" ", width // 2, int(height / 2), 1000, 800, manager).create_panel()

    # win/lose
    w_l = panel("You Win/Lose/Draw", width // 2, int(height / 2) - 150, 800, 240, manager).create_panel()

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

def declare_variables():
    game_state = "startup"
    screen_drawn = False # condition check for drawing screen
    current_suite = None

    # buttons
    play_button = None
    instructions_button = None
    exit_button = None
    edit_deck = None
    player_select_button = None
    settings_button = None
    deck_left = None
    deck_right = None
    top_card = None
    human = None
    elf = None
    dwarf = None
    undead = None
    description = None
    current_suite_card = None
    suite_right = None
    suite_left = None
    select = None
    replay = None
    pause_button = None
    background = None
    resume = None
    close_button = None

    return game_state, screen_drawn, current_suite, play_button, instructions_button, exit_button, edit_deck, player_select_button, settings_button, deck_left, deck_right, top_card, human, elf, dwarf, undead, description, current_suite_card, suite_right, suite_left, select, replay, pause_button, background, resume, close_button

# setup
fps = 60
clock = pygame.time.Clock()

info = pygame.display.Info()
width, height = info.current_w, info.current_h

screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Twine")

manager = pygame_gui.UIManager((width, height))


# game variables
player_1 = player("JohnDoe", 100, 10, False)
player_2 = player("JaneDoe", 100, 10, False)
clicked_card = None
selected_cards = []
new_game = None
active_ui_elements = []
new_game = None

# main loop
def main():
    run = True
    game_state, screen_drawn, current_suite, play_button, instructions_button, exit_button, edit_deck, player_select_button, settings_button, deck_left, deck_right, top_card, human, elf, dwarf, undead, description, current_suite_card, suite_right, suite_left, select, replay, pause_button, background, resume, close_button = declare_variables()
    global new_game # assigning new_game as a global variable for use in main game function

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
                    current_text = player_select_button.text

                    if current_text == "P1":
                        player_select_button.set_text("P2")
                    else:
                        player_select_button.set_text("P1")

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
                    print("Enter deck builder")
                    
                    # disables background UI
                    for element in active_ui_elements:
                        element.disable()

                    game_state = "deck"
                    screen_drawn = False


                # DECK BUILDER BUTTON HANDLING
                elif event.ui_element == human:
                    current_suite = "human"

                elif event.ui_element == elf:
                    current_suite = "elf"

                elif event.ui_element == dwarf:
                    current_suite = "dwarf"

                elif event.ui_element == undead:
                    current_suite = "undead"

                elif event.ui_element == deck_left:
                    pass

                elif event.ui_element == deck_right:
                    pass


                # PLAYING BUTTON HANDLING
                elif event.ui_element == pause_button:

                    # disables background UI
                    for element in active_ui_elements:
                        element.disable()

                    print("Settings Opened")
                    game_state = "pause_menu"
                    screen_drawn = False
                
                #TODO FIX THIS----------------------------------------------------------------------------------------------
                elif event.ui_element == resume:
                    
                    background.kill()
                    resume.kill()
                    close_button.kill()

                    screen.fill([155, 0, 0])

                    # enables background ui
                    for element in active_ui_elements:
                        element.enable()
                
                #-----------------------------------------------------------------------------------------------------------

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
                    game_state = "startup"
                    screen_drawn = False


        # game logic
        if game_state == "startup":
            if not screen_drawn:
                play_button, instructions_button, exit_button, edit_deck, player_select_button, settings_button = draw_startup()
                screen_drawn = True
        
        elif game_state == "deck":
            if not screen_drawn:
                deck_left, deck_right, top_card, human, elf, dwarf, undead, description, current_suite_card, suite_right, suite_left, select, close_button = draw_deck()
                screen_drawn = True

            # based on current suite, the current suite card is changed

        elif game_state == "instructions":
            if not screen_drawn:
                close_button = draw_instructions()
                screen_drawn = True

        elif game_state == "playing":
            if not screen_drawn:
                new_game = start_game()
                pause_button, type_button, end_round, card_1, card_2, card_3, card_4, card_5, top_of_deck, top_of_discard_pile = draw_playing()
                screen_drawn = True

            else:
                take_turn()

                if check_game_over():
                    game_state = "game_ended"

             
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