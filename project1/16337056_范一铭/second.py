import pandas as pd
from matplotlib import pyplot
from scipy import stats as scs

data = pd.read_csv ("000006.csv", sep=',')
daily = (data['high'] + data['low']) / 2

diff_value = daily.diff ()
# 删去第一个NAN
diff_value.drop ([0], inplace=True)

# 画直方图
pyplot.hist (daily, bins=100, weights=[1. / len (daily)] * len (daily))
pyplot.xlabel ('Stock price')
pyplot.ylabel ('Frequency')
pyplot.title ('Stock price - Frequency Histogram')
pyplot.savefig ('SPFH.jpg')
pyplot.show ()

pyplot.hist (diff_value, bins=400, weights=[1. / len (diff_value)] * len (diff_value))
pyplot.xlim(-2,2)
pyplot.xlabel ('Stock price different value')
pyplot.ylabel ('Frequency')
pyplot.title ('Stock price different value - Frequency Histogram')
pyplot.savefig ('SPDVFH.jpg')
pyplot.show ()


# 画QQ图
def qq(datas, title, name):
    fig = pyplot.figure ()
    ax = fig.add_subplot (111)
    scs.probplot (datas, dist=scs.norm, sparams=(0,), plot=ax)
    pyplot.title (title)
    pyplot.savefig (name)
    pyplot.show ()


qq (daily, 'Stock price QQ plot', 'SPQQ.jpg')
qq (diff_value, 'Stock price different value QQ plot', 'SPDVqq.jpg')
