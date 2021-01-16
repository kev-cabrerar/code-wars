def i_tri(s):
    total = 140.6
    rest = "{0:.2f}".format(total-s)

    if s <= 0:
        return 'Starting Line... Good Luck!'

    if (s > 0 and s <= 2.4):
        return {'Swim': rest+' to go!'}

    if (s > 2.4 and s <= 114.4):
        return {'Bike': rest+' to go!'}

    if (s > 114.4 and s < 130.6):
        return {'Run': "'"+rest+" to go!"}

    if (s > 130.6 and s < 140.6):
        return {'Run': 'Nearly there!'}

    if (s >= 140.6):
        return "You're done! Stop running!"
