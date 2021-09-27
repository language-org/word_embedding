# word_embedding

author: steeve laquitaine

## Get data

Curl and unarchive dataset in data/

```bash
cd data/
curl https://synalp.loria.fr/05_fasttext_res.zip -o data.zip
unzip data.zip
rm data.zip fasttext yelp_review_polarity.ftz
# MR500dev
# MR500test
# MR500train
cut -c2- MR500train > ft.train
# ft.train
cd ..
```

## Setup

```bash
conda create -n word_e python==3.7 -y
conda activate word_e
pip install -r requirements.txt
```

Get and build the latest fastext as a python module (1):

```bash
git clone https://github.com/facebookresearch/fastText.git
cd fastText
pip install .
# conda list fasttext displays fasttext
```

## run 

```bash
python main.py
# Progress:   8.0% words/sec/thread:   68325 lr:  0.045986 avg.loss:  3.155491 ETA:   0Progress:  15.1% words/sec/thread:   63977 lr:  0.042428 avg.loss:  2.869323 ETA:   0Progress:  21.0% words/sec/thread:   59350 lr:  0.039488 avg.loss:  2.796236 ETA:   0Progress:  29.2% words/sec/thread:   61861 lr:  0.035402 avg.loss:  2.743566 ETA:   0Progress:  38.0% words/sec/thread:   64143 lr:  0.030982 avg.loss:  2.719268 ETA:   0Progress:  45.1% words/sec/thread:   63601 lr:  0.027439 avg.loss:  2.706528 ETA:   0Progress:  52.7% words/sec/thread:   63356 lr:  0.023674 avg.loss:  2.697434 ETA:   0Progress:  61.8% words/sec/thread:   65156 lr:  0.019095 avg.loss:  2.691220 ETA:   0Progress:  70.8% words/sec/thread:   66375 lr:  0.014578 avg.loss:  2.688505 ETA:   0Progress:  80.1% words/sec/thread:   67332 lr:  0.009952 avg.loss:  2.687114 ETA:   0Progress:  89.5% words/sec/thread:   68343 lr:  0.005247 avg.loss:  2.686912 ETA:   0Progress:  98.2% words/sec/thread:   68593 lr:  0.000920 avg.loss:  2.685729 ETA:   0Progress: 100.4% words/sec/thread:   64747 lr: -0.000203 avg.loss:  2.685036 ETA:   0Progress: 100.0% words/sec/thread:   64739 lr:  0.000000 avg.loss:  2.685036 ETA:   0h 0m 0s ```



## References

(1) https://fasttext.cc/docs/en/support.html  
