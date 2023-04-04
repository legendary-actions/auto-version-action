import subprocess

def update_tag(last_tag, amount=1):
    parts = last_tag.split(".")
    patch_version = int(parts.pop())
    patch_version += amount
    parts.append(str(patch_version))
    return ".".join(parts)

last_tag = subprocess.run(['git', 'describe', '--tags', '--abbrev=0'], stdout=subprocess.PIPE)
amount_since_last = subprocess.run(['git', 'rev-list', f'{last_tag.stdout.decode("utf-8")}..HEAD', '--count'], stdout=subprocess.PIPE).stdout.decode('utf-8')
current_branch = subprocess.run(['git', 'branch', '--show-current'], stdout=subprocess.PIPE).stdout.decode('utf-8')

if current_branch != "master":
    print(current_branch.replace('/', '-'))
else:
    print(update_tag(last_tag, int(amount_since_last)))
