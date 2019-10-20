

class Tool:
    def __enter__(self):
        print("enter-- 获取资源")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit--释放资源")

    def Do(self):
        print("do some thing")


with Tool() as t:
        t.Do()
        
