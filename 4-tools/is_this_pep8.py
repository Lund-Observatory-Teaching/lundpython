a = "This code is not PEP 8 compliant! Not only will pycodestyle get very upset, it will make sure you will be upset too."
for sentence in a.split("! "):
    print(
        sentence, end="\n\n"
    )  # Notice how the Python interpreter does not require 4 space indents
