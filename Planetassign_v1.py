#Author: Lukas Zarvis
#Date: 2/3/25


#Surface gravity Constants
fMercury= 0.38
fVenus= 0.91
fMoon= 0.165
fMars= 0.38
fJupiter= 2.34
fSaturn= 0.93
fUranus= 0.92
fNeptune= 1.12
fPluto= 0.066

#Input Constants + conversion
sName= input("What is your name: ")
fWeight= float(input("What is your weight in lbs: "))


#Compute
fMercuryWeight= fWeight * fMercury
fVenusWeight= fWeight * fVenus
fMoonWeight= fWeight * fMoon
fMarsWeight= fWeight* fMars
fJupiterWeight= fWeight* fJupiter
fSaturnWeight= fWeight* fSaturn
fUranusWeight= fWeight * fUranus
fNeptuneWeight= fWeight * fNeptune
fPlutoWeight= fWeight * fPluto

#Intial print with line spacing
print(f"\n{sName}, Welcome to the Planetary Calculator!!")
print("Here are your weights on the different planets of our solar system.\n")

#Output Print with formatting for columns on both sides
print(f"{'Weight on Mercury is:':25s} {fMercuryWeight:10,.2f} lbs")
print(f"{'Weight on Venus is:':25s} {fVenusWeight:10,.2f} lbs")
print(f"{'Weight on Moon is:':25s} {fMoonWeight:10,.2f} lbs")
print(f"{'Weight on Mars is:':25s} {fMarsWeight:10,.2f} lbs")
print(f"{'Weight on Jupiter is:':25s} {fJupiterWeight:10,.2f} lbs")
print(f"{'Weight on Saturn is:':25s} {fSaturnWeight:10,.2f} lbs")
print(f"{'Weight on Uranus is:':25s} {fUranusWeight:10,.2f} lbs")
print(f"{'Weight on Neptune is:':25s} {fNeptuneWeight:10,.2f} lbs")
print(f"{'Weight on Pluto is:':25s} {fPlutoWeight:10,.2f} lbs")
