import WordConverter as wc

input_file_path = "/Users/feiyangyang/Desktop/自动化录入词语/人教版小学语文三年级下-2003年12月第1版.csv"
output_file_path = "/Users/feiyangyang/Desktop/自动化录入词语/人教版小学语文三年级下-2003年12月第1版_1.csv"

df = wc.word_table_from_csv(input_file_path)
df2 = wc.word_table_with_complete_info(df, retries= 5)
print(df2)
wc.word_table_to_csv(df2, output_file_path)
