import simplejson, json
import random
from pprint import pprint
import pchoice
import itertools

class Language (object):
    
    def __init__(self, filename):
        self._parseJson(filename)
        
    
    def build(self, minTokens=1, maxTokens=1000):
        generated = ""
        
        cur_token = self._chooseToken("root")
        old_val = ""
        
        while cur_token != None:
            val =  self._chooseValue(cur_token, old_val)
            
            if "delim" in self.lang_data[cur_token]:
                generated += self.lang_data[cur_token]["delim"]
                
            generated += val
            
            cur_token = self._chooseToken(cur_token)
            old_val = val
            
        
        return generated
    
    def _chooseToken(self, cur_token):
        token = self.lang_data[cur_token]
        
        if not "child_tokens" in token:
            return None
        
        if ("prob_final" in token):
            if random.uniform(0.0, 100.0) < token["prob_final"]:
               return None
        
        return token["child_tokens"][random.randint(0, len(token["child_tokens"]) - 1)]
    
    def _chooseValue(self, cur_token, cur_val):
        token = self.lang_data[cur_token]
        
        if not "vals" in token:
            return ""
        
        val_list = token["vals"]
        val_count = len(val_list)
        
        if not val_count:
            return ""
        
        return pchoice.choose( val_list, [100.0 / val_count] * val_count )
        
    def _parseJson(self, filename):
        json_data=open(filename)
        self.lang_data = json.load(json_data)
        json_data.close()
        
        if not "root" in self.lang_data:
            raise ValueError("No root node in language data")