def devide(a, b):
    try:
        result = a // b
        return f"yeah your result is: {result}"

    # except ZeroDivisionError:
    #     return f"ohh you divided with zerooooooo"
    except Exception as e:
        return f"ohh you divided with zerooooooo {e}"


result = devide(50, 0)

print(result)
