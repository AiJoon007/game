label path_test:
    call her_walk(action="enter")
    call cho_walk(action="enter")
    call her_walk("desk", "base", reduce="all")
    pause 0.5
    call cho_walk("desk", "base", reduce="all")
    $ complete_chibi_moves(hermione=1.1)

