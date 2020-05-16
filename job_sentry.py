import sentry_sdk
import math
from sentry_sdk import capture_exception, capture_message, configure_scope
sentry_sdk.init("https://f3dc11a6b24042eabfb0fd20947d2eb6@o393161.ingest.sentry.io/5241813")

#рабочий код
with configure_scope() as scope:
    mas = ['1','2','3','4']
    a = mas[1]
    #добавление тега
    scope.set_tag('test_tag', a)
    try:
        print(mas[5])
    except Exception:
        capture_message('Ошибка')

#деление на ноль
var_ZeroError = 2/0

#ошибка отступа
for i in range(2):
  print('Ошибка отступа')

#ошибка типа
a = 2
b = 'ABC'
var_TypeError = a + b

#переполнение
qw = math.exp(1000)

#ошибка утверждения
d = 100
e = "Python"
assert d == e

#ошибка ключа
s = {1:'a', 2:'b', 3:'c'}
print("Исключение KeyError", s[4])

#ошибка индекса
q = ['a', 'b', 'c']
print("Исключение IndexError", q[4])

#переменная не определена
print("NameError", ans)

#ошибка значения
print('ValueError', float('PythonRu'))

