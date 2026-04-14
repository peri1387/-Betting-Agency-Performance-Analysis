import pandas as pd
from faker import Faker
import random

fake = Faker('el_GR')  # Χρησιμοποιούμε ελληνικά data για να φαίνεται πιο real
fake_data = []

# Ορίζουμε τα παιχνίδια και τις προμήθειες/πιθανότητες (Domain Knowledge)
games = ['Kino', 'Pame Stoixima', 'Joker', 'Virtual Sports', 'Scratch']

print("Δημιουργία δεδομένων... περίμενε λίγο.")

for i in range(10000):  # Φτιάχνουμε 10.000 εγγραφές (συναλλαγές)
    game = random.choice(games)
    amount_staked = round(random.uniform(0.5, 50.0), 2)  # Ποντάρισμα από 0.5€ έως 50€
    
    # Απλή λογική: Στο 20% των περιπτώσεων ο παίκτης κερδίζει κάτι
    if random.random() < 0.20:
        payout_amount = round(amount_staked * random.uniform(1.2, 5.0), 2) # Κέρδος από 20% έως 400% του πονταρίσματος
    else:
        payout_amount = 0.0
        
    fake_data.append({
        "Transaction_ID": i + 1000,
        "Date": fake.date_between(start_date='-1y', end_date='today'),
        "Game_Type": game,
        "Amount_Staked": amount_staked,
        "Payout_Amount": payout_amount,
        "Customer_Type": random.choice(['Regular', 'Occasional', 'VIP'])
    })

# Μετατροπή σε DataFrame και αποθήκευση
df = pd.DataFrame(fake_data)
df.to_csv('opap_store_data.csv', index=False)

print("Έτοιμο! Το αρχείο 'opap_store_data.csv' δημιουργήθηκε.")
print(df.head()) # Δείξε μας τις πρώτες 5 γραμμές