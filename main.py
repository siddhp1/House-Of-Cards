from random import randint
import pydealer
import csv

# Create stack of winning cards
WINNING_CARDS = ["AS", "2S", "3S", "4S", "5S", "6S"]
winning_cards = pydealer.Stack()
winning_cards.add(WINNING_CARDS)

# Payout structure of game
PAYOUT_STRUCTURE = {
    0:0,
    1:20000,
    2:50000,
    3:100000,
    4:250000,
    5:2500000,
    6:250000000
}

# Number of iterations of game simulation
ITERATIONS = 100000

def play():
    # Simulate spinners
    cards_to_select = randint(1, 6)
    cards_in_tray = (randint(1, 6) - 1) * 3 + 12  
    
    # Create deck and shuffle
    deck = pydealer.Deck()
    deck.shuffle()
    
    # Remove "winning" cards
    deck.get_list(WINNING_CARDS)
    
    # Deal cards in tray
    tray = pydealer.Stack()
    tray.add(deck.deal(cards_in_tray - 6)) # Add random cards from deck
    tray.add(winning_cards) # Add winning cards
    tray.shuffle()
    
    # Draw a hand (size = cards_to_select)
    selected_cards = tray.deal(cards_to_select)
    
    # Determing number of winning cards selected
    num_winning = sum(card in winning_cards for card in selected_cards)
    earnings = PAYOUT_STRUCTURE.get(num_winning) # Get respective payout
    
    # Return round information
    return[cards_to_select, cards_in_tray, num_winning, earnings]
    
def main():
    # Get csv file path
    file_path = 'results.csv'
    
    # Access file 
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        # Column titles
        writer.writerow(["Cards to select", "Cards in tray", "Number of winning cards", "Earnings"])
        # Run simulation and write results to file
        for i in range(ITERATIONS):
            arr = play()
            writer.writerow(arr)
        print("Simulation Complete")

if __name__ == "__main__":
    main()
