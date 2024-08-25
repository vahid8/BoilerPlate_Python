import argparse #import package
# functions definition
def get_user_input_arguments():
    """ To get user input values for ip address , port """

    my_parser = argparse.ArgumentParser()

    my_parser.add_argument('--port', action='store', type=int, default="5566", help='port number')
    my_parser.add_argument('--ip', action='store', type=str,default="0.0.0.0", help= 'ip address')

    args = my_parser.parse_args()

    return args.ip, int(args.port)


if __name__ == '__main__':

    ip, port = get_user_input_arguments()
