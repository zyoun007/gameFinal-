import os.path
import random
grylaAlive = True
playerAlive = True
chestOpen = False
taxesFromkingGeorgeitem = False
grylaKey = False



while True:
    print('The Scenario')     
    path = 'grylascenario.txt' 

    infile = open(path, 'r')

    readFile = infile.read()
    print(readFile)

    #setting off (part 2)
    
    path = 'grylasettingoff.txt'
    infile = open(path, 'r')

    readFile = infile.read()
    print(readFile)

    settingInput = input('Please respond with a corresponding number:')
    if settingInput == "2":
                         print('Instead of facing your fears, you run, forever to be tormented by both Grÿla and your poor decision making.\n')
                         print('--> If you would like to try again after running away, please press "r"<--')
                         print('--> If you would like to quit, press "x" <--') 
                         restartQuit = input()
                         
                         if restartQuit == "x":
                            quit()
                         if restartQuit == "r":
                             continue
                                        
    if settingInput == "1":
        print('You continue your travels by opening the door')
        path = 'gencounter.txt'
        infile = open(path, 'r')

        readFile = infile.read()
        print(readFile)

        entrywayInput = input('Please respond with a corresponding number:')
        if entrywayInput == "1":
                             print('You opened the left door to a kitchen(3)')
        if entrywayInput == "2":
                             print('You opened the right door to a bedroom(4)')
        if entrywayInput == "3":
                          print('After adventuring into the hut, you decided to end your trip. You leave to be forever tormented by both Grÿla and your poor decision making.')
                          print('Press "x" to quit or "r" to restart') 
                          userInput = input() 
                          if userInput == "x":
                             quit()
                          if userInput == "r":
                             continue
        if entrywayInput == "4":
                             for rolls in range(1):
                                 randomDice = random.randrange(3)+1
                             if randomDice != 3:
                                 path = 'gencountertablefail.txt'
                                 infile = open(path, 'r')

                                 readFile = infile.read()
                                 print(readFile)
                                 
                             if randomDice == 3:
                                 taxesFromkingGeorge = True
                                 path = 'gencountertablesuccess.txt'
                                 infile = open(path, 'r')

                                 readFile = infile.read()
                                 print(readFile)

                                 entrywayInput = input('Please respond with a corresponding number:')
                                 if entrywayInput == "1":
                                     print('You opened the left door')
                                 if entrywayInput == "2":
                                     print('You opened the right door')
                                 if entrywayInput == "3":
                                     print('After adventuring into the hut, you decided to end your trip. You leave to be forever tormented by both Grÿla and your poor decision making.\n')                                  
                                     print('--> If you would like to try again after running away, please press "r"<--')
                                     print('--> If you would like to quit, press "x" <--') 
                                     userInput = input() 
                                     if userInput == "x":
                                        quit()
                                     if userInput == "r":
                                         continue
                                
                                     else:
                                         print()
                                         print()
                                         print('--> That input is not understood, would you like to restart from the beginning <--')
                                         print('--> Press "r" to restart from checkpoint or "x" to quit <--'\n)
                                         userInput = input()
                                         if userInput == "x":
                                                 quit()
                                         if userInput == "r":
                                                 continue

    
    else:
         print()
         print()
         print('--> That input is not understood, would you like to restart from the beginning <--')
         print('--> Press "r" to restart from checkpoint or "x" to quit <--\n')
         userInput = input()
         if userInput == "x":
             quit()
         if userInput == "r":
             continue
         else:
             print()
             print()
             print('--> That input is not understood, would you like to restart from the beginning <--')
             print('--> Press "r" to restart from checkpoint or "x" to quit <--\n')
             userInput = input()
             if userInput == "x":
                 quit()
             if userInput == "r":
                 continue
             else:
                 print()
                 print('Ok, hopefully, third time is the charm for you. Now please:\n')
                 print('--> Press "r" to restart from checkpoint or "x" to quit <--\n')
                 userInput = input()
                 if userInput == "x":
                     quit()
                 if userInput == "r":
                     continue
                 else:
                     print()
                     print('No, there is no secret code built into this. Stop searching.')
                     print('--> Press "r" to restart from checkpoint or "x" to quit <--\n') 
                     userInput = input()
                     if userInput == "x":
                         quit()
                     if userInput == "r":
                         continue
                     else:
                         print()
                         print('Oh, you want a secret, do you? Do it again, see what happens.')
                         print('--> Press "r" to restart from checkpoint or "x" to quit <--')
                         userInput = input()
                         if userInput == "x":
                             quit()
                         if userInput == "r":
                             continue
                         else:
                            print()
                            print()
                            print('--> Please press any key to find your secret gift <--')

                            userInput = input()
                            if userInput == "x":
                                quit()
                            else:
                                quit()



    if entrywayInput == "1":
        path = 'gkitchen.txt'
        infile = open(path, 'r')

        readFile = infile.read()
        print(readFile)

    kitchenInput = input('Please respond with a corresponding number:')
    if kitchenInput == "1":
        print()
        print('--> Your search reveals nothing')
        while kitchenInput =="1":
                path = 'gkitchen.txt'
                infile = open(path, 'r')

                readFile = infile.read()
                print(readFile)

                kitchenInput = input('Please respond with a corresponding number:')
        
    if kitchenInput == "2":
        print()
        print('--> You decide to travel down the stairs')
        
    if kitchenInput == "3":
        path = 'entryreturn.txt'
        infile = open(path, 'r')

        readFile = infile.read()
        print(readFile)

        entrywayInput = input('Please respond with a corresponding number:') 
    if entrywayInput == "2":
        path = 'gbedroom.txt'
        infile = open(path, 'r')

        readFile = infile.read()
        print(readFile)
        bedroomInput = input('Please respond with a corresponding number:')
        if bedroomInput == "1": 
            while bedroomInput == "1":
                print('Your search turned up nothing you did not already know')
                path = 'gbedroom.txt'
                infile = open(path, 'r')

                readFile = infile.read()
                print(readFile)
                
                bedroomInput = input('Please respond with a corresponding number:') 


        if bedroomInput == "2":
            print('Exit back to the EntryWay (2)')
        if bedroomInput == "3":
            print ('You attempted to open the chest, but surprise surprise, a key is required.\n')
            while bedroomInput =="3":
                path = 'gbedroom.txt'
                infile = open(path, 'r')

                readFile = infile.read()
                print(readFile)
                bedroomInput = ('Please respond with the corresponding number')
                



                
        #cellar
    #kitchenInput = 
    if kitchenInput == "2":
        path = 'gcellar.txt'
        infile = open(path, 'r')

        readFile = infile.read()
        print(readFile)

        cellarInput = input('Please respond with a corresponding number:')
