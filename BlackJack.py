import random;
print("**** Welcome to the world of Blackout - Bet & Win****\n");
class Player():
    temp_usedcards=[];
    dealer_cards=[];
    player_cards=[];
    dealer_repr=[];
    player_repr=[];
    hit_run = 1;
    suits=['Hearts','Diamonds','Spades','Clubs'];
    ranks=['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace'];
    values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11};
    def __init__(self,name,chips):
        self.name=name;
        self.chips=chips;

    def display_all(self,dealer_repr,player_repr,open_check):
        print("Dealer's Cards :\n");
        for x in range(len(dealer_repr)):
            print("------------------------");
            for i in range(0,3):
                print("|                                     |");
            if x==0 and self.open_check !='active':
                print(f"|         Card hidden       |");
            else:
                print("|    {:<20}   |".format(self.dealer_repr[x]));
            for i in range(0, 3):
                print("|                                     |");
            print("------------------------\n");

        print("Player's Cards :\n");
        for x in self.player_repr:
            print("------------------------");
            for i in range(0, 3):
                print("|                                     |");
            print("|    {:<20}   |".format(x));
            for i in range(0, 3):
                print("|                                     |");
            print("------------------------\n");


    def player_turn(self,player_cards,bet,open_check):
        self.win=0;
        self.current_check=len(self.player_cards)+1;
        while len(self.player_cards) != self.current_check:
            self.card_suits = random.choice(self.suits);
            self.card_ranks = random.choice(self.ranks);
            self.full_card = self.card_ranks + " of " + self.card_suits;
            if self.full_card not in self.temp_usedcards:
                self.temp_usedcards.append(self.full_card);
                self.player_repr.append(self.full_card);
                self.player_cards.append(self.values[self.card_ranks]);
        if sum(player_cards)>21:
            self.win=1;
            self.open_check='active';
        self.display_all(self.dealer_repr, self.player_repr, self.open_check);
        if self.win==1:
            print("*****Better luck next time, Dealer Wins*****\n");
            self.chips = self.chips - self.bet;
            print(str(self.chips) + " chips left in your account.");
            self.hit_run = 0;


    def dealer_turn(self,dealer_cards,player_cards,bet,open_check):
        while sum(self.dealer_cards)<=21:
            if  sum(self.dealer_cards)>sum(self.player_cards):
                self.display_all(self.dealer_repr, self.player_repr,self.open_check);
                print("*****Better luck next time, Dealer Wins*****");
                self.chips = self.chips-self.bet;
                print(str(self.chips) + " chips left in your account.");
                return;
            else:
                self.card_suits = random.choice(self.suits);
                self.card_ranks = random.choice(self.ranks);
                self.full_card = self.card_ranks + " of " + self.card_suits;
                if self.full_card not in self.temp_usedcards:
                    self.temp_usedcards.append(self.full_card);
                    self.dealer_repr.append(self.full_card);
                    self.dealer_cards.append(self.values[self.card_ranks]);
        self.display_all(self.dealer_repr, self.player_repr,self.open_check);
        print("*****Kudos!!!  "+self.name+" Wins");
        self.chips = self.chips+self.bet;
        print(str(self.chips) + " chips available in your account.");

    def playerenroll(self):
        self.bet=int(input("Place your bet :\n"));
        if self.bet>self.chips:
            print("Sorry, but you don't have enough chips to roll in.\n");
        else:
            self.open_check = '';
            print("******Game Started******\n");
            while len(self.dealer_cards)<2:
                self.card_suits = random.choice(self.suits);
                self.card_ranks = random.choice(self.ranks);
                self.full_card = self.card_ranks + " of " + self.card_suits;
                self.temp_usedcards.append(self.full_card);
                self.dealer_repr.append(self.full_card);
                self.dealer_cards.append(self.values[self.card_ranks]);
            while len(self.player_cards)<2:
                self.card_suits = random.choice(self.suits);
                self.card_ranks = random.choice(self.ranks);
                self.full_card = self.card_ranks + " of " + self.card_suits;
                if self.full_card not in self.temp_usedcards:
                    self.temp_usedcards.append(self.full_card);
                    self.player_repr.append(self.full_card);
                    self.player_cards.append(self.values[self.card_ranks]);
            self.display_all(self.dealer_repr,self.player_repr,self.open_check);
            while  self.hit_run==1:
                self.move=input("Press 'h' to hit or 's' to stay\n");
                if self.move=='h':
                    self.player_turn(self.player_cards,self.bet,self.open_check);
                if self.move=='s':
                    self.open_check='active';
                    self.dealer_turn(self.dealer_cards,self.player_cards,self.bet,self.open_check);
                    self.hit_run=0;

p_name=input("Enter you name :\n");
p_chips=int(input("Enter the chips to wants to buy :\n"));
User=Player(p_name,p_chips);
User.playerenroll();
