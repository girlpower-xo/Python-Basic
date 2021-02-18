import time

# Format
tijdFormat = "{0:02d}:{1:02d}:{2:02d}"

# Vraag aan gebruiker voor starttijd
tijd = input('Vul de tijd in (uu:mm:ss) ')

# Zet de starttijd van de gebruiker in variablen
tijdArray = tijd.split(':')

uren = int(tijdArray[0])
minuten = int(tijdArray[1])
seconden = int(tijdArray[2])


def printTijd(uren, minuten, seconden):
    print(tijdFormat.format(uren, minuten, seconden))


# Start de logica van de timer
printTijd(uren, minuten, seconden)

while(True):
    # Wacht 1 seconde
    time.sleep(1)
    seconden += 1

    if (seconden >= 60):
        seconden = 0
        minuten += 1

    if (minuten >= 60):
        minuten = 0
        uren += 1

    if (uren >= 24):
        uren = 0
        minuten = 0
        seconden = 0

    printTijd(uren, minuten, seconden)
