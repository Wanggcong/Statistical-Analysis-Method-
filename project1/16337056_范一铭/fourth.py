import os
import pandas as pd
import scipy.stats as stats

# 将所有csv文件读入，用名为all_stock的list存储每个DataFrame文件
inputdir = "C:/Users/fym/Desktop/data_selected"
all_stock = []
for root, dirs, files, in os.walk (inputdir):  # root 根目录，dirs 子目录
    files.sort (reverse=False)  # files是路径下包含所有文件的遍历列表(乱序)
    for filename in files:
        filepath = os.path.join (root, filename)  # 将路径和文件名拼接以便读取
        df = pd.read_csv (filepath, encoding='utf8')
        df['daily_price'] = (df['high'] + df['low']) / 2
        all_stock.append (df)

# 100*100的储存pearson的矩阵
pearson = [[0 for i in range (100)] for j in range (100)]

# 100*100的储存spearman的矩阵
spearman = [[0 for i in range (100)] for j in range (100)]

# pearson中前五
p_top_cor = [0 for i in range (5)]
# spearman中前五
s_top_cor = [0 for i in range (5)]
# pearson中后五
p_bottom_cor = [1 for i in range (5)]
# spearman中后五
s_bottom_cor = [1 for i in range (5)]

# pearson中前五的p
p_top_p = [0 for i in range (5)]
# spearman中前五的p
s_top_p = [0 for i in range (5)]
# pearson中后五的p
p_bottom_p = [0 for i in range (5)]
# spearman中后五的p
s_bottom_p = [0 for i in range (5)]

# pearson中前五的股票代码
p_top_code = [[0 for i in range (2)] for j in range (5)]
# spearman中前五的股票代码
s_top_code = [[0 for i in range (2)] for j in range (5)]
# pearson中后五的股票代码
p_bottom_code = [[0 for i in range (2)] for j in range (5)]
# spearman中后五的股票代码
s_bottom_code = [[0 for i in range (2)] for j in range (5)]

for i in range (0, len (all_stock)):
    for j in range (i, len (all_stock)):
        result = pd.merge (all_stock[i], all_stock[j], on='date')
        pr, pp = stats.pearsonr (result['daily_price_x'], result['daily_price_y'])
        sr, sp = stats.spearmanr (result['daily_price_x'], result['daily_price_y'])
        pearson[i][j] = pr
        pearson[j][i] = pr
        spearman[i][j] = sr
        spearman[j][i] = sr
        pr = abs (pr)
        sr = abs (sr)

        # pearson的前五
        pt_time = 0
        for k_time, k in enumerate (p_top_cor):
            if k < pr < 1:
                # 判断新pr是否进入list
                pt_time = k_time + 10
                break
        if pt_time >= 10:
            pt_time = pt_time - 10
            x1 = list (result['code_x'])
            y1 = list (result['code_y'])
            x = x1[0]
            y = y1[0]
            for (r_time, r), p, c in zip (enumerate (p_top_cor), p_top_p, p_top_code):
                if pt_time <= r_time:
                    # t开头的是temp值
                    t_r = r
                    t_p = p
                    t_c = c
                    p_top_cor[r_time] = pr
                    p_top_p[r_time] = pp
                    p_top_code[r_time] = [x, y]
                    pr = t_r
                    pp = t_p
                    [x, y] = t_c

        # pearson的后五
        pb_time = 0
        for k_time, k in enumerate (p_bottom_cor):
            if 0 < pr < k:
                # 判断新pr是否进入list
                pb_time = k_time + 10
                break
        if pb_time >= 10:
            pb_time = pb_time - 10
            x1 = list (result['code_x'])
            y1 = list (result['code_y'])
            x = x1[0]
            y = y1[0]
            for (r_time, r), p, c in zip (enumerate (p_bottom_cor), p_bottom_p, p_bottom_code):
                if pb_time <= r_time:
                    # t开头的是temp值
                    t_r = r
                    t_p = p
                    t_c = c
                    p_bottom_cor[r_time] = pr
                    p_bottom_p[r_time] = pp
                    p_bottom_code[r_time] = [x, y]
                    pr = t_r
                    pp = t_p
                    [x, y] = t_c

        # spearman的前五
        st_time = 0
        for k_time, k in enumerate (s_top_cor):
            if k < sr < 1:
                # 判断新pr是否进入list
                st_time = k_time + 10
                break
        if st_time >= 10:
            pt_time = pt_time - 10
            x1 = list (result['code_x'])
            y1 = list (result['code_y'])
            x = x1[0]
            y = y1[0]
            for (r_time, r), p, c in zip (enumerate (s_top_cor), s_top_p, s_top_code):
                if st_time <= r_time:
                    # t开头的是temp值
                    t_r = r
                    t_p = p
                    t_c = c
                    s_top_cor[r_time] = sr
                    s_top_p[r_time] = sp
                    s_top_code[r_time] = [x, y]
                    sr = t_r
                    sp = t_p
                    [x, y] = t_c

        # spearman的后五
        sb_time = 0
        for k_time, k in enumerate (s_bottom_cor):
            if 0 < sr < k:
                # 判断新pr是否进入list
                sb_time = k_time + 10
                break
        if sb_time >= 10:
            sb_time = sb_time - 10
            x1 = list (result['code_x'])
            y1 = list (result['code_y'])
            x = x1[0]
            y = y1[0]
            for (r_time, r), p, c in zip (enumerate (s_bottom_cor), s_bottom_p, s_bottom_code):
                if pb_time <= r_time:
                    # t开头的是temp值
                    t_r = r
                    t_p = p
                    t_c = c
                    s_bottom_cor[r_time] = sr
                    s_bottom_p[r_time] = sp
                    s_bottom_code[r_time] = [x, y]
                    sr = t_r
                    sp = t_p
                    [x, y] = t_c

print (pearson)

print (spearman)
print ('Pearson相关系数前五名的股票对及其p值：')
for p, c in zip (p_top_p, p_top_code):
    print ('股票名：%06d , %06d p值：%f' % (c[0], c[1], p))
print ('Pearson相关系数后五名的股票对及其p值：')
for p, c in zip (p_bottom_p, p_bottom_code):
    print ('股票名：%06d , %06d p值：%f' % (c[0], c[1], p))
print ('Spearson相关系数前五名的股票对及其p值：')
for p, c in zip (s_top_p, s_top_code):
    print ('股票名：%06d , %06d p值：%f' % (c[0], c[1], p))
print ('Spearson相关系数后五名的股票对及其p值：')
for p, c in zip (s_bottom_p, s_bottom_code):
    print ('股票名：%06d , %06d p值：%f' % (c[0], c[1], p))

