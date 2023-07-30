## Programs used in corpus building

### ch2col.pl

Convert tagged data to column (CRF format)
<br/>

Tagged data format
```
$ head -5 test.txt
  အခု/B သန့်စင်ခန်း/O ကို/N သုံး/N ပါရစေ/E
  လူငယ်/B တွေ/O က/O ပုံစံတကျ/O ရှိ/O မှု/O ကို/O မ/N ကြိုက်/N ဘူး/E
  ဒီ/B တစ်/O ခေါက်/O ကိစ္စ/O ကြောင့်/O ကျွန်တော့်/O ရဲ့/O သိက္ခာ/O အဖတ်ဆယ်/O လို့/N မ/O ရ/O အောင်/O ကျ/N သွား/N တယ်/E
  ဂီနီ/B နိုင်ငံ/O သည်/O ကမ္ဘာ/O ပေါ်/O တွင်/O ဘောက်/O ဆိုက်/O တင်ပို့/O မှု/O အများဆုံး/O နိုင်ငံ/N ဖြစ်/N သည်/E
  ဘာ/B လုပ်/N ရ/N မလဲ/N ဟင်/E
```
How to run ...
```
$ perl ch2col.pl test.txt > test.txt.col
```
Output
```
$ head -5 test.txt.col 
  အခု B
  သန့်စင်ခန်း N
  ကို N
  သုံး N
  ပါရစေ E
```

### col2line.pl

Convert tagged data format to column (CRF format) 
<br/>
```
$ head -5 test.txt.col 
  အခု B
  သန့်စင်ခန်း N
  ကို N
  သုံး N
  ပါရစေ E
```
How to run ...
```
$ perl ch2col.pl test.txt > test.txt.col
```
Output
```
$ head -5 test.txt
  အခု/B သန့်စင်ခန်း/O ကို/N သုံး/N ပါရစေ/E
  လူငယ်/B တွေ/O က/O ပုံစံတကျ/O ရှိ/O မှု/O ကို/O မ/N ကြိုက်/N ဘူး/E
  ဒီ/B တစ်/O ခေါက်/O ကိစ္စ/O ကြောင့်/O ကျွန်တော့်/O ရဲ့/O သိက္ခာ/O အဖတ်ဆယ်/O လို့/N မ/O ရ/O အောင်/O ကျ/N သွား/N တယ်/E
  ဂီနီ/B နိုင်ငံ/O သည်/O ကမ္ဘာ/O ပေါ်/O တွင်/O ဘောက်/O ဆိုက်/O တင်ပို့/O မှု/O အများဆုံး/O နိုင်ငံ/N ဖြစ်/N သည်/E
  ဘာ/B လုပ်/N ရ/N မလဲ/N ဟင်/E
```

### count_word_freq.pl

Count word frequency (tag frequency in this corpus) in the file
<br/>
```
$ head -5 train.tg
	B N N N E
	B O O O O O O N N E
	B O O O O O O O O N N N N N N E
	O O O O O O O O O O O N N E
	B N N N E
```
How to run ...
```
$ perl count_word_freq.pl train.tg
  B:  39535
  E:  39992
  N: 111905
  O: 352109
```

### eq_count.py, pair-chk.py

Check whether or not num of words and tags are equal.
<br/>
How to run ...
```
$ python pair-chk.py train.my train.tg
Line 8 : ['မချုပ်', 'တည်း', 'နိုင်', 'တော့', 'ပဲ', 'ကျောင်းဆောင်', 'ထဲ', 'က', 'အပျိုစင်', 'နတ်', 'ဘုရား', 'အသီးနား', 'ရဲ့', 'ရုပ်', 'ထု', 'ရှေ့', 'မှာ', 'ပဲ', 'မက်ဒူးဆာ', 'ကို', 'အနိုင်', 'အထက်', 'ပြု', 'လို့မယား', 'အဖြစ်', 'သိမ်းပိုက်', 'လိုက်', 'ပါ', 'လေ', 'တယ်', 'A'] <||> ['B', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'N', 'N', 'N', 'E']
```
==> num of words and tags are not equal in line 8.

### mk-pair.pl

Combine word and tags files <br/>
How to run ...
```
$ perl mk-pair.pl train.my train.tg > train.tagged
```

### mk-wordtag.pl

How to run
```
$ perl mk-wordtag.pl <input-file-name> <delimeter> <w|t|wt|cw|c> 
```
```
w = print word only (i.e. without POS tags), 
t = print tag only
wt = print word/tag
cw = print words including compound words,
lcw = list compound words, 
c = print sentence that contain tagging error of "word/" 
```
The following will print tags only
```
$ perl mk-wordtag.pl ./train.tagged "\/" t >> train.tg
$ head -5 train.tg
	B N N N E
	B O O O O O O N N E
	B O O O O O O O O N N N N N N E
	O O O O O O O O O O O N N E
	B N N N E
```

### tag-wise-report.py

Print tag-wise classification report for tags <br/>
Input files should be ...
```
$ head -5 test.tg
	B N N N E
	B O O O O O O N N E
	B O O O O O O O O N N N N N N E
	O O O O O O O O O O O N N E
	B N N N E
```
How to run ...
```
$ python tag-wise-report.py test.tg hyp.tg

              precision    recall  f1-score   support

           B       0.86      0.37      0.52      2092
           E       0.91      0.38      0.54      2149
           N       0.87      0.41      0.55      5749
           O       0.79      0.98      0.88     23057

    accuracy                           0.81     33047
   macro avg       0.86      0.54      0.62     33047
weighted avg       0.82      0.81      0.78     33047
```