#without item
        grylaHealth = 100
        playerHealth = 100
        while grylaHealth > 0:
        
            if cellarInput == "1":
                if taxesFromkingGeorgeitem == False:
                    print('You chose to attack Gryla')
                    for rolls in range (1):
                        playerDice = random.randrange(20)+1
                        print('You rolled a', playerDice) 
                        if playerDice == 20:
                                  print('Critical Hit')


                        if playerDice == 1:
                            print('Critical Fail')
                            grylaHealth += 50
                            print("Gryla's health is now", grylaHealth)

                        if playerDice >= 12:
                            grylaHealth -= 50
                            print("Gryla's health is at", grylaHealth)
                            print()
                                  

                              

                        if playerDice < 12:
                            print('Gryla has not been affected')
                            print("Gryla's health is at", grylaHealth)
                            #finish 

                       


                        if grylaHealth > 1:
                            print("Gryla's turn to attack you")
                            for rolls in range (1):
                                grylaDice = random.randrange(20)-3
                                print('Gryla rolled a', grylaDice)
                                if grylaDice >= 12:
                                    playerHealth -= 50
                                    print('Your health is at', playerHealth)
                                    if playerHealth > 0: 
                                        path = 'attackagain.txt'
                                        infile = open(path, 'r')

                                        readFile = infile.read()
                                        print(readFile) 
                                        cellarInput = input('Please respond with a corresponding number:')
                                        

                                if grylaDice < 12:
                                    print('Your health is at', playerHealth)
                                    path = 'attackagain.txt'
                                    infile = open(path, 'r')

                                    readFile = infile.read()
                                    print(readFile) 
                                    cellarInput = input('Please respond with a corresponding number:')
                                    continue
                                                                
                            
                


                if playerHealth == 0:
                    print('It is joever')
                    playerAlive = False
                      
            elif taxesFromkingGeorgeitem == True:
                    print('You chose to attack Gryla')
                    for rolls in range (1):
                        playerDice = random.randrange(20)+2
                        print('You rolled a', playerDice) 
                        if playerDice == 20:
                                  print('Critical Hit')


                        if playerDice == 1:
                            print('Critical Fail')
                            grylaHealth += 50
                            print("Gryla's health is now", grylaHealth)

                        if playerDice >= 12:
                            grylaHealth -= 50
                            print("Gryla's health is at", grylaHealth)
                            print()
                                  

                              

                        if playerDice < 12:
                            print('Gryla has not been affected')
                            print("Gryla's health is at", grylaHealth)
                            #finish 

                       


                        if grylaHealth > 1:
                            print("Gryla's turn to attack you")
                            for rolls in range (1):
                                grylaDice = random.randrange(20)-3
                                print('Gryla rolled a', grylaDice)
                                if grylaDice >= 12:
                                    playerHealth -= 50
                                    print('Your health is at', playerHealth)
                                    if playerHealth > 0: 
                                        path = 'attackagain.txt'
                                        infile = open(path, 'r')

                                        readFile = infile.read()
                                        print(readFile) 
                                        cellarInput = input('Please respond with a corresponding number:')
                                        

                                if grylaDice < 12:
                                    print('Your health is at', playerHealth)
                                    path = 'attackagain.txt'
                                    infile = open(path, 'r')

                                    readFile = infile.read()
                                    print(readFile) 
                                    cellarInput = input('Please respond with a corresponding number:')
                                    continue
                                                                
                            
                


            if playerHealth == 0:
                 print('It is joever')
                 playerAlive = False
                    
                            
                
            if grylaHealth == 0:
                  print('Gryla has been slained.')
                  print('Gryla disappears, but in her absence, a key appears.')
                  grylaAlive = False
                  print('You pick up the key.')
                  grylaKey = True

