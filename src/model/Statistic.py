class Statistic:

    def __new__(cls, *args, **kwargs):
        return super(Statistic, cls).__new__(cls)

    def __init__(self, st_id, name, value):
        self.id = st_id
        self.name = name
        self.value = value


st = Statistic('test', 'Salud', 100)
print(st.name)
print(st.id)
