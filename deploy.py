import subprocess
import os

commands = [
    "npm run docs:build",
    "cd docs/.vuepress/dist",
    "git init",
    "git add -A",
    r'git commit -m "deploy"',
    "git push -f git@github.com:Asteryond/Asteryond.github.io.git master:notes_page"
]

for command in commands:
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    print(output.decode())


