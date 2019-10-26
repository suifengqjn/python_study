
import numbers
# 需求：自定义一个类，可以将这个类的数据直接写入到数据表中
class IntField:
    # 数据描述符
    def __init__(self, db_column, min_value=None, max_value=None):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        self.db_column = db_column
        if min_value is not None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError("min_value must be int")
            elif min_value < 0:
                raise ValueError("min_value must be positive int")
        if max_value is not None:
            if not isinstance(max_value, numbers.Integral):
                raise ValueError("max_value must be int")
            elif max_value < 0:
                raise ValueError("max_value must be positive int")
        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError("min_value must be smaller than max_value")
    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("not int type")
        if value < 0:
            return ValueError("need > 0")
        self._value = value
    def __delete__(self, instance):

        pass
class CharField:
    def __init__(self, db_column, max_length=None):
        self._value = None
        self.db_column = db_column
        if max_length is None:
            raise ValueError("you must spcify max_lenth for charfiled")
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("string value need")
        if len(value) > self.max_length:
            raise ValueError("value len excess len of max_length")
        self._value = value
class User:
    name = CharField(db_cloumn="user_name", max_length=10)
    age = IntField(db_cloumn="user_age",min_value = 0,max_value = 100)

    class Meta:
        table_name = "user"

if __name__ == "__main__":
    print("a")