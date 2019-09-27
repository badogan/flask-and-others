#HelloWorldRoute
class BasriNumbers:
    
    def __init__(self, num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def MultiplyThem(self):
        '''
        multiply them
        >>> BasriNumbers(10,20).MultiplyThem()
        200.0
        '''
        return str(float(self.num1*self.num2))

class BasriAPICall:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def GetJSONData(self):
            import requests
            # Assign URL to variable: url
            url = self.endpoint
            # Package the request, send the request and catch the response: r
            r = requests.get(url)
            # Decode the JSON data into a dictionary: json_data
            json_data=r.json()
            return json_data


class BasriAPICallReduceDF:
    def __init__(self, inputDF):
        self.inputDF = inputDF

    def ReduceDF(self):
            i=1
            reduced_df=[]
            ignore_list=['','None',' ','  ','   ','    ','      ','      ']
            while i <20:
                ingredient = 'strIngredient'+str(i)
                measure = 'strMeasure'+str(i)
                condition_is_met = (self.inputDF['meals'][0][ingredient] not in ignore_list) & (self.inputDF['meals'][0][measure] not in ignore_list)
                if condition_is_met:
                    reduced_df.append({self.inputDF['meals'][0][ingredient]:self.inputDF['meals'][0][measure]})
                i=i+1
            return reduced_df
