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

class BasriDiceAPICall:
    def __init__(self, dice1,dice2,dice3,dice4,dice5,dice6):
        self.dice1 = dice1
        self.dice2 = dice2
        self.dice3 = dice3
        self.dice4 = dice4
        self.dice5 = dice5
        self.dice6 = dice6
        #self.random_seed = random_seed
        #self.upper_limit = upper_limit
        #self.stop_after_n_tries = stop_after_n_tries

    def CreateFigure(self):
            import numpy as np
            import base64
            from io import BytesIO
            from matplotlib.figure import Figure
            import pandas as pd
            received_dice_preferences = [self.dice1,self.dice2,self.dice3,self.dice4,self.dice5,self.dice6]
            list_keys = ['dice_key','dice_action']
            list_values = [[1,2,3,4,5,6],received_dice_preferences]
            zipped = list(zip(list_keys,list_values))
            data = dict(zipped)
            df_ref = pd.DataFrame(data)
            df_ref.index=df_ref.dice_key
            '''
            throw the dice. use that as dice_key.
            get the corresponding dice_action.
            move accordingly. it is a cumulative move
            '''
            df_values_reached=[] ; df_associated_dice_roll=[] ; df_dice_roll_count=[]
            current_value=0; dice_roll_count=1 ; upper_limit=100 ; stop_after_n_tries=2000 ; np.random.seed(42)
            while (current_value < upper_limit) & (stop_after_n_tries >0) :
                throw_the_dice = np.random.randint(1,7)
                condition = (df_ref.dice_key == throw_the_dice)
                next_move = df_ref[condition].dice_action.values
                current_value = current_value + next_move
                df_values_reached.append(current_value) # df_values_reached has values reached after every dice roll.
                df_associated_dice_roll.append(throw_the_dice) # df_associated_dice_roll_count has values to record the dice roll count
                df_dice_roll_count.append(dice_roll_count)
                dice_roll_count +=1 ; stop_after_n_tries -=1
            # Generate the figure **without using pyplot**.
            fig = Figure()
            ax = fig.subplots()
            ax.set_ylabel('Value Reached') ; ax.set_xlabel('Dice rolls counts') ; ax.set_title('After ' +str(dice_roll_count)+' dice rolls...')
            ax.plot(df_dice_roll_count,df_values_reached)
            # Save it to a temporary buffer.
            buf = BytesIO() ; fig.savefig(buf, format="png")
            # Embed the result in the html output.
            data = base64.b64encode(buf.getbuffer()).decode("ascii")
            url_to_pass = 'data:image/png;base64,'+ data
            return url_to_pass

