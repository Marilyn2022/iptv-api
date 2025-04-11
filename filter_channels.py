import re

def filter_channels(input_file, output_file):
    """
    过滤失效频道、购物频道、无内容频道以及含有微信公众号推广的频道
    """
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        lines = infile.readlines()
        keep_channel = False

        for line in lines:
            if line.startswith("#EXTINF"):
                # 判断是否包含过滤关键字
                if any(keyword in line for keyword in ["购物", "广告", "无内容", "微信公众号", "推广"]):
                    keep_channel = False
                else:
                    keep_channel = True
                    outfile.write(line)  # 保留频道信息
            elif keep_channel:
                # 写入频道地址
                outfile.write(line)

if __name__ == "__main__":
    input_file = "output/result.m3u"  # 输入文件路径
    output_file = "output/result_filtered.m3u"  # 输出文件路径
    filter_channels(input_file, output_file)
    print(f"过滤完成，结果已保存至 {output_file}")