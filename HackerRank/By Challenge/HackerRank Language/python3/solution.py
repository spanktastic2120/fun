# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
p = re.compile('^[\d]+\s(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$')
n = int(input())
for _ in range(n):
    print('VALID' if p.match(input()) else 'INVALID')
