#https://www.codewars.com/kata/583203e6eb35d7980400002a
def count_smileys(arr):
    eyes = [':',';']
    noses = ['-','~']
    mouths = [')','D' ]    
    smileys = 0
    
    if len(arr) == 0:
        return 0
        
    else:        
        for smiley in arr:
            if len(smiley) == 2:
                if smiley[0] in eyes and smiley[1] in mouths:
                    smileys =  smileys + 1
            elif len(smiley) == 3:
                if smiley[0] in eyes and smiley[1] in noses and smiley[2] in mouths:
                    smileys =  smileys + 1
                    
        return smileys