import pandas as pd 
import numpy as np
import WordAnalyzer as wa

def word_table_from_csv(csv_file_path):
    try:
        word_table = pd.read_csv(csv_file_path)
        return word_table
    except Exception as err:
        print(err)
        return None

def word_table_with_complete_info(word_table, retries = 3, verbose_output = True):
    try:
        complete_word_table = word_table.assign(拼音=lambda x: "", 
                                                释义=lambda x: "",
                                                例句=lambda x: "")
        word_series = complete_word_table["词语"]
        
        if verbose_output:
            print(word_series)
            print()

        for index, word in word_series.iteritems():
            
            if verbose_output:
                print("现在获取 " + word + " 信息：")

            word_info = wa.get_word_information(word, retries = retries)
            complete_word_table.loc[index,"拼音"] = word_info["pinyin"]
            complete_word_table.loc[index,"释义"] = word_info["meaning"]
            complete_word_table.loc[index,"例句"] = word_info["sample_sentence"]

            if verbose_output:
                print(complete_word_table.loc[index])
                print()

        return complete_word_table
    except Exception as err:
        print(err)
        return None

def word_table_to_csv(word_table, filepath):
    try:
        word_table.to_csv(filepath)
    except Exception:
        raise


