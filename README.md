# StatPop
繪製 NBA 數據用

![alt text](https://miro.medium.com/max/1050/1*UDZMcs_BU4bq2oD8gd5dyg.png)

## FUNCTION
#### statpop.py
* 以 `url`, `stat_category`, `stat_column`, `color` 為參數爬取並繪製球員數據圖。
* `stat_category` 目前僅支援 `per_game` 當參數。

## Requirements
python 3

## Usage
以爬取 Vince Carter 生涯得分圖為例
1. 至 [basketball-reference](https://www.basketball-reference.com/)並進入球員頁面後取得 URL。
2. 輸入 `per_game` 為參數。
3. 輸入想要繪製的數據(以得分`PTS`為例)。
4. 輸入圖表顏色。

如下:
```
if __name__ == "__main__":
    statpop = StatPop("https://www.basketball-reference.com/players/c/cartevi01.html",
                    "per_game",
                    "PTS",
                    "skyblue")
    statpop.draw()
```
即可完成繪製並儲存。

## Installation
`pip install -r requriements.txt`

