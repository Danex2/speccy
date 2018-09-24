## Speccy

A bot that let's discord users show off their custom pc builds with pcpartpicker

## How to run on on your own

1. clone this repo with `git clone https://github.com/Danex2/speccy.git` and install the packages in the requirements.txt
2. add a `users.db` file to the root of your project  
3. add a ``token.json`` to the root of your project and add this to it  
```{
    "token":"your token here"
}```
4. run the bot

or with docker  
1. ``docker build -t speccy .``  
2. ``docker run speccy``