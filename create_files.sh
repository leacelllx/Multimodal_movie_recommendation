#!/bin/bash

# Define an array of paths for placeholder files
declare -a files=(
    "README.md"
    "requirements.txt"
    "data/raw/.gitkeep"
    "data/processed/.gitkeep"
    "src/data_preprocessing/.gitkeep"
    "src/models/.gitkeep"
    "src/multimodal_rag/.gitkeep"
    "src/ui/.gitkeep"
    "src/utils/.gitkeep"
    "notebooks/data_exploration.ipynb"
    "notebooks/model_finetuning.ipynb"
    "notebooks/multimodal_testing.ipynb"
    "tests/.gitkeep"
    "docker/.gitkeep"
    "deployment/.gitkeep"
)

# Iterate through the files array and create them
for file in "${files[@]}"; do
    if [ ! -f "$file" ]; then
        touch "$file"
        echo "Created: $file"
    else
        echo "File already exists: $file"
    fi
done

# Add content to README.md if it's empty
if [ -f "README.md" ] && [ ! -s "README.md" ]; then
    echo "# Multimodal_movie_recommendation" > "README.md"
    echo "An advanced project for multimodal movie recommendations." >> "README.md"
    echo "Added content to README.md"
fi

echo "File creation process completed."
