### tinylispy

The tiny lisp interpreter written by python3

#### usage example
```
$ python3 tinylispy/main.py
tinylispy>>> (define a 100)
NIL
tinylispy>>> a
NUMBER:100
tinylispy>>> (add a 200)
NUMBER:300
tinylispy>>> (if true (sub 3 4) (div 5 6))
NUMBER:-1
tinylispy>>> ((lambda (x y) (add x y)) 10 20)
NUMBER:30
tinylispy>>> (define counter ((lambda (x) (lambda () (update x (add x 1)) x)) 0))
NIL
tinylispy>>> (counter)
NUMBER:1
tinylispy>>> (counter)
NUMBER:2
tinylispy>>> (counter)
NUMBER:3
```

#### dev commands
```
# unit tests
$ nosetests -sv
```

#### todo
- macro
