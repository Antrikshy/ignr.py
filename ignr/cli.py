import argparse, os, sys
import gitignoreio_api as api

parser = argparse.ArgumentParser()

# Accept list instruction, search instruction, OR create instruction
task = parser.add_mutually_exclusive_group(required=True)
task.add_argument('--list', '-l', action='store_true', help='list all available .gitignore templates')
task.add_argument('--search', '-s', dest='s_term', metavar='TECH', help='search for term in list of available templates')
task.add_argument('--new', '-n', dest='n_stack', metavar='TECH', nargs='+', help='space-separated technologies - "macOS Node Sass"')
task.add_argument('--preview', '-p', dest='p_stack', metavar='TECH', nargs='+', help='preview for space-separated technologies')

args = parser.parse_args()

# --list or --search
if args.list or args.s_term:
    template_list = api.get_template_list()

    if args.list:
        print '\n'.join(template_list)
    
    if args.s_term:
        for template in template_list:
            if args.s_term.lower() in template.lower():
                print template

    sys.exit(0)

# --new or --preview
else:
    preview_needed = args.p_stack is not None
    gi_stack = args.p_stack or args.n_stack

    # Catch error raised by api and report
    try:
        ignr_file = api.get_gitignore(gi_stack)
    except ValueError as ve:
        print "ERROR: " + ve.args[0] + " is invalid or is not supported on gitignore.io."
        sys.exit(1)

    # Add signature
    ignr_file = "{0}\n{1}\n".format(ignr_file, "# Generated using ignr.py - github.com/Antrikshy/ignr.py")

    # Just preview
    if preview_needed:
        print ignr_file

    # Write to file
    else:
        # .gitignore already exists
        if os.path.isfile('.gitignore'):
            overwrite = None

            while (True):
                choice = raw_input(".gitignore exists in current directory. Continue?\n[backup (b) / overwrite (o) / cancel (c)] ").lower()
                if choice in ['o', 'overwrite']:
                    break
                elif choice in ['b', 'backup']:
                    print "Backing up .gitignore as 'OLD_gitignore'..."
                    os.rename('.gitignore', 'OLD_gitignore')
                    break
                elif choice in ['c', 'cancel']:
                    print "Ok. Exiting..."
                    sys.exit(0)
                else:
                   print "Please respond with 'b', 'o' or 'c'."

        with open('.gitignore', 'w') as f:
            f.write(ignr_file)

        print "New .gitignore file generated for " + ", ".join(gi_stack) + "."

sys.exit(0)
