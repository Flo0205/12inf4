from ampelExtended import AmpelExtended

a = AmpelExtended("rot")

# Rot
print(a.ampel.getLampen())

a.schalten()

# Rot-Gelb
print(a.ampel.getLampen())

a.tageszeitWechsel()
a.schalten()

# Aus
print(a.ampel.getLampen())

a.schalten()

# Gelb
print(a.ampel.getLampen())
