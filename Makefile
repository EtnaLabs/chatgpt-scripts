gpt-update-filepaths:
    # Update .py files
    find . -name "*.py" ! -name "__init__.py" -exec sh -c 'grep -q "# $(echo $$0 | sed "s|^\./||")" $$0 || sed -i "" -e "1i\\
    # $(echo $$0 | sed "s|^\./||")\\
    " $$0' {} \;

    # Update javascript / typescript files
    find . -name "*.js" -or -name "*.ts" -or -name "*.tsx" ! -name "__init__.js" -exec sh -c 'head -n1 $$0 | grep -q "^//" && echo "Skipping $$0, already has a comment" || (printf "// $(echo $$0 | sed "s|^\./||")\n\n"; cat $$0) > $$0.tmp && mv $$0.tmp $$0' {} \;


gpt-context:
    # Check if it's a poetry project
    if [ -f pyproject.toml ]; then \
        echo "Running poetry project commands..."; \
        echo -e "Project tree: \n$$(tree -L 2 ./src)" > temp.txt; \
        echo -e "\nPackages: \n$$(cat pyproject.toml)" >> temp.txt; \
        pbcopy < temp.txt; \
        rm temp.txt; \
        echo "Copied to clipboard, now you can paste this in ChatGPT!"; \
    # Check if it's a nodejs project
    elif [ -f package.json ]; then \
        echo "Running nodejs project commands..."; \
        echo -e "Project tree: \n$$(tree -L 2 ./src)" > temp.txt; \
        echo -e "\nPackages: \n$$(cat package.json)" >> temp.txt; \
        pbcopy < temp.txt; \
        rm temp.txt; \
        echo "Copied to clipboard, now you can paste this in ChatGPT!"; \
    else \
        echo "Neither poetry nor nodejs project found."; \
    fi


.PHONY: gpt-update-filepaths gpt-context