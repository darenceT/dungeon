from clear_screen import ClearScreen
from datetime import date

class Art:

    @staticmethod
    def intro():
        """
        Display art at beggining of game before menu
        Credit to https://patorjk.com/software/taag
        """
        ClearScreen()
        print(
            '\n ▓█████▄  █    ██  ███▄    █   ▄████ ▓█████  ▒█████   ███▄    █ \n'
            ' ▒██▀ ██▌ ██  ▓██▒ ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▒██▒  ██▒ ██ ▀█   █ \n'
            ' ░██   █▌▓██  ▒██░▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▒██░  ██▒▓██  ▀█ ██▒\n'
            ' ░▓█▄   ▌▓▓█  ░██░▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██   ██░▓██▒  ▐▌██▒\n'
            ' ░▒████▓ ▒▒█████▓ ▒██░   ▓██░░▒▓███▀▒░▒████▒░ ████▓▒░▒██░   ▓██░\n'
            ' ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ \n'
            ' ░ ▒  ▒ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░ ▒ ▒░ ░ ░░   ░ ▒░\n'
            ' ░ ░  ░  ░░░ ░ ░    ░   ░ ░ ░ ░   ░    ░   ░ ░ ░ ▒     ░   ░ ░\n' 
            ' ░       ░              ░       ░    ░  ░    ░ ░           ░ \n'
            ' ▄████▄  ██▀███  ▄▄▄       █     █░ ██▓    ▓█████  ██▀███    \n'
            ' ▒██▀ ▀█ ▓██ ▒ ██▒████▄    ▓█░ █ ░█░▓██▒    ▓█   ▀ ▓██ ▒ ██▒ \n'
            ' ▒▓█    ▄▓██ ░▄█ ▒██  ▀█▄  ▒█░ █ ░█ ▒██░    ▒███   ▓██ ░▄█ ▒ \n'
            ' ▒▓▓▄ ▄██▒██▀▀█▄ ░██▄▄▄▄██ ░█░ █ ░█ ▒██░    ▒▓█  ▄ ▒██▀▀█▄  \n'
            ' ▒ ▓███▀ ░██▓ ▒██▒▓█   ▓██▒░░██▒██▓ ░██████▒░▒████▒░██▓ ▒██▒\n'
            ' ░ ░▒ ▒  ░ ▒▓ ░▒▓░▒▒   ▓▒█░░ ▓░▒ ▒  ░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░\n' 
            ' ░  ▒    ░▒ ░ ▒░ ▒   ▒▒ ░  ▒ ░ ░  ░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░ \n'
            ' ░         ░░   ░  ░   ▒     ░   ░    ░ ░      ░     ░░   ░\n' 
            ' ░ ░        ░          ░  ░    ░        ░  ░   ░  ░   ░\n'
            '          Run in Terminal/CMD for best experience!')
        input('\n              Press Enter to return to menu')

    def in_game():
        """
        Display art at top of screen during game. Added by Darence
        Credit to https://patorjk.com/software/taag
        """
        spaces ='              ' 
        stars = '************'
        ClearScreen()
        print(
            f'\n{spaces}+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+\n'
            f' {stars} |D|u|n|g|e|o|n| |C|r|a|w|l|e|r| {stars}\n'
            f'{spaces}+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+\n\n')

    def pillar(letter):
        """
        Display art when obtaining each pillar key. Added by Darence
        Credit to https://www.asciiart.eu/logos/caduceus
        """
        if letter == 'A':
            print(
                '                            .-.\n'
                '                      ___  ( A )  ___\n'
                '                 ,_.-\'   `\'-| |-\'`   \'-._,\n'
                '                  \'.      .-| |-.      .\'\n'
                '                    `~~~~`  |.\') `~~~~` \n'
                '                           (_.|\n'
                '                            |._)\n'
                '                            |.\')\n'
                '                           (_.|\n'
                '                            |._)\n'
                '                           (\'.|\n'
                '                            |._)\n'
                '                     jgs    \'-\'\n')
        elif letter == 'E':
            print(
                '                             _\n'
                '                     _____ ( E )  _____\n'
                '                    vVVVVV\__|__/VVVVVv\n'  
                '                   vVVVVVVvvv|vvvVVVVVVv\n'
                '                  vVVVV      |      VVVVv\n'
                '                 vVVV        | >=.   VVVv\n'
                '                 vVV         |____)   VVv\n'
                '                 v          (|          v\n'
                '                             |)\n'
                '                            (|\n'  
                '                             |)\n'
                '                            (|\n' 
                '                             |`\n'
                '                ejm          |\n')
        elif letter == 'I':
            print(
                '                       _____  _  _____\n'
                '                      (___  \(I)/  ___)\n'
                '                        (___ | | ___)\n'
                '                         /")`| |\'("\ \n'
                '                        | |  | |  | |\n'
                '                         \ \_| |_/ /\n'
                '                          `._!\' _.\'\n'
                '                            / .\'\ \n'
                '                           | / | |\n'
                '                            \|/ /\n'
                '                             /.<\n'
                '                            (| |)\n'
                '                             | \'\n'
                '                             | |\n'
                '                             `-\'\n')
        elif letter == 'P':
            print(
                '                             _\n'
                '                  _..._    /` `\    _..._\n'
                '                .\'     \'. |  P  | .\'     \'.\n'
                '          ,    /         \'.\   /.\'         \    ,\n'
                '          \`--\'  .--.    .-.> <.-.    .--.  \'--`/\n'
                '           \'.__.\'    \'._/ ^ ) ( ^ \_.\'    \'.__.\'\n'
                '                       |  |`| |`|  |\n'
                '                       \  \ | | /  /\n'
                '                        \'. \'; ;\' .\'\n'
                '                          \'. \' .\'\n'
                '                          /  /` \ \n'
                '                         |  | |  |\n'
                '                          \ \ / /\n'
                '                           \'.\'.\'\n'
                '                     jgs   / / \ \n'
                '                          / / \ \ \n'
                '                         | /| |\ |\n'
                '                         \/ | | \/\n'
                '                            \_/\n')
        print('  You see a shiny button and you are tempted to push it...')

    def lose(name):
        """
        Graphic for losing game, displays user's name and today's date, added by Darence
        Credit https://ascii.co.uk/art/rip
        """
        name = '{0: ^19}'.format(name)
        today = '{0: ^10}'.format(str(date.today()))
        print(
             '                   _____  _____\n'
             '                  <     `/     |\n'
             '                   >  _     _ (\n'
             '                  |  |_) | |_) |\n'
             '                  |  | \ | |   |\n'
             '                  |            |\n'
             '     _____._____%_|            |_______  _____\n'
             '   _/                                    \|   |\n'
             f'  |             {name}           <\'\n'
             '  |____.-.________             ____/|_________|\n'
             f'                  | {today} |\n'
             '                  |            |\n'
             '                  |            |\n'
             '                  |   _        <\n'
             '                  |__/         |\n'
             '                   / `--.      |\n'
             '               .%%|          -< @%%%\n'
             '               %`@|     v      |@@%@%%    - mfj\n'
             '           .%%%@@@|%    |    % @@@%%@%%%%\n\n'
             '              Your health reached 0!\n\n' 
             '                 ** GAME OVER **\n')
    
    @staticmethod
    def win(name):
        """
        Added by Pranav, edited by Darence
        Credit https://ascii.co.uk/art/doors
        """
        spaces = '                      '
        print(
            f'{spaces}    /|\n'
            f'{spaces}   / |\n'
            f'{spaces}  /  | \n'
            f'{spaces} /_ _|_ _ _ _ __\n'
            f'{spaces}|               |\n'
            f'{spaces}|   __________  |\n'
            f'{spaces}|  |   |   |  | |\n'
            f'{spaces}|  |-+-|-+-|-+| |\n'
            f'{spaces}|  |   |   |  | |\n'
            f'{spaces}|   ----------  |\n'               
            f'{spaces}|               |\n'
            f'{spaces}|   _______     |\n'
            f'{spaces}|  |A ▄ ▄ E| () |\n'
            f'{spaces}|  |I ▄ ▄ P| || |\n'
            f'{spaces}|   -------  () |\n'
            f'{spaces}|               |\n'
            f'{spaces}|               |\n'
            f'{spaces}|               |\n'
            f'{spaces}|_ _ _ _ _ _ _ _|\n\n'
            '  You have successfully collected all 4 pillars!\n'
            f'  Congratulations {name}, you successfully escaped the dungeon!')
