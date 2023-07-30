## Dataset

Two types of data - one containing sentence-only data and the other with sentence+paragraph data were prepared.

```
$ tree
.
├── data-sent
│   ├── sent_data_crf_format
│   │   └── train-test-style
│   │       ├── test.col
│   │       └── train.col.rdy
│   ├── sent_parallel
│   │   ├── test.my
│   │   ├── train.my
│   │   ├── train.tg
│   │   ├── valid.my
│   │   └── valid.tg
│   ├── sent_tagged
│   │   ├── test.tagged
│   │   ├── train.tagged
│   │   └── valid.tagged
├── data-sent+para
│   ├── sent+para_data_crf_format
│   │   ├── train-test-style
│   │   │   ├── test.col
│   │   │   └── train.col.rdy
│   │   └── train-valid-test-style
│   │       ├── test.col
│   │       ├── train.col
│   │       └── valid.col
│   ├── sent+para_parallel
│   │   ├── test.my
│   │   ├── test.tg
│   │   ├── train.my
│   │   ├── train.tg
│   │   ├── valid.my
│   │   └── valid.tg
│   └── sent+para_tagged
│       ├── test.tagged
│       ├── train.tagged
│       └── valid.tagged
│   ├── sent_data_crf_format
│   │   ├── train-test-style
│   │   │   ├── test.col
│   │   │   └── train.col.rdy
│   │   └── train-valid-test-style
│   │       ├── test.col
│   │       ├── train.col
│   │       └── valid.col
│   └── sent+para_data_crf_format
│       ├── train-test-style
│       │   ├── test.col
│       │   └── train.col.rdy
│       └── train-valid-test-style
│           ├── test.col
└───────────├── train.col
            └── valid.col
```
