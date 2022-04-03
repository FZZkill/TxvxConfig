# README-English about Txvx config manager
# 支持中文版本的README，贼TM接地气
<p><a href="./README_CN.MD">README-Chinese</a></p>
## What is?
It is a config manager
#### What can it do?
It can set config, read config, get config and create a config
## How to use it?
### 1,Install
#### Linux/Unix
Install python 3.9(If you use an earlier version, I cannot guarantee that this broken thing will work)
`pip install txvx`
####Windows
Address:)

### 2,Use
In you python code, write 'import txvx' <br>
and new a object
so...... <br>

    import txvx
    
    Txvx = txvx.run(FilePath)

### 3,Functions

| Functions  | Use             | Do                                                  |
|------------|-----------------|-----------------------------------------------------|
| get()      | get(var)        | get Config File {var} value                         |
| set()      | set(var, value) | set Config File {var} value                         |
| create()   | create()        | Create a new Config File(If it existed would erase) |
| add()      | add(var, vaule) | add a new config vaule                              |
| remove()   | remove(var)     | delete vaule and return the config vaule            |
| save()     | save()          | save infomation from RAM                            |
| show()     | show()          | return all registered vaule                         |
| showType() | showType()      | return now Type                                     |
| new()      | new(List)       | Look Last!                                          |
### 4,TxvxFile

Usually, Its name is 'xxx.txvx'<br>
Whatis in this file?for example

    example = 5
    example1 = Hello, World
    Writer = FZZkill

### The "new()" can before replacing the parameter

### 5,Important
If you choose infomation,Please use 'save()'!.This important

Date invaluable exercise caution

### Last

How to do new()<br>
    
    usage : now(List(need), Type(default = 2))

You can set Type '1' or '2'

    Type = 1 : ['xxx','xxx'] There can be only a couple
    Type = 2 : [['xxx1', 'xxx'],['xxx2', 'xxx']] 

How to provide a list of selected counting on you

### Last and Last(Let me say a few world on important business)
Writer: FZZkill<br>
Language: Python3.9<br>
Where: Github & Pypi
