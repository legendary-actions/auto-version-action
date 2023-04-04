import subprocess

def update_tag(last_tag, amount=1):
    parts = last_tag.split(".")
    patch_version = int(parts.pop())
    patch_version += amount
    parts.append(str(patch_version))
    return ".".join(parts)

last_tag_cmd = subprocess.run(['git', 'describe', '--tags', '--abbrev=0'], stdout=subprocess.PIPE)
last_tag = last_tag_cmd.stdout.decode("utf-8")
last_tag = last_tag.replace("\n", "")
amount_since_last = subprocess.run(['git', 'rev-list', f'{last_tag}..HEAD', '--count'], stdout=subprocess.PIPE).stdout.decode('utf-8').replace("\n", "")
current_branch = subprocess.run(['git', 'branch', '--show-current'], stdout=subprocess.PIPE).stdout.decode('utf-8').replace("\n", "")

if current_branch != "master":
    print("version=" + current_branch.replace('/', '-'))
else:
    print("version=" + update_tag(last_tag, int(amount_since_last)))
