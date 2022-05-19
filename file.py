def greeter(func):
  def wrapper(*args, **kwargs):
    new = [wrd.lower().capitalize() for wrd in func(*args, **kwargs).split()]
    return f'Aloha {" ".join(new)}'
  return wrapper


def sums_of_str_elements_are_equal(func):
    def sum_of_numbers(number):
        lst = []
        if number[0] == '-':
            i = 1
            while i < len(number):
                lst.append(-int(number[i]))
                i += 1
        else:
            i = 0
            while i < len(number):
                lst.append(int(number[i]))
                i += 1
        return sum(lst)

    def drugie_zad(*args, **kwargs):
        x = func(*args, **kwargs).split()
        if sum_of_numbers(x[0]) == sum_of_numbers(x[1]):
            return f'{sum_of_numbers(x[0])} == {sum_of_numbers(x[1])}'
        else:
            return f'{sum_of_numbers(x[0])} != {sum_of_numbers(x[1])}'

    return drugie_zad



def format_output(*required_keys):


    def decorator(func):
        def dict_maker(*args):
            funk = func(*args)

            dic = {}
            for key in required_keys:

                if "__" in key:
                    word_lst = key.split('__')
                    value4keys = []

                    for inner_key in word_lst:
                        if inner_key in funk.keys():
                            value4keys.append(funk.get(inner_key))
                        else:
                            raise ValueError

                    dic[key] = " ".join(value4keys)
                else:
                    if key in funk.keys():
                        if funk.get(key) == "":
                            dic[key] = "Empty value"
                        else:
                            dic[key] = funk.get(key)
                    else:
                        raise ValueError
            return dic

        return dict_maker

    return decorator



def add_method_to_instance(klass):
    def funk_dec(func):
        def wrapper(*args):
            return func()
        setattr(klass, func.__name__, wrapper)
        return wrapper
    return funk_dec

