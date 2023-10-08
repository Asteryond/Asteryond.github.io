# npm run docs:build

cd docs/.vuepress/dist

git init
git add -A
git commit -m "deploy"
git push -f git@github.com:Asteryond/Asteryond.github.io.git master:notes_page