#I for the life of me could not fully understand while statements. They broke more times than they didn't for me. I decided to do the long way instead. I know it will make the code harder to run.
#I know removal of a statement has something to due with the while statement but line 345 explains my issue and at the bottom will contant the reason for why my code is a junky and error filled) 

            elif cellarInput == "2":
                      print('You attempt to persuade Gryla')
                      for rolls in range (1):
                          playerDice = random.randrange (20)+1
                          grylaDice = random.randrange (20)+5
                          if playerDice > grylaDice:
                              print('Gryla has been persuaded and disappeared.')
                              print('In her absence, a key appears.')
                              grylaAlive = False
                              print('You pick up the key.')
                              grylaKey = True
                          elif playerDice <= grylaDice:
                             print('Your attempts to persuade Gryla has failed. She will not be persuaded by your attempts.')
                          path = 'attackagain.txt'
                          infile = open(path, 'r')

                          readFile = infile.read()
                          print(readFile)
                          cellarInput = input('Please respond with a corresponding number:')
                      
            elif cellarInput == "3":
                      print('You notice Gryla is unwell, so you attempt to cure her')
                      for rolls in range (1):
                          playerDice = random.randrange (20)+1
                          grylaDice = random.randrange (20)-1 #i think that's how it works
                          if playerDice > grylaDice:
                              print('Gryla has been cure thanks to your kindness.')
                              print('She disappears, and in her absence, a key appears.')
                              grylaAlive = False
                              print('You pick up the key.')
                              grylaKey = True
                          elif playerDice <= grylaDice:
                              print('Your attempts to cure Gryla has failed. She is not as unwell as you thought, any further attempts will be met in failure.')
                              path = 'attackagain.txt'
                              infile = open(path, 'r')

                              readFile = infile.read()
                              print(readFile)
                              cellarInput = input('Please respond with a corresponding number:')
                              continue

            if playerAlive == False: 
                path = 'playerdead.txt'
                infile = open(path, 'r')

                readFile = infile.read()
                print(readFile)
                restartQuit = input()
                if restartQuit == "1":
                    quit()
                if restartQuit == "2":
                   continue

            if grylaAlive == False:
                path = 'Gryladefeated.txt'
                infile = open(path, 'r')

                readFile = infile.read()
                print(readFile)
                endingInput = input('Please respond with a corresponding number:')
                while endingInput == "1":
                    print('Your search reveals nothing.')
                    path = 'Gryladefeated.txt'
                    infile = open(path, 'r')

                    readFile = infile.read()
                    print(readFile)
                    endingInput = input('Please respond with a corresponding number:')
                if endingInput == "2":
                    print('You entered the kitchen, press e to enter the entryway')
                    eForenter = input()
                    if eForenter == "e":
                        print('You entered the entryway. Press b to enter the bedroom.')
                        bForenter = input()
                        if bForenter == "b":
                            path = 'finalbedroom.txt'
                            infile = open(path, 'r')

                            readfile = infile.read()
                            print(readFile)
                            chestOpen = True

                            if chestOpen == True:
                               path = 'successfulending.txt'
                               infile = open(path, 'r')

                               readFile = infile.read()
                               print(readFile)
                               

                    


# Hey Tim, here's my notes for what happeened. So, I think I messed something up with the keywords for the bedroom. It still technically functions, but I don't know the rythme nor the reason
#The main path works of 112 and the rest. I hope. I made the game even more linear.
#I spent the better half of the last week trying to correctly use while loops. I seemingly couldn't make it work consistently, and I guess decided to not ask. I ended up just repeating the options by using if, elif, and else statements. I don't know if that was
#the only way to do it with our options or if I unnecessarily made my process of creation even longer. I think a lot of my issues came between this and my intentation issues, I would love to solve these issues however, I've exhausted my understanding of while loops, for loops,
#and my taped on option of using if statements. I could continue rambling, but I don't think it's really providing insight to my chaos.
