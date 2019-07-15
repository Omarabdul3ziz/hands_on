try :
    def fn():
        result = []
        for i in range(5):
            result.append((i+1)/i)
        return result
except ZeroDivisionError:
    result = ("Not working Here !")
else:
    print(result)
finally :
    print('you are welcome')