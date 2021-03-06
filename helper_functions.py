def get_build_folder(temp_filename: str):
    build_folder = temp_filename[:temp_filename.rfind('/')]
    return build_folder


def get_build_number(temp_filename: str):
    build_folder = get_build_folder(temp_filename)
    build_number = build_folder[:build_folder.find('_')]
    build_number = build_number[(build_number.rfind('/') + 1):]
    return build_number


def get_build_folder_name(temp_filename: str):
    build_folder = get_build_folder(temp_filename)
    build_folder_name = build_folder[:build_folder.rfind('/')]
    build_folder_name = build_folder_name[build_folder_name.rfind('/') + 1:]
    return build_folder_name


def printProgressBar(iteration,
                     total,
                     prefix='',
                     suffix='',
                     decimals=1,
                     length=40,
                     fill='█',
                     printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(
        100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print('\n')


def get_description_dict():
    desc_dict = {}
    desc_filename = 'descriptions.txt'
    with open(desc_filename) as desc_file:
        for line in desc_file:
            split_line = line.split('-', 1)
            (key, value) = split_line
            desc_dict[key] = value

    return desc_dict