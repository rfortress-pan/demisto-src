import os
import sys
import json


DEV_PATH = sys.argv[1]
SITES_FILE = sys.argv[2]
ARGS = sys.argv[3:]

GREEN = '\033[92m'
END = '\033[0m'


def yes_no(question, default='yes'):
    '''Ask a yes/no question via raw_input() and return their answer.

    'question' is a string that is presented to the user.
    'default' is the presumed answer if the user just hits <Enter>.
            It must be 'yes' (the default), 'no' or None (meaning
            an answer is required of the user).

    The 'answer' return value is True for 'yes' or False for 'no'.
    '''
    valid = {'yes': True, 'y': True, 'ye': True, 'no': False, 'n': False}
    if default is None:
        prompt = ' [y/n] '
    elif default == 'yes':
        prompt = ' [Y/n] '
    elif default == 'no':
        prompt = ' [y/N] '
    else:
        raise ValueError(f'invalid default answer: "{default}"')

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write('Please respond with "yes" or "no" ' '(or "y" or "n").\n')


# Import inquirer
try:
  import inquirer

# If it doesn't exist, install it
except:
    if yes_no(f'\n\nThe {GREEN}"inquirer"{END} package is not installed and is required for this script.\n\nWould you like to install it?'):
        from pip._internal import main as pipmain
        pipmain(['install', 'inquirer'])

        import inquirer

    else:
        print('Cannot continue without the inquirer package.')
        sys.exit(0)

from inquirer.themes import GreenPassion


def read_sites():
    # Read the SITES_FILE with all of the XSOAR instance environment details
    if os.path.isfile(os.path.join(DEV_PATH, SITES_FILE)) is False:
        write_sites({})
        return {}

    with open(os.path.join(DEV_PATH, SITES_FILE), 'r') as data:
        sites = json.load(data)

    if sites == '':
        return {}

    return sites


def write_sites(data):
    with open(os.path.join(DEV_PATH, SITES_FILE), 'w') as f:
        f.write(json.dumps(data, indent=4))


def list_sites(sites):
    # Prompt the user for which XSOAR instance to use
    questions = [
        inquirer.List('selection',
            message='Select an XSOAR instance',
            choices=sites.keys(),
        ),
    ]
    answers = inquirer.prompt(questions, theme=GreenPassion())
    return answers['selection']


def add_environment():
    sites = read_sites()

    questions = [
        inquirer.List('version',
            message="Which version?",
            choices=['XSOAR 8', 'XSOAR 6'],
        ),
    ]
    version = inquirer.prompt(questions, theme=GreenPassion())
    version = int(version['version'][-1])

    print(f'!!! {version}')

    questions = [
      inquirer.Text('name', message="Enter Instance Name"),
      inquirer.Text('url', message="Enter API URL"),
      inquirer.Text('key', message="Enter API Key")
    ]
    if version == 8:
        questions.append(inquirer.Text('id', message="Enter API ID"))
    answers = inquirer.prompt(questions, theme=GreenPassion())

    api_name = answers['name']
    api_url = answers['url']
    api_key = answers['key']
    api_id = answers['id'] if version == 8 else None

    if api_name in sites:
        print('\n\nSite name already exsists. Try again.')
        add_environment()

    else:
        sites[api_name] = {
            'url': api_url,
            'key': api_key
        }
        if version == 8:
            sites[api_name]['id'] = api_id

    write_sites(sites)

    set_environment(api_name)


def rem_environment():
    sites = read_sites()
    environment = list_sites(sites)
    print(environment)
    if yes_no(f'Are you sure you want to remove {GREEN}{environment}{END}?', 'no'):
        api_url = sites[environment]['url']
        del sites[environment]
        write_sites(sites)
        print(f'\nRemoved {GREEN}{api_url}{END}.\n')

    else:
        print('\nNo changes made.\n')


def set_environment(environment=None):
    sites = read_sites()
    if sites == {}:
        print(f'No environments exist. Use {GREEN}demisto-sdk add{END} to add a site.\n')
        sys.exit()


    if environment is None:
        environment = list_sites(sites)

    # Grab the url and key for the selected XSOAR instance
    api_url = sites[environment]['url']
    api_key = sites[environment]['key']
    api_id = None

    # Support for XSOAR 8
    if 'id' in sites[environment]:
        api_url = f'{api_url}/xsoar'
        api_id = sites[environment]['id']

    # Save the environment variables so the bash script can source them
    with open(os.path.join(DEV_PATH, 'tmp.env'), 'w') as f:
        f.write(f'export DEMISTO_BASE_URL="{api_url}"\n')
        f.write(f'export DEMISTO_API_KEY="{api_key}"\n')

        # Support for XSOAR 8
        if api_id is None:
            f.write(f'unset XSIAM_AUTH_ID')
        else:
            f.write(f'export XSIAM_AUTH_ID="{api_id}"')


def main():
    if len(ARGS) == 0:
        set_environment(None)

    else:
        if ARGS[0] == 'add':
            add_environment()

        # Use 'del', 'rem', 'delete', or 'remove'
        if ARGS[0][:3] in ['del', 'rem']:
            rem_environment()

        # Use 'det' or 'details'
        if ARGS[0][:3] == 'det':
            print(f'API URL: {GREEN}{os.environ["DEMISTO_BASE_URL"]}{END}')
            print(f'API Key: {GREEN}{os.environ["DEMISTO_API_KEY"]}{END}')
            print(f'API ID:  {GREEN}{os.environ["XSIAM_AUTH_ID"]}{END}\n')


main()