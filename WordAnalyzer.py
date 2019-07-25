from bs4 import BeautifulSoup
import requests

def get_word_information(word, url = "https://hanyu.baidu.com/s?wd={}&ptype=zici", retries = 3):
    query_url = url.format(word)
    word_info = {"word": "", "pinyin": "", "meaning": "", "sample_sentence": ""}
    while retries >= 1:
        try:
            response = requests.get(query_url, timeout = 20)
            word_infor_content = BeautifulSoup(response.content,"lxml")

            word_info["word"] = word

            pinyin_tag = word_infor_content.find("dt", class_ = "pinyin")
            word_info["pinyin"] = extract_pinyin(pinyin_tag.text)

            meaning_tag = pinyin_tag.parent.dd
            meaning_text_p_tags = meaning_tag.find_all('p')
            combined_meaning_text = ""
            for meaning_text_p in meaning_text_p_tags:
                combined_meaning_text = combined_meaning_text + meaning_text_p.text.strip()
            word_info["meaning"] = combined_meaning_text
            
            sample_sentence = extract_sample_sentence(word)
            word_info["sample_sentence"] = sample_sentence

            return word_info
        except Exception as err:
            retries = retries - 1
            if retries == 0:
                print("All retry times have been used, but it's not successful.")
                return word_info
            print(" ! ERROR ! -- "+word)
            print(err)            
            print("there are " + str(retries) + " retry times left.")


def extract_sample_sentence(word, url = "https://hanyu.baidu.com/s?wd={}造句" ):
    query_url = url.format(word)
    try:
        response = requests.get(query_url, timeout = 20)
        sample_sentence_content = BeautifulSoup(response.content, "lxml")
        sample_sentence = sample_sentence_content.find("div", class_ = "zaoju-item").p.text.replace('"', '')
        return sample_sentence
    except Exception:
        raise


def extract_pinyin(pinyin):
    try:
        first_sub_strs = pinyin.split("[")
        second_sub_strs = first_sub_strs[1].split("]")
        return second_sub_strs[0].strip()
    except Exception as err:
        print(err)
        return ""




