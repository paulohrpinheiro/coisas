from mod2.services import mod2_function


def mod1_function():
    mod2 = mod2_function()

    return 'From _mod1_ I get this from _mod2_: [{}]'.format(mod2)
