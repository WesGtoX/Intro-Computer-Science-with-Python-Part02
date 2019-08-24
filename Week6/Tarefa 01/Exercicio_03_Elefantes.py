# import pytest

def incomodam(n):
    if n <= 0:
        return ""
    elif n % 1 == 0:
        return "incomodam " + incomodam(n - 1)
    else:
        return ""


def elefantes(n):
    if n == 1:
        return "Um elefante incomoda muita gente"
    elif n == 2:
        return elefantes(n-1) + f"\n{n} elefantes " + incomodam(n) + "muito mais"
    elif n > 2:
        return elefantes(n-1) + f"\n{n-1} elefantes incomodam muita gente" + \
               f"\n{n} elefantes " + incomodam(n) + "muito mais"
    else:
        return ""


# @pytest.mark.parametrize("entrada, esperado", [
#     (0, ""),
#     (1, "Um elefante incomoda muita gente"),
#     (2, "Um elefante incomoda muita gente\n"
#         "2 elefantes incomodam incomodam muito mais"),
#     (3, "Um elefante incomoda muita gente\n"
#        "2 elefantes incomodam incomodam muito mais\n"
#        "2 elefantes incomodam muita gente\n"
#        "3 elefantes incomodam incomodam incomodam muito mais"),
#     (4, "Um elefante incomoda muita gente\n"
#        "2 elefantes incomodam incomodam muito mais\n"
#        "2 elefantes incomodam muita gente\n"
#        "3 elefantes incomodam incomodam incomodam muito mais\n"
#        "3 elefantes incomodam muita gente\n"
#        "4 elefantes incomodam incomodam incomodam incomodam muito mais"),
#     (-1, ""),
#     (-2, ""),
#     (5, "Um elefante incomoda muita gente\n"
#         "2 elefantes incomodam incomodam muito mais\n"
#         "2 elefantes incomodam muita gente\n"
#         "3 elefantes incomodam incomodam incomodam muito mais\n"
#         "3 elefantes incomodam muita gente\n"
#         "4 elefantes incomodam incomodam incomodam incomodam muito mais\n"
#         "4 elefantes incomodam muita gente\n"
#         "5 elefantes incomodam incomodam incomodam incomodam incomodam muito mais"),
# ])
# def test_eval(entrada, esperado):
#     assert elefantes(entrada) == esperado
