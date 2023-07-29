# mySentence
Corpus and models for Burmese (Myanmar language) Sentence Segmentation

README file [in English language](https://github.com/ye-kyaw-thu/mySentence/blob/main/README.md):  

- [Introduction](#Introduction)
- [License Information](#License-Information)
- [Version Information](#Version-Information)
- [Corpus Development](#Corpus-Development)
  - [Corpus Information](#Corpus-Information)
  - [Word Segmentation](#Word-Segmentation)
  - [Corpus Annotation](#Corpus-Annotation)
  - [Data Preparation](#Data-Preparation)
- Experiments
  - [JIIST Experiments](./ver1.0/jiist-experiments)
  - [CITA Experiments](./ver1.0/cita-experiments)
- [Contributors](#Contributors)
- [Publications](#Publications)
  - [Citations](#Citations)
  - [Workshop Presentation](#Workshop-Presentation)

## Introduction

Sentence Segmentation ဆိုတာ စာပိုဒ် ထဲက စာသား​တွေကို ဝါကျ တစ်​ကြောင်းစီ အဖြစ် ပိုင်းဖြတ်​ပေးတဲ့ အပိုင်း ဖြစ်ပါတယ်။ မြန်မာစာ အ​ရေးစနစ်​တွေမှာ များ​သောအားဖြင့် သဒ္ဒါ မှန်ပြီး ပုဒ်မ "။" နဲ့ အဆုံးသတ်​လေ့ ရှိကြပါတယ်။ ​နေ့စဉ်သုံး အ​ပြောစကား​တွေမှာ​တော့ ဝါကျ​တွေကို အဆုံးသတ်ဖို့ နည်းစနစ်​တွေ သတ်မှတ်ထားတာ မရှိပါ။ ဒါ​ကြောင့် ​အ​ပြောစနစ် အ​ခြေခံတဲ့ စကားသံ မှ စာ၊ စာ မှ စကားသံ နဲ့ Chatbot ​စတဲ့ နည်းပညာ​တွေ လုပ်​ဆောင်ချက် တိုးတက်ဖို့ အတွက် ဝါကျ အဆုံးသတ်​တွေကို သိနားလည်ဖို့ လိုလာပါပြီ။ ဒီ Corpus မှာ​တော့ ဝါကျ တစ်​ကြောင်းစီရဲ့ စ၊ လယ်၊ ဆုံး စကားလုံး​တွေကို Tag ​တွေ နဲ့ မှတ်သားထားပြီး ဝါကျ နဲ့ စာပိုဒ် ​ဆိုတဲ့ ​ဒေတာ ပုံစံ ၂ မျိုးလုံး ပါဝင်ပါတယ်။

## License Information
Creative Commons Attribution-NonCommercial-Share Alike 4.0 International (CC BY-NC-SA 4.0) License. [Detail Information](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Version Information
Version 1.0 Release Date:

## Corpus Development

### Corpus Information
ဒီ Corpus ထဲမှာ ပါတဲ့ မြန်မာ စာ​ကြောင်း​တွေနဲ့ စာပိုဒ်​တွေကို ​အောက်ပါ ​နေရာ အသီးသီးက​နေ စု​ဆောင်းထားပါတယ်။

| Data Resources | sentence  | paragraph  |
|---|-: |-: |
| [myPOS ver3.0](https://github.com/ye-kyaw-thu/myPOS) | 40,191 | 2,917 |
| [Covid-19 Q&A](https://www3.nhk.or.jp/nhkworld/my/news/qa/coronavirus/) | 1,000 | 1,350 |
| [Shared By Louis Augustine Page](www.facebook.com/sharedbylouisaugustine) | 547 | 1,885 |
| [Maung Zi's Tales Page](www.facebook.com/MaungZiTales) | 2,516 | 581 |
| [Wikipedia](https://my.wikipedia.org/wiki/%E1%80%97%E1%80%9F%E1%80%AD%E1%80%AF%E1%80%85%E1%80%AC%E1%80%99%E1%80%BB%E1%80%80%E1%80%BA%E1%80%94%E1%80%BE%E1%80%AC) | 2,780 | 1,060 |
| Others | 93 | 672 |
| **Total** | **47,127** | **8,465** |

### Word Segmentation

မြန်မာ အ​ရေးစနစ်မှာ စကားလုံး​တွေကို Space နဲ့ မပိုင်းဖြတ်ပါဘူး။ ပုဒ်စု​ phrase ​တွေကိုသာ ဖတ်ရ လွယ်ကူ​စေရန် ပိုင်းဖြတ်​လေ့ ရှိပါတယ်။ စာ​ကြောင်း​တွေကို ရုပ်ရင်း စကားလုံး​တွေ အဖြစ် ပိုင်းဖြတ်ဖို့ [myWord](https://github.com/ye-kyaw-thu/myWord/) ကို သုံးထားပါတယ်။ ပိုင်းဖြတ်တဲ့ ​နေရာမှာ သုံးထားတဲ့ နည်းစနစ်က​တော့ [myPOS](https://github.com/ye-kyaw-thu/myPOS) corpus က အတိုင်း ဖြစ်ပါတယ်။   

B (Begin), O (Other), N (Next), E (End).

### Corpus Annotation
စာ​ကြောင်း နဲ့ စာပိုဒ်ထဲက စာလုံး​တွေကို ​ဒီ အတိုင်း Tag ထားပါတယ်။
<br/>
"/E" ဆိုတဲ့ ဝါကျအဆုံးပြ Tag ၂ ခု ထက် ပိုပြီး ပါရင် စာပိုဒ် အဖြစ် သတ်မှတ်ပါတယ်။  
<br/>
​ဝါကျ စာ​ကြောင်း ကို Tag ထားတဲ့ ဥပမာ  

Untagged sentence: ကျွန်တော် ပျင်း လာ ပြီ  
Tagged sentence : ကျွန်တော်/B ပျင်း/N လာ/N ပြီ/E  

စာပိုဒ်ကို Tag ထားတဲ့ ဥပမာ   

Untagged paragraph: တောင်းပန် ပါ တယ် ကျွန်တော် က အချစ် ကား ပို ကြိုက် တယ်  
Tagged paragraph: တောင်းပန်/B ပါ/N တယ်/E ကျွန်တော်/B က/O အချစ်/O ကား/N ပို/N ကြိုက်/N တယ်/E  

### Dataset Preparation

ဝါကျ​တွေချည်း ပါတဲ့ sentence-only ​ဒေတာနဲ့ ဝါကျ​တွေ​ရော စာပိုဒ်​တွေပါ ပါတဲ့ sentence+paragraph ​ဒေတာ ၂ မျိုးစလုံး ကို ပြင်ဆင်ခဲ့ကြပါတယ်။ ပြီးမှ ကျွန်​တော်တို့က Train, Valid, Test ဆို ခွဲပြီး ​အောက်ပါ အတိုင်း ခွဲလိုက်ပါတယ်။
```
$ wc ./data/data-sent/sent_tagged/*
    4712    63622  1046667 test.tagged
   40000   543541  8955710 train.tagged
    2414    32315   531166 valid.tagged
   47126   639478 10533543 total
   
$ wc ./data/data-sent+para/sent+para_tagged/*
    5512    96632  1573446 test.tagged
   47002   834243 13612719 train.tagged
    3079    61782  1001138 valid.tagged
   55593   992657 16187303 total
```
Dataset format example
```
$ head -5 ./data/data-sent/sent_tagged/train.tagged 
ဘာ/B ရယ်/O လို့/O တိတိကျကျ/O ထောက်မပြ/O နိုင်/O ပေမဲ့/O ပြဿနာ/O တစ်/O ခု/O ခု/O ရှိ/O တယ်/N နဲ့/N တူ/N တယ်/E
လူ့/B အဖွဲ့အစည်း/O က/O ရှပ်ထွေး/O လာ/O တာ/O နဲ့/O အမျှ/O အရင်/O က/O မ/O ရှိ/O ခဲ့/O တဲ့/O လူမှုရေး/O ပြဿနာ/O တွေ/O ဖြစ်ပေါ်/N လာ/N ခဲ့/N တယ်/E
အခု/B အလုပ်/O လုပ်/N နေ/N ပါ/N တယ်/E
ကြည့်/B ရေစာ/O တွေ/O က/O အဲဒီ/O တစ်/O ခု/O နဲ့/N မ/N တူ/N ဘူး/E
ဘူမိ/B ရုပ်သွင်/O ပညာ/O သည်/O ကုန်းမြေသဏ္ဌာန်/O များ/O ကို/O လေ့လာ/O သော/N ပညာရပ်/N ဖြစ်/N သည်/E
```

CRF အတွက် Column ​တွေ နဲ့ CRF Format လည်း ပြင်ပါတယ်။

```
$ wc ./data/data-sent/sent_data_crf_format/*
   68334   127244  1051379 test.col
  583541  1087082  8995710 train.col
   34729    64630   533580 valid.col
  686604  1278956 10580669 total

$ wc ./data/data-sent+para/sent+para_data_crf_format/*
  102144   193264  1578958 test.col
  881245  1668486 13659721 train.col
   64861   123564  1004217 valid.col
 1048250  1985314 16242896 total
```
CRF format example
```
$ head -5 ./data/data-sent/sent_data_crf_format/train.col 
ဘာ B
ရယ် O
လို့ O
တိတိကျကျ O
ထောက်မပြ O
```
Neural Machine Translation အတွက် parallel ပုံစံလည်း ပြင်ခဲ့ပါတယ်။
```
$ wc ./data/data-sent/sent_parallel/*
    4712    63622   919423 test.my
   40000   543541  7868628 train.my
   40000   543541  1087082 train.tg
    2414    32315   466536 valid.my
    2414    32315    64630 valid.tg
   89540  1215334 10406299 total

$ wc ./data/data-sent+para/sent+para_parallel/*
    5512    96632  1380183 test.my
    5512    96632   193264 test.tg
   47002   834243 11944271 train.my
   47002   834243  1668486 train.tg
    3079    61782   877576 valid.my
    3079    61782   123564 valid.tg
  111186  1985314 16187344 total
```
```
$ head -2 ./data/data-sent/sent_parallel/train.my
ဘာ ရယ် လို့ တိတိကျကျ ထောက်မပြ နိုင် ပေမဲ့ ပြဿနာ တစ် ခု ခု ရှိ တယ် နဲ့ တူ တယ်
လူ့ အဖွဲ့အစည်း က ရှပ်ထွေး လာ တာ နဲ့ အမျှ အရင် က မ ရှိ ခဲ့ တဲ့ လူမှုရေး ပြဿနာ တွေ ဖြစ်ပေါ် လာ ခဲ့ တယ်

$ head -2 ./data/data-sent/sent_parallel/train.tg
B O O O O O O O O O O O N N N E
B O O O O O O O O O O O O O O O O N N N E
```

## Contributors
- [Ye Kyaw Thu](https://sites.google.com/site/yekyawthunlp/) (Language Understanding Laboratary: LU Lab., Myanmar, National Electronics and Computer Technology Center: NECTEC, Pathumthani, Thailand)
- [Thura Aung](https://sites.google.com/view/thura-aung/) (Language Understanding Laboratary: LU Lab., Myanmar)

## Publications
### Citations
လူကြီးမင်းတို့ရဲ့ သု​တေသန အလုပ်​တွေမှာ mySentence ​မော်ဒယ်​တွေ ကို အသုံးပြုရင်ပဲ ဖြစ်​စေ၊ ​ဒေတာ များကို ပြန်လည် အသုံးပြုရင်ပဲ ဖြစ်​စေ ​အောက်ပါ စာတမ်းကို အကိုးအကား အ​နေနဲ့ ​​ဖော်ပြ​ပေး​စေလိုပါတယ်။

<!-- - Thura Aung, Ye Kyaw Thu, Zar Zar Hlaing, "mySentence: Sentence Segmentation for Myanmar language using Neural Machine Translation Approach" -->  

- Ye Kyaw Thu, Thura Aung, Thepchai Supnithi, "Neural Sequence Labeling based Sentence Segmentation for Myanmar Language", the 12th Conference on Information Technology and its applications (CITA 2023), Lecture Notes in Networks and Systems, vol 734. Springer, Cham. [https://doi.org/10.1007/978-3-031-36886-8_24](https://doi.org/10.1007/978-3-031-36886-8_24), July 28-29, Danang, Vietnam, pp. 285-296


### Workshop Presentation

Thura Aung, Ye Kyaw Thu, Zar Zar Hlaing, "mySentence: Sentence Segmentation for Myanmar language using Neural Machine Translation Methods", the 4th joint Workshop on NLP/AI R&D, November 5, 2022 at Chiang Mai, Thailand. [[workshop_link]](https://isai-nlp-aiot2022.aiat.or.th/workshop-on-nlp-ai-rd/)  
