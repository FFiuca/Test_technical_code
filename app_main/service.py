from . import repository

class CalculateService(repository.CalculateRepository):

    def calculate_segitiga(self):
        val = list(str(self.size))

        result = []
        for idx, r in enumerate(val):
            temp = str(r).ljust(int(idx)+2, "0")
            result.append(temp)

        return result

    def calculate_ganjil(self):
        result = []
        for x in range(0, int(self.size)+1):
            if x%2!=0:
                result.append(x)

        return result

    def calculate_prima(self):
        result = []
        for x in range(1, int(self.size)+1):
            if x%1==0 and x%x==0:
                result.append(x)

        return result
