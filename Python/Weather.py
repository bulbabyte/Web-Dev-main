weatherIsNice = True
haveUmbrella = False

if not (haveUmbrella or weatherIsNice):
    print("Stay inside")
else:
    print("Go for a walk")

# More readable version

weatherIsNice = True
haveUmbrella = False

if haveUmbrella or weatherIsNice:
    print('Go for a walk')
else:
    print('Stay inside')
    