#!/usr/bin/env python3
import shutil
import os
import sys
import configparser


# Global Variables
kleiPath = os.path.expanduser('~/Documents/Klei')

def CreateIniFile(dstFolder, serverName):
        # DEFAULT VALUES
        # GAMEPLAY
        gameMode = "survival"
        maxPlayers = 10
        pvp = "false"
        pauseEmpty = "true"

        # NETWORK
        clusterName = "My World"
        clusterDescription = "My Description"
        clusterPw = ""
        clusterIntention = "cooperative"
        autosave = "true"
        enableKick = "false"
        tickRate = 60

        # MISC
        maxSnapshots = 10
        console = "true"
        
        # SHARD
        shard = "true"
        bindIP = "127.0.0.1"
        masterIP = "127.0.0.1"
        masterPort = "10889"
        clusterKey = "dst"

        ####
        modify = 0
        while True:
                while True:
                        try:
                                modify = int(input("\nDo you wish to modify the ini file options?\n1-Yes\n2-No\n"))
                                break
                        except:
                                print("\nEnter a valid number!\n")
                if(modify !=1 and modify != 2):
                        print("\nPlease, choose either 1 or 2\n")
                else:
                        break         
        if(modify == 1):
                while True:
                        while True:
                                try:
                                        choice = int(input('\nSelect the game mode:\n1-Survival\n2-Wilderness\n3-Endless\n'))
                                        break
                                except:
                                        print("\nInput a valid number!\n")                
                        if(choice!=1 and choice!=2 and choice!=3):	
                                print('\nInput a valide choice!\n')
                        else:
                                break
                if(choice==1):
                        gameMode="survival"
                elif(choice==2):
                        gameMode="wilderness"
                else:
                        gameMode="endless"

                clusterName = ''
                clusterDescription = ''
                clusterPw = ''
                
                while(clusterName == ''):
                        clusterName = input('\nEnter the server name: ')
                while(clusterDescription == ''):
                        clusterDescription = input('\nEnter the server description: ')
                clusterPw = input('\nEnter the server password(empty for none): ')
                while True:
                        try:
                                tickRate = int(input('\nEnter the server tick(15, 30, 45, 60): '))
                        except:
                                print("\nEnter a valid number!\n")
                        if(tickRate != 15 and tickRate != 30 and tickRate != 45 and tickRate != 60):
                                print("\nEnter one of the 4 numbers told!\n")
                        else:
                                break
        
        config = configparser.ConfigParser()
        config['GAMEPLAY'] = {'game_mode': gameMode,
                              'max_players': maxPlayers,
                              'pvp': pvp,
                              'pause_when_empty': pauseEmpty
                              }
        config['NETWORK'] = {'cluster_name': clusterName,
                             'cluster_description': clusterDescription,
                             'cluster_password': clusterPw,
                             'cluster_intention': clusterIntention,
                             'autosaver_enabled': autosave,
                             'enable_vote_kick': enableKick,
                             'tick_rate': tickRate
                             }
        config['MISC'] = {'max_snapshots': maxSnapshots,
                          'console_enabled': console
                          }
        config['SHARD'] = {'shard_enabled': shard,
                           'bind_ip': bindIP,
                           'master_ip': masterIP,
                           'master_port': masterPort,
                           'cluster_key': clusterKey
                           }
        with open(os.path.join(kleiPath,dstFolder,serverName,"cluster.ini"), 'w+') as configFile:
                config.write(configFile)



def main():
    while True:
            serverName = ''
            while serverName == '':
                serverName = input('\nEnter the name of the server you wish to create a bat for: ')
            fileName = serverName + '.bat'

            isbeta=0
            while True:
                while True:
                        try:
                                isbeta = int(input('\nWhat kind of world will it be?\n1 - Normal World\n2 - Beta World\n'))
                                break
                        except:
                                print("\nEnter a valid number!\n")
                if(isbeta !=1 and isbeta !=2):
                        print("\nPlease, select either 1 or 2\n")
                else:
                        break
            if(isbeta==1):
                    dstFolder = "DoNotStarveTogether"
                    textToSave = 'c:\\steamcmd\\steamcmd.exe +login anonymous +app_update 343050 +quit\ncd /D "c:\\steamcmd\\steamapps\\common\\Don\'t Starve Together Dedicated Server\\bin64"\nstart dontstarve_dedicated_server_nullrenderer_x64 -console -cluster ' + serverName + ' -shard Master\nstart dontstarve_dedicated_server_nullrenderer_x64 -console -cluster ' + serverName + ' -shard Caves'
            elif(isbeta==2):
                    #dstFolder = "DoNotStarveTogetherReturnOfThemBeta"
                    dstFolder = "DoNotStarveTogetherBetaBranch"
                    textToSave = 'c:\\steamcmd\\steamcmd.exe +force_install_dir "c:\\steamcmd\\steamapps\\common\\DST Beta" +login anonymous +app_update 343050 -beta updatebeta +quit\ncd /D "c:\\steamcmd\\steamapps\\common\\DST Beta\\bin64"\nstart dontstarve_dedicated_server_nullrenderer_x64 -console -cluster ' + serverName + ' -shard Master\nstart dontstarve_dedicated_server_nullrenderer_x64 -console -cluster ' + serverName + ' -shard Caves'


            if os.path.isfile(os.path.join(kleiPath, fileName)):
                    print("\nThere's already a bat file with this name, so please choose another name\n")
            elif os.path.isdir(os.path.join(kleiPath, dstFolder, serverName)):
                    print("\nThere's already a folder with this name, so please choose another name\n")
            else:
                    break



    file = open(os.path.join(kleiPath, fileName), "w+")
    file.write(textToSave)
    file.close()
    worldtype = 0
    worldFolder = "DST_Worlds"
    #worldFolder = "Empty_Folder"
    dstWorlds = os.listdir(os.path.join(kleiPath, worldFolder))
    worldNames = ""
    worldNumber = 0
    print('\nSelect the type of world do you wish to create:\n')
    #print(dstWorlds)
    if(dstWorlds == []): # If there are no folders to copy, just exit the program
            print('\nThere are no world folders... Add some and then run this again, buddy\n')
            sys.exit()
    for f in dstWorlds:
            worldNumber+=1
            worldNames += str(worldNumber) + " - " + str(f) + '\n'        
    print(worldNames)
    #print('1 - DEFAULT_WORLD\n2 - EASY_WORLD\n3 - PERFECT_WORLD\n4 - BASIC_WORLD')
    #print(kleiPath)
    while True:
        while True:
                try:
                        worldtype = int(input())
                        break
                except:
                        print("\nPlease, enter a valid number!\n")
        if (worldtype <= 0 or worldtype > worldNumber):
                print("\nSelect a valid option!\n")
        else:
                break

            
    #print(dstWorlds[worldtype-1])

    shutil.copytree(os.path.join(kleiPath, worldFolder, dstWorlds[worldtype-1]), os.path.join(kleiPath, dstFolder, serverName)) 
    answer = 0
    while True:
        while True:
                try:
                        answer = int(input('\nDo you want to create a new cluster.ini file or just use the one in the folder?\n1 - Create new cluster.ini\n2 - Just use the one in the folder, whatever\n'))
                        break
                except:
                        print("\nPlease, enter a valid number\n")
        if answer == 1:
            CreateIniFile(dstFolder, serverName)
            input("\nWorld created successfully! Press enter to exit")
            break
        elif answer == 2:
            input("\nWorld created successfully! Press enter to exit")
            break
        else:
            print('\nJust answer 1 or 2, buddy\n')

if __name__ == "__main__":
    main()

