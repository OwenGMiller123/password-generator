import passgen as pg
import writejson as wj
import os


###>>>    ,------.                       ,--. ,--.  ,--.  ,--.,--.    <<<###
###>>>    |  .--. ' ,--,--. ,---.  ,---. |  | |  |,-'  '-.`--'|  |    <<<###
###>>>    |  '--' |' ,-.  |(  .-' (  .-' |  | |  |'-.  .-',--.|  |    <<<###
###>>>    |  | --' \ '-'  |.-'  `).-'  `)'  '-'  '  |  |  |  ||  |    <<<###
###>>>    `--'      `--`--'`----' `----'  `-----'   `--'  `--'`--'    <<<###
def command_repeat(continue_query):
    while continue_query == 'Y' or 'N':
        if continue_query == 'Y':
            command_cont = True
            return command_cont
        elif continue_query == 'N':
            command_cont = False
            return command_cont
        else:
            continue_query = input('Command not recognized; please enter \'Y\' or \'N\': ').upper()


if __name__ == '__main__':
    quit_util = False
    print('\n~Welcome to PassUtil~\n')

    print('Type \'help\' and hit Enter for the full command list.')

    folder_path = ''
    file_path = ''
    while quit_util is False:
        print('')
        user_command = input('Enter Your Command: ')
        print('')

        ###>>>                             <<<###
        ###>>> PASSWORD .TXT FILE COMMANDS <<<###
        ###>>>                             <<<###
        if user_command == 'help':
            print('\n☆ﾟ.*･｡ﾟCommand List☆ﾟ.*･｡ﾟ\n')
            print('>>> gen p ---> Creates a new password list and dumps that list to a .txt file.')
            print('>>> pt all p ---> Prints all the passwords from the password .txt file you have generated.')
            print('>>> w json ---> Writes data to .json file. If a file does not exist, prompts for a file/folder name '
                  'and creates it.')
            print('>>> get p by ind ---> Prints the passwords from .txt within a user-specified range.')
            print('>>> spice p ---> Adds user-specified characters to all passwords in a .txt file.')
            print('>>> trim p ---> Removes user-specified characters from all passwords in a .txt file.')
            print('>>> dir name ---> Gets a directory name for managing folders.')
            print('>>> mk dir ---> Creates a new directory based on the dir name.')
            print('>>> del dir ---> Deletes a specified directory and all files inside that directory.')
            print('>>> del p ---> Deletes a specified file.')
            print('>>> file name ---> Gets a file name for creating files and retrieving file data.')
            print('>>> get pswds list ---> Retrieves and prints a password from your randomly generated .txt file.')
            print('>>> quit ---> Quits the program.\n')

        if user_command == 'gen p':
            comm_cont = True
            while comm_cont is True:
                user_input = input('Please enter a name for your new file: ') + '.txt'
                if user_input == 'exit.txt':
                    while user_input == 'exit.txt':
                        user_input = input('This name will interfere with utility functionality. '
                                           'Please choose another: ')
                new_password_list = pg.generate_passwords_auto()
                pg.create_txt_dump(new_password_list, user_input)
                cont_reply = input('Would you like to generate another password list? (Y/N): ').upper()
                new_password_list = []
                comm_cont = command_repeat(cont_reply)

        if user_command == 'pt all p':
            comm_cont = True
            while comm_cont is True:
                user_input = input('Please enter your .txt password filename. Type \'exit\' to quit: ') + '.txt'
                if os.path.exists(user_input) is True:
                    print(user_input + '\n')
                    retrieved_list = pg.retrieve_txt_dump(user_input)
                    for st in retrieved_list:
                        print(st)
                    print('')
                    cont_reply = input('Would you like to retrieve another full password list? (Y/N): ').upper()
                    comm_cont = command_repeat(cont_reply)
                elif os.path.exists(user_input) is False and user_input == 'exit.txt':
                    print('Exiting Command...')
                    comm_cont = False
                else:
                    print('File name not recognized. Please check to ensure file exists. '
                          'Input \'exit\' or an hit \'Enter\' to quit.')

        if user_command == 'get p by ind':
            comm_cont = True
            while comm_cont is True:
                user_input = input('Please enter your .txt file name: ') + '.txt'
                if os.path.exists(user_input) is True:
                    retrieved_list = pg.retrieve_txt_dump(user_input)
                    pg.retrieve_password_by_index(retrieved_list)
                    cont_reply = input('Would you like to retrieve additional passwords? (Y/N): ').upper()
                    comm_cont = command_repeat(cont_reply)
                elif os.path.exists(user_input) is False and user_input == 'exit.txt':
                    print('Exiting Command...')
                    comm_cont = False
                else:
                    print('File name not recognized. Please check to ensure file exists.')

        if user_command == 'spice p':
            comm_cont = True
            while comm_cont is True:
                user_input = input('Please enter the password file name you would like to spice: ') + '.txt'
                if os.path.exists(user_input) is True:
                    password_list = pg.retrieve_txt_dump(user_input)
                    spiced_list = pg.spice_passwords(password_list)
                    pg.create_txt_dump(spiced_list, user_input)
                    cont_reply = input('Would you like to add additional spice to a password file? (Y/N): ').upper()
                    comm_cont = command_repeat(cont_reply)
                elif os.path.exists(user_input) is False and user_input == 'exit.txt':
                    print('Exiting Command...')
                    comm_cont = False
                else:
                    print('File name not recognized. Please check to ensure file exists.')

        if user_command == 'trim p':
            comm_cont = True
            while comm_cont is True:
                user_input = input('Please enter the password file name you would like to trim: ') + '.txt'
                if os.path.exists(user_input) is True:
                    password_list = pg.retrieve_txt_dump(user_input)
                    trimmed_list = pg.trim_passwords(password_list)
                    pg.create_txt_dump(trimmed_list, user_input)
                    cont_reply = input('Would you like to trim more characters from a password file? (Y/N): ').upper()
                    comm_cont = command_repeat(cont_reply)
                elif os.path.exists(user_input) is False and user_input == 'exit.txt':
                    print('Exiting Command...')
                    comm_cont = False
                else:
                    print('File name not recognized. Please check to ensure file exists.')

        if user_command == 'w json':
            comm_cont = True
            while comm_cont is True:

                folder_path = wj.get_folder_name()
                file_path = wj.get_file_name(folder_path)
                print('\nFile Path: ' + file_path + '\n')
                wj.check_for_file(folder_path, file_path)

                add_cont = True
                while add_cont is True:
                    add_query = input('\nWould you like to add password entries to this file? (Y/N): ').upper()
                    if add_query == 'Y':
                        wj.add_json_entry(file_path)
                    elif add_query == 'N':
                        add_cont = False
                    else:
                        print('Command not recognized. Please enter Y for yes, or N for no.')

                cont_reply = input('Would you like to create more directories and files? (Y/N): ').upper()
                print('')

                comm_cont = command_repeat(cont_reply)

        if user_command == 'dir name':
            folder_path = wj.get_folder_name()

        if user_command == 'mk dir':
            mk_folder = input('Enter the name of the folder you would like to create: ')
            wj.create_folder(folder_path)
            print('')

        if user_command == 'get json':
            json_folder_path = wj.get_folder_name()
            json_file_path = wj.get_file_name(json_folder_path)

        if user_command == 'del dir':
            del_dir = input('Enter the name of the directory you would like to delete: ')
            wj.delete_folder(del_dir)

        if user_command == 'del p':
            del_txt = input('Enter the name of the .txt file you would like to delete: ') + '.txt'
            wj.delete_file(del_txt)

        if user_command == 'file name':
            folder_path = wj.get_folder_name()
            file_path = wj.get_file_name(folder_path)

        if user_command == 'quit':
            quit_util = True
            
        # print('Command does not exist. Type \'help\' to return the full command list.\n')
        
    print('Operations Complete. Goodbye!')
