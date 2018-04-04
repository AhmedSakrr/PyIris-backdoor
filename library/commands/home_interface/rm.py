import library.modules.config as config

config.main()

def main(command):
    try:
        list_type = command.split(' ')[1]
        hostname =  command.split(' ',2)[2]
        if list_type == 'wh':
            config.white_list.remove(hostname)
            print '[+]Removed from whitelist'
        elif list_type == 'bl':
            config.black_list.remove(hostname)
            print '[+]Removed from blacklist'
        else:
            raise IndexError
    except IndexError:
        print '[-]Please specify a valid list and a hostname to remove from a list'
    except ValueError:
        print '[-]Item user wants to remove does not exist'