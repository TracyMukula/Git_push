from itertools import permutations

class ConcatIndex:
    def __init__(self,main_string :str,words :list[str]) -> None:
        self.main_string = main_string
        self.words = words
    
    @property
    def concatenate_words(self) -> set[str]:
        """To join the given words in the array (words)"""
        concat_words :list[str] = list()
        
        if len(self.words) > 1:
            for i in range(2,len(self.words)+1):
                #This approach utilizes slicing of lists but left it due to verbosity
                    # for j in range(1,len(self.words)):
                    #     temp :list[str] = self.words[i:j+1]
                    #     if len(temp) > 1:
                            # concat_words.append(''.join(temp))
                            # print(f'temp: {temp}, concat: {concat_words}')
                        
                            # temp.reverse()
                            # concat_words.append(''.join(temp))
                            # print(f'temp_r: {temp}, concat: {concat_words}')

                # I prefer this approach using permutations from the itertools module.
                #Form a list of tuples of every possible arrangement of the words given to used in concatenations.
                concats :list[tuple] = list(permutations(self.words,i))
                for item in concats:
                    #make the concatenations with te join method
                    concat_words.append(''.join(item))
        
        print(f"Formed concats:\n {set(concat_words)}\n")
        return set(concat_words)

    def get_index(self, word:str):
        """To extract the index of a matched concatenation in the main_string"""
        
        return self.main_string.index(word.lower()) if word.lower() in self.main_string.lower() else None
    
    def run_app(self):
        indices_fetched :list[str] = list() #To store the starting index of every matched string
        fetched_words = self.concatenate_words #Form the set of concatenated words
        mactched_concats :dict[str:int] = dict() #To store every matched word from those obtained by concatenation
        
        for word in fetched_words:
            # print(f"indx: {self.get_index(word)}")
            if self.get_index(word) is not None:
                indices_fetched.append(self.get_index(word)) #get the starting index for a matcehd word in the main_string
                mactched_concats.update({word: self.get_index(word)}) #store a dictionary of matched word and its starting index
        
        print(f"Concatenated string to starting index matching:\n {mactched_concats}\n")
        print(f"Starting indices for concatenated strings: {tuple(indices_fetched)}")


#USE CASE
c = ConcatIndex(main_string='barfoothefoobarman', words=['bar', 'foo', 'the'])
c.run_app()