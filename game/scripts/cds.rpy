python early:
    def parse_chibi(l):
        who = l.simple_expression()
        action = l.simple_expression()

        return (who, action)

    def execute_chibi(p):
        print(f"{p}")
        who, action = p
        func = eval(f"{who}_chibi.{action}")

        # print(f"Execution: {who} {action}")

    def lint_chibi(p):
        who, action = p
        try:
            chibi = eval(f"{who}_chibi")
        except Exception:
            renpy.error(f"Character chibi not defined: {who}")

    def predict_chibi(p):
        who, action = p

        chibi = eval(f"{who}_chibi")
        doll = eval(f"{who}")

        layers = (
            l[0] for pose in chibi.poses.keys()
            for k in doll.states.values() if k[0] and k[2]
            for l in k[0].get_layers(k[0]._hash, subpath=posixpath.join("chibi", pose)).values()
        )

        return layers

    renpy.register_statement(
        name="chibi",
        parse=parse_chibi,
        execute=execute_chibi,
        lint=lint_chibi,
        predict=predict_chibi,
    )

    def parse_random(l):
        l.require(":")
        l.expect_eol()

        ll = l.subblock_lexer()
        blocks = []

        while ll.advance():
            with ll.catch_error():
                weight = 1.0
                condition = "True"

                if ll.keyword("block"):
                    ll.expect_block("block")

                    block = ll.subblock_lexer().renpy_block()

                    if ll.keyword("weight"):
                        weight = float(ll.require(ll.float))

                    if ll.keyword("if"):
                        ll.expect_block("if block")
                        condition = ll.require(ll.python_expression)
                else:
                    block = ll.renpy_statement()

                blocks.append((block, weight, condition))

        return {"blocks": blocks}

    def next_random(p):
        blocks = [(block, weight, condition) for block, weight, condition in p["blocks"] if eval(condition)]
        total_weight = sum(weight for _, weight, _ in blocks)
        n = renpy.random.random() * total_weight

        for block, weight, _ in blocks:
            if n <= weight:
                break
            else:
                n -= weight

        return block

    renpy.register_statement(
        name="random",
        block=True,
        predict_all=True,
        parse=parse_random,
        next=next_random,
    )
