import configparser















if __name__  == "__main__":
    config = configparser.ConfigParser()
    config['headers'] = {'user-agent': 'stevens student from bia 660'}

    with open('config.ini', 'w') as f:
        config.write(f)
