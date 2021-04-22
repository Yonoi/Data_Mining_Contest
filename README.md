## File Structure

.
├── data
│   ├── 海南进入生活垃圾全焚烧时代.csv
│   └── 合安高铁进入试运行.csv
├── main.py
├── non_weibo_data
│   ├── 合安高铁进入试运行.csv
│   └── 重庆尾号888888手机号法拍85万.csv
├── packages
│   ├── analyze_network.py
│   ├── analyze_non_weibo_data.py
│   ├── analyze_novel_and_emotion.py
│   ├── create_network.py
│   ├── diffusion_line.py
│   ├── diffusion_rate.py
│   ├── __init__.py
│   ├── spatial_features.py
│   └── user_features.py
├── Phase_1_report.pdf
├── README.md
├── requirements.txt
└── res
    ├── adjlist
    │   ├── 海南进入生活垃圾全焚烧时代.adjlist
    │   └── 合安高铁进入试运行.adjlist
    └── images
        ├── i级转发分布--合安高铁进入试运行.png
        ├── 粉丝区间分布--合安高铁进入试运行.png
        ├── 各省市分布--合安高铁进入试运行.png
        ├── 国内外分布--合安高铁进入试运行.png
        ├── 扩散速率图--合安高铁进入试运行.png
        ├── 情感变化--合安高铁进入试运行.png
        ├── 情感分析--合安高铁进入试运行.png
        ├── 认证类型--合安高铁进入试运行.png
        ├── 事件传播线--合安高铁进入试运行.png
        ├── 信息敏感性--合安高铁进入试运行.png
        └── 性别分布--合安高铁进入试运行.png

## Usage

* Environment: Ubuntu16.04+, python3.6+

* Other: see `requirements.txt`

  ```bash
  $ pip install -r requirements.txt
  ```

* Usage: Follow the prompts in the main function to uncomment some code, and run related function modules(tips: you need to open main.py for related editing)

  ```bash
  $ python3 main.py
  ```

  

