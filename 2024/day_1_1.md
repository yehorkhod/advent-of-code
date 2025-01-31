# This one will be in vim

Copy to q register ("qy"):
~~~
gg0f €ý5eGx:sortGopOVggx:sortOP}ddddGexggep}dG:%s/   /-Vgg:.!bc:%s/-/:%s/\n/+A€kb:.!bc
~~~

Run in input txt file:
~~~
@q
~~~

# Explanation

Start of the file:
~~~
gg 0
~~~

Remove second column:
~~~
f €ý5  e G x
~~~

Sort it:
~~~
:sort
~~~

Paste second column to the bottom
~~~
G o  p
~~~

Remove first column:
~~~
O  V gg x
~~~

Sort it:
~~~
:sort
~~~

Concatenate columns back
~~~
O  P } dd dd  G e x gg ep } d G
~~~

Change spaces with minuses:
~~~
:%s/   /-
~~~

Select all the lines and evaluate subtraction:
~~~
V gg :.!bc
~~~

Get absolute value by removing minuses:
~~~
:%s/-/
~~~

Change new lines with pluses:
~~~
:%s/\n/+
~~~

Remove plus in the end of the line:
~~~
A €kb 
~~~

Calculate the sum:
~~~
:.!bc
~~~
