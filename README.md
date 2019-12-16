# Brainfuxck
a Brainfuck interputer written in Python

### Brainfuck简介

>Brainfuck是一种简单的、图灵完备的语言，只包含8种字符， Daniel B Cristofani 仅仅用429个字符就用Brainfuck实现了Brainfuck的编译器[A Very Short Self-Interpreter](https://arxiv.org/abs/cs/0311032v1)
>这种语言基于一个简单的机器模型，除了指令，这个机器还包括：一个以字节为单位、被初始化为零的数组、一个指向该数组的指针（初始时指向数组的第一个字节）、以及用于输入输出的两个字节流。

|字符|含义|
|---|---|
|>|指针加一|
|<|指针减一|
|+|指针指向的字节的值加一|
|-|指针指向的字节的值减一|
|.|输出指针指向的单元内容（ASCⅡ码）|
|,|输入内容到指针指向的单元（ASCⅡ码）|
|[|如果指针指向的单元值为零，向后跳转到对应的]指令的次一指令处|
|]|如果指针指向的单元值不为零，向前跳转到对应的[指令的次一指令处|


### usage
bf.py
```
code='Your code'
bf = BF(code)
bf.run()
```
